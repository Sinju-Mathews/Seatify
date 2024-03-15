import 'package:flutter/material.dart';
import 'package:flutter_form/bottom_nav.dart';
import 'package:flutter_form/top_nav.dart';

class MyBookings extends StatefulWidget {
  const MyBookings({super.key});

  @override
  State<MyBookings> createState() => _MyBookingsState();
}

class _MyBookingsState extends State<MyBookings> {
  @override
  Widget build(BuildContext context) {
    return Center(
      child: Text('Booking'),
    );
  }
}
