# Define Fizz
def Fizz(num):
    if num % 3 == 0:
        print("Fizz")

# Define Buzz
def Buzz(num):
    if num % 5 == 0:
        print("Buzz")

# Define FizzBuzz
def FizzBuzz(num):
    if num % 3 == 0 and num % 5 == 0:
        print("FizzBuzz")

# Output of anything else should be the integer
    else: print(num) 

# Define the range of numbers to iterate through
for num in range(1, 101):
    # Call the functions Fizz, Buzz, and FizzBuzz based on the conditions
    Fizz(num)
    Buzz(num)
    FizzBuzz(num)
