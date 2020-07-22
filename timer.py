# Let's make a countdown timer in python
# first, we need to import time
import time
# this will allow us to use time functions, such as the sleep() function

# next, let's ask the user how many seconds we want to count down from
seconds = int(input("How many seconds to wait?"))

# next let's use a ranged loop to count downwards
for i in range(seconds) :
    print(str(seconds - i) + " seconds remain")
    # we also need to have Python sleep for 1 second between each iteration
    time.sleep(1)

# let's try it!