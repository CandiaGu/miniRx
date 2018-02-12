// defines pins numbers
const int stepPin1 = 3; 
const int dirPin1 = 4;
const int stepPin2 = 5; 
const int dirPin2 = 7;
const int stepPin3 = 11; 
const int dirPin3 = 12;

void setup(){
  // Open serial connection.
  Serial.begin(9600);
  // initialize digital pin LED_BUILTIN as an output.
  pinMode(stepPin1, OUTPUT);
  pinMode(dirPin1, OUTPUT);
  pinMode(stepPin2, OUTPUT);
  pinMode(dirPin2, OUTPUT);
  pinMode(stepPin3, OUTPUT);
  pinMode(dirPin3, OUTPUT);
 
}

void loop(){
  if(Serial.available() > 0) {
    char var = Serial.read();
    turnClockwiseOnce(var);
  }
}

void turnClockwiseOnce(int motor){
  int stepPin; int dirPin;
  switch(motor){
    case '1':
      stepPin = stepPin1;
      dirPin = dirPin1;
      break;
    case '2':
      stepPin = stepPin2;
      dirPin = dirPin2;
      break;
    case '3':
      stepPin = stepPin3;
      dirPin = dirPin3;
      break;
  }

  digitalWrite(dirPin,HIGH); // Enables the motor to move in a particular direction
  // Makes 200 pulses for making one full cycle rotation
  for(int x = 0; x < 200; x++) {
    digitalWrite(stepPin,HIGH); 
    delayMicroseconds(500); 
    digitalWrite(stepPin,LOW); 
    delayMicroseconds(500); 
  }
}

