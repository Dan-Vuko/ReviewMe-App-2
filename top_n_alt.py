def welcome():
    print("Welcome to ReviewMe!\n1. Find the Rating of the Restaurant\n2. List top n restaurants\n3. Exit\n")  


def user_input1():
    min_number, max_number = 1, 3 # min and max number of options
    while True:   # loop until user enters a valid number
        try: option = int(input("What would you like to do? (Enter 1, 2 or 3):\n")); break  # if the input is valid, break out of the loop
        except ValueError: print("Please enter an integer between 1 and 3.") # if the input is invalid, print an error message and continue the loop
    if option < min_number: print("Invalid value. Please enter a non-negative integer.")
    if option > max_number: print("Please enter an integer between 1 and 3.")   
    if option >= min_number and option <= max_number: return option   
    else: return user_input1()
     


def read_score_data():
    filename = "tester.txt"     
    with open(filename) as file:
        return dict([(a, float(x)) for a, x in [line.strip().split(",") for line in file]])

        

def check_data():   
    filename = "tester.txt"    
    with open(filename) as file:
        return all([len(line.strip().split(",")) == 2 for line in file])


def validate_text():
    return all([isinstance(x, float) for x in dict([(a, float(x)) for a, x in [line.strip().split(",") for line in open("scores.txt")]]).values()])


def option_1():
    return input("What is the name of the restaurant?\n")


def check_restaurant_name(restaurant_name, data):
    return print(f"{restaurant_name} has a rating of {data[restaurant_name]}") if restaurant_name in data else False


def top_n_restaurants():   
    data = read_score_data()   
    while True:    
        try:   
            n = int(input("How many restaurants would you like to list?\n"))
            # write the following as a lambda function
            if n < 0:
                print("Invalid value. Please enter a non-negative integer.")
                main()   
                break   
            if n > len(data):
                print(f"The top {len(sorted(data.items(), key=lambda x: x[1], reverse=True))} restaurants and their ratings are:\n" 
                + "\n".join([f"{key} ({value})" for key, value in sorted(data.items(), key=lambda x: x[1], reverse=True)]))
                exit()
            else:
                print(f"The top {n} restaurants and their ratings are:\n" 
                + "\n".join([f"{key} ({value})" for key, value in sorted(data.items(), key=lambda x: x[1], reverse=True)[:n]]))
                exit()
        except ValueError: print("Invalid Value. Please enter an integer between 1 and 3."); return False  


def main():
        try:   
            option = user_input1()   
            if option == 1:   
                restaurant_name = option_1()
                data = read_score_data()   
                if check_restaurant_name(restaurant_name, data) == False: print(f"We don’t have rating for {restaurant_name}"), main()   
            elif option == 2:
                top_n_restaurants()
                data = read_score_data()
                if main() == False: main()
            elif option == 3:   
                print("Goodbye!"), exit()   
            else:   
                print("Please enter an integer between 1 and 3.")   
        except ValueError: print("ERROR"), exit()



def print_error_exit():
    print("Error reading data. Each line of scores.txt should contain a restaurant name, followed by a comma, followed by a valid score, and no restaurant should appear more than once in the file.")
    exit()  


if __name__ == "__main__":
    if check_data() == True and validate_text() == True:
        welcome()
        main()
    else:
        print_error_exit()
