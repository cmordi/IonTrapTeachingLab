void setup() {
  Serial.begin(9600);     // sets up serial communication for user input
  
  pinMode(22, OUTPUT);    // sets the digital pin 22 as output
  pinMode(23, OUTPUT);    // sets the digital pin 23 as output
  pinMode(24, OUTPUT);    // sets the digital pin 24 as output
  pinMode(25, OUTPUT);    // sets the digital pin 25 as output
  pinMode(26, OUTPUT);    // sets the digital pin 26 as output
  pinMode(27, OUTPUT);    // sets the digital pin 27 as output
  pinMode(28, OUTPUT);    // sets the digital pin 28 as output
  pinMode(29, OUTPUT);    // sets the digital pin 29 as output
  pinMode(30, OUTPUT);    // sets the digital pin 30 as output
  pinMode(31, OUTPUT);    // sets the digital pin 31 as output
}

void loop() {
  Serial.println("\nEnter a sentence containing any number of compatible commands. To see a list of commands, please enter 'commands' without the quotations.");
  
  while (Serial.available() == 0) {
  // only prompts user for input once between inputs
  }

  String input = Serial.readString();
  input.trim();
  Serial.println(input);

  
// COMMANDs
  if(input == "commands"){
    Serial.println("\nThere are five (5) sets of controllable electrodes: a, b, c, d, e. Always begin your command with the electrode set you wish to control, or begin with 'all' to control all at once.");
    Serial.println("The electrodes can be connected to ground via the 'low' command, or to voltage via the 'high' command. The electrodes can be grounded, then disconnected via the 'off' command.");
    Serial.println("Ex.1) a high, b low, c off, d off, e high <enter>");
    Serial.println("Ex.2) a high b high c low d off e high <enter>");
    Serial.println("Ex.3) all off <enter> a low <enter>");
    Serial.println("Ex.4) all off <enter>");
    Serial.println("Note 1: No particular delimiter is necessary (see examples 1 and 2). \nNote 2: Incompatible commands cannot be entered together (see example 3).");
    Serial.println("Please always end your session with the 'all off' command.");
  }


// ERRORs
//  if(){
//
//  }


// ALLs
  if(input.indexOf("all low") > -1){
    // connects all segmented electrodes to ground at once

    // removes paths for voltage
    digitalWrite(22, LOW);
    digitalWrite(24, LOW);
    digitalWrite(26, LOW);
    digitalWrite(28, LOW);
    digitalWrite(30, LOW);
    delay(200);

    // connects all electrodes to ground
    digitalWrite(23, HIGH);
    digitalWrite(25, HIGH);
    digitalWrite(27, HIGH);
    digitalWrite(29, HIGH);
    digitalWrite(31, HIGH);

    Serial.println("Voltage set to low on all arduino controlled electrodes.");
  }


  if(input.indexOf("all high") > -1){
      // turns on voltage for all segmented electrodes at once

      // removes paths for ground
      digitalWrite(23, LOW);
      digitalWrite(25, LOW);
      digitalWrite(27, LOW);
      digitalWrite(29, LOW);
      digitalWrite(31, LOW);
      delay(200);

      // connects paths for voltage
      digitalWrite(22, HIGH);
      digitalWrite(24, HIGH);
      digitalWrite(26, HIGH);
      digitalWrite(28, HIGH);
      digitalWrite(30, HIGH);

      Serial.println("Voltage set to high on all arduino controlled electrodes.");
  }


  if(input.indexOf("all off") > -1){
    // drains voltage and removes voltage paths for all segmented electrodes at once

    Serial.println("Powering off all arduino controlled electrodes...");

    // removes paths for voltage
    digitalWrite(22, LOW);
    digitalWrite(24, LOW);
    digitalWrite(26, LOW);
    digitalWrite(28, LOW);
    digitalWrite(30, LOW);
    delay(200);

    // connects all electrodes to ground to remove any voltage
    digitalWrite(23, HIGH);
    digitalWrite(25, HIGH);
    digitalWrite(27, HIGH);
    digitalWrite(29, HIGH);
    digitalWrite(31, HIGH);
    delay(200);

    // removes paths for ground
    digitalWrite(23, LOW);
    digitalWrite(25, LOW);
    digitalWrite(27, LOW);
    digitalWrite(29, LOW);
    digitalWrite(31, LOW);

    Serial.println("All arduino controlled electrodes powered off.");
  }


// individual LOWs
  if(input.indexOf("a low") > -1){
    digitalWrite(30, LOW); // sets the digital pin 30 to off;
    delay(200);
    digitalWrite(31, HIGH); // sets the digital pin 31 to on;
    Serial.println("Voltage set to low on electrode set 'a.'");
  }

  if(input.indexOf("b low") > -1){
    digitalWrite(28, LOW); // sets the digital pin 28 to off;
    delay(200);
    digitalWrite(29, HIGH); // sets the digital pin 29 to on;
    Serial.println("Voltage set to low on electrode set 'b.'");
  }

  if(input.indexOf("c low") > -1){
    digitalWrite(26, LOW); // sets the digital pin 26 to off;
    delay(200);
    digitalWrite(27, HIGH); // sets the digital pin 27 to on;
    Serial.println("Voltage set to low on electrode set 'c.'");
  }

  if(input.indexOf("d low") > -1){
    digitalWrite(24, LOW); // sets the digital pin 24 to off];
    delay(200);
    digitalWrite(25, HIGH); // sets the digital pin 25 to on;
    Serial.println("Voltage set to low on electrode set 'd.'");
  }

  if(input.indexOf("e low") > -1){
    digitalWrite(22, LOW); // sets the digital pin 22 to off;
    delay(200);
    digitalWrite(23, HIGH); // sets the digital pin 23 to on;
    Serial.println("Voltage set to low on electrode set 'e.'");
  }


// individual HIGHs
  if(input.indexOf("a high") > -1){
    digitalWrite(31, LOW); // sets the digital pin 31 to off;
    delay(200);
    digitalWrite(30, HIGH); // sets the digital pin 30 to on;
    Serial.println("Voltage set to high on electrode set 'a.'");
  }

  if(input.indexOf("b high") > -1){
    digitalWrite(29, LOW); // sets the digital pin 29 to off;
    delay(200);
    digitalWrite(28, HIGH); // sets the digital pin 28 to on;
    Serial.println("Voltage set to high on electrode set 'b.'");
  }

  if(input.indexOf("c high") > -1){
    digitalWrite(27, LOW); // sets the digital pin 27 to off;
    delay(200);
    digitalWrite(26, HIGH); // sets the digital pin 26 to on;
    Serial.println("Voltage set to high on electrode set 'c.'");
  }

  if(input.indexOf("d high") > -1){
    digitalWrite(25, LOW); // sets the digital pin 25 to off;
    delay(200);
    digitalWrite(24, HIGH); // sets the digital pin 24 to on;
    Serial.println("Voltage set to high on electrode set 'd.'");
  }

  if(input.indexOf("e high") > -1){
    digitalWrite(23, LOW); // sets the digital pin 23 to off;
    delay(200);
    digitalWrite(22, HIGH); // sets the digital pin 22 on;
    Serial.println("Voltage set to high on electrode set 'e.'");
  }


// individual OFFs
  if(input.indexOf("a off") > -1){
    digitalWrite(30, LOW); // sets the digital pin 30 to off;
    delay(200);
    digitalWrite(31, HIGH); // sets the digital pin 31 on;
    delay(400);
    digitalWrite(31, LOW); // sets the digital pin 31 off;
    Serial.println("Voltage turned off for electrode set 'a.'");
  }

  if(input.indexOf("b off") > -1){
    digitalWrite(28, LOW); // ensures the digital pin 28 is off;
    delay(200);
    digitalWrite(29, HIGH); // sets the digital pin 29 on;
    delay(400);
    digitalWrite(29, LOW); // sets the digital pin 29 off;
    Serial.println("Voltage turned off for electrode set 'b.'");
  }

  if(input.indexOf("c off") > -1){
    digitalWrite(26, LOW); // sets the digital pin 26 to off;
    delay(200);
    digitalWrite(27, HIGH); // sets the digital pin 27 to on;
    delay(400);
    digitalWrite(27, LOW); // sets the digital pin 27 to off
    Serial.println("Voltage turned off for electrode set 'c.'");
  }

  if(input.indexOf("d off") > -1){
    digitalWrite(24, LOW); // sets the digital pin 24 to off];
    delay(200);
    digitalWrite(25, HIGH); // sets the digital pin 25 to on;
    delay(400);
    digitalWrite(25, LOW); // sets the digital pin 25 to off;
    Serial.println("Voltage turned off for electrode set 'd.'");
  }

  if(input.indexOf("e off") > -1){
    digitalWrite(22, LOW); // sets digital pin 22 to off;
    delay(200);
    digitalWrite(23, HIGH); // sets digital pin 23 to on;
    delay(400);
    digitalWrite(23, LOW); // sets digital pin 23 off;
    Serial.println("Voltage turned off for electrode set 'e.'");
  }

}