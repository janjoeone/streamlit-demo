height = float(input("Enter your height in m: \t"))
weight = float(input("Enter your weight in kg: \t"))

BMI = weight / height ** 2
print("Your BMI is: %.2f" % BMI)