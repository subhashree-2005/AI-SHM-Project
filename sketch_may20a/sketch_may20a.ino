#include <ESP8266WiFi.h>
#include <Firebase_ESP_Client.h>
#include <Wire.h>
#include <Adafruit_MPU6050.h>
#include <Adafruit_Sensor.h>
// ================= WIFI =================
#define WIFI_SSID "LAPTOP-5BN0O3FO 4459"
#define WIFI_PASSWORD "Subu@14562005"
// ================= FIREBASE =================
#define API_KEY "AIzaSyA_ThER2zL3lZkSv6ES7Nx5qwEmjbcjzfA"
#define DATABASE_URL "https://ai-shm-project-default-rtdb.asiasoutheast1.firebasedatabase.app/"
// Firebase objects
FirebaseData fbdo;
FirebaseAuth auth;
FirebaseConfig config;
// MPU6050
Adafruit_MPU6050 mpu;// ================= SETUP =================
void setup() {
Serial.begin(115200);
// WiFi Connection
WiFi.begin(WIFI_SSID, WIFI_PASSWORD);
Serial.print("Connecting to WiFi");
while (WiFi.status() != WL_CONNECTED) {
delay(500);
Serial.print(".");
}
Serial.println("");
Serial.println("WiFi Connected");
// Firebase Setup
config.api_key = API_KEY;
config.database_url = DATABASE_URL;Firebase.begin(&config, &auth);
Firebase.reconnectWiFi(true);
// MPU6050 Setup
Wire.begin();
if (!mpu.begin()) {
Serial.println("MPU6050 NOT FOUND");
while (1) {
delay(10);
}
}
Serial.println("MPU6050 READY");
}
// ================= LOOP =================
void loop() {
sensors_event_t a, g, temp;
mpu.getEvent(&a, &g, &temp);float ax = a.acceleration.x;
float ay = a.acceleration.y;
float az = a.acceleration.z;
// RMS Calculation
float rms = sqrt(
((ax * ax) +
(ay * ay) +
(az * az)) / 3
);
// Frequency Approximation
float frequency = rms * 10;
// Damage Detection
String status;
if (rms < 1.0) {
status = "Healthy";
}
else {
status = "Damaged";
}// Firebase JSON
FirebaseJson json;
json.set("rms", rms);
json.set("frequency", frequency);
json.set("status", status);
json.set("ax", ax);
json.set("ay", ay);
json.set("az", az);
json.set("ax", ax);
json.set("ay", ay);
json.set("az", az);
// Send to Firebase
if (Firebase.RTDB.pushJSON(
&fbdo,
"/sensor_data",
&json
)) {Serial.println("DATA SENT");
Serial.print("RMS: ");
Serial.println(rms);
Serial.print("Frequency: ");
Serial.println(frequency);
Serial.print("Status: ");
Serial.println(status);
}
else {
Serial.println("FAILED");
Serial.println(
fbdo.errorReason()
);
}
delay(3000);
}