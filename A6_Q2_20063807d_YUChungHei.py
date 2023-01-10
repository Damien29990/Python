def cleanup(solution):
    s1 = solution.replace(" ","")
    s2 = s1.upper()
    alist = list(s2.split(">"))
    return alist
def islegal(state):
    if int(state.find("|CG")) >= 0:
        return False
    elif int(state.find("CG|")) >= 0:
        return False
    elif int(state.find("|GW")) >= 0:
        return False
    elif int(state.find("GW|")) >= 0:
        return False
    else:
        return True
def canmove(state1,state2):
    x = state1.find("|")
    y = state2.find("|")
    a = state1.find("M")
    b = state2.find("M")
    if (x < a and y < b) or (x > a and y > b):
        return False
    else:
        return True
    

def check(statelist):
    solution = True
    if statelist[0].find("|") != 0:
        print("Start state %s is incorrect" % statelist[0])
        solution = False
    x = len(statelist)
    y = 0
    z = 0
    while y != x:
        if islegal(statelist[y]) is False:
            print("The state %s is illegal" % statelist[y])
            solution = False
        y += 1
    while z != x-1:
        if canmove(statelist[z],statelist[z+1]) is False:
            print("The move %s -> %s is not allowed" % (statelist[z],statelist[z+1]))
            solution = False
        z += 1
    if statelist[-1].find("|") != (len(statelist[-1])-1):
        print("End state %s is incorrect" % statelist[-1])
        solution = False
    if solution is False:
        return False
    else:
        return True

def main(solutionList):
    x = 0
    while x != len(solutionList):
        print("Input solution: %s" % solutionList[x].replace(" ",""))
        if check(cleanup(solutionList[x])) is False:
            print("Input solution is incorrect")
        else:
            print("Input solution is correct")
        x += 1
            
