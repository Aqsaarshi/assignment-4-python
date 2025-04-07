def main():
    MAX_VALUE = 10000 # constant value

    #Starting values of fibonacci sequence 
    a, b = 0, 1 
    #print Fibonacci numbers until we reach MAX_VALUE 
    while a < MAX_VALUE:
        print(a, end=" ")
        a, b = b, a + b


if __name__ == "__main__":
    main()