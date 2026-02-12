"""
sequence is a category of data types that store an ordered collection of items
Pythno have six built-in sequence types: list, tupes, strings, range objects.... 
"""
def for_loop_sequence():
    # example with list sequence
    fruits = ["apple", "banana", "cherry", "date"]
    print("Looping over list sequence:")
    for fruit in fruits:
        print(fruit)

    # example with string sequence
    print("\nLooping over string sequence:")
    word = "Venkata"
    for i in word:
        print(i)
for_loop_sequence()