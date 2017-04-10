
    # Create a function that takes a list as a parameter,
    # and returns a new list with every second element from the orignal list
    # example: [1, 2, 3, 4, 5] should produce [2, 4]
# print(seconds([1, 2, 3, 4, 5])) # should print [2, 4]

def seconds(numbers):
    seconds = []
    for number in numbers[1::2]:
        seconds.append(number)
    return(seconds)


print(seconds(["apple", "orange", "lemon", "banana", "pear", "strawberry"]))
