sentence = input("Enter a sentence: ")
LIST1 = sentence.split()
print("\nWords with their index:")
for index, word in enumerate(LIST1):
    print(f"Index {index}: {word}")
LIST2 = list(range(1, len(LIST1) + 1))
LIST3 = list(zip(LIST1, LIST2))
print("\nCombined LIST3 (word, number):")
print(LIST3)