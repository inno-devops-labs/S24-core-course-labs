import 'package:flutter/material.dart';
import 'dart:io';

import 'package:prometheus_client/format.dart' as format;
import 'package:prometheus_client/prometheus_client.dart';
import 'package:prometheus_client/runtime_metrics.dart' as runtime_metrics;

import 'package:app_dart/time.dart';

Future main() async {
  // Register runtime metrics with the default metrics registry
  runtime_metrics.register();

  // Create a Histogram metrics without labels. Always register your metric,
  // either at the default registry or a custom one.
  final durationHistogram = Histogram(
    name: 'http_request_duration_seconds',
    help: 'The duration of http requests in seconds.',
  )..register();

  // Create a metric of type counter, with a label for the requested path:
  final metricRequestsCounter = Counter(
      name: 'metric_requests_total',
      help: 'The total amount of requests of the metrics.',
      labelNames: ['path'])
    ..register();

  // Create a http server
  final server = await HttpServer.bind(
    InternetAddress.loopbackIPv4,
    8080,
  );
  print('Listening on localhost:${server.port}');

  await for (HttpRequest request in server) {
    // Measure the request duration
    await durationHistogram.observeDuration(Future(() async {
      // Count calls to the metric endpoint by path.
      metricRequestsCounter.labels([request.uri.path]).inc();

      // Output metrics in the text representation
      request.response.headers.add('content-type', format.contentType);
      final metrics =
          await CollectorRegistry.defaultRegistry.collectMetricFamilySamples();
      format.write004(request.response, metrics);

      await request.response.close();
    }));
  }
  runApp(const MainApp());
}

class MainApp extends StatefulWidget {
  const MainApp({super.key});

  @override
  State<MainApp> createState() => _MainAppState();
}

class _MainAppState extends State<MainApp> {
  String? _time;
  String? _date;

  @override
  void initState() {
    _setTime();
    super.initState();
  }

  Future<void> _setTime() async {
    final time = Time();
    await time.getMoscowTime();

    setState(() {
      _time = time.moscowTime[1].split('.')[0];
      _date = time.moscowTime[0];
    });
  }

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      home: Scaffold(
        body: Center(
          child: _time != null
              ? Column(
                  children: [
                    Text(
                      _time!,
                      style: const TextStyle(fontSize: 60),
                    ),
                    Text(
                      _date!,
                      style: const TextStyle(fontSize: 30),
                    ),
                  ],
                )
              : const CircularProgressIndicator(),
        ),
      ),
    );
  }
}
