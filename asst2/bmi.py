# Maxwell Richard Tamer Mahoney ID #: 201804029
# Accepts weight (in kg) and height (in meters), returning the category of BMI.
import sys

weight = float(sys.argv[1])
height = float(sys.argv[2])

bmi = weight // height ** 2

if bmi < 15:
    print("Starvation")
elif bmi < 17.5:
    print("Anorexic")
elif bmi < 18.5:
    print("Underweight")
elif bmi >= 18.5 and bmi < 25:
    print("Ideal")
elif bmi >= 25 and bmi < 30:
    print("Overweight")
elif bmi >= 30 and bmi < 40:
    print("Obese")
elif bmi >= 40:
    print("Morbidly Obese")
