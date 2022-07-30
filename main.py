#inputs
height = float(input("Please enter your height in cm"))
weight = float(input("Please enter your weight in kg"))

#BMI Formula
BMI = weight / (height/100) ** 2

#printing BMI
print(f"Your BMI is {BMI} ")

#if conditions for BMI
if BMI <= 18.4:
    print("You're underweight.")

elif BMI <=24.9:
    print("You're healthy.")

elif BMI<=29.9:
    print("You're over weight.")

elif BMI<=34.9:
    print("You're severley over weight.")

elif BMI<=39.9:
    print("You're obese.")

else:
    print("You're severely obese.")

