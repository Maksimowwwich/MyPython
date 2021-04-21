from math import sqrt

def string(string, char):
    i = 0
    count = 0
    while i < len(string):
        if string[i] == char:
            count += 1
        i += 1
    return count

print(string('sasha', 's'))
print(sqrt(16))

def pidor():
    print('pidor;)')