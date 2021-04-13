 //Fade an LED with a flex sensor
 //More info: http://www.ardumotive.com/how-to-use-a-flex-sensor-en.html
 //Dev: Michalis Vasilakis // Date: 9/7/2015 // www.ardumotive.com  */

#include <PubSubClient.h>
#include <Arduino.h>
#include <ESP8266WiFi.h>
#include <ESP8266WiFiMulti.h>
#include <WiFiClient.h>

WiFiClient client;

const char IP[] = "192.168.11.170"; // ip of the MQTT broker
const char ssid[] = "IAAC-WIFI"; //name of the network
const char pswd[] ="enteriaac2013"; //password of the local network

PubSubClient mqtt_client; 
ESP8266WiFiMulti WiFiMulti;


//Constants:
const int ledPin = 16;   //pin 3 has PWM funtion
const int flexPin = A0; //pin A0 to read analog input

//Variables:
int value; //save analog value

void ConAndPub(int val){
    Serial.print("send Func");
    if ((WiFiMulti.run() == WL_CONNECTED)) {
      Serial.println("WIFIIIII");
    }
    else{
      while (WiFiMulti.run() != WL_CONNECTED){
          WiFi.mode(WIFI_STA);
          WiFiMulti.addAP(ssid,pswd);
          Serial.print(".");
          delay(100);
        }
      
      }
      if (!mqtt_client.connected()){
        Serial.println("mqtt not connect");
        }
      Serial.println("entered reconnect");
      mqtt_client.setServer(IP,1883);
      mqtt_client.setClient(client);
      while (!mqtt_client.connected()){
        mqtt_client.connect("esp_master");
        Serial.println("MQTT trying to Connect");
        delay(1000);
        }

    char cstr[16];
    itoa(val, cstr, 10);
    Serial.print(cstr);
    mqtt_client.publish("Finger",cstr);
  
    }
  


void setup(){
  WiFi.mode(WIFI_STA);
  WiFiMulti.addAP(ssid,pswd);  
  pinMode(ledPin, OUTPUT);  //Set pin 3 as 'output'
  Serial.begin(115200);       //Begin serial communication

}

void loop(){
  
  value = analogRead(flexPin);         //Read and save analog value from potentiometer
  Serial.println(value);               //Print value
  value = map(value, 700, 900, 0, 255);//Map value 0-1023 to 0-255 (PWM)
  analogWrite(ledPin, value);          //Send PWM value to led
  delay(100);                          //Small delay
  ConAndPub(value);
}
