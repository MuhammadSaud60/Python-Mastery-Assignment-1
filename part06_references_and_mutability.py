

"""
    Name: Muhammad Saud
    Cohort: PSEB-AI-PEW-01 (PSEB-AI-PEW-01)

"""


# Warm-up: Predict, then run


# a = [1, 2, 3]
# b = a
# b.append(4)
# print(a) # prediction?
# c = a.copy()
# c.append(5)
# print(a, c) # prediction?
# print(a is b, a is c, a == a[:])

"""
    MY PREDICTION: 
        print(a) -> [1,2,3,4]
        print(a, c) -> [1,2,3], [1,2,3,5]
    
    AFTER RUN:
        I missed 4 in both a and c.
"""

# Build: Fix the cart bug

# def add_item(item, cart=[]):
#     cart.append(item)
#     return cart


# item_1 = add_item('shoes')
# item_2 = add_item('shirt')

# #  both share same items 
# print(item_1, item_2)


# # fix

# def add_item(item, cart=None):
#     if cart is None:
#         cart = []
#     cart.append(item)
#     return cart 


# item_1 = add_item('shoes')
# item_2 = add_item('shirt')

# #  now both will share own item
# print(item_1, item_2)


# Challenge: Safe class copy
import copy

classes = {"A": ["Ali", "Sara"]}
shallow_copy = copy.copy(classes)
deep_copy = copy.deepcopy(classes)

shallow_copy["A"].append("Ahmed")
deep_copy["A"].append("Mina")

print("Original:", classes)
print("Shallow copy:", shallow_copy)
print("Deep copy:", deep_copy)
