from math import log10

def find_leftmost_1(arr):
    for num in arr:
        if int(num) == 0:
            print(-1) # if the number is 0, then there is no 1 in it, also, log10(0) is undefined
        else:
            print(len(num) - int(log10(int(num)) + 1) + 1) # log10(100) = 2, so we add 1 to get the leftmost 1 as {log10(num) + 1 = number of digits of num} and it's 1 based index so we add 1 at the end



t = int(input())
binary_str = []
for i in range(t):
    binary_str.append(input())

find_leftmost_1(binary_str)
