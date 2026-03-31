fruits = ["apple", "banana", "cherry", "mango", "orange"]
print("Fruits in reverse order with their lengths:")
for fruit in fruits[::-1]:   
    print(fruit, "-> length:", len(fruit))
reversed_fruits = []
for fruit in fruits:
    reversed_fruits.append(fruit[::-1])  
print("\nList of reversed fruit names:")
print(reversed_fruits)