def add_three_copies(my_list , data):
    """Adds three copies of data to the given list (mutable behavior)."""

    my_list.append(data)
    my_list.append(data)
    my_list.append(data)

def main():
    #USER INPUT 
    message = input("Enter a message to copy:")

    #Empty list before midification 
    my_list = []
    print("List before:" , my_list)

    #call the function (list changes with out returning)
    add_three_copies(my_list,message)

    #list after modification 
    print("List after:", my_list)  


if __name__ == '__main__':
    main()