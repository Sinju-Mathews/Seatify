import 'dart:ui'; // Import this to use ImageFilter for blur effect
import 'package:flutter/material.dart';

class MyAccount extends StatefulWidget {
  const MyAccount({Key? key}) : super(key: key);

  @override
  State<MyAccount> createState() => _MyAccountState();
}

class _MyAccountState extends State<MyAccount> {
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
    return Stack(
      children: [
        // Background Image
        Container(
          decoration: BoxDecoration(
            image: DecorationImage(
              image: AssetImage('assets/themebg4.png'),
              fit: BoxFit.cover,
            ),
          ),
        ),
        // Blurred Container
        Positioned.fill(
          child: Container(
            color: Colors.black.withOpacity(0.2), // Add a semi-transparent black color
            child: BackdropFilter(
              filter: ImageFilter.blur(sigmaX: 2, sigmaY: 2), // Apply blur effect
              child: Center(
                child: Container(
                  height: 400,
                  width: 250,
                  padding: EdgeInsets.all(10),
                  decoration: BoxDecoration(
                    color: Colors.white.withOpacity(0.7), // Add a semi-transparent white color
                    borderRadius: BorderRadius.circular(10.0), // Add rounded corners
                  ),
                  child: Column(
                    mainAxisAlignment: MainAxisAlignment.center,
                    children: <Widget>[
                      CircleAvatar(
                        radius: 50,
                        // Placeholder for user's profile picture
                        backgroundImage: AssetImage('assets/profile_placeholder.png'),
                      ),
                      SizedBox(height: 20),
                      Text(
                        'John Doe',
                        style: TextStyle(fontSize: 24, fontWeight: FontWeight.bold),
                      ),
                      SizedBox(height: 10),
                      Text(
                        'john.doe@example.com',
                        style: TextStyle(fontSize: 18),
                      ),
                      SizedBox(height: 20),
                      ElevatedButton(
                        onPressed: () {
                          // Add functionality for editing profile
                        },
                        child: Text('Edit Profile'),
                      ),
                      ElevatedButton(
                        onPressed: () {
                          // Add functionality for signing out
                        },
                        child: Text('Sign Out'),
                      ),
                    ],
                  ),
                ),
              ),
            ),
          ),
        ),
      ],
    );
  }
}
