import random

input = open('sort.in')
output = open('sort.out', 'w')
count = input.readline()
file = list(map(int, input.readline().split()))


def quick(file):
    if len(file) <= 1:
        return file
    else:
        elem = random.choice(file)
    left = [n for n in file if n < elem]
    right = [n for n in file if n > elem]
    curr = [elem] * file.count(elem)
    return quick(left) + curr + quick(right)


file = quick(file)
answer = ' '.join(map(str, file))
output.write(answer)
