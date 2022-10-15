import random as r
import mergeSortInversion as msi

def genRandomArr(n):
    tmp = []
    for a in range(n):
        tmp.append(r.randint(0,10000000))
    return tmp

def main():
    # get data from file 
    inp = open("IntegerArray.txt","r")
    inputArr = []
    for each in inp:
        n = each[:len(each)-1]
        inputArr.append(int(n))
    
    
    
    (arr,i) = msi.countInversions(genRandomArr(10000000),10000000)
    print(i)
    
    


main()


