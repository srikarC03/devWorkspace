import math
import random
import copy

def satClause(values,x1,x2):
    if x1>=0 and x2>=0: return values[x1] or values[x2]
    elif x1>=0 and x2<0: return values[x1] or not values[abs(x2)]
    elif x1<0 and x2>=0: return not values[abs(x1)] or values[x2]
    else: return not values[abs(x1)] or not values[abs(x2)]

def satisfiable(clauses,values):
    falseInd = []
    count = 0
    for clause in clauses:
        if not satClause(values,clause[0],clause[1]):
            falseInd.append(count)
        count+=1
    return falseInd

def clauseReduce(clauses):
    C = copy.deepcopy(clauses)

    # identify variables that only occur as one type 
    varType = {}
    for clause in C:
        for var in clause:
            if abs(var) in varType:
                if varType[abs(var)][0] and varType[abs(var)][1] != var:
                    varType[abs(var)][0] = False
            else:
                varType[abs(var)] = [True,var]

    # identify clauses that can be removed
    clauseInd = []
    count = 0
    for clause in C:
        if varType[abs(clause[0])][0] or varType[abs(clause[1])][0]: clauseInd.append(count)
        count+=1
    del varType

    # remove uneeded clauses
    bias = 0
    for ind in clauseInd:
        C.pop(ind-bias)
        bias+=1
    del clauseInd

    return C

def randAssign(values):
    for var in values:
        values[var] = bool(random.getrandbits(1))
    


def papadimitriou(clauses):
    # Remove uneeded clauses
    print("Starting...")
    prevClauses = clauses
    currClauses = clauseReduce(clauses)

    while prevClauses!=currClauses:
        prevClauses = currClauses
        currClauses = clauseReduce(currClauses)
    print("Unnecessary clauses removed...")
    # Count number of variables
    variables = {}
    for clause in currClauses:
        for var in clause:
            if abs(var) in variables: continue
            else: variables[abs(var)] = None
    
    print("Variables identified...")
        
    # Use multiple randomized local searches to find if satisfiable, return unsatisfiable if no solution found
    outIter = math.floor(math.log(len(variables),2))
    inIter = 2*len(variables)*len(variables)
    
    for i in range(outIter):
        randAssign(variables)
        for j in range(inIter):
            falseClauses = satisfiable(currClauses,variables)
            if len(falseClauses) == 0: 
                print("Finished")
                return True 
            else:
                randVar = abs(random.choice(currClauses[random.choice(falseClauses)]))
                variables[randVar] = not variables[randVar]

    print("Finished")
    return False

