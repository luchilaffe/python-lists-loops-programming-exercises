theBools = [0,1,0,0,1,1,1,0,0,1,0,1,1,0,0,0,0,0,0,0,0,1,0,0,0,0,1]

#Your code go here:
def bul(x):
    if x == 0:
        return "woko"
    elif x == 1:
        return "wiki"
    else:
        return "There's a problem here"

print(list(map(lambda value: str(bul(value)), theBools)))

