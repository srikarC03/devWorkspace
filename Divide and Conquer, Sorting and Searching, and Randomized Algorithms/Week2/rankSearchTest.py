import rankSearch as rs
import random

def genRand(m):
    x = []
    for n in range(2**m):
        x.append(random.randint(0,100000))
    return x

def main(n):
    tmp = genRand(n)
    print(tmp)
    x = rs.getSecondGreatest(tmp)
    print("Second Greatest: " + str(x)+"\n")


while True:
    inp = input("\nPlease enter a number from 1 to 10, that will exponentiate 2 to represent the length of an array; enter q to quit: ")
    if inp == "q":
        break
    inp = int(inp)
    main(inp)



