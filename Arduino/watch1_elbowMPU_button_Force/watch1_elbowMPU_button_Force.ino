#include <WiFi.h>
#include <PubSubClient.h>
#include <WiFiClient.h>
#include <Arduino.h>
#include <Wire.h>
#include <Adafruit_Sensor.h>
#include <Adafruit_BNO055.h>
#include <utility/imumaths.h>



Adafruit_BNO055 bno = Adafruit_BNO055(55);

//Force Sensor
int forcePin =  15;
uint8_t forceRead;

WiFiClient esp32client;
PubSubClient MQTT_CLIENT;

//const char  IP[] = "192.168.1.10"; //HOME
//const char ssid[] ="MiFibra-C9FA";// HOME
//const char pswd[] =  "mrkKGDDF";// HOME
/*
char  IP[] = "10.3.141.1"; //HOME
char ssid[] ="Team2_ExZZu";// HOME
char pswd[] =  "123456789";// HOME
*/
/*
const char  IP[] = "10.3.141.1"; //HOME
const char ssid[] ="Team2_ExZZu";// HOME
const char pswd[] =  "123456789";// HOME
*/
int buttonPin =2;
//char ssid[] ="IAAC-WIFI";// HOME
//char pswd[] = "enteriaac2013";// HOME
//char  IP[] = "192.168.10.177"; //HOME

char ssid[] ="IAAC-WIFI";// HOME
char pswd[] =  "enteriaac2013";// HOME
char  IP[] = "192.168.10.177"; //HOME

char X[20];
char Y[20];
char Z[20];
char F[20];
char C[20];
char tmp_str[10];
String x;
String y;
String z;
String f;
String c;


void SendMsg(){
  
  sensors_event_t event;
  bno.getEvent(&event);
  forceRead = analogRead(forcePin);
  int button = analogRead(buttonPin);
  

  //Serial.print("X: ");
  //Serial.print(event.orientation.x, 4);
  //Serial.print("\tY: ");
  //Serial.print(event.orientation.y, 4);
  //Serial.print("\tZ: ");
  //Serial.print(event.orientation.z, 4);
  //Serial.print("\tF: ");
  //Serial.print(forceRead);
  //Serial.print("\tclick: ");
  //Serial.print(button);
  //Serial.println("");
  Serial.print(analogRead(forcePin));
  Serial.print(digitalRead(forcePin));
  Serial.print (forcePin);
  x = String(event.orientation.x);
  y = String(event.orientation.y);
  z = String(event.orientation.z);
  f = String(forceRead);
  c = String(button);

  x.toCharArray(X, x.length() + 1);
  y.toCharArray(Y, y.length() + 1);
  z.toCharArray(Z, z.length() + 1);
  f.toCharArray(F, f.length() + 1);
  c.toCharArray(C, c.length() + 1);

  


  Serial.print("X: ");
  Serial.print(X);
  Serial.print("\tY: ");
  Serial.print(Y);
  Serial.print("\tZ: ");
  Serial.print(Z);
  Serial.print("\tF: ");
  Serial.print(forceRead);
  Serial.print("\tclick: ");
  Serial.print(button);
  Serial.println("");

 MQTT_CLIENT.publish("/watch1/X",X);    
 MQTT_CLIENT.publish("/watch1/Y",Y);    
 MQTT_CLIENT.publish("/watch1/Z",Z);    
 MQTT_CLIENT.publish("/ToolF",F);    
 MQTT_CLIENT.publish("/ArdClick",C);    

       
    }




void Connect(){
  if (WiFi.status()==!WL_CONNECTED && MQTT_CLIENT.connected()) return;
  if (WiFi.status() !=WL_CONNECTED){
    Serial.println("Starting connecting WiFi.");
    delay(10);
    WiFi.begin(ssid, pswd);
    while (WiFi.status() != WL_CONNECTED) {
      delay(500);
      Serial.print(".");
    }
    Serial.println("WiFi connected");
    Serial.println("IP address: ");
    Serial.println(WiFi.localIP());
  }

    while (!MQTT_CLIENT.connected()){
       MQTT_CLIENT.setClient(esp32client);
       MQTT_CLIENT.setServer(IP,1883);
       MQTT_CLIENT.connect("esp_master_elbow");
      Serial.println("MQTT trying to Connect");
      delay(1000);
  }

}

void BNO055_Init(){
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
}






void setup() {
 
  Serial.begin(115200);
    Connect();
    BNO055_Init();
    pinMode(forcePin,INPUT);

    Serial.print("Done Setup");
    
  // put your setup code here, to run once:
}

void loop() {
 Connect();
 SendMsg();
 Serial.println(analogRead(forcePin));

}
