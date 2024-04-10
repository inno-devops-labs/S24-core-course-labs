import 'package:flutter/material.dart';
import 'package:intl/intl.dart';

void main() {
  runApp(const MyApp());
}

class MyApp extends StatelessWidget {
  const MyApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Moscow Time',
      theme: ThemeData(
        colorScheme: ColorScheme.fromSeed(seedColor: Colors.deepPurple),
        useMaterial3: true,
      ),
      home: const MoscowTimeWidget(),
    );
  }
}

class MoscowTimeWidget extends StatefulWidget {
  const MoscowTimeWidget({super.key});

  @override
  MoscowTimeWidgetState createState() => MoscowTimeWidgetState();
}

class MoscowTimeWidgetState extends State<MoscowTimeWidget> {
  String _moscowTime = '';

  @override
  void initState() {
    super.initState();
    _updateMoscowTime();
  }

  void _updateMoscowTime() {
    setState(() {
      var moscowTime = DateTime.now()
          .toUtc()
          .add(const Duration(hours: 3)); // Moscow is 3 hours ahead of UTC
      _moscowTime = DateFormat('HH:mm').format(moscowTime);
    });
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text('Moscow Time'),
      ),
      body: Center(
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: <Widget>[
            const Text(
              'Moscow Time:',
              style: TextStyle(fontSize: 20),
            ),
            Text(
              _moscowTime,
              style: const TextStyle(fontSize: 30, fontWeight: FontWeight.bold),
            ),
          ],
        ),
      ),
      floatingActionButton: FloatingActionButton(
        onPressed: _updateMoscowTime,
        tooltip: 'Refresh',
        child: const Icon(Icons.refresh),
      ),
    );
  }
}
