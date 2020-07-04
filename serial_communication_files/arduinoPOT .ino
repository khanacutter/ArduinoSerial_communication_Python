
#define pot A0

int deger= 0;

void setup() {
 Serial.begin(9600);
 Serial.println('Pot degerleri');
 
}

void loop() {
 deger= analogRead(pot);
 float voltaj=(5.00/1024.00)*deger;
 Serial.println(voltaj);
 delay(500);

}
