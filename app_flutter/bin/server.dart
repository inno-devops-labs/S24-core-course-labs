import 'package:intl/intl.dart';

import 'package:prometheus_client/prometheus_client.dart';
import 'package:prometheus_client/runtime_metrics.dart' as runtime_metrics;
import 'package:prometheus_client_shelf/shelf_metrics.dart' as shelf_metrics;
import 'package:prometheus_client_shelf/shelf_handler.dart' as shelf_handler;
import 'package:shelf/shelf.dart' as shelf;
import 'package:shelf/shelf_io.dart' as io;
import 'package:shelf_router/shelf_router.dart' as shelf_router;

main() async {
  runtime_metrics.register();

  final greetingCounter = Counter(
    name: 'greetings_total',
    help: 'The total amount of greetings',
  )..register();

  final moscowCounter = Counter(
    name: 'moscow_total',
    help: 'The total amount of requests for time in Moscow',
  )..register();


  final app = shelf_router.Router();

  app.get('/', (shelf.Request request) {
    final moscowTime =
        DateTime.now().toUtc().add(const Duration(hours: 3)); // Moscow is UTC+3
    final formattedTime = DateFormat('yyyy-MM-dd HH:mm:ss').format(moscowTime);
    moscowCounter.inc();
    return shelf.Response.ok('Current time in Moscow: $formattedTime');
  });

   app.get('/hello', (shelf.Request request) {
    greetingCounter.inc();
    return shelf.Response.ok('hello-world');
  });

  app.get('/metrics', prometheusHandler());

  var handler = const shelf.Pipeline()
      .addMiddleware(shelf_metrics.register())
      .addHandler(app);
  var server = await io.serve(handler, '0.0.0.0', 8080);

  print('Serving at http://${server.address.host}:${server.port}');
}

prometheusHandler() {
  return shelf_handler.prometheusHandler();
}