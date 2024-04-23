import 'dart:html';
import 'package:cloud_firestore/cloud_firestore.dart';

void main() {
  updateCounter();
  querySelector('#output')?.text = 'Your Dart app is running.';
}

void updateCounter() async {
  final cRef = FirebaseFirestore.instance.collection('VISITS');
  await cRef
      .doc(
      "DloKdWlOkFqIi08SmtuP") //the id which was generated automatically
      .set({"count": FieldValue.increment(1)}, SetOptions(merge: true));
}