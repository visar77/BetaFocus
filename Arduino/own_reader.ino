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
  unsigned int waves[8];
  unsigned int all_values[12];

  int valIndex = 0;

  while (index < payLoadLength) {
    while (payload[index] == 0x55) {
      extendedCodeLevel++;
      index++;
    }

    int code = payload[index];

    if (code == 0x02) {
      Serial.print("POOR_SIGNAL (0-200): ");
      all_values[0] = payload[++index];
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
      int raw = 0;
      for (int j=0; i<length; j++) {
          raw += payload[++index];
      }
      Serial.print("Raw wave value (-32768 to 32767): ");
      all_values[3] = payload[++index];
      Serial.println(all_values[3]);
    } else if (code == 0x83) {
      int length = payload[++index];
      Serial.print("length:");
      Serial.println(length);
      for (int j=0; j<length; j++) {
          waves[j/3] += payload[++index];
          if (j != 0 && j % 3 == 0) {
            Serial.print(j/3);
            Serial.print("-Wave: ");
            Serial.println(waves[j/3]);
            all_values[4 + j/3] = waves[j/3];
            Serial.println(all_values[4 + j/3]);
          }
      }

    }
    index++;
  }
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