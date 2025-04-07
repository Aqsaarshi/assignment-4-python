def count_even(lst):
    #list ko populate karte hain user ke input se
    while True:
        user_input = input("Enter an integer or press enter to stop: ") 
     

        if user_input == "":
            break
# user input ko integer main convert karte ha
        try:
            number = int(user_input)
            lst.append(number) # list main number add krte ha 
        except ValueError:
            print("Please enter a valid integer.")

    even_count = sum(1 for num in lst if num % 2 == 0)  # Fixed the equality operator here

    print(f"Number of even numbers: {even_count}")

def main():
    lst = []
    count_even(lst)

if __name__ == "__main__":
    main()
