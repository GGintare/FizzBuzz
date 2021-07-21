# FizzBuzz
# For each number from 1 to 100 - print Fizz when number is divisible by 3. Print Buzz when number is divisible by 5.
# Print FizzBuzz when number is divisible by 3 and 5. Else print the number itself.
# Bonus tasks:
# 0. Return Foo whenever number is divisible by 7. Print FizzBuzzFoo when number is divisible by 3, 5 and 7.
# 1. Make a results array instead of printing to console.
# 2. Allow user to input any range.
# 3. Accept range bounds as command line argument.
# 4. Extract only numbers from the array and sort them.
# 5. Filter only prime numbers from the list you made in task 4.
# 6. From the provided excel sheet get only the lines with numbers from task 5.
# 7. Return only * from the list you made in task 6.

for x in range(1, 101):
    if x % 3 == 0 and x % 5 == 0 and x % 7 == 0:
        print('FizzBuzzFoo')
    elif x % 3 == 0 and x % 5 == 0:
        print('FizzBuzz')
    elif x % 7 == 0:
        print('Foo')
    elif x % 5 == 0:
        print('Buzz')
    elif x % 3 == 0:
        print('Fizz')
    else:
        print(x)
print('hello')
