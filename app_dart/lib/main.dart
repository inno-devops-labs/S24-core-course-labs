import 'package:flutter/material.dart';
import 'package:timezone/browser.dart' as tz;

void main() {
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
    await tz.initializeTimeZone();
    final moscowTz = tz.getLocation('Europe/Moscow');
    final time = tz.TZDateTime.now(moscowTz).toString().split(' ');

    setState(() {
      _time = time[1].split('.')[0];
      _date = time[0];
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
