import 'dart:ui';
import 'package:flutter/material.dart';
import 'package:flutter_form/search.dart';


class Home extends StatefulWidget {
  const Home({Key? key}) : super(key: key);

  @override
  State<Home> createState() => _HomeState();
}


class _HomeState extends State<Home> {
  void search() {
    Navigator.push(
        context,
        MaterialPageRoute(
          builder: (context) => Search()
        ));
  }
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: Stack(
        children: [
          // Background Image
          Container(
            decoration: BoxDecoration(
              image: DecorationImage(
                image: AssetImage('assets/themebg3.png'),
                fit: BoxFit.cover,
              ),
            ),
          ),
          // Blurred Container
          Positioned.fill(
            child: Container(
              color: Colors.black.withOpacity(0.1), // Add a semi-transparent black color
              child: BackdropFilter(
                filter: ImageFilter.blur(sigmaX: 2, sigmaY: 2), // Apply blur effect
                child: Padding(
                  padding: const EdgeInsets.all(16.0),
                  child: Column(
                    crossAxisAlignment: CrossAxisAlignment.stretch,
                    mainAxisSize: MainAxisSize.min,
                    children: [
                      Container(
                        padding: EdgeInsets.all(16.0),
                        decoration: BoxDecoration(
                          color: Colors.white.withOpacity(0.7), // Add a semi-transparent white color
                          borderRadius: BorderRadius.circular(10.0), // Add rounded corners
                        ),
                        child: Column(
                          crossAxisAlignment: CrossAxisAlignment.stretch,
                          children: [
                            const Text(
                              'Select Departure:',
                              style: TextStyle(fontSize: 15, fontWeight: FontWeight.bold),
                            ),
                            const SizedBox(height: 10),
                            ElevatedButton(
                              onPressed: () {
                                _showDepartureDialog(context);
                              },
                              style: ElevatedButton.styleFrom(
                                shape: RoundedRectangleBorder(
                                  borderRadius: BorderRadius.circular(8.0), // Rounded corners
                                ),
                                 backgroundColor: Color.fromARGB(255, 216, 124, 62)
                                ),
                              child: Text(
                                'Departure',
                                style: TextStyle( fontSize: 15, color: Colors.white),
                                
                                 // White text color
                              ),
                            ),
                            const SizedBox(height: 10),
                            const Text(
                              'Select Destination:',
                              style: TextStyle(fontSize: 15, fontWeight: FontWeight.bold),
                            ),
                            const SizedBox(height: 10),
                            ElevatedButton(
                              onPressed: () {
                                _showDestinationDialog(context);
                              },
                              style: ElevatedButton.styleFrom(
                                shape: RoundedRectangleBorder(
                                  borderRadius: BorderRadius.circular(8.0), // Rounded corners
                                ),
                                backgroundColor: Color.fromARGB(255, 216, 124, 62)
                              ),
                              child: Text(
                                'Destination',
                                style: TextStyle(fontSize: 15,color: Colors.white), // White text color
                              ),
                            ),
                            const SizedBox(height: 20),
                            const Text(
                              'Select Date:',
                              style: TextStyle(fontSize: 15, fontWeight: FontWeight.bold),
                            ),
                            const SizedBox(height: 10),
                            GestureDetector(
                              onTap: () {},
                              child: Container(
                                padding: const EdgeInsets.all(10),
                                decoration: BoxDecoration(
                                  border: Border.all(color: Colors.grey),
                                  borderRadius: BorderRadius.circular(5),
                                ),
                                child: const Row(
                                  mainAxisAlignment: MainAxisAlignment.spaceBetween,
                                  children: [
                                    Text('Select Date'),
                                    Icon(Icons.calendar_today),
                                  ],
                                ),
                              ),
                            ),
                          ],
                        ),
                      ),
                      const SizedBox(height: 20),
                      ElevatedButton(
                        onPressed: () {
                              search();
                            },
                        style: ElevatedButton.styleFrom(
                          shape: RoundedRectangleBorder(
                            borderRadius: BorderRadius.circular(8.0), // Rounded corners
                          ), backgroundColor: Colors.teal.shade300
                        ),
                        child: const Text(
                          'Search',
                          style: TextStyle(fontSize: 15,color: Colors.white), // White text color
                        ),
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

  void _showDepartureDialog(BuildContext context) {
    showDialog(
      context: context,
      builder: (BuildContext context) {
        return AlertDialog(
          title: Text('Select Departure'),
          content: Column(
            mainAxisSize: MainAxisSize.min,
            children: [
              DropdownButton<String>(
                items: <String>['state 1', 'state 2', 'state 3']
                    .map((String value) {
                  return DropdownMenuItem<String>(
                    value: value,
                    child: Text(value),
                  );
                }).toList(),
                onChanged: (_) {},
                hint: const Text('Select state'),
              ),
              const SizedBox(width: 10),
              DropdownButton<String>(
                items: <String>['District 1', 'District 2', 'District 3']
                    .map((String value) {
                  return DropdownMenuItem<String>(
                    value: value,
                    child: Text(value),
                  );
                }).toList(),
                onChanged: (_) {},
                hint: const Text('Select District'),
              ),
              const SizedBox(width: 10),
              DropdownButton<String>(
                items: <String>['place 1', 'place 2', 'place 3']
                    .map((String value) {
                  return DropdownMenuItem<String>(
                    value: value,
                    child: Text(value),
                  );
                }).toList(),
                onChanged: (_) {},
                hint: const Text('Select place'),
              ),
            ],
          ),
          actions: [
            TextButton(
              onPressed: () {
                Navigator.pop(context);
              },
              child: Text('OK'),
            ),
          ],
        );
      },
    );
  }

  void _showDestinationDialog(BuildContext context) {
    showDialog(
      context: context,
      builder: (BuildContext context) {
        return AlertDialog(
          title: Text('Select Destination'),
          content: Column(
            mainAxisSize: MainAxisSize.min,
            children: [
              DropdownButton<String>(
                items: <String>['state 1', 'state 2', 'state 3']
                    .map((String value) {
                  return DropdownMenuItem<String>(
                    value: value,
                    child: Text(value),
                  );
                }).toList(),
                onChanged: (_) {},
                hint: const Text('Select state'),
              ),
              const SizedBox(width: 10),
              DropdownButton<String>(
                items: <String>['District 1', 'District 2', 'District 3']
                    .map((String value) {
                  return DropdownMenuItem<String>(
                    value: value,
                    child: Text(value),
                  );
                }).toList(),
                onChanged: (_) {},
                hint: const Text('Select District'),
              ),
              const SizedBox(width: 10),
              DropdownButton<String>(
                items: <String>['place 1', 'place 2', 'place 3']
                    .map((String value) {
                  return DropdownMenuItem<String>(
                    value: value,
                    child: Text(value),
                  );
                }).toList(),
                onChanged: (_) {},
                hint: const Text('Select place'),
              ),
            ],
          ),
          actions: [
            TextButton(
              onPressed: () {
                Navigator.pop(context);
              },
              child: Text('OK'),
            ),
          ],
        );
      },
    );
  }
}
