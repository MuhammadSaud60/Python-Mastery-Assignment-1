
"""
    Name: Muhammad Saud
    Cohort: PSEB-AI-PEW-01 (PSEB-AI-PEW-01)

"""



# Warm-up: Shopping list

items = ["milk", "bread", "eggs"]

items.append('tea')

items.remove('bread')

items.sort()


for num, item in enumerate(items):

    print(num, " ", item)



# Build: Phone book


CONTACTS = {'Ali': '12345678', 'Saad': '5443245', 'Khan': '37846392', 'Abid': '576938945', 'Zaid': '56384623'}

SEARCH = True

print('CHOOSE AN OPTION: 1) add, 2) search, 3) delete, 4) show all, 5) exit')

while SEARCH:    
    try:
        user_choose = int(input('Select (1-5): '))
    except ValueError:
        print('Please enter a valid number option.')
        continue

    if user_choose == 1:
        name = input('Enter name: ')
        contact_num = input('Enter contact number: ')
        CONTACTS[name] = contact_num
        print(f'Added {name} successfully.')

    elif user_choose == 2:
        find = input('Find name: ')
        if find in CONTACTS:
            print(f'{find}: {CONTACTS[find]}')
        else:
            print(f'Not Found: "{find}"')

    elif user_choose == 3:
        delete_contact = input('Type name to delete: ')
        if delete_contact in CONTACTS:
            del CONTACTS[delete_contact]
            print('Deleted successfully.')
        else:
            print(f'Unable to delete. "{delete_contact}" does not exist.')

    elif user_choose == 4:
        if not CONTACTS:
            print('(Directory is empty)')
        for name, contact in CONTACTS.items():
            print(f'{name}: {contact}')

    elif user_choose == 5:
        print('Goodbye')
        break

    else:
        print('Please choose an option between 1 and 5.')



# Challenge: Class result sheet

STUDENTS = {
    'Ali': [85, 90, 78, 82, 88, 91, 86],
    'Saad': [76, 88, 92, 80, 84, 89, 93],
    'Khan': [5, 81, 87, 90, 86, 83, 92],
    'Abid': [79, 85, 88, 91, 77, 84, 19],
    'Zaid': [90, 87, 82, 95, 88, 91, 85],
}

TOPPER_SCORE = 0
TOPPER_NAME = ''
BELOW_40 = set()

for student, marks in STUDENTS.items():
    print(f'======= {student} =======')
    total = sum(marks)
    print(f'Total: {total}')
    print(f'Average: {sum(marks)/len(marks)}')


    if total > TOPPER_SCORE:
        TOPPER_SCORE = total
        TOPPER_NAME = student


    for mark in marks:
        if mark < 40:
            BELOW_40.add(student)



print('\n==================================================\n')
print(f'Topper: {TOPPER_NAME} with {TOPPER_SCORE} Score.')
print(f'STUDENT WHO SCORE BELOW 40 IN ANY SUBJECT: {BELOW_40}')
print('\n==================================================\n')
