#stack way is not allowed (reinvent the wheel!)
def replace_substring(original_string, new_substring, start, end):
    return original_string[:start] + new_substring + original_string[end:]

def calc(n):
    
    ind = 0
    isexpo = False
    num2 = 0
    exp0 = []
    islift = False  # Flag to track whether multiplication or division is pending
    rleft = 1  # Running total for multiplication or division
    exp = []  # List to store the parsed expression
    addition = []  # List to store addition and subtraction operations
    num = ""  # String to accumulate the current number
    ismin = False

    if n[0] == "-":
        ismin = True
    # Phase 1: Parse the input expression
    for i in n:
        if (i == "+" or i == "-" or i == "x" or i == "÷" or i == "^") and not ismin:
            if n[ind+1] == "-":
                ismin = True
                exp0.append(num)
                exp0.append(i)
                num = ""
                continue

        if (i == "+" or i == "-" or i == "x" or i == "÷" or i == "^") and (not ismin):
            if i == "^":
                isexpo = True
            exp0.append(num)
            exp0.append(i)
            num = ""
        else:
            num += i
            ismin = False
        ind+=1
    exp0.append(num)
    
    #exponants evaluation
    if(len(exp0) == 3 and isexpo == True):
        return float(exp0[0])**float(exp0[-1])
    else:
        index3 = 0
        for i in exp0:
            if i == "+" or i == "-" or i == "x" or i == "÷":
                exp.append(num2)
                exp.append(i)
            elif i == "^":
                num2 = float(exp0[index3-1])**float(exp0[index3+1])
            else:
                if exp0[index3-1] != "^":
                    num2 = i
            index3+=1
        
        exp.append(num2)

    # Phase 2: Evaluate multiplication and division operations
    index = 0
    for j in exp:
        if j == "+" or j == "-":
            if not islift:
                addition.append(exp[index - 1])
                addition.append(j)
            else:
                addition.append(rleft)
                addition.append(j)
            rleft = 1
            islift = False

        if j == "x":
            if not islift:
                rleft = float(exp[index - 1]) * float(exp[index + 1])
            else:
                rleft = rleft * float(exp[index + 1])
            islift = True

        if j == "÷":
            if not islift:
                rleft = float(exp[index - 1]) / float(exp[index + 1])
            else:
                rleft = rleft / float(exp[index + 1])
            islift = True

        index += 1

    # Check if no addition/subtraction is needed and continue if needed
    if len(addition) == 0:
        return rleft
    else:
        if islift:
            addition.append(rleft)
        else:
            addition.append(exp[-1])

    # Phase 3: Evaluate addition and subtraction operations and return final result
    result = 0
    index2 = 0
    for f in addition:
        if index2 == 1:
            if f == "+":
                result = float(addition[index2 - 1]) + float(addition[index2 + 1])
            elif f == "-":
                result = float(addition[index2 - 1]) - float(addition[index2 + 1])
        else:
            if f == "+":
                result = result + float(addition[index2 + 1])
            elif f == "-":
                result = result - float(addition[index2 + 1])
        index2 += 1

    return result

def infparan(n2):
    c = 0
    starters = 0
    enders = 0
    ind = 0
    arr=[]
    ispar=False
    num=""
    ismin = False

    if n2[0] == "-":
        ismin = True
   
    for i in n2:
        if (i == "+" or i == "-" or i == "x" or i == "÷" or i == "^") and not ismin and ispar == False:
            if n2[ind+1] == "-":
                ismin = True
                arr.append(num)
                arr.append(i)
                num = ""
                continue

        if  (i=="+" or i=="-" or i=="x" or i=="÷" or i=="^") and ispar == False and not ismin:
            arr.append(num)
            arr.append(i)
            num = ""
        elif i == "(":
            starters+=1
            num = num + i
            ispar = True
        elif i == ")" and starters == (enders + 1):
            num = num + i
            ispar = False
            starters = 0
            enders = 0
            arr.append(num)
            num = ""
        else:
            num = num + i
            ismin = False
            if i == ")":
                enders+=1
        ind+=1
    arr.append(num)

    while '' in arr:
        arr.remove('')
        

    z = 0
    
    for _ in arr:
        if arr[z][0] == "(":
            while True:
                gdep = 0
                mdep = 0
                
                msp = 0
                mep = 0
                
                csp = 0
                x = 0
                
                for j in arr[z]:
                    if j == "(":
                        gdep += 1
                        csp = x
                    
                    if j == ")":
                        if gdep > mdep:
                            msp = csp
                            
                            mdep = gdep
                            mep = x
                        
                        gdep -= 1
                            
                    x+=1
                
                pr = calc(arr[z][msp+1:mep])
               
                arr[z] = replace_substring(str(arr[z]),str(pr),msp,mep+1)
                # print(arr[z])
                
                if mdep == 1:
                    break 
        z += 1
    
    res = ""
    for k in arr:
        res = res + k
        
    return calc(res)

print(infparan("2x2+(5+3)+(6÷2x(2+3x(5+3)+1))+(2-1)"))
