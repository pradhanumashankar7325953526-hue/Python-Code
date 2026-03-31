n = int(input("Enter number of items: "))
dict1 = {}
for i in range(n):
    key = input(f"Enter key {i+1}: ")
    value = input(f"Enter value {i+1}: ")
    dict1[key] = value
dict2 = {}
for key, value in dict1.items():
    dict2[value] = key
print("\nFirst Dictionary:")
print(dict1)
print("\nSecond Dictionary (values as keys, keys as values):")
print(dict2)