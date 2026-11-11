"""
    Name: Muhammad Saud
    Cohort: PSEB-AI-PEW-01 (PSEB-AI-PEW-01)

"""


# Warm-up: Even, odd and sign

# number = int(input('Enter a number: '))

# # 1. Determine Sign
# if number == 0:
#     print('Number is Zero')
# elif number < 0:
#     print('Number is Negative')
# else:
#     print('Number is Positive')

# if number != 0: 
#     if number % 2 == 0:
#         print(f'{number} is Even')
#     else:
#         print(f'{number} is Odd')


# # Build: Grade calculator

# marks = int(input("Enter marks out of 100: "))

# if marks < 0 or marks > 100:
#     print("Invalid marks")
    
# elif marks >= 80:
#     print("Grade: A")
# elif marks >= 70:
#     print("Grade: B")
# elif marks >= 60:
#     print("Grade: C")
# elif marks >= 33:
#     print("Grade: D")
# else:
#     print("Grade: Fail")


# Challenge: Electricity bill

units = int(input('Enter total units: '))
FIXED_CHARGES = 50

if units <= 100:

    bill = units * 10

elif units <= 200:

    bill = (100 * 10) + ((units - 100) * 15)

else:
    bill = (100 * 10) + (100 * 15 ) + ((units - 200) * 20)


total_bill = bill + FIXED_CHARGES

print(f'TOTAL BILL: {total_bill}')