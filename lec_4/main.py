def classify_numbers(numbers):
    even_numbers = []
    odd_numbers = []

    for num in numbers:
        if num % 2 == 0:
            even_numbers.append(num)
        else:
            odd_numbers.append(num)

    return even_numbers, odd_numbers


user_input = input("Enter a list of numbers separated by spaces: ")

numbers = [int(x) for x in user_input.split()]


even_numbers, odd_numbers = classify_numbers(numbers)

# Print the list of even numbers and the list of odd numbers
print("Even numbers:", even_numbers)
print("Odd numbers:", odd_numbers)
