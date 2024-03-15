import 'package:flutter/material.dart';

class TopNav extends StatefulWidget {
  const TopNav({super.key});

  @override
   _TopNavState createState() => _TopNavState();
}
   class _TopNavState extends State<TopNav>{
   @override
     Widget build(BuildContext context) {
    return Scaffold(
          appBar: AppBar(
            leading: IconButton(
                onPressed: () {}, icon: const Icon(Icons.arrow_back_ios)),
            title: const Text('rabbit'),
            actions: [
              IconButton(onPressed: (){}, icon: const Icon(Icons.exit_to_app))
            ],
          ),
      );
   }
}
