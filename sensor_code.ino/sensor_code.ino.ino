#include <ESP8266WiFi.h>
#include <FirebaseESP8266.h>

#include <Wire.h>
#include <Adafruit_MPU6050.h>
#include <Adafruit_Sensor.h>

#include <ArduinoJson.h>

// WIFI
#define WIFI_SSID "YOUR_WIFI_NAME"
#define WIFI_PASSWORD "YOUR_WIFI_PASSWORD"

// FIREBASE
#define FIREBASE_HOST "ai-shm-project-default-rtdb.asia-southeast1.firebasedatabase.app"
#define FIREBASE_AUTH ""

// Firebase objects
FirebaseData firebaseData;

Adafruit_MPU6050 mpu;

void setup() {

  Serial.begin(115200);

  WiFi.begin(WIFI_SSID, WIFI_PASSWORD);

  while (WiFi.status() != WL_CONNECTED) {

    delay(500);

    Serial.print(".");
  }

  Serial.println("WiFi Connected");

  Firebase.begin(FIREBASE_HOST, FIREBASE_AUTH);

  Wire.begin();

  if (!mpu.begin()) {

    Serial.println("MPU6050 not found");

    while (1) {

      delay(10);
    }
  }

  Serial.println("MPU6050 Ready");
}

void loop() {

  sensors_event_t a, g, temp;

  mpu.getEvent(&a, &g, &temp);

  float ax = a.acceleration.x;
  float ay = a.acceleration.y;
  float az = a.acceleration.z;

  // RMS Calculation
  float rms = sqrt(
    ((ax * ax) + (ay * ay) + (az * az)) / 3
  );

  // Frequency estimation
  float frequency = rms * 10;

  String status;

  if (rms < 1.0) {

    status = "Healthy";
  }

  else {

    status = "Damaged";
  }

  FirebaseJson json;

  json.set("rms", rms);

  json.set("frequency", frequency);

  json.set("status", status);

  Firebase.pushJSON(
    firebaseData,
    "/sensor_data",
    json
  );

  Serial.print("RMS: ");
  Serial.println(rms);

  Serial.print("Frequency: ");
  Serial.println(frequency);

  Serial.print("Status: ");
  Serial.println(status);

  delay(3000);
}