import math

def getFloatInput(prompt):
    return float(input(prompt + ": "))

def getGallonsOfPaint(squareFeet, feetPerGallon):
    return math.ceil(squareFeet / feetPerGallon)

def getLaborHours(hoursPerGallon, gallons):
    return hoursPerGallon * gallons

def getLaborCost(laborHours, laborCharge):
    return laborHours * laborCharge

def getPaintCost(gallons, paintPrice):
    return gallons * paintPrice

def getSalesTax(state):
    taxRates = {
        "CT": 0.06,
        "MA": 0.0625,
        "ME": 0.085,
        "NH": 0.0,
        "RI": 0.07,
        "VT": 0.06
    }
    return taxRates.get(state.upper(), 0.0)

def showCostEstimate(gallons, laborHours, laborCost, paintCost, taxAmount, totalCost):
    print(f"Gallons Needed: {gallons:.2f}")
    print(f"Labor Hours: {laborHours:.2f}")
    print(f"Labor Cost: {laborCost:.2f}")
    print(f"Paint Cost: {paintCost:.2f}")
    print(f"Sales Tax: {taxAmount:.2f}")
    print(f"Total Cost: {totalCost:.2f}")

def main():
    squareFeet = getFloatInput("Enter Square Feet")
    paintPrice = getFloatInput("Enter Paint Price")
    feetPerGallon = getFloatInput("Enter Feet per Gallon")
    laborHoursPerGallon = getFloatInput("Enter Labor Hours per Gallon")
    laborCharge = getFloatInput("Enter Labor Charge per Hour")

    state = input("Enter State: ")

    gallons = getGallonsOfPaint(squareFeet, feetPerGallon)
    laborHours = getLaborHours(laborHoursPerGallon, gallons)
    laborCost = getLaborCost(laborHours, laborCharge)
    paintCost = getPaintCost(gallons, paintPrice)
    taxRate = getSalesTax(state)
    taxAmount = (laborCost + paintCost) * taxRate
    totalCost = laborCost + paintCost + taxAmount

    showCostEstimate(gallons, laborHours, laborCost, paintCost, taxAmount, totalCost)

main()
