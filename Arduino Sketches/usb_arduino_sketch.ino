const int MAX_LENGTH = 173;
int thirdLastByte = 0;
unsigned char entirePackage[173]; // for incoming serial data
unsigned char payload[256];
int lastByte = 0;
int secondLastByte = 0;
int checksum = 0;
int payLoadLength = 0;
bool synced = false;
int i = 0;

void parsePayload() {
  int extendedCodeLevel = 0;
  int index = 0;

  unsigned char attention;
  unsigned char meditation;
  unsigned int raw_wave;
  unsigned int waves[8] = {0};
  unsigned int all_values[12] = {0};

  Serial.println("-----------------------------------");

  while (index < payLoadLength) {
    while (payload[index] == 0x55) {
      extendedCodeLevel++;
      index++;
    }
    int code = payload[index];
    if (code == 0x02) {
      Serial.print("SIGNAL_QUALITY (0-100): ");
      all_values[0] = (200 - payload[++index]) / 2;
      Serial.println(all_values[0]);
    } else if (code == 0x04) {
      Serial.print("ATTENTION (0 to 100): ");
      all_values[1] = payload[++index];
      Serial.println(all_values[1]);
    } else if (code == 0x05) {
      Serial.print("MEDITATION (0 to 100): ");
      all_values[2] = payload[++index];
      Serial.println(all_values[2]);
    } else if (code == 0x80) {
      int length = payload[++index];
      if (length != 2) {
        Serial.println("LENGTH OF RAW_VALUES WAS NOT 2!!! ERROR!!!");
        return;
      }
      short raw = (payload[index + 2] >> 8) | payload[index + 1];
      index += 2;
      Serial.print("Raw wave value (-32768 to 32767): ");
      all_values[3] = payload[++index];
      Serial.println(all_values[3]);
    } else if (code == 0x83) {
      int length = payload[++index];
      if (length != 24) {
        Serial.println("LENGTH OF EEG_POWERS WAS NOT 24!!! ERROR!!!");
        return;
      }
      //Serial.print("length:");
      //Serial.println(length);
      for (int j=0; j<8; j++) {
          unsigned int first_int = payload[++index];
          unsigned int second_int = payload[++index];
          unsigned int third_int = payload[++index];
          waves[j] = ((first_int << 16) | (second_int << 8) | (third_int));
          all_values[j+3] = waves[j];
          if (j == 0) Serial.print("Delta");
          else if (j == 1) Serial.print("Theta");
          else if (j == 2) Serial.print("Low-Alpha");
          else if (j == 3) Serial.print("High-Alpha");
          else if (j == 4) Serial.print("Low-Beta");
          else if (j == 5) Serial.print("High-Beta");
          else if (j == 6) Serial.print("Low-Gamma");
          else Serial.print("Mid-Gamma");
          Serial.print("-Wave: ");
          Serial.println(waves[j]);
      }
    }
    index++;
  }
  Serial.print("CSV: ");
  for (int j=0; j<11; j++) {
    Serial.print(all_values[j]);
    Serial.print(";");
  }
  Serial.print(all_values[11]);
  Serial.println("\n-----------------------------------");
}

void setup() {
  Serial.begin(9600);
}

void loop() {

  // PACKAGE: SYNC SYNC PAYLOADLENGTH DATA CHECKSUM
  // SYNC, PAYLOADLENGTH and CHECKSUM all one byte
  // SYNC = 0x44 = 170

  if (Serial.available() > 0) {
    // read the incoming byte:
    if (synced) {
      int index = 0;
      int checksumPackage = 0;
      Serial.readBytes(payload, payLoadLength);
      Serial.print("Payload: ");
      for (int j=0; j<payLoadLength; j++) {
        Serial.print(payload[j]);
        Serial.print(" ");
        checksumPackage += payload[j];
      }
      Serial.println();
      checksumPackage &= 255;
      checksumPackage = ~checksumPackage & 255;
      //Serial.print("Checksum of packages: ");
      //Serial.println(checksumPackage);
      checksum = Serial.read();
      //Serial.println(checksum);
      if (checksum == checksumPackage) {
        Serial.println("Success");
        parsePayload();
      } else {
        Serial.println("FAILED: CHECKSUM NOT MATCHING");
      }
      synced = false;
    } else {
      lastByte = Serial.read();
      if (lastByte != 170 && secondLastByte == 170 && thirdLastByte == 170 && !synced) {
        if (lastByte > 170) {
          Serial.println("FAILED: PAYLOADLENGTH TOO LONG");
        } else {
          entirePackage[0] = 170; //SYNC
          entirePackage[1] = 170; //SYNC
          entirePackage[2] = lastByte;
          payLoadLength = lastByte;
          Serial.print("Payloadlength: ");
          Serial.println(payLoadLength);
          i = 0;
          synced = true;
        }
      }
      secondLastByte = lastByte;
      thirdLastByte = secondLastByte;
    }
  }
}