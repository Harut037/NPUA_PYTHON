def sum_of_elements(numbers, exclude_negative=False):
    if exclude_negative:
        numbers = [num for num in numbers if num >= 0]
    return sum(numbers)


user_input = input("Enter a list of numbers separated by spaces: ")


numbers = [int(x) for x in user_input.split()]


exclude_negative = input("Do you want to exclude negative numbers? (yes/no): ").lower()

if exclude_negative == 'yes':
    exclude_negative = True
else:
    exclude_negative = False


result = sum_of_elements(numbers, exclude_negative)


print(f"The sum of the elements {'excluding' if exclude_negative else 'including'} negative numbers is: {result}")
