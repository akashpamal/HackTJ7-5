import 'package:flutter/material.dart';
import 'input_textbox.dart';
import 'package:flutter/cupertino.dart';


void main() {
  runApp(MaterialApp(
    home: HomePage(),
  ));
}

class HomePage extends StatelessWidget {
  LocationTextBox currentLocationTextBox =
      new LocationTextBox('Current Location');
  LocationTextBox destinationTextBox = new LocationTextBox('Destination');

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text('Transportation'),
        centerTitle: true,
        elevation: 10,
      ),
      body: Padding(
        padding: const EdgeInsets.all(8.0),
        child: Column(
          children: [
            Padding(
              padding: const EdgeInsets.all(8.0),
              child: currentLocationTextBox,
            ),
            Padding(
              padding: const EdgeInsets.all(8.0),
              child: destinationTextBox,
            ),
            Padding(
              padding: const EdgeInsets.all(8.0),
              child: CupertinoButton(
                onPressed: () {
                  print('Button was pressed');
                  print('Current location' + this.currentLocationTextBox.getText());
                },
                color: Colors.blue,
                child: Text('Calculate ETA'),
              ),
//              child: FlatButton(
//                onPressed: () {
//                  print('Button was pressed');
//                },
//                child: Text('Calculate Location'),
//                color: Colors.blue,
//              ),
            ),
          ],
        ),
      ),
    );
  }
}
