def mergeSort(arr,n,order):
    choices = [0,1]
    if order not in choices: return []
    elif order == 0:
        A = [] 
        if len(arr) == 1: return [arr,1]
        m = (n//2)
        (B,n1) = mergeSort(arr[:m],m,order)
        (C,n2) = mergeSort(arr[m:],n-m,order)
        i=0
        j=0
        for ind in range(n):
            if i > n1-1:
                A.append(C[j])
                j+=1
            elif j > n2-1:
                A.append(B[i])
                i+=1
            elif B[i][0] == C[j][0]:
                if B[i][1] > C[j][1]:
                    A.append(B[i])
                    i+=1
                else:
                    A.append(C[j])
                    j+=1
            elif B[i][0] < C[j][0]:
                A.append(B[i])
                i+=1
            else: 
                A.append(C[j])
                j+=1
        return [A,n]
    else:
        A = [] 
        if len(arr) == 1: return [arr,1]
        m = (n//2)
        (B,n1) = mergeSort(arr[:m],m,order)
        (C,n2) = mergeSort(arr[m:],n-m,order)
        i=0
        j=0
        for ind in range(n):
            if i > n1-1:
                A.append(C[j])
                j+=1
            elif j > n2-1:
                A.append(B[i])
                i+=1
            elif B[i][0] == C[j][0]:
                if B[i][1] > C[j][1]:
                    A.append(B[i])
                    i+=1
                else:
                    A.append(C[j])
                    j+=1
            elif B[i][0] > C[j][0]:
                A.append(B[i])
                i+=1
            else: 
                A.append(C[j])
                j+=1
        return [A,n]
    
def diffSchedule():
    file = open("schedule.txt")
    schedule = []
    count = 0
    for each in file.readlines():
        if count == 0: count+=1
        else:
            each = list(map(int,each.split(" ")))
            tmp = [each[0]-each[1],each[0],each[1]]
            schedule.append(tmp)
    
    schedule = mergeSort(schedule,len(schedule),1)[0]
    return schedule

def optSchedule():
    file = open("schedule.txt")
    schedule = []
    count = 0
    for each in file.readlines():
        if count == 0: count+=1
        else:
            each = list(map(int,each.split(" ")))
            tmp = [each[0]/each[1],each[0],each[1]]
            schedule.append(tmp)
    
    schedule = mergeSort(schedule,len(schedule),1)[0]
    return schedule

def cost(schedule):
    sum = 0
    compTime = 0
    for task in schedule:
        compTime+=task[2]
        sum+=(compTime*task[1])
    return sum

