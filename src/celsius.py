def celsius_to_fahrenheit(celsius):
    if not isinstance(celsius, (int, float)) or isinstance(celsius, bool):
        raise TypeError("celsius value must be an int or float")

    if celsius < -273.15:
        raise ValueError("temperature below absolute zero is not physically possible")

    return celsius * 9 / 5 + 32
