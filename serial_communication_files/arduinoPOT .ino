
#define pot A0

int value= 0;

void setup() {
 Serial.begin(9600);
 Serial.println('Pot values');
 
}

void loop() {
 value= analogRead(pot);
 float voltage=(5.00/1024.00)*value;
 Serial.println(voltage);
 delay(500);

}
