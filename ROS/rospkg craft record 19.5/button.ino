


void setup() {
  // put your setup code here, to run once:
pinMode(2,INPUT);
Serial.begin(115200);

}

void loop() {
  Serial.println(digitalRead(2));
}
