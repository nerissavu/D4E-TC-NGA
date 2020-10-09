height = float(input("height(cm): "))
mass = float(input('mass(kg): '))

BMI = mass/(height*height/10000)
print('BMI =', BMI )

if BMI < 16:
    print('You are severely underweight')
elif BMI < 18.5: 
    print('You are underweight')
elif BMI < 25:
    print('You are normal')
elif BMI < 30:
    print('You are overweight')
else:
    print('You are obese')



