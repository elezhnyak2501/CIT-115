# ------------------------------------------------------------- 
# Compound Interest Savings Program
# -------------------------------------------------------------

# validate numeric input
def getNumericValue(sPrompt, bAllowZero, bAllowNegative):
    while True:
        try:
            sInput = input(sPrompt)
            fValue = float(sInput)

            # Negative check
            if not bAllowNegative and fValue < 0:
                print("Input must be a positive numeric value")
                continue

            # Zero check
            if not bAllowZero and fValue == 0:
                print("Input must be a positive numeric value")
                continue

            return fValue

        except ValueError:
            print("Input must be a positive numeric value")


# -------------------------------------------------------------
# 1. Prompt user for input with validation
# -------------------------------------------------------------

# Deposit: Must be numeric & positive
fDeposit = getNumericValue("What is the Original Deposit (positive value): ", bAllowZero=False, bAllowNegative=False)

# Interest Rate %: Must be numeric, positive, non-zero
fInterestPct = getNumericValue("What is the Interest Rate (positive value): ",
                               bAllowZero=False, bAllowNegative=False)

# Number of Months: Must be numeric, positive, non-zero
iMonths = int(getNumericValue("What is the Number of Months (positive value): ", bAllowZero=False, bAllowNegative=False))

# Goal: Numeric, can be zero, but NOT negative
fGoal = getNumericValue("What is the Goal Amount (can enter 0 but not negative): ", bAllowZero=True, bAllowNegative=False)


# -------------------------------------------------------------
# 3. Convert interest percentage → monthly interest rate
# -------------------------------------------------------------

fInterestDecimal = fInterestPct / 100
fMonthlyRate = fInterestDecimal / 12

# Balance used for the monthly output loop
fBalance = fDeposit


# -------------------------------------------------------------
# 4. Compound interest loop for the given number of months
# -------------------------------------------------------------
for iMonthCounter in range(1, iMonths + 1):
    fMonthlyInterest = fBalance * fMonthlyRate     
    fBalance += fMonthlyInterest                   
    print("Month: {} Account Balance is: {:,.2f}".format(iMonthCounter, fBalance))


# -------------------------------------------------------------
# 5. Loop to determine months needed to reach goal
# -------------------------------------------------------------


print("Goal Prediction")


if fGoal == 0:
    print("No goal entered. Goal prediction skipped.")
else:
    fGoalBalance = fDeposit        
    iGoalMonths = 0              

    while fGoalBalance < fGoal:
        iGoalMonths += 1
        fMonthlyInterest = fGoalBalance * fMonthlyRate
        fGoalBalance += fMonthlyInterest

    print("It will take {:,} months to reach your goal of ${:,.2f}.".format(iGoalMonths, fGoal))
