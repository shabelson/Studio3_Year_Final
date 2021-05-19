
#include <Arduino.h>
#include <WiFi.h>
#include <WiFiMulti.h>
#include <WiFiClientSecure.h>
#include <WebSocketsClient.h>
#include <ArduinoJson.h>
#include <Wire.h>
#include <Adafruit_Sensor.h>
#include <Adafruit_BNO055.h>
#include <utility/imumaths.h>

//IMU
Adafruit_BNO055 bno = Adafruit_BNO055(55);

//Force Sensor
const int forcePin =  15;
int forceRead = 0;

//WebServer

const char* ssid = "IAAC-WIFI";
const char* pass = "enteriaac2013";

WiFiServer server(80);
WebSocketsClient webSocket;


void CompileMsg(float X,float Y, float Z, int F,bool B)
{
  

  StaticJsonBuffer<128> jsonBuffer;
  JsonObject& root = jsonBuffer.createObject();
  root["X"] = X;
  root["Y"] = Y;
  root["Z"] = Z;
  root["F"] = F;
  root["B"] = B;
  
  String databuf;
  root.printTo(databuf);
  webSocket.sendTXT(databuf);
  

}

void Connect(){
  
  WiFi.begin(ssid,pass);
  while (WiFi.status()!=WL_CONNECTED)
  {
    delay(1000);
    Serial.println("Trying to Connect Wifi..");
  }
  Serial.println(WiFi.localIP());
  }

void setup(void)
{
  //pinMode(forcePin,INPUT);
  Serial.begin(9600);
  Serial.println("Orientation Sensor Test"); Serial.println("");

  /* Initialise the sensor */
  if (!bno.begin())
  {
    /* There was a problem detecting the BNO055 ... check your connections */
    Serial.print("Ooops, no BNO055 detected ... Check your wiring or I2C ADDR!");
    while (1);
  }

  delay(1000);
  Connect();
  bno.setExtCrystalUse(true);
  webSocket.begin("192.168.10.177", 80, "/");
  webSocket.setReconnectInterval(1000);
}


void loop(void)
{

  bool button = false;

  WiFiClient client = server.available();
  if (client.connected()  && webSocket.handshake(client)))
  {
  sensors_event_t event;
  bno.getEvent(&event);
  forceRead = analogRead(forcePin);
  Serial.print("X: ");
  Serial.print(event.orientation.x, 4);
  Serial.print("\tY: ");
  Serial.print(event.orientation.y, 4);
  Serial.print("\tZ: ");
  Serial.print(event.orientation.z, 4);
  Serial.print("\tF: ");
  Serial.print(forceRead);
  Serial.print("\tclick: ");
  Serial.print(button);
  Serial.println("");
 
    while (client.connected()) {
 
     CompileMsg(event.orientation.x,event.orientation.y, event.orientation.z, forceRead,button);
      }
 
      delay(10); // Delay needed for receiving the data correctly
   }
   else
   {
    Serial.println(server.available());
    }

  
  
  delay(100);
}
