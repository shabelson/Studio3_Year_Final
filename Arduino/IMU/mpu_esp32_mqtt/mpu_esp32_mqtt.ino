#include <SPI.h>
#include "MPU9250_SPI.h"
#include "MadgwickAHRS.h"
//#include "Esp32MQTTClient.h"
//#include <WiFiClient.h>
#include <PubSubClient.h>
//#include <AzureIotHub.h>
#include <WiFi.h>

WiFiClient esp32client;
PubSubClient MQTT_CLIENT;

//const char  IP[] = "192.168.56.1"; //HOME
//const char ssid[] ="MiFibra-B93B";// HOME
//const char pswd[] =  "3brRyg9p";// HOME

const char  IP[] = "10.3.141.1"; //HOME
const char ssid[] ="Team2_ExZZu";// HOME
const char pswd[] =  "123456789";// HOME
/*
const char  IP[] = "10.3.141.1"; //HOME
const char ssid[] ="Team2_ExZZu";// HOME
const char pswd[] =  "123456789";// HOME
*/


char tmp_str[7];
static bool hasIoTHub = false;


#define SPI_CLOCK 8000000  // 8MHz clock works.
#define SS_PIN1   15
Madgwick filter;
MPU9250 MpuSetup(int spClk,int ssPin)

{
  MPU9250 mpuTemp(SPI_CLOCK, SS_PIN1);
  return mpuTemp;
}
//UTILITIES///
char* int16ToStr(double i) { 
  sprintf(tmp_str, "%6f", i);
  return tmp_str;
  }

void WAITFORINPUT(){            
    while(!Serial.available()){};  
    while(Serial.available()){     
      Serial.read();             
    };                             
  }                                  


//MPU//


  MPU9250 mpu1(SPI_CLOCK, SS_PIN1);
void MPUSetup()
{

  
     mpu1.init(true);
    //mpu2.init(true);
    //mpu3.init(true);

    uint8_t wai1 = mpu1.whoami();
    //uint8_t wai2 = mpu2.whoami();
    //uint8_t wai3 = mpu3.whoami();

    if (wai1 == 0x71) {
      Serial.println("Successful connection");
    }
    else {
      Serial.print("Failed connection: ");
      Serial.println(wai1, HEX);
    }

    uint8_t wai_AK89631 = mpu1.AK8963_whoami();
    if (wai_AK89631 == 0x24) {
      Serial.println("Successful connection to mag");
    }
    else {
      Serial.print("Failed connection to mag: ");
      Serial.println(wai_AK89631, HEX);
    }
    WAITFORINPUT();

     mpu1.calib_mag();
    //mpu2.calib_mag();
    //mpu3.calib_mag();
   }
void MPURead(MPU9250 locMpu,float locArray[])
{
    locMpu.read_all();
    locArray[0] = locMpu.gyro_data[0];
    locArray[1] = locMpu.gyro_data[1];
    locArray[2] = locMpu.gyro_data[2];
    locArray[3] = locMpu.accel_data[0];
    locArray[4] = locMpu.accel_data[1];
    locArray[5] = locMpu.accel_data[2];
    locArray[6] = locMpu.mag_data[0];
    locArray[7] = locMpu.mag_data[1];
    locArray[8] = locMpu.mag_data[2];
    filter.update(locArray[0],locArray[1],locArray[2],
                      locArray[3],locArray[4],locArray[5],
                      locArray[6],locArray[7],locArray[8]);
    Serial.print(locArray[8]);
    Serial.println();
    SendMsg(filter);
  
}

//MQTT
void SendMsg(Madgwick locFilter){
  

       
       float q0,q1,q2,q3;
       
       q0,q1,q2,q3= locFilter.q0,locFilter.q1,locFilter.q2,locFilter.q3;
       
       MQTT_CLIENT.publish("/IMU1/q0",int16ToStr(q0));
       MQTT_CLIENT.publish("/IMU1/q1",int16ToStr(q1));
       MQTT_CLIENT.publish("/IMU1/q2",int16ToStr(q2));
       MQTT_CLIENT.publish("/IMU1/q3",int16ToStr(q3));
    }


void Connect(){
  Serial.println("connecting");
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
       MQTT_CLIENT.connect("esp_master_wrist");
      Serial.println("MQTT trying to Connect");
      delay(1000);
  }

}

  
  void setup() {
    Serial.begin(115200);
    Serial.println("s1");
    Connect();
    Serial.println("s2");
    SPI.begin();
    MPUSetup();
    Serial.println("donesetup");
  }


  void loop() {
    float mpu1Data[9];

    
    MPURead(mpu1,mpu1Data);
    Serial.print(filter.q1);  
    Serial.println();
    delay(10);
  }
