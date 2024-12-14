#include <Servo.h>

Servo servo1;  // Create a Servo object for the first servo
Servo servo2;  // Create a Servo object for the second servo

#define SERVO1_PIN 9  // Servo motor 1 connected to pin 9
#define SERVO2_PIN 10 // Servo motor 2 connected to pin 10

void setup() {
  Serial.begin(9600);  // Start serial communication

  servo1.attach(SERVO1_PIN); // Attach servo 1 to pin 9
  servo2.attach(SERVO2_PIN); // Attach servo 2 to pin 10

  servo1.write(90);  // Set initial position for servo 1
  servo2.write(90);  // Set initial position for servo 2
}

void loop() {
  if (Serial.available() > 0) {
    char command = Serial.read();

    if (command == 'D') { // "Dance" command
      danceRoutine();
    } else if (command == 'R') { // Reset position
      resetPosition();
    }
  }
}

void danceRoutine() {
  // Move servos in a simple dance pattern
  for (int i = 0; i < 3; i++) { // Repeat dance sequence 3 times
    servo1.write(45); // Move servo 1 to 45 degrees
    servo2.write(135); // Move servo 2 to 135 degrees
    delay(500);        // Wait for 500 milliseconds

    servo1.write(135); // Move servo 1 to 135 degrees
    servo2.write(45);  // Move servo 2 to 45 degrees
    delay(500);        // Wait for 500 milliseconds

    servo1.write(90);  // Move servo 1 to center (90 degrees)
    servo2.write(90);  // Move servo 2 to center (90 degrees)
    delay(500);        // Wait for 500 milliseconds
  }
}

void resetPosition() {
  servo1.write(90); // Reset servo 1 to center (90 degrees)
  servo2.write(90); // Reset servo 2 to center (90 degrees)
}
