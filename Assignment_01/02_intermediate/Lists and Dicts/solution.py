def main():
    # create a list called fruits_list that contains the following fruits
    fruits_lists = ['apple', 'banana', 'orange', 'grape', 'pineapple']
    print(f"Length of the fruit list: {len(fruits_lists)}")

    # Add 'mango' at the end of the list 
    fruits_lists.append('mango')

    print(f"Updated fruits list: {fruits_lists}")


# ---------- INDEX GAME ----------
def access_element(my_list, index):
    """Function to access an element in a list"""
    if index < 0 or index >= len(my_list):    
        return "Index out of range!"
    return my_list[index]

def modify_element(my_list, index, new_value):
    """Function to modify an element at a specific index"""
    if index < 0 or index >= len(my_list):
        return "Index out of range!"
    
    my_list[index] = new_value
    return f"Element at index {index} has been updated to {new_value}"

def slice_list(my_list, start, end):
    """Function to slice a list from start to end"""
    if start < 0 or end > len(my_list) or start > end:
        return "Invalid start or end index!"
    return my_list[start:end]

def game():
    # initialize a list with 5 elements (numbers and strings)
    my_list = [10, 20, 30, 'apple', 'banana']
    print("\nWelcome to the Index Game!!")
    print("The list is currently:", my_list)

    while True:
        # Prompt the user for an operation
        print("\nChoose an operation:")    
        print("1. Access element")    
        print("2. Modify element")    
        print("3. Slice list")    
        print("4. Exit")    

        choice = input("Enter the number of the operation you want to perform: ")

        if choice == '1':
            index = int(input("Enter an index to access: "))
            print("Result:", access_element(my_list, index))

        elif choice == '2':
            index = int(input("Enter an index to modify: "))
            new_value = input("Enter the new value: ")
            print(modify_element(my_list, index, new_value))

        elif choice == '3':
            start = int(input("Enter the start index: "))
            end = int(input("Enter the end index: "))
            print("Sliced list:", slice_list(my_list, start, end)) 

        elif choice == '4':
            print("Thanks for playing!!")
            break

        else:
            print("Invalid choice! Please try again.") 


if __name__ == "__main__":
    main()
    game()
