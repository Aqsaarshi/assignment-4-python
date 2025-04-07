def main():
    #ASK USER TO ENTER A Number
    curr_value = int(input("Enter a number: "))
    # Repeat doubling the number until its 100 or greater
    while curr_value < 100:
        # double the value
        curr_value *= 2
        
        print(curr_value)

if __name__ == "__main__":
    main()        