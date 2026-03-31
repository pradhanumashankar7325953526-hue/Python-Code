a = {
    'Bob': 88,
    'roll no': 5,
    'sec': 'A',
    'branch':'cse'
}
print("The dictionary created is:")
print(a)
print("-" * 20)
print("Display the key-value pairs:") 
for name, score in a.items():
    print(f"{name}'s score is {score}")
print("-" * 20)
print("Display the only keys:")
for name in a.keys():
    print(name)
print("-" * 20)
print("Displaying only the values:")
for score in a.values():
    print(score)