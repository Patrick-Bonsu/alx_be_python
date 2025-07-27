# Global Conversion Factors
FAHRENHEIT_TO_CELSIUS_FACTOR=5/9
CELSIUS_TO_FAHRENHEIT_FACTOR=9/5

def convert_to_celsius(fahrenheit):
    """Convert Fahrenheit to Celsius using the global factor."""
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):
    """Convert Celsius to Fahrenheit using the global factor."""
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32

def main():
    try:
        # Get temperature input from user
        temp_input = input("Enter the temperature to convert: ").strip()
        unit = input("Is the temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()

        # Validate temperature input
        temperature = float(temp_input)

        # Perform conversion
        if unit == "F":
            converted = convert_to_celsius(temperature)
            print(f"{temperature}°F is {converted:.2f}°C")
        elif unit == "C":
            converted = convert_to_fahrenheit(temperature)
            print(f"{temperature}°C is {converted:.2f}°F")
        else:
            raise ValueError("Invalid unit. Please enter 'C' for Celsius or 'F' for Fahrenheit.")

    except ValueError as e:
        print("Invalid temperature. Please enter a numeric value.")
        print("Details:", e)

if __name__ == "__main__":
    main()
