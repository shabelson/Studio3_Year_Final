#include <WiFi.h>
#include <WiFiClient.h>

#define SERVER_PORT 5000

char ssid[] =   "MiFibra-C9FA" ;
char pass[] =   "mrkKGDDF";

int IN_PIN =  2;
WiFiClient client;
enum Protocol{
    PIN, 
    VALUE, 
    BUFFER_SIZE 
    };

void setup(){
    Serial.begin(115200);
    pinMode(IN_PIN, INPUT);
    WiFi.begin(ssid, pass);
 
    while (WiFi.status() != WL_CONNECTED){
      Serial.print(".");
        delay(500);
    }
}
 
 
void loop(){
    
    if (!client.connect(WiFi.gatewayIP(), SERVER_PORT)){
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
}
