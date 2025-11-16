# Prompt for input
pv = float(input("Principal Investment (PV): "))
r_percent = float(input("Interest Rate (R): "))
t = float(input("Number of Periods (t): "))
m = int(input("Compounding (m): "))

# Convert interest rate to decimal
r = r_percent / 100

# Calculate Future Value
fv = pv * (1 + r / m) ** (m * t)

# Print result formatted to 2 decimal places with $
print(f"Future Value (FV): ${fv:.2f}")
