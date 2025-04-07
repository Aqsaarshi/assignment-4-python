'''This program counts the number of times each number appears in a list. It uses a dictionary to keep track of the information.

An example run of the program looks like this (user input is in blue):

Enter a number: 3 Enter a number: 4 Enter a number: 3 Enter a number: 6 Enter a number: 4 Enter a number: 3 Enter a number: 12 Enter a number: 3 appears 3 times. 4 appears 2 times. 6 appears 1 times. 12 appears 1 times.'''
def main():
    #dictionary to store the ount of numbers 
    num_counts = {}

    while True:
        user_input = input("\033[94mEnter a number (or press Enter to stop): \033[0m") # Blue Text 

        #Stop input if user presses Enter without typing anything 
        if user_input == "":
            break 

        #Convert input to an integar 
        number = int(user_input)

        # Increase Count in dictionary 
        if number in num_counts:
            num_counts[number]+1 
        else:
            num_counts[number]=1

    # Print the count of each number   
    print("\nNumber occurances:")
    for num, count in num_counts.items():
        print(f"{num} appears {count} times.")

    #Required line to run the main() function 
if __name__ == '__main__':
    main()        