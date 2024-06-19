## u can make this better using stacks but it is prohibited in this challenge (do it alone bro)
# this is a simple truth table generator where you 
#can pass the Boolean function and it will generate 
#you a table 
#Note: this is not the best code design but it is 
# ok for this challenge!
#try yourself before taking a look 


# from decimal to binary (you can use the one in python for better experience)

def dtob(n):
    point = False
    right = ""
    left = int(float(n))
    n_str = str(n)
    n_len = len(n_str)

    for char in n_str:
        if char == ".":
            point = True
            continue
        if point:
            right += char

    if not point:
        left_binary = []
        result = ""
        stop = False

        while not stop:
            left_binary.append(left % 2)
            left = int(left / 2)

            if left == 0:
                stop = True

        i = 1
        arr_len = len(left_binary)

        for _ in left_binary:
            result += str(left_binary[arr_len - i])
            i += 1

        return result
    else:
        left_binary = []
        result = ""
        stop = False

        while not stop:
            left_binary.append(left % 2)
            left = int(left / 2)

            if left == 0:
                stop = True

        i = 1
        arr_len = len(left_binary)

        for _ in left_binary:
            result += str(left_binary[arr_len - i])
            i += 1

        right = float("0." + right) * 2
        intg = [int(right)]
        stop = False
        counter = 0

        while not stop:
            fract = ""
            point2 = False

            for char in str(right):
                if char == ".":
                    point2 = True
                    continue
                if point2:
                    fract = fract + char

            if fract == "0" or counter == 6:
                stop = True
                break

            fract = float("0." + fract)
            right = float(fract) * 2
            intg.append(int(right))
            counter += 1

        result2 = ""
        for x in intg:
            result2 += str(x)

        return result + "." + result2

#truth table generator
def trg(f,d2 = "no",d1 = "no",appe = "no"):   
    vari = ""
    arr = []
    
    arr2 = []
    collector = ""
    isparan = False
    noparan = False
    
    if d2 == "no":
        noparan = True
    else:
        noparan = False
        
        
    for i in f:
        
        if i == "(":
            isparan = True
            collector += i
                
        elif i == ")":
            isparan = False
            collector += i
            arr.append(collector)
            collector = ""
            continue
        
        elif isparan:
            collector += i
            
            
        if i != "+" and i != "." and not isparan:
            vari += i
        elif not isparan:
            
            if vari != "":
                arr.append(vari)
                
            vari = ""
            arr.append(i)
        
        if i != '+' and i != '.' and i != "(" and i != ")" and i != '~' and i not in arr2:
            arr2.append(i)
    if vari != "":
        arr.append(vari)
    
    if appe != "no":
        arr2 = appe
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
    
    
    if not noparan:
        w1 = 0
        for mi in d1:
            tmp = mi
            
            w = 0
            for v in d2[w1]:
                Map[w][tmp] = d2[w1][w]
                w += 1
            w1 += 1
        
    
    h = 0
    for i in Map:
        sub = []
        x = 0

        for j in arr:
            if j[0] == '~':
                if i[j[1]] == "1":
                    sub.append("0")
                else:
                    sub.append("1")
            elif j != "+" and j != ".":
                sub.append(i[j])
            else:
                sub.append(j)
            x += 1
        
        add = []
        ismult = False
        multres = ""
        d = 0
        
        for j in sub:
            if not ismult and j == ".":
                if sub[d - 1] == "0" or sub[d + 1] == "0":
                    multres = "0"
                else:
                    multres = "1"
                ismult = True
            elif ismult and j == ".":
                if multres == "0" or sub[d + 1] == "0":
                    multres = "0"
                else:
                    multres = "1"

            elif not ismult and j == "+":
                add.append(sub[d - 1])
                add.append(j)

                if d == len(sub) - 2:
                    add.append(sub[d + 1])

            elif ismult and j == "+":
                add.append(multres)
                multres = ""
                ismult = False
                add.append(j)

                if d == len(sub) - 2:
                    add.append(sub[d + 1])
            d += 1
        
        if len(add) == 0:
            Map[h]["res"] = multres
        else:
            if add[-1] == "+":
                add.append(multres)
                
            first = True
            c = 0
            addres = ""
            for j in add:
                if j == "+" and first:
                    first = False
                    if add[c - 1] == "1" or add[c + 1] == "1":
                        addres = "1"
                    else:
                        addres = "0"
                elif j == "+" and not first:
                    if addres == "1" or add[c + 1] == "1":
                        addres = "1"
                    else:
                        addres = "0"
                c += 1

            Map[h]["res"] = addres
        h += 1
    
    return Map

# print(trg("x.y+x.z"))

def bparan(F):
    arr = []
    arr2 = []
    arr4 = []
    arr5 = []
    collector = ""
    isparan = False
    
    for i in F:
            
        if i == "(":
            isparan = True
            collector += i
            
        elif i == ")":
            isparan = False
            collector += i
            arr.append(collector)
            collector = ""
        
        elif isparan:
            collector += i
        
        if i != '+' and i != '.' and i != '~' and i != "(" and i != ")" and i not in arr2:
            arr2.append(i)
          
   
    varsn = len(arr2)
    
    if varsn == 0:
        return trg(F)
    else:
        d2 = []
        ind = 0
        
        for i in arr:
            tmp = []
            d = trg(i[1:-1],appe = arr2)
            
            for j in range(len(d)):
                tmp.append(d[j]["res"])
                
            arr3 = []
            
            for x in i:
                 if x != '+' and x != '.' and x != '~' and x != "(" and x != ")" and x not in arr3:
                     arr3.append(x)
            
            # parsn = len(arr3)
            # dublications = varsn - parsn
          
            # for s in range(dublications):        
            #     tmp = tmp + tmp
            
            d2.append(tmp)
           
        
        return trg(F,d2,arr)

            
                
print(bparan("(x+y).c"))
