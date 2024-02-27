import 'package:flutter/material.dart';
import 'dart:ui';
import 'package:flutter_form/sign_up.dart';

class LoginScreen extends StatefulWidget {
  const LoginScreen({super.key});

  @override
  State<LoginScreen> createState() => _LoginScreenState();
}

class _LoginScreenState extends State<LoginScreen> {
  final _formKey = GlobalKey<FormState>();
  TextEditingController _emailController = TextEditingController();
  TextEditingController _passController = TextEditingController();
  bool passkey = true;

  void login() {
    print(_emailController.text);
    Navigator.push(
        context,
        MaterialPageRoute(
          builder: (context) => SignUp(),
        ));
  }

  void Signup() {
    print(_emailController.text);
    Navigator.push(
        context,
        MaterialPageRoute(
          builder: (context) => SignUp(),
        ));
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: Stack(
        children: [
          // Background Image with Blur
          Positioned.fill(
            child: Image.asset(
              'assets/bus.jpg',
              fit: BoxFit.cover,
            ),
          ),
          Positioned.fill(
            child: BackdropFilter(
              filter: ImageFilter.blur(sigmaX: 5, sigmaY: 5),
              child: Container(
                color:
                    Colors.black.withOpacity(0.5), // Adjust opacity as needed
              ),
            ),
          ),

          // Login Form
          Center(
            child: Container(
              padding: EdgeInsets.all(20),
              child: Form(
                key: _formKey,
                child: SingleChildScrollView(
                  child: Column(
                    children: [
                      const Center(
                        child: Text(
                          'Seatify',
                          style: TextStyle(
                            fontSize: 60,
                            fontStyle: FontStyle.italic,
                            fontFamily: 'Seatify',
                            color: Colors.white,
                            shadows: <Shadow>[
                              Shadow(
                                offset: Offset(2.0, 2.0),
                                blurRadius: 3.0,
                                color: Colors.grey,
                              ),
                            ],
                          ),
                        ),
                      ),
                      Container(
                        decoration: BoxDecoration(
                          color: Colors
                              .transparent, // Set container background color to transparent
                          borderRadius: BorderRadius.circular(40),
                        ),
                        padding: EdgeInsets.all(7),
                        child: TextFormField(
                          validator: (value) {
                            if (value == null || value.isEmpty) {
                              return 'Please enter Email';
                            }
                            return null;
                          },
                          style: TextStyle(
                              color: Colors.white), // Set text color to white
                          decoration: InputDecoration(
                            hintText: 'Email',
                            hintStyle: TextStyle(
                                color: Colors
                                    .white), // Set hint text color to white
                          ),
                          keyboardType: TextInputType.emailAddress,
                          controller: _emailController,
                        ),
                      ),
                      SizedBox(
                        height: 50,
                      ),
                      Container(
                        decoration: BoxDecoration(
                            color: Colors.transparent,
                            borderRadius: BorderRadius.circular(40)),
                        padding: EdgeInsets.all(7),
                        child: TextFormField(
                          validator: (value) {
                            if (value == null || value.isEmpty) {
                              return 'Please enter Password';
                            }
                            return null;
                          },
                          decoration: InputDecoration(
                            suffixIcon: InkWell(
                              onTap: () {
                                setState(() {
                                  passkey = !passkey;
                                });
                              },
                              child: Icon(passkey
                                  ? Icons.visibility_off
                                  : Icons.visibility),
                            ),
                            hintText: 'Password',
                            hintStyle: TextStyle(color: Colors.white),
                          ),
                          obscureText: passkey,
                          keyboardType: TextInputType.visiblePassword,
                          controller: _passController,
                        ),
                      ),
                      SizedBox(
                        height: 50,
                      ),
                      Row(
                        mainAxisAlignment: MainAxisAlignment.spaceEvenly,
                        children: [
                          ElevatedButton.icon(
                            onPressed: () {
                              if (_formKey.currentState!.validate()) {
                                login();
                              }
                            },
                            icon: const Icon(Icons.login_outlined),
                            label: const Text('Login'),
                          ),
                          ElevatedButton.icon(
                            onPressed: () {
                              Signup();
                            },
                            icon: const Icon(Icons.account_circle_outlined),
                            label: const Text('SIGN UP'),
                          ),
                        ],
                      ),
                    ],
                  ),
                ),
              ),
            ),
          ),
        ],
      ),
    );
  }
}
