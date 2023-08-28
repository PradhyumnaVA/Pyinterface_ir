int x;
char data_01[4]="yes";
char data_02[4]="no";

void setup() {
  // put your setup code here, to run once:
  pinMode(7,INPUT);
  pinMode(13, OUTPUT);
  Serial.begin(9600);
  //Serial.setTimeout(1);
}

void loop() {
  // put your main code here, to run repeatedly:
  //while (!Serial.available());
  x = digitalRead(7);
  if(x==1){
    Serial.println(data_02);
    digitalWrite(13,LOW);
  }
  else if(x==0){
    Serial.println(data_01);
    digitalWrite(13,HIGH);
  }
  delay(1000);
}
