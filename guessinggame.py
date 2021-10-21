import math
upperBound = math.inf
lowerBound = -math.inf
i = 1
while True:
    i = int(input())
    if(i == 0):
        break
    response = input()
    if response == "too high":
        if(upperBound > i):
            upperBound = i

    elif response == "too low":
        if(lowerBound < i):
            lowerBound = i

    elif response == "right on":
        if (lowerBound < i < upperBound):
            print("Stan may be honest")
        else:
            print("Stan is dishonest")
        lowerBound = -math.inf
        upperBound = math.inf

    elif(lowerBound > upperBound):
        print("Stan is dishonest")
        lowerBound = -math.inf
        upperBound = math.inf
    

    