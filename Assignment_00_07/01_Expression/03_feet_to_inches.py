"Converts feet to inches. Feet is an American unit of measurement. There are 12 inches per foot. Foot is the singular, and feet is the plural."
INCHES_IN_FOOT : int = 12 # Conversion factor . THere are 12 inches for 1 foot.

def main():
    feet: float = float(input("Enter number of feet :"))
    inches:float = feet * INCHES_IN_FOOT # perform the conversion 
    print("That is", inches,"inches!")

if __name__ == '__main__':
    main()
