import serial
arduinoSerialData=serial.Serial("COM5",9600)
from datetime import datetime
import time

path="datas_storage_notebook" 	


try:
    while 1:
        if(arduinoSerialData.inWaiting()!=0):
            myData=arduinoSerialData.readline()
            myData=myData.rstrip()
                        
            with open(path,"a")as f:
                    
                # f.write(str(datetime.now().strftime('%H:%M:%S'))+'\n') 
                moment = datetime.now()
                calendar = datetime.strftime(moment, '%H:%M:%S')
                f.write(str(calendar)+'   ')
                decoded_Data= myData.decode('utf-8')
                #decoded_Data.strip("29289")
                f.write(str(decoded_Data)+'\n') 
                #time.sleep(1)
                        #b = b'1234'
                        #print(b.decode('utf-8'))  # '1234'   
                        
except KeyboardInterrupt:
    arduinoSerialData.close()