# Body Mass Index Calculator
height = input("What is your height in m: ")
weight = input("What is your current weight in kg: ")

int_height = float(height)
int_weight = int(weight)
total = int_weight / int_height ** int_height        # "/" float , "//" rounded

print("Your current BMI is: " + str(round(total)))

