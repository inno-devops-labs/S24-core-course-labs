import 'package:app_dart/time.dart';
import 'package:test/test.dart';
import 'package:timezone/browser.dart' as tz;

void main() {
  group('Test current time and time on refresh', () {
    test('time value should be the current Moscow time', () async {
      final time = Time();
      await time.getMoscowTime();
      final currentTime = time.moscowTime;
      currentTime[1] = (currentTime[1].split('.'))[0];

      await tz.initializeTimeZone();
      final moscowTz = tz.getLocation('Europe/Moscow');
      final expectedTime = tz.TZDateTime.now(moscowTz).toString().split(' ');
      expectedTime[1] = (expectedTime[1].split('.'))[0];

      expect(currentTime, expectedTime);
    });

    test('time should be updated on refresh', () async {
      final time = Time();

      await time.getMoscowTime();
      final firstResponse = time.moscowTime;

      await Future.delayed(const Duration(seconds: 2));

      await time.getMoscowTime();
      final secondResponse = time.moscowTime;

      expect(firstResponse, isNot(secondResponse));
    });
  });
}
