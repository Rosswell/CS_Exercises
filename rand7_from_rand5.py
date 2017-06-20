import random
def rand5():
    return random.randrange(1,6)

def rand7():
    append_list = list(range(1,8)) * 3 + [0] * 4 # creating a list for filling the 5x5 matrix with 1-7 3 times and zeros for the rest of the values
    rand_dict = {x: append_list[5*(x):5*(x)+5] for x in range(5)} # creating the 5x5 matrix as a hash table with dict comprehension
    result = 0
    while result == 0: # loop selects a random value from the 5x5 matrix, which contains an equal distribution of 1-7
        i = rand5() # equivalent of rand5()
        j = rand5() # equivalent of rand5()
        result = rand_dict[i-1][j-1]
    return result

for _ in range(50):
    print(rand7())