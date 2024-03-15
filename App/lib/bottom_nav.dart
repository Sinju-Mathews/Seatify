import 'package:flutter/material.dart';
import 'package:flutter_form/home.dart';
import 'package:flutter_form/my_account.dart';
import 'package:flutter_form/my_booking.dart';
import 'package:flutter_form/user_dashboard.dart';

class BottomNav extends StatefulWidget {
  final TabController? tabController;
  const BottomNav({Key? key, required this.tabController}) : super(key: key);

  @override
  _BottomNavState createState() => _BottomNavState();
}

class _BottomNavState extends State<BottomNav>
    with SingleTickerProviderStateMixin {
  late TabController _tabController;

  final _selectedColor = const Color.fromARGB(255, 28, 178, 178);
  final _unselectedColor = const Color(0xff5f6368);

  final _tabs = [
    const Tab(icon: Icon(Icons.home), text: "Home"),
    const Tab(icon: Icon(Icons.book), text: "My bookings"),
    const Tab(icon: Icon(Icons.person), text: "Account"),
  ];

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

  void _navigateToScreen(int index) {
    switch (index) {
      case 0:
        // Call Home function
        Navigator.push(context, MaterialPageRoute(builder: (context) => Home(),));
        break;
      case 1:
        // Call MyBookings function
        Navigator.push(context, MaterialPageRoute(builder: (context) => MyBookings(),));
        break;
      case 2:
        // Call MyAccount function
        Navigator.push(context, MaterialPageRoute(builder: (context) => MyAccount(),));
        break;
    }
  }

  @override
  Widget build(BuildContext context) {
    return Padding(
      padding: const EdgeInsets.all(8.0),
      child: Row(
        children: [
          Flexible(
            child: TabBar(
              controller: widget.tabController,
              tabs: _tabs,
              labelColor: _selectedColor,
              indicatorColor: _selectedColor,
              unselectedLabelColor: _unselectedColor,
              indicatorSize: TabBarIndicatorSize.label,
              onTap: _navigateToScreen,
            ),
          ),
        ],
      ),
    );
  }
}
