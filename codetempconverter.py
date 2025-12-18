# Welcome message
print("Welcome to Emily's Temp Converter!")

# Prompt for temperature input
fltTempInput = input("Enter a temperature: ")

# Validate and convert temperature input
try:
    fltTempValue = float(fltTempInput)
except ValueError:
    print("Invalid temperature input. Please enter a number.")
    exit()

# Prompt for unit input
strTempUnit = input("Is this in (F)ahrenheit or (C)elsius? Enter F or C: ").strip().upper()

# Validate unit input
if strTempUnit not in ['F', 'C']:
    print("Enter a F or C")
    exit()

# Temperature conversion logic
if strTempUnit == 'F':
    if fltTempValue > 212:
        print("Temp can not be > 212")
    else:
        fltCelsius = (5.0 / 9.0) * (fltTempValue - 32)
        print(f"The Celsius equivalent is: {round(fltCelsius, 1)}")
elif strTempUnit == 'C':
    if fltTempValue > 100:
        print("Temp can not be > 100")
    else:
        fltFahrenheit = ((9.0 / 5.0) * fltTempValue) + 32
        print(f"The Fahrenheit equivalent is: {round(fltFahrenheit, 1)}")
