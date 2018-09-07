#define MOTOR_L1 2
#define MOTOR_L2 3
#define MOTOR_R1 4
#define MOTOR_R2 5

void back(){
  digitalWrite(MOTOR_L1, HIGH);
  digitalWrite(MOTOR_L2, LOW);
  digitalWrite(MOTOR_R1, LOW);
  digitalWrite(MOTOR_R2, HIGH);
}

void front(){
  digitalWrite(MOTOR_L1, LOW);
  digitalWrite(MOTOR_L2, HIGH);
  digitalWrite(MOTOR_R1, HIGH);
  digitalWrite(MOTOR_R2, LOW);
}

void steerLeft(){
  digitalWrite(MOTOR_L1, LOW);
  digitalWrite(MOTOR_L2, HIGH);
  digitalWrite(MOTOR_R1, LOW);
  digitalWrite(MOTOR_R2, HIGH);
}

void steerRight(){
  digitalWrite(MOTOR_L1, HIGH);
  digitalWrite(MOTOR_L2, LOW);
  digitalWrite(MOTOR_R1, HIGH);
  digitalWrite(MOTOR_R2, LOW);
}

void idle(){
   digitalWrite(MOTOR_L1, LOW);
  digitalWrite(MOTOR_L2, LOW);
  digitalWrite(MOTOR_R1, LOW);
  digitalWrite(MOTOR_R2, LOW);
}

void setup() {
  // put your setup code here, to run once:
 pinMode(MOTOR_L1, OUTPUT);
 pinMode(MOTOR_L2, OUTPUT);
 pinMode(MOTOR_R1, OUTPUT);
 pinMode(MOTOR_R2, OUTPUT);

  front();
  delay(3000);
  steerRight();
  delay(700);
  front();
  delay(1500);
  steerLeft();
  delay(1400);
  front();
  delay(1500);
  idle();
 
}

void loop() {
 // back();;
 
  // put your main code here, to run repeatedly:
  //digitalWrite(2, HIGH);
  //digitalWrite(3, LOW);
  //digitalWrite(4, HIGH);
  //digitalWrite(5, LOW);
  //delay(2000);
  //digitalWrite(2, LOW);
  //digitalWrite(3, HIGH);
  //digitalWrite(4, LOW);
  //digitalWrite(5, HIGH);
  //delay(2000);
}
