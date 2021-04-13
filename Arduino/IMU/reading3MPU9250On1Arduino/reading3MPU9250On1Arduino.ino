/**
   Sample program for the MPU9250 using SPI

   Sample rate of the AK8963 magnetometer is set at 100Hz.
   There are only two options: 8Hz or 100Hz so I've set it at 100Hz
   in the library. This is set by writing to the CNTL1 register
   during initialisation.

   Copyright (C) 2015 Brian Chen

   Open source under the MIT license. See LICENSE.txt.
*/

#include <SPI.h>
#include "MPU9250_SPI.h"

#define SPI_CLOCK 8000000  // 8MHz clock works.
/*
   Copyright (C) 2015 Brian Chen

   Open source under the MIT license. See LICENSE.txt.
*/

#include <SPI.h>
/*
  08:41:26.592 -> 23MOSI
  08:41:26.592 -> 19MISO
  08:41:26.592 -> 18SCK
  08:41:26.592 -> 5SS
*/



#define SS_PIN1   5
#define SS_PIN2   6
//#define SS_PIN3   5

MPU9250 MpuSetup(int spClk,int ssPin)
{
  MPU9250 mpuTemp(SPI_CLOCK, SS_PIN1);
  return mpuTemp;
  }



#define WAITFORINPUT(){            \
    while(!Serial.available()){};  \
    while(Serial.available()){     \
      Serial.read();             \
    };                             \
  }                                  \

  MPU9250 mpu1 = MpuSetup(SPI_CLOCK,SS_PIN1) ;
  //MPU9250 mpu2(SPI_CLOCK, SS_PIN2);
  //MPU9250 mpu3(SPI_CLOCK, SS_PIN3);



  void setup() {
    Serial.begin(115200);


    SPI.begin();

    Serial.println("Press any key to continue1");
    WAITFORINPUT();

     mpu1.init(true);
    //mpu2.init(true);
    //mpu3.init(true);

    Serial.println("Press any key to continue2");
    WAITFORINPUT();
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

    /*
      if (wai2 == 0x71){
       Serial.println("Successful connection");
      }
      else{
       Serial.print("Failed connection: ");
       Serial.println(wai2, HEX);
      }

      if (wai3 == 0x71){
       Serial.println("Successful connection");
      }
      else{
       Serial.print("Failed connection: ");
       Serial.println(wai3, HEX);
      }
    */
    uint8_t wai_AK89631 = mpu1.AK8963_whoami();
    if (wai_AK89631 == 0x48) {
      Serial.println("Successful connection to mag");
    }
    else {
      Serial.print("Failed connection to mag: ");
      Serial.println(wai_AK89631, HEX);
    }
    /*

      uint8_t wai_AK89632 = mpu2.AK8963_whoami();
      if (wai_AK89632 == 0x48){
        Serial.println("Successful connection to mag");
      }
      else{
        Serial.print("Failed connection to mag: ");
        Serial.println(wai_AK89632, HEX);
      }

      uint8_t wai_AK89633 = mpu3.AK8963_whoami();
      if (wai_AK89633 == 0x48){
        Serial.println("Successful connection to mag");
      }
      else{
        Serial.print("Failed connection to mag: ");
        Serial.println(wai_AK89633, HEX);
      }
    */
    mpu1.calib_acc();
    mpu1.calib_mag();
    //mpu3.calib_mag();

    mpu1.calib_acc();
    //mpu2.calib_mag();
    //mpu3.calib_mag();

    Serial.println("Send any char to begin main loop.");
    WAITFORINPUT();
  }

  void loop() {
    // various functions for reading
      mpu1.read_mag();
    // mpu.read_acc();
    // mpu.read_gyro();

    mpu1.read_all();
    //mpu2.read_all();
    //mpu3.read_all();

    Serial.print("mpu1:Gyro_X");   Serial.print('\t');
    Serial.println(mpu1.gyro_data[0]);   Serial.print('\t');
    /*
      Serial.print("mpu2:Gyro_X");   Serial.print('\t');
      Serial.println(mpu2.gyro_data[0]);   Serial.print('\t');

      Serial.print("mpu3:Gyro_X");   Serial.print('\t');
      Serial.println(mpu3.gyro_data[0]);   Serial.print('\t');
    */
    //Serial.print(mpu1.gyro_data[1]);   Serial.print('\t');
    //Serial.print(mpu1.gyro_data[2]);   Serial.print('\t');
    //Serial.print(mpu.accel_data[0]);  Serial.print('\t');
    //Serial.print(mpu.accel_data[1]);  Serial.print('\t');
    //Serial.print(mpu.accel_data[2]);  Serial.print('\t');
    Serial.print(mpu1.mag_data[0]);    Serial.print('\t');
    //Serial.print(mpu.mag_data[1]);    Serial.print('\t');
    //Serial.print(mpu.mag_data[2]);    Serial.print('\t');
    Serial.println();
    //Serial.println(mpu.temperature);

    delay(10);
  }
