    # Create a function that takes a filename as string parameter,
    # counts the occurances of the letter "a", and returns it as a number.
    # If the file does not exist, the function should return 0 and not break.
    # print(count_as("afile.txt")) # should print 28
    # print(count_as("not-a-file")) # should print 0

def count_as(file_name):
    f = open(file_name, "r")
    text = f.read()
    a_counter = 0
    for letter in text:
        if letter == "a" or letter == "A":
            a_counter += 1
    return a_counter

print(count_as("/Users/MrFox/OneDrive/greenfox/exam-trial-basics/countas/afile.txt"))
