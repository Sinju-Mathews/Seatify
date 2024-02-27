import 'dart:io';

import 'package:flutter/material.dart';
import 'package:flutter/widgets.dart';
import 'package:flutter_form/login_screen.dart';
import 'package:image_picker/image_picker.dart';
import 'dart:ui';

class SignUp extends StatefulWidget {
  const SignUp({super.key});

  @override
  State<SignUp> createState() => _SignUpState();
}

class _SignUpState extends State<SignUp> {
  final _formKey = GlobalKey<FormState>();
  bool agreePersonalData = true;
  XFile? _selectedImage;
  String? _imageUrl;
  TextEditingController _nameController = TextEditingController();
  TextEditingController _emailController = TextEditingController();
  TextEditingController _dobController = TextEditingController();
  TextEditingController _addressController = TextEditingController();
  TextEditingController _passController = TextEditingController();

  Future<void> _pickImage() async {
    final pickedFile =
        await ImagePicker().pickImage(source: ImageSource.gallery);

    if (pickedFile != null) {
      setState(() {
        _selectedImage = XFile(pickedFile.path);
      });
    }
  }

  List<Map<String, dynamic>> state = [
    {'id': 'Kerala', 'name': 'Kerala'},
    {'id': 'Tamilnadu', 'name': 'Tamilnadu'},
    {'id': 'Rajasthan', 'name': 'Rajasthan'},
  ];

  String? selectstate;

  List<Map<String, dynamic>> district = [
    {'id': 'ernakulam', 'name': 'Ernakulam'},
    {'id': 'idukki', 'name': 'Idukki'},
    {'id': 'kottayam', 'name': 'Kottayam'},
  ];

  String? selectdistrict;

  List<Map<String, dynamic>> place = [
    {'id': 'muvattupuzha', 'name': 'Muvattupuzha'},
    {'id': 'aluva', 'name': 'Aluva'},
    {'id': 'guruvayoor', 'name': 'Guruvayoor'},
  ];

  String? selectplace;

  String? selectedGender;

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
          builder: (context) => LoginScreen(),
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
                      Center(
                        child: GestureDetector(
                          onTap: _pickImage,
                          child: Stack(
                            children: [
                              CircleAvatar(
                                radius: 50,
                                backgroundColor:
                                    Color.fromARGB(255, 84, 115, 120),
                                backgroundImage: _selectedImage != null
                                    ? FileImage(File(_selectedImage!.path))
                                    : _imageUrl != null
                                        ? NetworkImage(_imageUrl!)
                                        : const AssetImage(
                                                'assets/images/dummy-profile-pic.png')
                                            as ImageProvider,
                                child: _selectedImage == null &&
                                        _imageUrl == null
                                    ? const Icon(
                                        Icons.add,
                                        size: 40,
                                        color:
                                            Color.fromARGB(255, 240, 239, 239),
                                      )
                                    : null,
                              ),
                              if (_selectedImage != null || _imageUrl != null)
                                const Positioned(
                                  bottom: 0,
                                  right: 0,
                                  child: CircleAvatar(
                                    backgroundColor: Colors.white,
                                    radius: 18,
                                    child: Icon(
                                      Icons.edit,
                                      size: 18,
                                      color: Color.fromARGB(255, 238, 231, 231),
                                    ),
                                  ),
                                ),
                            ],
                          ),
                        ),
                      ),
                      SizedBox(
                        height: 50,
                      ),
                      TextFormField(
                        style: TextStyle(color: Colors.white),
                        controller: _nameController,
                        validator: (value) {
                          if (value == null || value.isEmpty) {
                            return 'Please enter Full name';
                          }
                          return null;
                        },
                        decoration: InputDecoration(
                          label: const Text('Full Name'),
                          labelStyle:
                              TextStyle(color: Colors.tealAccent.shade100),
                          hintText: 'Enter Full Name',
                          hintStyle: const TextStyle(
                            color: Color.fromARGB(255, 255, 255, 255),
                          ),
                          border: OutlineInputBorder(
                            borderSide: const BorderSide(
                              color: Color.fromARGB(
                                  255, 255, 255, 255), // Default border color
                            ),
                            borderRadius: BorderRadius.circular(10),
                          ),
                          enabledBorder: OutlineInputBorder(
                            borderSide: const BorderSide(
                              color: Color.fromARGB(
                                  255, 249, 249, 249), // Default border color
                            ),
                            borderRadius: BorderRadius.circular(10),
                          ),
                        ),
                      ),
                      SizedBox(
                        height: 50,
                      ),
                      TextFormField(
                        style: TextStyle(color: Colors.white),
                        controller: _emailController,
                        validator: (value) {
                          if (value == null || value.isEmpty) {
                            return 'Please enter Email';
                          }
                          return null;
                        },
                        decoration: InputDecoration(
                          label: const Text('Email'),
                          labelStyle:
                              TextStyle(color: Colors.tealAccent.shade100),
                          hintText: 'Enter Email',
                          hintStyle: const TextStyle(
                            color: Color.fromARGB(255, 255, 255, 255),
                          ),
                          border: OutlineInputBorder(
                            borderSide: const BorderSide(
                              color: Color.fromARGB(
                                  255, 255, 255, 255), // Default border color
                            ),
                            borderRadius: BorderRadius.circular(10),
                          ),
                          enabledBorder: OutlineInputBorder(
                            borderSide: const BorderSide(
                              color: Color.fromARGB(
                                  255, 255, 255, 255), // Default border color
                            ),
                            borderRadius: BorderRadius.circular(10),
                          ),
                        ),
                      ),
                      SizedBox(
                        height: 50,
                      ),
                      TextFormField(
                        style: TextStyle(color: Colors.white),
                        controller: _dobController,
                        validator: (value) {
                          if (value == null || value.isEmpty) {
                            return 'Please enter Email';
                          }
                          return null;
                        },
                        keyboardType: TextInputType.datetime,
                        decoration: InputDecoration(
                          label: const Text('DOB'),
                          labelStyle:
                              TextStyle(color: Colors.tealAccent.shade100),
                          hintText: 'Enter Date of Birth',
                          hintStyle: const TextStyle(
                            color: Color.fromARGB(255, 255, 255, 255),
                          ),
                          border: OutlineInputBorder(
                            borderSide: const BorderSide(
                              color: Color.fromARGB(
                                  255, 255, 255, 255), // Default border color
                            ),
                            borderRadius: BorderRadius.circular(10),
                          ),
                          enabledBorder: OutlineInputBorder(
                            borderSide: const BorderSide(
                              color: Color.fromARGB(
                                  255, 255, 255, 255), // Default border color
                            ),
                            borderRadius: BorderRadius.circular(10),
                          ),
                        ),
                      ),
                      SizedBox(
                        height: 50,
                      ),
                      Padding(
                        padding: const EdgeInsets.only(left: 5, right: 5),
                        child: Row(
                          mainAxisAlignment: MainAxisAlignment.spaceBetween,
                          children: [
                            const Text(
                              'Gender: ',
                              style: TextStyle(
                                  fontWeight: FontWeight.w400,
                                  fontSize: 16,
                                  color: Colors.white),
                            ),
                            Row(
                              children: [
                                Radio<String>(
                                  fillColor:
                                      MaterialStatePropertyAll(Colors.white),
                                  value: 'Male',
                                  groupValue: selectedGender,
                                  onChanged: (value) {
                                    setState(() {
                                      selectedGender = value!;
                                    });
                                  },
                                ),
                                const Text('Male',
                                    style: TextStyle(color: Colors.white)),
                              ],
                            ),
                            Row(
                              children: [
                                Radio<String>(
                                  fillColor:
                                      MaterialStatePropertyAll(Colors.white),
                                  value: 'Female',
                                  groupValue: selectedGender,
                                  onChanged: (value) {
                                    setState(() {
                                      selectedGender = value!;
                                    });
                                  },
                                ),
                                const Text('Female',
                                    style: TextStyle(color: Colors.white)),
                              ],
                            ),
                            Row(
                              children: [
                                Radio<String>(
                                  fillColor:
                                      MaterialStatePropertyAll(Colors.white),
                                  value: 'Others',
                                  groupValue: selectedGender,
                                  onChanged: (value) {
                                    setState(() {
                                      selectedGender = value!;
                                    });
                                  },
                                ),
                                const Text('Others',
                                    style: TextStyle(color: Colors.white)),
                              ],
                            ),
                          ],
                        ),
                      ),
                      SizedBox(
                        height: 50,
                      ),
                      DropdownButtonFormField<String>(
                        dropdownColor: Color.fromARGB(220, 60, 87, 87),
                        value: selectstate,
                        decoration: InputDecoration(
                          label: const Text('State'),
                          labelStyle:
                              TextStyle(color: Colors.tealAccent.shade100),
                          hintText: 'Select state',
                          hintStyle: const TextStyle(
                            color: Colors.white,
                          ),
                          border: OutlineInputBorder(
                            borderSide: const BorderSide(
                              color: Colors.white, // Default border color
                            ),
                            borderRadius: BorderRadius.circular(10),
                          ),
                          enabledBorder: OutlineInputBorder(
                            borderSide: const BorderSide(
                              color: Colors.white, // Default border color
                            ),
                            borderRadius: BorderRadius.circular(10),
                          ),
                        ),
                        onChanged: (String? newValue) {
                          setState(() {
                            selectstate = newValue;
                          });
                        },
                        isExpanded: true,
                        items: state.map<DropdownMenuItem<String>>(
                          (Map<String, dynamic> stat) {
                            return DropdownMenuItem<String>(
                              value: stat['id'],
                              child: Text(stat['name'],
                                  style: TextStyle(color: Colors.white)),
                            );
                          },
                        ).toList(),
                      ),
                      SizedBox(
                        height: 50,
                      ),
                      DropdownButtonFormField<String>(
                        dropdownColor: Color.fromARGB(220, 60, 87, 87),
                        value: selectdistrict,
                        decoration: InputDecoration(
                          label: const Text('District'),
                          labelStyle:
                              TextStyle(color: Colors.tealAccent.shade100),
                          hintText: 'Select District',
                          hintStyle: const TextStyle(
                            color: Colors.white,
                          ),
                          border: OutlineInputBorder(
                            borderSide: const BorderSide(
                              color: Colors.white, // Default border color
                            ),
                            borderRadius: BorderRadius.circular(10),
                          ),
                          enabledBorder: OutlineInputBorder(
                            borderSide: const BorderSide(
                              color: Colors.white, // Default border color
                            ),
                            borderRadius: BorderRadius.circular(10),
                          ),
                        ),
                        onChanged: (String? newValue) {
                          setState(() {
                            selectdistrict = newValue;
                          });
                        },
                        isExpanded: true,
                        items: district.map<DropdownMenuItem<String>>(
                          (Map<String, dynamic> dist) {
                            return DropdownMenuItem<String>(
                              value: dist['id'],
                              child: Text(dist['name'],
                                  style: TextStyle(color: Colors.white)),
                            );
                          },
                        ).toList(),
                      ),
                      SizedBox(
                        height: 50,
                      ),
                      DropdownButtonFormField<String>(
                        dropdownColor: Color.fromARGB(220, 60, 87, 87),
                        value: selectplace,
                        decoration: InputDecoration(
                          label: const Text('Place'),
                          labelStyle:
                              TextStyle(color: Colors.tealAccent.shade100),
                          hintText: 'Select Place',
                          hintStyle: const TextStyle(
                            color: Colors.white,
                          ),
                          border: OutlineInputBorder(
                            borderSide: const BorderSide(
                              color: Colors.white, // Default border color
                            ),
                            borderRadius: BorderRadius.circular(10),
                          ),
                          enabledBorder: OutlineInputBorder(
                            borderSide: const BorderSide(
                              color: Colors.white, // Default border color
                            ),
                            borderRadius: BorderRadius.circular(10),
                          ),
                        ),
                        onChanged: (String? newValue) {
                          setState(() {
                            selectplace = newValue;
                          });
                        },
                        isExpanded: true,
                        items: place.map<DropdownMenuItem<String>>(
                          (Map<String, dynamic> place) {
                            return DropdownMenuItem<String>(
                              value: place['id'],
                              child: Text(place['name'],
                                  style: TextStyle(color: Colors.white)),
                            );
                          },
                        ).toList(),
                      ),
                      SizedBox(
                        height: 50,
                      ),
                      TextFormField(
                        style: TextStyle(color: Colors.white),
                        controller: _addressController,
                        validator: (value) {
                          if (value == null || value.isEmpty) {
                            return 'Please enter address';
                          }
                          return null;
                        },
                        keyboardType: TextInputType.multiline,
                        decoration: InputDecoration(
                          label: const Text('Address'),
                          labelStyle:
                              TextStyle(color: Colors.tealAccent.shade100),
                          hintText: 'Enter Address',
                          hintStyle: const TextStyle(
                            color: Colors.white,
                          ),
                          border: OutlineInputBorder(
                            borderSide: const BorderSide(
                              color: Colors.white, // Default border color
                            ),
                            borderRadius: BorderRadius.circular(10),
                          ),
                          enabledBorder: OutlineInputBorder(
                            borderSide: const BorderSide(
                              color: Colors.white, // Default border color
                            ),
                            borderRadius: BorderRadius.circular(10),
                          ),
                        ),
                      ),
                      SizedBox(
                        height: 50,
                      ),
                      TextFormField(
                        style: TextStyle(color: Colors.white),
                        controller: _passController,
                        obscureText: true,
                        obscuringCharacter: '*',
                        validator: (value) {
                          if (value == null || value.isEmpty) {
                            return 'Please enter Password';
                          }
                          return null;
                        },
                        decoration: InputDecoration(
                          label: const Text('Password'),
                          labelStyle:
                              TextStyle(color: Colors.tealAccent.shade100),
                          hintText: 'Enter Password',
                          hintStyle: const TextStyle(
                            color: Colors.white,
                          ),
                          border: OutlineInputBorder(
                            borderSide: const BorderSide(
                              color: Colors.white, // Default border color
                            ),
                            borderRadius: BorderRadius.circular(10),
                          ),
                          enabledBorder: OutlineInputBorder(
                            borderSide: const BorderSide(
                              color: Colors.white, // Default border color
                            ),
                            borderRadius: BorderRadius.circular(10),
                          ),
                        ),
                      ),
                      SizedBox(
                        height: 50,
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
                ),
              ),
            ),
          ),
        ],
      ),
    );
  }
}
