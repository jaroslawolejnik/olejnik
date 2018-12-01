int dioda = 13;
int sekundy = 500;
int sekundy2 = 5000;
void setup() {
  pinMode(dioda, OUTPUT);
}
void loop () {
  for (int i = 0; i < 3; i++) {
    digitalWrite(dioda, HIGH);
    delay(sekundy);
    digitalWrite(dioda, LOW);
    delay(sekundy);
    }

for (int i = 0; i < 3; i++) {
  digitalWrite(dioda,HIGH);
  delay(sekundy2);
  digitalWrite(dioda,LOW);
  delay(sekundy2);
  }

for (int i = 0; i < 3; i++) {
  digitalWrite(dioda,HIGH);
  delay(sekundy);
  digitalWrite(dioda,LOW);
  delay(sekundy);
  }


  delay(5000);
}
