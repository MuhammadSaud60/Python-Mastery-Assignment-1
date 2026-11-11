"""
    Name: Muhammad Saud
    Cohort: PSEB-AI-PEW-01 (PSEB-AI-PEW-01)

"""


# Warm-up: Student ID

std_name = input('Enter Your Full Name: ').strip()
std_age = int(input('Enter Your Age: '))
std_class = input('In Which class do you read? ').strip()
std_city = input('Where are you from (only City)? ').strip()


print('======= STUDENT CARD =======')
print(f'Name: {std_name}')
print(f'Age: {std_age}')
print(f'Class: {std_class}')
print(f'City: {std_city}')
print('============================')


# types

print(f'Type of Name value is {type(std_name)}')
print(f'Type of Age value is {type(std_age)}')
print(f'Type of Class value is {type(std_class)}')
print(f'Type of City value is {type(std_city)}')



# Build: Shop Bill

SUBTOTAL = 0.0

try:    
    prouduct_name = input('Product Name: ').strip()
        

    if not prouduct_name:
        print('Product cannot be empty')
        

    price = float(input(f'{prouduct_name} Price: '))

    if price <= 0:
        print(f'Please enter {prouduct_name} Price')
        

    quantity = int(input('Quantity: '))

    if quantity <= 0:
        print(f'Please enter {prouduct_name} quantity')
        


    SUBTOTAL += price * quantity
        

except ValueError as e:
    print(f'Please Enter correct data {e}')



DISCOUNT = round(SUBTOTAL * 0.05, 2) 
DISCOUNT_SUBTOTAL = SUBTOTAL - DISCOUNT
TAX = DISCOUNT_SUBTOTAL * 0.17

FINAL_TOTAL = round(DISCOUNT_SUBTOTAL + TAX, 2)

    


print("======== BILL ========")
print(f'SUB TOTAL: {SUBTOTAL} ')
print(f'5% DISCOUNT: {DISCOUNT}')
print(f'17% TAX: {TAX:.2f}')
print(f'FINAL TOTAL: {FINAL_TOTAL}')
print('=======================')



# Challenge: Unit Convertor

try:
    temperature = float(input('Enter Temperature (Celsius): '))

    distance = float(input('Enter Distance (KM): '))


    fahrenheit = (temperature * 9/5) + 32
    kelvin = temperature + 273.15
    miles = distance * 0.621371
    meters = distance * 1000

    print(f'Temperature in Fahrenheit: {fahrenheit:.1f}')
    print(f'Temperature in Kelvin: {kelvin:.1f}')
    print(f'Distance in Miles: {miles:.1f}')
    print(f'Distance in Meters: {meters:.1f}')

except ValueError as e:
    print('Please check your input values.')