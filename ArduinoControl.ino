#include <serial>

int highPins[5] = {22, 24, 26, 28, 30}; // Maps to sets 'e', 'd', 'c', 'b', 'a'
int lowPins[5] = {23, 25, 27, 29, 31};  // Maps to sets 'e', 'd', 'c', 'b', 'a'

void setup() {
  Serial.begin(9600);     // Sets up serial communication for user input
  
  for (int i = 0; i < 5; i++) {
    pinMode(highPins[i], OUTPUT);  // Sets the digital pins as output
    pinMode(lowPins[i], OUTPUT);   // Sets the digital pins as output
  }
}

void turnHigh(int pin) {
  digitalWrite(lowPins[pin], LOW);
  delay(200);
  digitalWrite(highPins[pin], HIGH);
}

void turnLow(int pin) {
  digitalWrite(highPins[pin], LOW);
  delay(200);
  digitalWrite(lowPins[pin], HIGH);
}

void turnOff(int pin) {
  digitalWrite(highPins[pin], LOW);
  delay(200);
  digitalWrite(lowPins[pin], HIGH);
  delay(400);
  digitalWrite(lowPins[pin], LOW);
}

void handleCommands(String input, String electrode, int pin) {
  if (input.indexOf(electrode + " high") > -1) {
    turnHigh(pin);
    Serial.println("Voltage set to high on electrode set '" + electrode + "'.");
  }
  
  if (input.indexOf(electrode + " low") > -1) {
    turnLow(pin);
    Serial.println("Voltage set to low on electrode set '" + electrode + "'.");
  }
  
  if (input.indexOf(electrode + " off") > -1) {
    turnOff(pin);
    Serial.println("Voltage turned off for electrode set '" + electrode + "'.");
  }
}

void loop() {
  Serial.println("\nEnter a sentence containing any number of compatible commands. To see a list of commands, please enter 'commands' without the quotations.");

  while (Serial.available() == 0) {
    // Only prompts user for input once between inputs
  }

  String input = Serial.readString();
  input.trim();
  Serial.println(input);

  if(input == "commands") {
    // Same printouts as before...
  }
  
  if(input.indexOf("all high") > -1) {
    for (int i = 0; i < 5; i++) {
      turnHigh(i);
    }
    Serial.println("Voltage set to high on all arduino controlled electrodes.");
  }
  
  if(input.indexOf("all low") > -1) {
    for (int i = 0; i < 5; i++) {
      turnLow(i);
    }
    Serial.println("Voltage set to low on all arduino controlled electrodes.");
  }
  
  if(input.indexOf("all off") > -1) {
    for (int i = 0; i < 5; i++) {
      turnOff(i);
    }
    Serial.println("All arduino controlled electrodes powered off.");
  }
  
  handleCommands(input, "e", 0);
  handleCommands(input, "d", 1);
  handleCommands(input, "c", 2);
  handleCommands(input, "b", 3);
  handleCommands(input, "a", 4);
}

