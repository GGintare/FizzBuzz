# FizzBuzz
# For each number from 1 to 100 - print Fizz when number is divisible by 3. Print Buzz when number is divisible by 5.
# Print FizzBuzz when number is divisible by 3 and 5. Else print the number itself.
# Bonus tasks:
# 0. Return Foo whenever number is divisible by 7. Print FizzBuzzFoo when number is divisible by 3, 5 and 7.
# 1. Make a results array instead of printing to console.
#    1.1 Make a function
# 2. Allow user to input any range.
# 3. Accept range bounds as command line argument.
# 4. Extract only numbers from the array and sort them.
# 5. Filter only prime numbers from the list you made in task 4.
# 6. From the provided excel sheet get only the lines with numbers from task 5.
# 7. Return only * from the list you made in task 6.


def main_function():
    result = []
    for x in range(1, 101):
        string = ""
        if x % 3 == 0:
            string = string + 'Fizz'
        if x % 5 == 0:
            string = string + 'Buzz'
        if x % 7 == 0:
            string = string + 'Foo'
        
        if string:
            result.append(string)
        else:
            result.append(x)
 
    return result

print(main_function())
print("test")
