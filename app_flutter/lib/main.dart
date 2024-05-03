import 'dart:async';
import 'dart:html' as html;

import 'package:flutter/material.dart';
import 'package:intl/intl.dart';
import 'package:url_strategy/url_strategy.dart';

void main() {
  runApp(
    MaterialApp(
      title: 'Reading and Writing Files',
      initialRoute: '/',
      routes: {
        '/': (context) => FlutterDemo(),
        '/visits': (context) => VisitsPage(),
      },
    ),
  );
}

class FlutterDemo extends StatelessWidget {
  const FlutterDemo({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text('Reading and Writing Files'),
      ),
      body: Center(
        child: FutureBuilder<DateTime>(
          future: _getMoscowTime(),
          builder: (context, snapshot) {
            if (snapshot.hasData) {
              return Text(
                'Current time in Moscow: ${DateFormat.jm().format(snapshot.data!)}',
              );
            } else if (snapshot.hasError) {
              return Text('Error: ${snapshot.error}');
            } else {
              return CircularProgressIndicator();
            }
          },
        ),
      ),
      floatingActionButton: FloatingActionButton(
        onPressed: () {
          Navigator.pushNamed(context, '/visits');
        }
        , 
        child: const Icon(Icons.list),
      ),
    );
  }

  Future<DateTime> _getMoscowTime() async {
    final now = DateTime.now();
    final moscowTime = now.add(Duration(hours: 3));
    final counterValue = html.window.localStorage['counter'];

    if (counterValue == null) {
      html.window.localStorage['counter'] = '1';
    } else {
      html.window.localStorage['counter'] = (int.parse(counterValue) + 1).toString();
    }
    return moscowTime;
  }
}

class VisitsPage extends StatelessWidget {
  const VisitsPage({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text('Number of Visits'),
      ),
      body: Center(
        child: FutureBuilder<int>(
          future: _readCounter(),
          builder: (context, snapshot) {
            if (snapshot.hasData) {
              return Text(
                'Number of visits: ${snapshot.data}',
              );
            } else if (snapshot.hasError) {
              return Text('Error: ${snapshot.error}');
            } else {
              return CircularProgressIndicator();
            }
          },
        ),
      ),
    );
  }

  Future<int> _readCounter() async {
    final counterValue = html.window.localStorage['counter'];
    if (counterValue == null) {
      return 0;
    } else {
      return int.parse(counterValue);
    }
  }
}
