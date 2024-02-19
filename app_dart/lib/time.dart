import 'package:timezone/browser.dart' as tz;

class Time {
  List<String> moscowTime = [];

  Time() {
    getMoscowTime();
  }

  Future<void> getMoscowTime() async {
    await tz.initializeTimeZone();
    final moscowTz = tz.getLocation('Europe/Moscow');
    moscowTime = tz.TZDateTime.now(moscowTz).toString().split(' ');
  }
}
