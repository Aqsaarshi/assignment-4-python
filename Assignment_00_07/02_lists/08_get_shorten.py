MAX_LENGTH = 3 

def shorten(lst):
    while len(lst) > MAX_LENGTH: # jab tak list ka size Max_length se bada hai 
        removed_item = lst.pop() # last element remove kro 
        print("Removed:" , removed_item) # Remove kiya hua item print kro 


def main():
    lst=[]

    #user se list input lena 
    n = int(input("Enter number of element in the list:"))        
    for _ in range (n):
        value = input("Enter a value : ")
        lst.append(value)


    print("Original list:", lst)  # Pehli list print karo
    shorten(lst)  # shorten function ko call karo
    print("Shortened list:", lst)  # Final list print karo)

if __name__ == '__main__':
    main()    