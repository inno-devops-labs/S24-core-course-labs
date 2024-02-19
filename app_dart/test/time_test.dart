import 'package:app_dart/time.dart';
import 'package:test/test.dart';
import 'package:timezone/browser.dart' as tz;

void main() {
  group('Test current time and time on refresh', () {
    test('time value should be the current Moscow time', () async {
      final time = Time();

      await tz.initializeTimeZone();
      final moscowTz = tz.getLocation('Europe/Moscow');
      final currentTime = tz.TZDateTime.now(moscowTz).toString().split(' ');

      expect(time.moscowTime, currentTime);
    });

    test('time should be updated on refresh', () async {
      final time = Time();

      final firstResponse = time.moscowTime;

      await Future.delayed(const Duration(seconds: 2));

      final secondResponse = time.moscowTime;

      expect(firstResponse, isNot(secondResponse));
    });
  });
}