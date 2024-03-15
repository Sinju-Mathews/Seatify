import 'package:flutter/material.dart';
class BottomNav extends StatefulWidget {
  const BottomNav({super.key});

  @override
  _BottomNavState createState() => _BottomNavState();
}

class _BottomNavState extends State<BottomNav>
    with SingleTickerProviderStateMixin {
  late TabController _tabController;

  final _selectedColor =  const Color.fromARGB(255, 28, 178, 178);
  final _unselectedColor = const Color(0xff5f6368);


  final _tabs = [
    const Tab(icon: Icon(Icons.home), text: "Home",),
    const Tab(icon: Icon(Icons.book),text: "My bookings"),
    const Tab(icon: Icon(Icons.person),text: "Account"),
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

  @override
  Widget build(BuildContext context) {
    return Padding(
        padding: const EdgeInsets.all(8.0),
        child: Row(
          children: [
            ///Default Tabbar with indicator width of the label
            Flexible(
              child: TabBar(
                controller: _tabController,
                tabs: _tabs,
                labelColor: _selectedColor,
                indicatorColor: _selectedColor,
                unselectedLabelColor: _unselectedColor,
                indicatorSize: TabBarIndicatorSize.label,
              ),
            ),
        
            /// Custom Material Design tabbar used in google's products
          
          ]
              
        ),
      );
  }
}