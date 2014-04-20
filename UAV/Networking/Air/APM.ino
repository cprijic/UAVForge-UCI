
#define N 100
void setup (){
  Serial.begin(9600);
  Serial.flush();
  Serial.println("Arduino connected");
}

void loop (){
  
  int i=0;
  char commandbuffer[N];

  if(Serial.available()){
     while( Serial.available() && i< N-1) {
        commandbuffer[i++] = Serial.read();
     }
     commandbuffer[i++]='\0';
     Serial.print((char*)commandbuffer);  
    }
}
