# ---------------------------------------------
# Grade Analyzer
# ---------------------------------------------
# Made by: Emily Lezhnyak
# ---------------------------------------------

# 1. Person’s name
strName = input("Name of the person for grade calculation: ")

# 2. 4 test scores - whole numbers
try:
    intTest1 = int(input("Enter Test Score 1: "))
    intTest2 = int(input("Enter Test Score 2: "))
    intTest3 = int(input("Enter Test Score 3: "))
    intTest4 = int(input("Enter Test Score 4: "))
except ValueError:
    print("Error: Only whole numbers are accepted for test scores.")
    raise SystemExit

# 3. Drop the lowest grade
strDropLowest = input("Do you want to drop the lowest grade? (Y/N): ").upper()

# 4. No score is less than 0
if intTest1 < 0 or intTest2 < 0 or intTest3 < 0 or intTest4 < 0:
    print("Test scores must be greater than 0.")
    raise SystemExit

# 5. Drop Lowest input
if strDropLowest not in ("Y", "N"):
    print("Enter Y or N to Drop the Lowest Grade.")
    raise SystemExit

# 6. Compute average 
fltAverage = 0.0

if strDropLowest == "Y":

    if intTest1 <= intTest2 and intTest1 <= intTest3 and intTest1 <= intTest4:
        fltAverage = (intTest2 + intTest3 + intTest4) / 3.0
    elif intTest2 <= intTest1 and intTest2 <= intTest3 and intTest2 <= intTest4:
        fltAverage = (intTest1 + intTest3 + intTest4) / 3.0
    elif intTest3 <= intTest1 and intTest3 <= intTest2 and intTest3 <= intTest4:
        fltAverage = (intTest1 + intTest2 + intTest4) / 3.0
    else:
        fltAverage = (intTest1 + intTest2 + intTest3) / 3.0
else:
    # Use all 4 scores
    fltAverage = (intTest1 + intTest2 + intTest3 + intTest4) / 4.0

# 7. Average is already a float, but we’ll format later for 1 decimal place

# 8. Determine letter grade
if fltAverage >= 97.0:
    strGrade = "A+"
elif fltAverage >= 94.0:
    strGrade = "A"
elif fltAverage >= 90.0:
    strGrade = "A-"
elif fltAverage >= 87.0:
    strGrade = "B+"
elif fltAverage >= 84.0:
    strGrade = "B"
elif fltAverage >= 80.0:
    strGrade = "B-"
elif fltAverage >= 77.0:
    strGrade = "C+"
elif fltAverage >= 74.0:
    strGrade = "C"
elif fltAverage >= 70.0:
    strGrade = "C-"
elif fltAverage >= 67.0:
    strGrade = "D+"
elif fltAverage >= 64.0:
    strGrade = "D"
elif fltAverage >= 60.0:
    strGrade = "D-"
else:
    strGrade = "F"

# 13, 14. Output results 
print("\n Grade Analysis:")
print(f"Student Name: {strName}")
print(f"Test Average: {fltAverage:.1f}")
print(f"Letter Grade: {strGrade}")

