#include "WiFi.h"
#include <WiFiClient.h>

//char ssid[] =   "MiFibra-C9FA" ;
//char pass[] =   "mrkKGDDF";

char ssid[] =   "IAAC-WIFI" ;
char pass[] =   "enteriaac2013";
/*
WiFiClient client;
enum Protocol{
    PIN, 
    VALUE, 
    BUFFER_SIZE 
    };
*/
int IN_PIN =  2;

void setup(){
    //WiFi.mode(WIFI_STA);
    WiFi.begin(ssid, pass);
    Serial.begin(115200);
    pinMode(IN_PIN, INPUT);
    
  
    while (WiFi.status() != WL_CONNECTED){
      Serial.print(WiFi.status());
      Serial.print(".");
      Serial.println(WL_CONNECTED);
      delay(500);
    }

}
 
void loop(){
    /*if (!client.connect(WiFi.gatewayIP(), SERVER_PORT)){
        return;
    }
 
    uint8_t buffer[Protocol::BUFFER_SIZE];
    int value = digitalRead(IN_PIN);
    Serial.println(value);
    buffer[Protocol::PIN] = IN_PIN;
    buffer[Protocol::VALUE] = value;
    client.write(buffer, Protocol::BUFFER_SIZE);
    client.flush();
    client.stop();
    */
    Serial.println(digitalRead(IN_PIN));   
}
