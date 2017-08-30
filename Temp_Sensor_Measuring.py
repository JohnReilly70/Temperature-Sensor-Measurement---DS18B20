import os
import glob
import time
import Temp_Sensor_Class as TSC



def main():
    
    os.system('modprobe w1-gpio')
    os.system('modprobe w1-therm')
     
    base_dir = '/sys/bus/w1/devices/'
    device_folders = glob.glob(base_dir + '28*')
    sensor_list = [TSC.Temp_Sensor(device_id) for device_id in device_folders]
     
	
    while True:
        
        try:
            for sensor in sensor_list:
                
                sensor.read_temp()
                print(sensor.temp) #This is where you could switch on or off a heater
                
            time.sleep(1)
            
        except KeyboardInterrupt:
            print ("Program Exited Cleanly")

if __name__ == '__main__':
    main()
