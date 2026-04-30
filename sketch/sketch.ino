#include <Arduino_RouterBridge.h>

#define PIN_AVANTI_M1 7
#define PIN_AVANTI_M2 2

#define PIN_INDIETRO_M1 8
#define PIN_INDIETRO_M2 4

#define PIN_PWM_M1 9
#define PIN_PWM_M2 10

void AvantiMotori(int velocità,int durata_ms)
{
  digitalWrite(PIN_AVANTI_M1,HIGH);
  digitalWrite(PIN_AVANTI_M2,HIGH);
  digitalWrite(PIN_INDIETRO_M1,LOW);
  digitalWrite(PIN_INDIETRO_M2,LOW);
  analogWrite(PIN_PWM_M1,velocità);
  analogWrite(PIN_PWM_M2,velocità);
  delay(durata_ms);
  digitalWrite(PIN_AVANTI_M1,LOW);
  digitalWrite(PIN_AVANTI_M2,LOW);
  digitalWrite(PIN_INDIETRO_M1,LOW);
  digitalWrite(PIN_INDIETRO_M2,LOW);
  analogWrite(PIN_PWM_M1,0);
  analogWrite(PIN_PWM_M2,0);
}
void IndietroMotori(int velocità,int durata_ms)
{
  digitalWrite(PIN_AVANTI_M1,LOW);
  digitalWrite(PIN_AVANTI_M2,LOW);
  digitalWrite(PIN_INDIETRO_M1,HIGH);
  digitalWrite(PIN_INDIETRO_M2,HIGH);
  analogWrite(PIN_PWM_M1,velocità);
  analogWrite(PIN_PWM_M2,velocità);
  delay(durata_ms);
  digitalWrite(PIN_AVANTI_M1,LOW);
  digitalWrite(PIN_AVANTI_M2,LOW);
  digitalWrite(PIN_INDIETRO_M1,LOW);
  digitalWrite(PIN_INDIETRO_M2,LOW);
  analogWrite(PIN_PWM_M1,0);
  analogWrite(PIN_PWM_M2,0);
}
void DestraMotori(int velocità,int durata_ms)
{
  digitalWrite(PIN_AVANTI_M1,HIGH);
  digitalWrite(PIN_AVANTI_M2,LOW);
  digitalWrite(PIN_INDIETRO_M1,LOW);
  digitalWrite(PIN_INDIETRO_M2,HIGH);
  analogWrite(PIN_PWM_M1,velocità);
  analogWrite(PIN_PWM_M2,velocità);
  delay(durata_ms);
  digitalWrite(PIN_AVANTI_M1,LOW);
  digitalWrite(PIN_AVANTI_M2,LOW);
  digitalWrite(PIN_INDIETRO_M1,LOW);
  digitalWrite(PIN_INDIETRO_M2,LOW);
  analogWrite(PIN_PWM_M1,0);
  analogWrite(PIN_PWM_M2,0);
}
void SinistraMotori(int velocità,int durata_ms)
{
  digitalWrite(PIN_AVANTI_M1,LOW);
  digitalWrite(PIN_AVANTI_M2,HIGH);
  digitalWrite(PIN_INDIETRO_M1,HIGH);
  digitalWrite(PIN_INDIETRO_M2,LOW);
  analogWrite(PIN_PWM_M1,velocità);
  analogWrite(PIN_PWM_M2,velocità);
  delay(durata_ms);
  digitalWrite(PIN_AVANTI_M1,LOW);
  digitalWrite(PIN_AVANTI_M2,LOW);
  digitalWrite(PIN_INDIETRO_M1,LOW);
  digitalWrite(PIN_INDIETRO_M2,LOW);
  analogWrite(PIN_PWM_M1,0);
  analogWrite(PIN_PWM_M2,0);
}

void setup() {
  pinMode(PIN_AVANTI_M1,OUTPUT);
  pinMode(PIN_AVANTI_M2,OUTPUT);
  pinMode(PIN_INDIETRO_M1,OUTPUT);
  pinMode(PIN_INDIETRO_M2,OUTPUT);
  pinMode(PIN_PWM_M1,OUTPUT);
  pinMode(PIN_PWM_M2,OUTPUT);
  Bridge.begin();
  Bridge.provide("AvantiMotori",AvantiMotori);
  Bridge.provide("IndietroMotori",IndietroMotori);
  
}

void loop() {
  
}


