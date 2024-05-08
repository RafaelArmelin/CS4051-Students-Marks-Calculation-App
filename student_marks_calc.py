# Function to calculate the mean of the numbers.
def calculate_mean(numbers):
# Calculate the sum of all numbers and divide by the count of numbers
    return sum(numbers) / len(numbers) if len(numbers) > 0 else 0

#Function to calculate the median of the numbers.
def calculate_median(numbers): 
    numbers.sort() #Sort the numbers in ascending order
    #Check if the count of numbers is even or odd
    n = len(numbers)
    if n % 2 == 0: # If even, calculate the average of the two middle numbers
        return (numbers[n // 2 - 1] + numbers[n // 2]) / 2
    else: # If odd, return the middle number
        return numbers[n // 2]

#Function to calculate the mode of the numbers.
def calculate_mode(numbers): 
    mode_count = 0
    mode = None
    # Iterate through each number
    for num in numbers:
        # Count the occurrences of the current number in the list
        count = numbers.count(num)
        # Update mode and mode count if the current number has a higher count
        if count > mode_count:
            mode_count = count
            mode = num
    return mode

#Function to calculate the skewness of the numbers.
def calculate_skewness(numbers):
    n = len(numbers)
    mean = calculate_mean(numbers) # Calculate the mean of the numbers
    
    variance = sum((x - mean) ** 2 for x in numbers) / n # Calculate the variance of the numbers
    
    std_dev = variance ** 0.5 # Calculate the standard deviation
    # Calculate the skewness using the formula
    skewness = sum((x - mean) ** 3 for x in numbers) * n / ((n - 1) * (n - 2) * std_dev ** 3) if std_dev != 0 else 0
    return skewness

# Function to get the numbers from the user.
def get_numbers():
    numbers = []
    while True:
        num_input = input("Please, enter your number (type 'done' to finish): ")
        if num_input.lower() == 'done':
            break
        elif ',' in num_input:  # Check if input contains commas
            for num_str in num_input.split(','):
                try:
                    num_int = int(num_str)
                    numbers.append(num_int)
                except ValueError:
                    print(f"Ignoring non-integer value: {num_str}")
        elif num_input.isdigit():  # Check if input consists of digits
            numbers.append(int(num_input))
        else:
            print("Invalid input! Please enter a valid number.")
    print("\nThe numbers you have entered are: ", numbers)
    return numbers
# Function to validade the user inputs
def validate_input(numbers):
    validated_numbers = []
    for num in numbers:
        try:
            validated_numbers.append(int(num)) 
        except ValueError:
            print(f"Invalid input '{num}'! Please enter a valid number.")
    return validated_numbers

# Function to read numbers from a file.
def read_numbers_from_file(filename):
    try:
        with open(filename, 'r') as file:
            numbers = []
            for line in file:
                line = line.strip()
                if line:
                    numbers.extend(map(int, line.split(',')))
            print(f"The numbers read from the file '{filename}' are: ", numbers)
            return numbers
    except FileNotFoundError:
        print("File not found.")
        return []

def main():
    numbers = [] #starting with an empty array list
    print("\n\nHELLO! WELCOME TO YOUR STUDENTS MARKS CALCULATOR :)\n") #Greeting the user 
    
    while True:
        # Prompting the user to choose how they would like to imput their marks, typed or read from a file
        user_first_input = input("Press 1 if you'd like to type your numbers or\nPress 2 if you prefer to read the numbers from a file: ")
        
        if user_first_input == '1':
            print("\nYou have chosen to 'type your numbers'! \n") #just clari
            numbers = get_numbers() #calling the function to get the user number inputs
            break  # Exit the loop if option 1 is chosen
        elif user_first_input == '2':
            print("\nYou have chosen to 'read from a file'! \n")
            filename = input("Please, enter the full name of your text file: ")
            numbers_from_file = read_numbers_from_file(filename) #calling the function to read the numbers from a file
            if numbers_from_file:
                numbers.extend(numbers_from_file)
            break  # Exit the loop if option 2 is chosen
        else:
            print("Invalid choice!\n")

    while True:
        print("\nMenu:") # Creating a menu of actions for the user to choose
        print("1. Print the mean of the numbers")
        print("2. Print the median of the numbers")
        print("3. Print the mode of the numbers")
        print("4. Find the skewness of the numbers")
        print("5. Enter a NEW set of numbers")
        print("6. Enter MORE numbers to your current set")
        print("7. Exit the application\n")
        
        choice = input("Enter the number of your choice: ")
        if choice == '1':
            if len(numbers) >= 2:
                mean = calculate_mean(numbers) # Calling the function to calculate the mean
                print("The Mean is: ", mean) # Printing the mean result
            else:
                # Error message to prompt the user to enter a minimum range of numbers
                print("ERROR! You must enter at least two numbers before calculating the mean.") 
        elif choice == '2':
            if len(numbers) >= 2:
                median = calculate_median(numbers) # Calling the function to calculate the median
                print("The Median is: ", median) # Printing the median result
            else:
                print("ERROR! You must enter at least two numbers before calculating the median.") 
        elif choice == '3':
            if len(numbers) >= 2:
                mode = calculate_mode(numbers) # Calling the function to calculate the mode
                print("The Mode is: ", mode) # Printing the mode result
            else:
                print("ERROR! You must enter at least two numbers before calculating the mode.")
        elif choice =='4':
            if len(numbers) >= 2:
                skewness = calculate_skewness(numbers) # Calling the function to calculate the skewness
                print("The Skewness is: ", skewness) # Printing the skewness result
            else:
                print("ERROR! You must enter at least two numbers before calculating the skewness.")
        elif choice == '5':
            numbers = get_numbers() # Prompt user to enter new numbers
            numbers = validate_input(numbers) # Validate and convert the input
        elif choice == '6':
            new_numbers = get_numbers() # Prompt user to enter new numbers
            new_numbers = validate_input(new_numbers) # Validate and convert the input
            numbers += new_numbers # Add the new numbers to the current set
            print("Your current list of numbers are: ", numbers) # print the new current set of numbers
        elif choice == '7':
            print("\nEXITING THE APPLICATION!\n\n") # Exit the application message
            break # Break and exit the application message
        else:
            # Prompting the user to choose a number within the set range
            print("Invalid choice. Please enter a number between 1 and 7.") 

# Main starting point of the program execution when the python script is run directly
if __name__ == "__main__":
    main()
