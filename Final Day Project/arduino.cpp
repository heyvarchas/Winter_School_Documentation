char receivedData[64];                 // Character buffer to store incoming serial data
char* token_abc;                       // Pointer used for tokenizing the received string

void setup() {
  Serial.begin(9600);                  // Initialize serial communication at 9600 baud rate
}

void loop() {
  if (Serial.available()) {            // Check if data is available on the serial port
    int bytesRead = Serial.readBytesUntil('\n', receivedData, sizeof(receivedData) - 1);
    // Read incoming serial data until newline character or buffer limit is reached

    receivedData[bytesRead] = '\0';
    // Null-terminate the received character array to make it a valid C-string

    token_abc = strtok(receivedData, ",");
    // Extract the first token separated by comma

    String token = String(token_abc);  // Convert first token to Arduino String
    int a = token.toInt();             // Convert first token to integer

    int b = (String(strtok(NULL, ","))).toInt();
    // Extract second token, convert to String, then to integer

    int c = (String(strtok(NULL, ","))).toInt();
    // Extract third token, convert to String, then to integer
  }
}