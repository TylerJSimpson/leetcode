class Solution:
    def convertTemperature(self, celsius: float) -> List[float]:
        """
        convertTemperature returns temperature in Kelvin and Fahrenheit when given Celsius input
        celsius: float (0 <= celsius <= 1000)
        """
        kelvin_fahrenheit_array = []                    #create array for kelvin and fahrenheit results
        kelvin = celsius + 273.15                       #calculate kelvin
        kelvin_fahrenheit_array.append(kelvin)          #add kelvin to array
        fahrenheit = celsius * 1.80 + 32.00             #calculate fahrenheit
        kelvin_fahrenheit_array.append(fahrenheit)      #add fahrenheit to array
        return kelvin_fahrenheit_array
