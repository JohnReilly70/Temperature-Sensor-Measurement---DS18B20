import time

class Temp_Sensor():

    global pins
    pins = [3,5,7,8,10,11,13,15,16,17,19,21,22,
            23,24,26,29,31,32,33,35,36,37,38,40]
    
    def __init__(self, device_id):
        self.__name = pins.pop(0)
        self.__temp = 0
        self.__device_id = device_id
        self.__device_file = device_id + '/w1_slave'

    @property
    def device_id(self):
        return self.__device_id

    @property
    def name(self):
        return self.__name

    @property
    def temp(self):
        return self.__temp

    @temp.setter
    def temp(self, temp):
        self.__temp = temp

    def __sub__(self, sensor_2):
        '''
        Returns temperature difference between current sensor and
        another chosen sensor
        '''
        return self.__temp - sensor_2.temp

    def __str__(self):
        return f'''Temp Sensor Pin:{self.__name}
                \nTemp DegreeC:{self.__temp},
                \nDevice_id:{self.__device_id},
                \nDevice File:{self.__device_file'''

    def __repr__(self):
        return f'Sensor:{self.__name},Temp:{self.__temp}'

    def read_temp_raw(self):
        with open(self.__device_file, 'r') as f:
            lines = f.readlines()
        return lines

    def read_temp(self):
        lines = read_temp_raw()
        while lines[0].strip()[-3:] != 'YES':
            time.sleep(0.2)
            lines = read_temp_raw()
        equals_pos = lines[1].find('t=')
        if equals_pos != -1:
            temp_string = lines[1][equals_pos+2:]
            temp_c = float(temp_string) / 1000.0
            self.__temp = temp_c
