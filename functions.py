def convert_temperature(value, conversion_type):
    if conversion_type.lower()=='celsius to fahrenheit':
       return (value* 9/5)+32
    elif conversion_type.lower()=='fahrenheit to celsius':
       return (value -32) *5/9
    else:
       return none


def get_user_input():
    conversion_type =input('Enter conversion type (Celsius to Fahrenheit or Fahrenheit to Celsius): ')
    temperature_value = float(input('Enter the temperature value to convert: '))
    return conversion_type, temperature_value

def main():
    conversion_type, temperature_value = get_user_input()
    result = convert_temperature(temperature_value, conversion_type)
    
    if result is not None:
        print(f"Converted temperature: {result:.2f}")
    else:
        print("Invalid conversion type. Please enter 'Celsius to Fahrenheit' or 'Fahrenheit to Celsius'.")

if __name__ == "__main__":
    main()
