import 'package:flutter/material.dart';
import 'package:flutter_form/bottom_nav.dart';
import 'package:flutter_form/home.dart';
import 'package:flutter_form/my_account.dart';
import 'package:flutter_form/my_booking.dart';
import 'package:flutter_form/top_nav.dart';

class UserDashboard extends StatefulWidget {
  const UserDashboard({super.key});

  @override
  State<UserDashboard> createState() => _UserDashboardState();
}

class _UserDashboardState extends State<UserDashboard>
    with SingleTickerProviderStateMixin {
  late TabController _tabController;
  @override
  void initState() {
    _tabController = TabController(length: 3, vsync: this);
    super.initState();
  }

  @override
  void dispose() {
    super.dispose();
    _tabController.dispose();
  }
  final _selectedColor = const Color.fromARGB(255, 28, 178, 178);
  final _unselectedColor = const Color(0xff5f6368);
  @override
  Widget build(BuildContext context) {
    return Scaffold(
        appBar: const TopNav(),
        body: TabBarView(
          controller: _tabController,
          children: const [
            Home(),
            MyBookings(),
            MyAccount(),
          ],
        ),
        bottomNavigationBar: BottomAppBar(
          child: TabBar(
            controller: _tabController,
            labelColor: _selectedColor,
            indicatorColor: _selectedColor,
            unselectedLabelColor: _unselectedColor,
            tabs: const [
              Tab(icon: Icon(Icons.home), text: "Home"),
              Tab(icon: Icon(Icons.book), text: "My bookings"),
              Tab(icon: Icon(Icons.person), text: "Account"),
            ],
          ),
        ));
  }
}
