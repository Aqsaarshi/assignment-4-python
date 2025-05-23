import time

def countdown(t):
    while t:
        mins, secs = divmod(t, 60)
        timer = '{:02d} : {:02d}'.format(mins, secs)  # Corrected the format string
        print(timer, end="\r")
        time.sleep(1)
        t -= 1 

    print('Timer completed')

t = int(input('Enter the time in seconds: '))  # Convert input to integer
countdown(t)
