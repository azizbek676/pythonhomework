def convert_cel_to_far(celsius: float) -> float:
    """Converts temperature from Celsius to Fahrenheit."""
    return celsius * 9 / 5 + 32

def convert_far_to_cel(fahrenheit: float) -> float:
    """Converts temperature from Fahrenheit to Celsius."""
    return (fahrenheit - 32) * 5 / 9
fahrenheit = float(input("Enter a temperature in Fahrenheit: "))
celsius_from_far = convert_far_to_cel(fahrenheit)
print(f"{fahrenheit} Fahrenheit is equal to {celsius_from_far:.2f} Celsius.")
celsius = float(input("Enter a temperature in Celsius: "))
fahrenheit_from_cel = convert_cel_to_far(celsius)
print(f"{celsius} Celsius is equal to {fahrenheit_from_cel:.2f} Fahrenheit.")
