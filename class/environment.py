class environment(object):
    def __init__(self):
        '''
        # class environment

        This class contains several informations about user environment.
        User records detail information about their environment, and sever would calculate client future state about weather(or cilmate).

        + temperature
        This variable contains 
        + humidity

        + wind_velocity

        + get_ temperature

        + get_humidity

        + get_wind_velocity


        '''

        self.temperature = None # must be celcius not fahrenheit
        self.humidity = None
        self.wind_velocity = None


    def get_temperature(self, temperature):
        self.temperature = temperature
        return True
    
    def get_humidity(self, humidity):
        self.humidity = humidity
        return True

    def get_wind_velocity(self, wind_velocity):
        self.wind_velocity = wind_velocity
        return True


    