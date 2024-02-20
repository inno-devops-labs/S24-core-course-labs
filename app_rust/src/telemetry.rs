use opentelemetry::sdk::propagation::TraceContextPropagator;
use opentelemetry::sdk::{trace, trace::Tracer, Resource};
use opentelemetry::KeyValue;
use opentelemetry_otlp::WithExportConfig;
use std::fs::File;
use std::fs::OpenOptions;
use tracing::subscriber::set_global_default;
use tracing::Subscriber;
use tracing_bunyan_formatter::{BunyanFormattingLayer, JsonStorageLayer};
use tracing_log::LogTracer;
use tracing_subscriber::{layer::SubscriberExt, EnvFilter, Registry};

pub fn create_trace(exporter_endpoint: &str, service_name: &str) -> Tracer {
    let exporter = opentelemetry_otlp::new_exporter()
        .tonic()
        .with_endpoint(exporter_endpoint);

    opentelemetry_otlp::new_pipeline()
        .tracing()
        .with_exporter(exporter)
        .with_trace_config(
            trace::config().with_resource(Resource::new(vec![KeyValue::new(
                opentelemetry_semantic_conventions::resource::SERVICE_NAME,
                service_name.to_string(),
            )])),
        )
        .install_batch(opentelemetry::runtime::Tokio)
        .expect("Error: Failed to initialize the tracer.")
}

pub fn create_log_file(file_name: Option<String>) -> Result<File, std::io::Error> {
    let file_name = file_name.unwrap_or("log.log".to_string());
    let file = OpenOptions::new()
        .create(true)
        .append(true)
        .open(file_name.as_str())?;
    Ok(file)
}

pub fn get_subscriber(env: &str, name: &str, _exporter_url: &str) -> impl Subscriber + Send + Sync {
    //let tracer = create_trace(exporter_url, name);
    let _file = create_log_file(None).expect("Failed to create a file for logging");
    let env_filter = EnvFilter::try_from_default_env().unwrap_or_else(|_| EnvFilter::new(env));
    //let formatting_layer = BunyanFormattingLayer::new(name.into(), file);
    //let tracing_layer = tracing_opentelemetry::layer().with_tracer(tracer);
    let formatting_layer_std_out = BunyanFormattingLayer::new(name.into(), std::io::stdout);

    //global::set_text_map_propagator(TraceContextPropagator::new());
    Registry::default()
        .with(env_filter)
        //.with(tracing_layer)
        .with(JsonStorageLayer)
        .with(formatting_layer_std_out)
}

pub fn initialize_subscriber(subscriber: impl Subscriber + Sync + Send) {
    LogTracer::init().expect("Failed to initialize the log - tracer ");
    set_global_default(subscriber).expect("Failed to set the subscriber");
}
