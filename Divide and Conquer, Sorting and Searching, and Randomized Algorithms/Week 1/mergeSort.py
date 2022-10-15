def mergeSort(inputList,start,end):
    out = []

    if start == end: return [inputList[start]]

    mid = (start + end) // 2
    former = mergeSort(inputList,start,mid)
    latter = mergeSort(inputList,mid+1,end)

    i = 0
    j = 0
    for n in range(start,end+1):
        if i > len(former)-1 :
            out.append(latter[j])
            j+=1
        elif j > len(latter)-1 :
            out.append(former[i])
            i+=1
        elif former[i] < latter[j]:
            out.append(former[i])
            i+=1
        else:
            out.append(latter[j])
            j+=1
    return out

def main():
    inp = list(map(int,input("Enter some numbers: ").split()))
    print( mergeSort( inp, 0, len(inp)-1)  )

main()