int x;

void setup() {
  Serial.begin(115200);
  Serial.setTimeout(1);
  pinMode(LED_BUILTIN, OUTPUT);
}

void  loop() {
  while (!Serial.available());
  x = Serial.readString().toInt();
  if(x==0){
    digitalWrite(LED_BUILTIN, LOW);
  }
  else{
    digitalWrite(LED_BUILTIN, HIGH);
  }
    

  //Serial.print(x + 1);
}

// void setup()
// {
//   pinMode(LED_BUILTIN, OUTPUT);
// }

// void loop()
// {
//   digitalWrite(LED_BUILTIN, HIGH);
//   delay(1000); // Wait for 1000 millisecond(s)
//   digitalWrite(LED_BUILTIN, LOW);
//   delay(1000); // Wait for 1000 millisecond(s)
// }