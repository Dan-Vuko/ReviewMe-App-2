# ______            _                ___ ____    ___
# |  __ \          (_)               |  \/  |    | |
# | |__) |_____   ___  _____      __ | \  / | ___| |
# |  _  // _ \ \ / / |/ _ \ \ /\ / / | |\/| |/ _ \ |
# | | \ \  __/\ V /| |  __/\ V  V /  | |  | |  __/_|
# |_|  \_\___| \_/ |_|\___| \_/\_/   |_|  |_|\___(_)

# No bugs found in the program
# Everything works as expected 100% of the time
# Code could be more efficient and readable with some changes, and shorter

# [!] NOTE: I did not realise until after completing the assignment that the project rubric states we must use tuples instead of dictionaries.

### Welcome Message ###
def welcome():
    print("Welcome to ReviewMe!\n")   # Print welcome message #
    print("1. Find the Rating of the Restaurant\n2. List top n restaurants\n3. Exit\n")   # Prompt user for input #

### User Input Function ###
def user_input1():
    min_number = 1   # Set the minimum number as a variable #
    max_number = 3   # Set the maximum number as a variable #
    while True:   # Run the loop until the user enters a valid input #
        try:   # Try to run the program #
            option = int(input("What would you like to do? (Enter 1, 2 or 3):\n"))   # Prompt the user for input #
            break   # Break the loop if the user enters a valid input #
        except ValueError:   # If the user enters an invalid input, print an error message #
            print("Please enter an integer between 1 and 3.")
    if option < min_number:   # If the user enters a number less than the minimum number, print an error message #
        print("Invalid value. Please enter a non-negative integer.")   # Print an error message #
    if option > max_number:   # If the user enters a number greater than the maximum number, print an error message #
        print("Please enter an integer between 1 and 3.")   # Print an error message #
    if option >= min_number and option <= max_number:   # If the user enters a valid input, return the input #
        return option   # Return the input #
    else:   # If the user enters an invalid input, return the input #
        return user_input1()   # Return the user_input1 function #

### Read Score Data Function ###
def read_score_data():
    filename = "scores.txt"   # Set variable for text file #
    data = {}   # Create a dictionary #
    with open(filename) as file:   # Open the file #
        for line in file:   # Read each line #
            (key, val) = line.strip().split(",")   # Split the line on the comma #
            data[(key)] = val   # Add the key and value to the dictionary #
    return data   # return data from read_score_data function # 

### Check Data function ###
def check_data():   # Check the data in the text file #
    filename = "scores.txt"    # Set variable for text file #
    with open(filename) as file:   # Open the file #
        for line in file:   # Read each line #
            if len(line.strip().split(",")) == 2:   # Check if the line has 2 values #
                return True   # If it does, return True #
            else:  # If it doesn't, return False #
                return False

### Validate Text File ###
def validate_text():   # Validate the text file #
    values = {}   # Create a dictionary #
    filename = "scores.txt"   # Open the file #
    with open(filename) as file:
        for line in file:   # Read each line #
            (key, val) = line.strip().split(",")   # Split the line on the comma #
            values[(key)] = val
    try:   # Try to convert the values to integers #
        values = dict([(a, float(x)) for a, x in values.items()])   # Convert the values to floats #
        return True   # return True if the values are floats #
    except ValueError:   # If the values are not floats, return False #
        return False   

### Restaurant name function ###
def option_1():   # Find the name of the restaurant #
    print("What is the name of the restaurant?")   # Prompt the user for the name of the restaurant #
    restaurant_name = input()   # Set the restaurant name as a variable #
    return restaurant_name   # Return restaurant name from option_1 function #

### Check Restaurant Name Function ###
def check_restaurant_name(restaurant_name, data):  # Check if the restaurant name is in the text file #
    if restaurant_name in data:   # if the restaurant name is in the dictionary, print the restaurant name and rating #
        print(f"{restaurant_name} has a rating of {data[restaurant_name]}")   # Print the restaurant name and rating #
    else:   # If the restaurant name is not in the dictionary, print an error message #
        print(f"We don’t have rating for {restaurant_name}")   # Print an error message #
        return False   # Return False if the restaurant name is not in the dictionary #

### Top n Restaurants Function ###
def top_n_restaurants():   # Find the top n restaurants #
    data = read_score_data()   # Call the read_score_data function #
    while True:    # Run the loop until the user enters a valid input #
        try:   # Try to run the program #
            n = int(input("How many restaurants would you like to list?\n"))   # Prompt the user for input #
            if n < 0:   # If the user enters a number less than 0, print an error message #
                print("Invalid value. Please enter a non-negative integer.")   # Print an error message #
                main()   # Call the main function #
                break   # Break the loop #
            if n > len(data):   # If the user enters a number greater than the number of restaurants, continue #
                sorted_data = sorted(data.items(), key=lambda x: x[1], reverse=True)   # Sort the data in descending order #
                max_number = len(sorted_data)   # Set the maximum number as the number of restaurants #
                print(f"The top {max_number} restaurants and their ratings are:")   # Print the top n restaurants #
                for key, value in sorted_data:   # For each key and value in the sorted data, print the key and value #
                    print(f"{key} ({value})")   # Print the top n restaurants and their ratings #
                exit()   # Break the loop #
            else:   # Else, print the top n restaurants and their ratings #
                sorted_data = sorted(data.items(), key=lambda x: x[1], reverse=True)   # Sort the data in descending order #
                print(f"The top {n} restaurants and their ratings are:")   # Print the top n restaurants #
                for i in range(n):   # For each key and value in the sorted data, print the key and value #
                    print(f"{i+1}. {sorted_data[i][0]} ({sorted_data[i][1]})")  # Print the top n restaurants and their ratings #
                exit()
        except ValueError:   # If the user enters an invalid input, print an error message #
            print("Invalid Value. Please enter an integer between 1 and 3.")   # Print an error message #
            return False   # Return False to the main function #
            
### Exit Function ###
def option_3():   # Creates the exit function #
    print("Goodbye!")   # Print a goodbye message #
    exit()   # Exit the program #

### Main Function ###
def main():
    try:   # Try to run the program #
        option = user_input1()   # Call the user_input1 function #
        if option == 1:   # If the user enters 1, run the option_1 function #
            restaurant_name = option_1()   # Call the option_1 function #
            data = read_score_data()   # Sets the data as the read_score_data function #
            if check_restaurant_name(restaurant_name, data) == False:   # If the restaurant name is not in the dictionary, call the main function to loop again #
                main()   # Call the main function #
        elif option == 2:   # If the user enters 2, run the top_n_restaurants function #
            top_n_restaurants()   # Call the top_n_restaurants function #
            data = read_score_data()   # Sets the data as the read_score_data function #
            if main() == False:  # If the user enters an invalid input, call the main function to loop again #
                main()   # Call the main function #
        elif option == 3:   # If the user enters 3, run the option_3 function #
            option_3()   # Call the option_3 function #
        else:   # If the user enters an invalid input, print an error message #
            print("Please enter an integer between 1 and 3.")   # Print an error message #
    except ValueError:   # If the user enters an invalid input, print an error message #
        print("ERROR")   # Print an error message #
        exit()   # Exit the program #


### Initialize the program ###
if __name__ == "__main__":
    if check_data() == True:   # Run Check Data, check if the data is valid #
        if validate_text() == True:   # Run Validate Text, check if the data is valid #
            welcome()   # Run Welcome function #
            main()   # Run Main function #
        else:   # If the data is not valid, print an error message #
            print("Error reading data. Each line of scores.txt should contain a restaurant name, followed by a comma, followed by a valid score, and no restaurant should appear more than once in the file.")
               # Print an error message #
            exit()   # Exit the program #
    if check_data() == False:   # If the data is not valid, print an error message #
        print(
            "Error reading data. Each line of scores.txt should contain a restaurant name, followed by a comma, followed by a valid score, and no restaurant should appear more than once in the file."
        )
        # Print an error message #
        exit()   # Exit the program #
