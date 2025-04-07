inventory ={
    "apple": 500,
    "banana":300,
    "pear":1000,
    "mango":150,

}

# ya function fruits ke naam pe kitna stock hai, wo return karega 
def num_in_stock(fruit):
    return inventory.get(fruit,0)

def main():
    fruit = input("Enter a fruit: ").lower() # user se fruit ka naam lena 
    stock = num_in_stock(fruit)#stock check karna

    if stock > 0 :
        print("This fruit is in stock! Here is how many :")
        print(stock)

    else:
        print("This fruit is not in stock.") 

if __name__ == "__main__":
    main()          