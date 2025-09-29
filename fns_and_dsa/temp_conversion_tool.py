FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

temperature = float(input("Enter the temperature to convert: "))
temperature_type = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").upper()

def convert_to_celsius(fahrenheit):
        converted = (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
        print(f"{fahrenheit}℉ is {converted}℃")
        
def convert_to_fahrenheit(celsius):
        converted = (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32
        print(f"{celsius}℃ is {converted}℉")
        
if temperature_type == 'F':
    convert_to_celsius(temperature)
elif temperature_type == 'C':
    convert_to_fahrenheit(temperature)
else:
    print("Invalid temperature. Please enter a numeric value.")

    
    

    