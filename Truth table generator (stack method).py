#truth table generator using stack method!
# ! is not gate
# . is and gate 
# + is or gate

# I used @ to make ! works like a binary operator and so the stack algorethem works with it!

from collections import deque #stack
from tabulate import tabulate # pip install tabulate to resolve any errors

def Bpostfix(ex):
   operators = [".","+","!"]
   stack = deque()
   ex = '('+ex+')'
   
   res = ""
   for i in ex:
       
    if i == "(":
        stack.append(i)
           
    if i not in operators and i != "(" and i != ")":
        res = res + i
    
    if i == "!":
        while stack[-1] == "!":
            res = res + stack.pop()
        stack.append(i)
        
    if i == ".":
        while stack[-1] == "." or stack[-1] == "!":
            res = res + stack.pop()
        stack.append(i)
        
    if i == "+":
        while stack[-1] == "." or stack[-1] == "+":
            res = res + stack.pop()
        
        stack.append(i)
        
    
    if i == ")":
        while stack[-1] != "(":
            res = res + stack.pop()
        
        stack.pop()

   return res


def evalit(po):
    operands = deque()
    for i in po:
        if i == "0" or i == "1" or i == "@":
            operands.append(str(i))
        else:
            op1 = operands.pop()
            op2 = operands.pop()
            
            if i == ".":
                if op1 == "0" or op2 == "0":
                    operands.append("0")
                else:
                    operands.append("1")
            elif i == "+":
                if op1 == "1" or op2 == "1":
                    operands.append("1")
                else:
                    operands.append("0")
            else:
               if op1 == "0":
                   operands.append("1")
               else:
                   operands.append("0")
                
    return operands.pop() 

def trg2(ex):
    op = ["+",".","!"]
    arr2 = [] # put letters and then sort()
    ex2 = ""
    
    for i in ex:
        if i not in op and i != "(" and i != ")" and i != "@" and i not in arr2:
            arr2.append(i)
        if i == "!":
            ex2 += "@" + i
        else:
            ex2 += i 
        
    
    arr2.sort()
    n = ""
    
    Map = []
    dic = dict()

    for i in range(2**len(arr2)):
        n = dtob(i)
        dic = dict()

        if len(n) < len(arr2):
            for j in range(len(arr2) - len(n)):
                n = '0' + n

        r = 0
        for m in arr2:
            dic[m] = n[r]
            r += 1
        
        dic["res"] = "0"
        Map.append(dic)
    
    post = Bpostfix(ex2)
    z = 0
    
    for i in Map:
        tmp = ""
        x= 0
        
        for j in post:
            
            if j not in op and j != "@":
                 tmp+=i[j]
            else:
                tmp+=j
        
            x+=1
        
        Map[z]["res"] = evalit(tmp)
        z += 1
    
    return Map
        
def print_table(Map, variables):
    headers = variables + ["Result"]
    rows = [[entry[var] for var in variables] + [entry["res"]] for entry in Map]
    print(tabulate(rows, headers, tablefmt="grid"))

result = trg2("(x.y+!(z+x))")
variables = ["x", "y", "z"]
print_table(result, variables)
