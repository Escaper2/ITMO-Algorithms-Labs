file = open('garland.in')
output = open('garland.out','w')
input = file.readline().split()
numberOfLamps = input[0]
numberOfLamps = int(numberOfLamps)
heightOfFirstlamp = input[1]
heightOfFirstlamp = float(heightOfFirstlamp)
def bin(heightOfFirstlamp,numberOfLamps):
    right = heightOfFirstlamp
    left = 0
    nextLamp = 0
    while (right - left) > 0.000001:
        mid = (right + left) / 2
        garland = girland(numberOfLamps, heightOfFirstlamp, mid)
        if garland is None:
            left = mid
            continue
        else:
            right = mid

        nextLamp = garland[numberOfLamps - 1]

    return nextLamp



def girland(numberOfLamps, heightOfFirstlamp, mid):
    garland = [heightOfFirstlamp, mid]
    for numberOfLamps in range(2, numberOfLamps):
        lampHeight = formula(garland[numberOfLamps - 2], garland[numberOfLamps - 1])
        if lampHeight < 0:
            return None
        garland.append(lampHeight)

    return garland

def formula(firstHeight, secondHeight):
    return 2 * secondHeight - firstHeight + 2

answer = (bin(heightOfFirstlamp,numberOfLamps))
output.write(str(round(answer,2)))


