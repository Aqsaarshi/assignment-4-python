def subtract_seven(num):
    return num -7

def main():
    number = int(input("Enter a number:"))# user se numbr lena 
    result = subtract_seven(number) #helper function call 
    print("REsult after subtracting 7 :" , result)

if __name__ == "__main__":
    main()