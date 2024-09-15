# 1. *Create a function* that takes an array, an index,
#  and a value as parameters. Inside the function,
#  use the insert method to insert the value at the
#  specified index in the array. Return the modified array.
def insert_value_at_index(array, index, value):
    # Insert the value at the specified index
    array.insert(index, value)
    return array
def main():
    input_array = input("Enter elements of the array separated by spaces: ")
    array = list(map(int, input_array.split()))  # Convert input string to list of integers
    index = int(input("Enter the index where you want to insert the value: "))
    value = int(input("Enter the value to insert: "))
    # Call the function
    modified_array = insert_value_at_index(array, index, value)
    print("Modified array:", modified_array)

# Run the main function
if __name__ == "__main__":
    main()
# 2. *Implement a simple shopping cart program* 
#  using an array. Create functions to add items, 
# remove items, and update quantities using array methods.
#  Print the cart's contents after each operation.
# Function to display the cart's contents
arr = input("Welcome to my Mart !")
arr1 = input("Add Items To Cart : ")
items = list(arr1.split())  

def shopping_cart(items):
    print(f"Your items are {items}")
    ask_input = input("Do you want to remove any item from your cart?  ")
    if ask_input.lower() == "yes":
        remove_item = input("Which item do you want to remove?  ")
        if remove_item in items:
            items.remove(remove_item)
            print(f"Removed {remove_item} from your cart.")
        else:
            print(f"{remove_item} is not in your cart.")
    print(f"Now your updated cart is {items}")
    return items
    
result = shopping_cart(items)
print(result)

# 3. *Write a program* that uses a while loop to print the first 25 integers.
count : int = 1
while count <= 25 :
        print (count)
        count  = count + 1

# # 4. *Write a program* that uses a while loop to print the first 10 even numbers.
count : int = 1
while count <= 20 :
        if count %2 ==0 :
           print (count)
        count  = count + 1

# 5. *Create a function* that takes a positive integer as a 
# parameter and uses a for loop to calculate and return the factorial of that number.
# Get the user input and convert it to an integer
# Get the user input and convert it to an integer
number = int(input("Enter a positive integer: "))
factorial = 1
for i in range(1, number + 1):
    factorial *= i
print("The factorial of", number, "is", factorial)

# 6. *Write a program* that has an array of numbers;
#  if the number is negative, it should remove the negative number from the array.
array = input("Enter a number with spaces : ")
remove_numbers = list(map(int, array.split()))
add = []
for i in remove_numbers :
    if i > 0:
            add.append(i)
print(add)
# 7. *Create a function* that takes an array of numbers as a parameter.
# Use a while loop to calculate and return the sum of all the numbers in the array.
# Function to calculate the sum of an array of numbers
def sum_of_numbers(array):
    total_sum = 0
    index = 0
    while index < len(array):
        total_sum += array[index]
        index += 1
    return total_sum
input_string = input("Enter numbers separated by spaces: ")
array = list(map(int, input_string.split()))
result = sum_of_numbers(array)
print("The sum of the numbers is", result)

# 8. *Implement a program* that takes a list of temperatures in
# Celsius as input from the user. Convert each temperature to 
# Fahrenheit using the formula F = (C * 9/5) + 32 and store the 
# converted temperatures in an array. Use a while loop to perform 
# the conversion for each temperature.
# Function to convert a list of temperatures from Celsius to Fahrenheit
def convert_to_fahrenheit(celsius_temps):
    fahrenheit_temps = []
    index = 0
    # Use a while loop to convert each temperature
    while index < len(celsius_temps):
        # Get the current Celsius temperature
        celsius_temp = celsius_temps[index]
        # Convert Celsius to Fahrenheit
        fahrenheit_temp = (celsius_temp * 9/5) + 32
        fahrenheit_temps.append(fahrenheit_temp)
        index += 1
    return fahrenheit_temps
input_string = input("Enter temperatures in Celsius separated by spaces: ")
celsius_temps = list(map(float, input_string.split()))
# Convert the Celsius temperatures to Fahrenheit and print the result
fahrenheit_temps = convert_to_fahrenheit(celsius_temps)
print("Temperatures in Fahrenheit:", fahrenheit_temps)

# 9. *Write a program* to remove all the odd numbers from an array.
arr = input("Enter a number : ")
remove_odd = list(map(int, arr.split()))
add = []
count = 0
while count < len(remove_odd) :
        if remove_odd[count] %2 == 0 :
            add.append(remove_odd[count])
        count  = count + 1
print("modified list is ,", add)
# complete


