#include <BluetoothSerial.h>
#include <SPI.h>
#include <Wire.h>
#include <Adafruit_GFX.h>
#include <Adafruit_SSD1306.h>

BluetoothSerial SerialBT;
#define SCREEN_WIDTH 128 // OLED display width, in pixels
#define SCREEN_HEIGHT 32 // OLED display height, in pixels
#define OLED_RESET     -1 // Reset pin # (or -1 if sharing Arduino reset pin)
#define SCREEN_ADDRESS 0x3C ///< See datasheet for Address; 0x3D for 128x64, 0x3C for 128x32
Adafruit_SSD1306 display(SCREEN_WIDTH, SCREEN_HEIGHT, &Wire, OLED_RESET);

// Global variables for package parsing
const int MAX_LENGTH = 173;
int thirdLastByte = 0;
unsigned char entirePackage[173]; // for incoming serial data
unsigned char payload[256];
unsigned char attention = 255;
unsigned char quality = 255;
int lastByte = 0;
int secondLastByte = 0;
int checksum = 0;
int payLoadLength = 0;
bool synced = false;
int i = 0;

// Global variables for drawing
#define GRAPH_HEIGHT 23
uint8_t graph_data[SCREEN_WIDTH] = {0};
uint8_t head_index = 0;
static const unsigned char PROGMEM image_data_Brain[] = {
    // ∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙
    // ∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙
    // ∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙
    // ∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙████████████∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙
    // ∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙██████████████∙∙∙∙∙∙∙∙∙∙███████████∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙
    // ∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙███∙∙∙∙∙∙∙∙∙∙███∙∙∙∙∙∙∙∙∙∙███∙∙∙∙∙∙∙█████∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙
    // ∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙██████∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙██████∙∙∙∙∙∙∙∙∙██∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙
    // ∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙████∙∙██∙∙∙∙∙∙∙∙∙█████∙∙∙∙∙∙∙∙∙████∙∙∙█████∙∙███████████∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙
    // ∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙███∙∙∙∙∙∙∙∙∙∙∙∙∙████∙∙███∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙██████∙∙∙∙∙∙∙████∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙
    // ∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙██∙∙∙∙∙∙∙∙∙███████∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙███∙∙∙∙∙∙∙∙∙██∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙
    // ∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙███∙∙∙∙∙∙∙███∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙████████████∙∙∙∙∙∙∙∙∙∙███∙∙∙∙∙∙∙∙███∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙
    // ∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙███∙███∙∙∙∙∙██∙∙∙∙∙∙∙∙█████████∙∙∙∙∙∙∙∙∙∙██∙∙∙∙∙∙∙∙∙███∙∙∙∙∙████████∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙
    // ∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙██∙∙∙∙∙∙∙∙∙∙∙███∙∙∙∙████∙∙∙∙███∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙████∙∙∙∙∙∙∙∙∙∙∙∙∙██∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙
    // ∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙███∙∙∙∙∙∙∙∙███∙∙∙∙∙██∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙████∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙███∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙
    // ∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙███∙∙██∙∙∙██∙∙∙∙∙██∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙██∙∙∙∙∙∙███∙∙∙∙∙∙∙∙∙∙███∙∙∙∙∙∙███∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙
    // ∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙████∙∙∙∙██∙∙∙∙∙███∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙███████████∙∙∙∙∙∙∙∙∙∙∙███∙∙∙∙█████∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙
    // ∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙██∙∙∙∙∙∙███████∙∙∙∙∙∙∙█████∙∙█████∙∙∙∙∙∙∙∙∙∙∙∙∙████████∙∙∙∙∙∙∙███∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙
    // ∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙██∙∙∙∙∙∙∙███∙∙∙∙∙∙∙∙∙∙∙∙∙████∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙███∙∙∙∙∙∙∙∙∙███∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙
    // ∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙██████████∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙██∙∙∙∙∙∙∙∙∙∙∙∙∙██∙∙∙∙∙∙∙∙∙∙██∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙
    // ∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙██∙∙∙∙∙∙∙∙∙∙∙██∙∙∙∙∙∙∙∙∙███∙∙∙∙∙∙∙∙∙∙███████████████∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙
    // ∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙████∙∙∙∙∙∙███∙∙∙∙∙∙∙∙∙∙██████████████∙∙∙∙∙∙∙∙███∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙
    // ∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙████████████∙∙∙∙█████∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙███∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙
    // ∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙██████∙████∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙███∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙
    // ∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙███∙∙∙∙████∙∙∙∙∙∙∙∙∙∙∙∙∙∙███∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙
    // ∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙███∙∙∙∙∙████████████████∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙
    // ∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙███∙∙∙∙∙∙∙██∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙
    // ∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙███∙∙∙∙∙∙██∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙
    // ∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙███∙∙∙∙███∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙
    // ∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙████████∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙
    // ∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙██∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙
    // ∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙
    // ∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙
    0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
    0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
    0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
    0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x1f, 0xfe, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
    0x00, 0x00, 0x00, 0x00, 0x00, 0x03, 0xff, 0xf0, 0x03, 0xff, 0x80, 0x00, 0x00, 0x00, 0x00, 0x00,
    0x00, 0x00, 0x00, 0x00, 0x00, 0x0e, 0x00, 0x70, 0x03, 0x80, 0xf8, 0x00, 0x00, 0x00, 0x00, 0x00,
    0x00, 0x00, 0x00, 0x00, 0x01, 0xf8, 0x00, 0x00, 0x07, 0xe0, 0x0c, 0x00, 0x00, 0x00, 0x00, 0x00,
    0x00, 0x00, 0x00, 0x00, 0x0f, 0x30, 0x07, 0xc0, 0x1e, 0x3e, 0x7f, 0xf0, 0x00, 0x00, 0x00, 0x00,
    0x00, 0x00, 0x00, 0x00, 0x38, 0x00, 0x3c, 0xe0, 0x00, 0x03, 0xf0, 0x1e, 0x00, 0x00, 0x00, 0x00,
    0x00, 0x00, 0x00, 0x00, 0x30, 0x07, 0xf0, 0x00, 0x00, 0x00, 0x38, 0x03, 0x00, 0x00, 0x00, 0x00,
    0x00, 0x00, 0x00, 0x00, 0x70, 0x1c, 0x00, 0x07, 0xff, 0x80, 0x1c, 0x03, 0x80, 0x00, 0x00, 0x00,
    0x00, 0x00, 0x00, 0x01, 0xdc, 0x18, 0x07, 0xfc, 0x00, 0xc0, 0x1c, 0x1f, 0xe0, 0x00, 0x00, 0x00,
    0x00, 0x00, 0x00, 0x03, 0x00, 0x1c, 0x3c, 0x38, 0x00, 0x00, 0x78, 0x00, 0x30, 0x00, 0x00, 0x00,
    0x00, 0x00, 0x00, 0x03, 0x80, 0x70, 0x60, 0x00, 0x00, 0x03, 0xc0, 0x00, 0x38, 0x00, 0x00, 0x00,
    0x00, 0x00, 0x00, 0x01, 0xcc, 0x60, 0xc0, 0x00, 0x0c, 0x0e, 0x00, 0x70, 0x38, 0x00, 0x00, 0x00,
    0x00, 0x00, 0x00, 0x00, 0x78, 0x60, 0xe0, 0x00, 0x3f, 0xf8, 0x00, 0xe1, 0xf0, 0x00, 0x00, 0x00,
    0x00, 0x00, 0x00, 0x00, 0x30, 0x3f, 0x80, 0xf9, 0xf0, 0x00, 0x7f, 0x80, 0xe0, 0x00, 0x00, 0x00,
    0x00, 0x00, 0x00, 0x00, 0x18, 0x0e, 0x00, 0x0f, 0x00, 0x00, 0x0e, 0x00, 0xe0, 0x00, 0x00, 0x00,
    0x00, 0x00, 0x00, 0x00, 0x0f, 0xfc, 0x00, 0x00, 0x06, 0x00, 0x0c, 0x00, 0xc0, 0x00, 0x00, 0x00,
    0x00, 0x00, 0x00, 0x00, 0x00, 0x06, 0x00, 0x30, 0x07, 0x00, 0x3f, 0xff, 0x80, 0x00, 0x00, 0x00,
    0x00, 0x00, 0x00, 0x00, 0x00, 0x03, 0xc0, 0xe0, 0x07, 0xff, 0xe0, 0x1c, 0x00, 0x00, 0x00, 0x00,
    0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x7f, 0xf8, 0x7c, 0x00, 0x00, 0x1c, 0x00, 0x00, 0x00, 0x00,
    0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x0f, 0xde, 0x00, 0x00, 0x38, 0x00, 0x00, 0x00, 0x00,
    0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x01, 0xc3, 0xc0, 0x00, 0xe0, 0x00, 0x00, 0x00, 0x00,
    0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x70, 0x7f, 0xff, 0x80, 0x00, 0x00, 0x00, 0x00,
    0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x1c, 0x06, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
    0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x0e, 0x06, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
    0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x07, 0x0e, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
    0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x03, 0xfc, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
    0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x60, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
    0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
    0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00
};

void drawGraph(){
  uint8_t i;
  for (i = 0; i < SCREEN_WIDTH; ++i){
    display.drawLine(SCREEN_WIDTH - i, GRAPH_HEIGHT - graph_data[head_index], SCREEN_WIDTH-i, GRAPH_HEIGHT, SSD1306_WHITE);
    head_index = (head_index + 1) % SCREEN_WIDTH;
  }
}

void addDataToGraph(uint8_t data){
  head_index = head_index == 0 ? head_index = SCREEN_WIDTH-1 : head_index-1 ;
  graph_data[head_index] = (uint8_t)(data * (GRAPH_HEIGHT/100.));
}

void draw() {
  display.clearDisplay();
  //
  display.setCursor(2, GRAPH_HEIGHT+2);
  display.print(F("QLTY:"));

  display.setCursor(SCREEN_WIDTH/4 +2, GRAPH_HEIGHT+2);
  display.print(quality); //Replace with Signal Quality

  display.setCursor(SCREEN_WIDTH/2 +3, GRAPH_HEIGHT+2);
  display.print(F("ATTN:"));

  display.setCursor((SCREEN_WIDTH/4) *3 +3, GRAPH_HEIGHT+2);

  unsigned char data = 0;
  if (attention == 255) {
    display.print(F("-")); //Replace with Attentionvalue
  }
  else {
    data = attention;
    display.print(data);
  }
  addDataToGraph(data);
  drawGraph();
  display.display();
}

/* Returns
 * 1 if payload could be parsed without issed
 * 0 if package couldn't be read, because the CHECKSUM was false or PAYLOADLENGTH is too long
 */
int parsePayload(void) {
  int extendedCodeLevel = 0;
  int index = 0;

  unsigned char attention;
  unsigned char meditation;
  unsigned int raw_wave;
  unsigned int waves[8] = {0};
  unsigned int all_values[12] = {0};

  SerialBT.println("-----------------------------------");

  while (index < payLoadLength) {
    while (payload[index] == 0x55) {
      extendedCodeLevel++;
      index++;
    }
    int code = payload[index];
    if (code == 0x02) {
      SerialBT.print("SIGNAL_QUALITY (0-100): ");
      all_values[0] = (200 - payload[++index]) / 2;
      quality = (char) all_values[0];
      SerialBT.println(all_values[0]);
    } else if (code == 0x04) {
      SerialBT.print("ATTENTION (0 to 100): ");
      all_values[1] = payload[++index];
      attention = (char) all_values[1];
      SerialBT.println(all_values[1]);
    } else if (code == 0x05) {
      SerialBT.print("MEDITATION (0 to 100): ");
      all_values[2] = payload[++index];
      SerialBT.println(all_values[2]);
    } else if (code == 0x80) {
      int length = payload[++index];
      if (length != 2) {
        SerialBT.println("LENGTH OF RAW_VALUES WAS NOT 2!!! ERROR!!!");
        return 0;
      }
      short raw = (payload[index + 2] >> 8) | payload[index + 1];
      index += 2;
      SerialBT.print("Raw wave value (-32768 to 32767): ");
      all_values[3] = payload[++index];
      SerialBT.println(all_values[3]);
    } else if (code == 0x83) {
      int length = payload[++index];
      if (length != 24) {
        SerialBT.println("LENGTH OF EEG_POWERS WAS NOT 24!!! ERROR!!!");
        return 0;
      }
      //Serial.print("length:");
      //Serial.println(length);
      for (int j=0; j<8; j++) {
        unsigned int first_int = payload[++index];
        unsigned int second_int = payload[++index];
        unsigned int third_int = payload[++index];
        waves[j] = ((first_int << 16) | (second_int << 8) | (third_int));
        all_values[j+3] = waves[j];
        SerialBT.print(j);
        SerialBT.print("-Wave: ");
        SerialBT.println(waves[j]);
      }
    }
    index++;
  }
  SerialBT.print("CSV: ");
  for (int j=0; j<11; j++) {
    SerialBT.print(all_values[j]);
    SerialBT.print(";");
  }
  SerialBT.print(all_values[11]);
  SerialBT.println("\n-----------------------------------");

  return 1;
}

/* Returns
 * 1 if package was read without any issue
 * 0 if package couldn't be read, because the CHECKSUM was false or PAYLOADLENGTH is too long
 * -1 if still not done reading the package
 */
int readPackage() {
  if (Serial.available() > 0) {
  // read the incoming byte:
  if (synced) {
    int index = 0;
    int checksumPackage = 0;
    Serial.readBytes(payload, payLoadLength);
    SerialBT.print("Payload: ");
    for (int j=0; j<payLoadLength; j++) {
      SerialBT.print(payload[j]);
      SerialBT.print(" ");
      checksumPackage += payload[j];
    }
    SerialBT.println();
    checksumPackage &= 255;
    checksumPackage = ~checksumPackage & 255;
    //Serial.print("Checksum of packages: ");
    //Serial.println(checksumPackage);
    checksum = Serial.read();
    //Serial.println(checksum);
    synced = false;
    if (checksum == checksumPackage) {
      SerialBT.println("Success");
      int success = parsePayload();
      return success;
    }
    else {
      SerialBT.println("FAILED: CHECKSUM NOT MATCHING");
      return 0;
    }
  }
  lastByte = Serial.read();
  if (lastByte != 170 && secondLastByte == 170 && thirdLastByte == 170 && !synced) {
      if (lastByte > 170) {
        SerialBT.println("FAILED: PAYLOADLENGTH TOO LONG");
        return 0;
      }
      entirePackage[0] = 170; //SYNC
      entirePackage[1] = 170; //SYNC
      entirePackage[2] = lastByte;
      payLoadLength = lastByte;
      SerialBT.print("Payloadlength: ");
      SerialBT.println(payLoadLength);
      i = 0;
      synced = true;
    }
    secondLastByte = lastByte;
    thirdLastByte = secondLastByte;
  }
  return -1;
}

void setup() {
  Serial.begin(9600);
  SerialBT.begin(9600);

  if(!display.begin(SSD1306_SWITCHCAPVCC, SCREEN_ADDRESS)) {
    Serial.println("SSD1306 allocation failed");
    SerialBT.println("SSD1306 allocation failed");
    while (true); // Don't proceed, loop forever
  }

  display.clearDisplay();
  display.drawBitmap(0, 0, image_data_Brain, 128, 32, SSD1306_WHITE);
  display.display();
  display.setTextSize(1);
  display.setTextColor(SSD1306_WHITE);

  delay(3000);
}

void loop() {
  int success = readPackage();
  if (success == -1) return;
  if (success == 0) {
    attention = 255;
  }
  draw();
}
