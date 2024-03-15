import 'package:flutter/material.dart';
import 'package:flutter_form/bottom_nav.dart';
import 'package:flutter_form/top_nav.dart';

class MyAccount extends StatefulWidget {
  const MyAccount({super.key});

  @override
  State<MyAccount> createState() => _MyAccountState();
}

class _MyAccountState extends State<MyAccount> {
  @override
   String _userName = '';
  String _userEmail = '';

  void _fetchUserDataFromFirebase() {
    // Your code to retrieve data from Firebase Firestore
    // For example:
    // firestoreInstance.collection("users").doc(userId).get().then((value) {
    //   setState(() {
    //     _userName = value.data()["name"];
    //     _userEmail = value.data()["email"];
    //   });
    // });
  }
  @override
  void initState() {
    super.initState();
    // Fetch user data when the screen is first initialized
    _fetchUserDataFromFirebase();
  }
   @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text('User Profile'),
      ),
      body: Center(
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: <Widget>[
            CircleAvatar(
              radius: 50,
              // You can add user's profile picture here
              // For example: backgroundImage: NetworkImage('user_profile_image_url'),
            ),
            SizedBox(height: 20),
            Text(
              _userName,
              style: TextStyle(fontSize: 24, fontWeight: FontWeight.bold),
            ),
            SizedBox(height: 10),
            Text(
              _userEmail,
              style: TextStyle(fontSize: 18),
            ),
          ],
        ),
      ),
    );
  }
}
