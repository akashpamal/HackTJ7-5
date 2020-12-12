import 'package:flutter/cupertino.dart';
import 'package:flutter/material.dart';

class LocationTextBox extends StatelessWidget {
  Color borderColor = Colors.purple;

  TextEditingController textFieldController = new TextEditingController();
  String hintText;

  LocationTextBox(this.hintText);

  @override
  Widget build(BuildContext context) {
    return TextFormField(
      controller: this.textFieldController,
      textAlign: TextAlign.left,
      decoration: InputDecoration(
        labelText: '${this.hintText}',
//            labelStyle: TextStyle(height:5, fontWeight: FontWeight.bold),
        border: OutlineInputBorder(),
//        disabledBorder: OutlineInputBorder(
//            borderSide: BorderSide(color: Colors.green, width: 20)),
        enabledBorder: OutlineInputBorder(
            borderSide: BorderSide(color: Colors.blue, width: 2)),
        hintText: 'Enter ' + this.hintText,
        hintStyle: TextStyle(color: Colors.grey),
      ),
      // ignore: missing_return
      validator: (value) {
        if (value.isEmpty) {
          return 'Please enter ${this.hintText}';
        }
      },
    );
  }

  String getText() {
    return this.textFieldController.text;
  }
}
