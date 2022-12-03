from re import search

with open(r"C:\Users\agapo\Documents\University\Year 1\Module 2\Advent of Code\Day 3\input.txt", "r") as f:
    file = f.read()

#Part 1

sum = 0
same = ""
index = 0
low = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
upper = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

for i in file.splitlines():
    first_half  = i[:len(i)//2]
    second_half = i[len(i)//2:]

    same = same.join(set(first_half).intersection(second_half))

    if same in low:
        sum += low.index(same) + 1
    elif same in upper:
        sum += upper.index(same) + 27

print(sum)