# BDJ Real Estate Sales Analyzer Program
# Author: Emily Lezhnyak
# Description: Analyzes real estate sales using lists and functions

def getFloatInput(number):
    while True:
        try:
            value = float(input(number))
            if value <= 0:
                print("Input a number that is greater than 0.")
            else:
                return value
        except ValueError:
            print("Input a number that is greater than 0.")

def getMedian(sales_list):
    sales_list.sort()
    count = len(sales_list)
    mid = count // 2

    if count % 2 == 1:
        return sales_list[mid]
    else:
        return (sales_list[mid - 1] + sales_list[mid]) / 2

def main():
    lstSales = []

    while True:
        fSalesPrice = getFloatInput("Enter property sales value: ")
        lstSales.append(fSalesPrice)

        while True:
            choice = input("Enter another value Y or N: ").upper()
            if choice in ["Y", "N"]:
                break
            else:
                print("Enter another value Y or N.")

        if choice == "N":
            break

    lstSales.sort()

    # Output each property
    for index, value in enumerate(lstSales, start=1):
        print(f"Property {index}    ${value:,.2f}")

    # Calculations
    fMin = min(lstSales)
    fMax = max(lstSales)
    fTotal = sum(lstSales)
    fAverage = fTotal / len(lstSales)
    fMedian = getMedian(lstSales)
    fCommission = fTotal * 0.03

    # Output Summary
    print(f"Minimum Sale:   ${fMin:,.2f}")
    print(f"Maximum Sale:   ${fMax:,.2f}")
    print(f"Total Sales:    ${fTotal:,.2f}")
    print(f"Average Sale:   ${fAverage:,.2f}")
    print(f"Median Sale:    ${fMedian:,.2f}")
    print(f"Commission:     ${fCommission:,.2f}")

# Program starts
if __name__ == "__main__":
    main()
