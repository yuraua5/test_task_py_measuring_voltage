const int analogPin = A0;
int nplc = 1;

void setup() {
  Serial.begin(9600);
  pinMode(analogPin, INPUT);
}

void loop() {
  if (Serial.available()) {
    String command = Serial.readStringUntil('\n');
    command.trim();

    if (command.startsWith("SET_NPLC")) {
      int newNPLC = command.substring(9).toInt();
      if (newNPLC == 1 || newNPLC == 5 || newNPLC == 10) {
        nplc = newNPLC;
        Serial.println("NPLC set to " + String(nplc));
      }
    }
  }

  int rawValue = analogRead(analogPin);
  Serial.println(rawValue);
  delay(1000 / nplc);
}
