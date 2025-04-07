import random 
DONE_LIKEIHOOD = 0.3 
def done():
    """Returns true with a certain likelihood , simulating the chaotic behaviour."""
    return random.random() < DONE_LIKEIHOOD

def chaotic_counting():
    """Counts from 1 to 10 , byt may stop early if done () returns True."""
    for i in range(1,11):
        if done():
            return
        print(i,end=" ")


def main():
    print("I am going to count until I feel like stopping , whichever first.") 
    chaotic_counting()
    print("\nI'm done.") 

if __name__ == '__main__':
    main()    
