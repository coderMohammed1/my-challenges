# pls referee to the truth table generator file as we need it in here
# this will solve a kmap of 4x2 (3 vars)

def kmaper(f):
    d2 = []
    tmp = []
    
    arr = []
    arr2 = []
    c = 0
    isonce = True
    
    tabel  = bparan(f)
   
    for i in f:
      
        if i != '+' and i != '.' and i != '~' and i != "(" and i != ")" and i not in arr2:
            arr2.append(i)
    
    arr2.sort()

    for i in tabel:
        if c != 2 and c != 3 and c != 6 and c != 7:
            
            if str(tabel[c]["res"]) != '1':
                isonce = False
                
            tmp.append(tabel[c]["res"])
        else:
            
            if str(tabel[c]["res"]) != '1':
                isonce = False
            
            if c == 2 or c == 6:
                tmp.append(tabel[c+1]["res"])
            else:
                tmp.append(tabel[c-1]["res"])
        
        if c == 3:
            d2.append(tmp)
            tmp = []
    
        c+=1
        
    d2.append(tmp)
    
    if isonce:
        return 1
    
    adds = []
    groubs = []
    tmp = []
    filterd = []
    added = 0
    
    #4s
 
    if str(d2[0][0]) == '1' and str(d2[1][0]) == '1' and str(d2[0][3]) == '1' and str(d2[1][3]) == '1':
        
        tmp.append("0")
        tmp.append("4")
        
        tmp.append("2")
        tmp.append("6")
        
        for i in tmp:
            if i in adds:
                added += 1
        
        if added < 4:
            adds = adds + tmp
            groubs.append(tmp)
            
        tmp = []
        added = 0
    
    if str(d2[0][0]) == '1' and str(d2[0][1]) == '1' and str(d2[1][0]) == '1' and str(d2[1][1]) == '1':
    
        tmp.append("0")
        tmp.append("1")
        
        tmp.append("4")
        tmp.append("5")
        
        for i in tmp:
            if i in adds:
                added += 1
        
        if added < 4:
            adds = adds + tmp
            groubs.append(tmp)
            
        tmp = []
        added = 0
    
    if str(d2[0][1]) == '1' and str(d2[1][1]) == '1' and str(d2[0][2]) == '1' and str(d2[1][2]) == '1':
    
        tmp.append("1")
        tmp.append("5")
        
        tmp.append("3")
        tmp.append("7")
        
        for i in tmp:
            if i in adds:
                added += 1
        
        if added < 4:
            adds = adds + tmp
            groubs.append(tmp)
            
        tmp = []
        added = 0
    
    if str(d2[0][2]) == '1' and str(d2[1][2]) == '1' and str(d2[0][3]) == '1' and str(d2[1][3]) == '1':
    
        tmp.append("3")
        tmp.append("7")
        
        tmp.append("2")
        tmp.append("6")
        
        for i in tmp:
            if i in adds:
                added += 1
        
        if added < 4:
            adds = adds + tmp
            groubs.append(tmp)
            
        tmp = []
        added = 0
    
    if str(d2[0][0]) == '1' and str(d2[0][1]) == '1' and str(d2[0][2]) == '1' and str(d2[0][3]) == '1':
    
        tmp.append("0")
        tmp.append("1")
        
        tmp.append("3")
        tmp.append("2")
        
        for i in tmp:
            if i in adds:
                added += 1
        
        if added < 4:
            adds = adds + tmp
            groubs.append(tmp)
            
        tmp = []
        added = 0
        
    
    if str(d2[1][0]) == '1' and str(d2[1][1]) == '1' and str(d2[1][2]) == '1' and str(d2[1][3]) == '1':
    
        tmp.append("4")
        tmp.append("5")
        
        tmp.append("7")
        tmp.append("6")
        
        for i in tmp:
            if i in adds:
                added += 1
        
        if added < 4:
            adds = adds + tmp
            groubs.append(tmp)
            
        tmp = []
        added = 0
    
    #2s
    if d2[0][0] == "1" and d2[0][3] == "1":
        tmp.append("0")
        tmp.append("2")
        
        if len(tmp) > 0: # to check if all elemnts were added before!
            for j in tmp:
                if j in adds:
                    added += 1
            
            if added < 2:
                groubs.append(tmp)
                adds = adds + tmp
                
            tmp = []
            added = 0

    if d2[1][0] == "1" and d2[1][3] == "1":
        tmp.append("4")
        tmp.append("6")
        
        if len(tmp) > 0: # to check if all elemnts were added before!
            for j in tmp:
                if j in adds:
                    added += 1
            
            if added < 2:
                groubs.append(tmp)
                adds = adds + tmp
            
            tmp = []
            added = 0
                
    c2 = 0
    for i in range(3):
        if d2[0][c2] == "1" and d2[0][c2+1] == "1":
            if c2 == 0:
                tmp.append("0")
                tmp.append("1")
            elif c2 == 1:
                tmp.append("1")
                tmp.append("3")
            else:
                tmp.append("3")
                tmp.append("2")
        
        if len(tmp) > 0: # to check if all elemnts were added before!
            for j in tmp:
                if j in adds:
                    added += 1
            
            if added < 2:
                groubs.append(tmp)
                adds = adds + tmp
                
        tmp = []
        added = 0
            
        c2 += 1
        
    c2 = 0
    for i in range(3):
        if d2[1][c2] == "1" and d2[1][c2+1] == "1":
            if c2 == 0:
                tmp.append("4")
                tmp.append("5")
            elif c2 == 1:
                tmp.append("5")
                tmp.append("7")
            else:
                tmp.append("7")
                tmp.append("6")
        
        if len(tmp) > 0: # to check if all elemnts were added before!
            for j in tmp:
                if j in adds:
                    added += 1
            
            if added < 2:
                groubs.append(tmp)
                adds = adds + tmp
                
            tmp = []
            added = 0
                
        c2 += 1
    
    c2 = 0
    for i in range(4):
        if d2[0][c2] == "1" and d2[1][c2] == "1":
            if c2 != 2 and c2 != 3:
                tmp.append(str(c2))
                tmp.append(str(c2+4))
            else:
                if c2 == 2:
                    tmp.append("3")
                    tmp.append("7")
                else:
                    tmp.append("2")
                    tmp.append("6")
            

        if len(tmp) > 0: # to check if all elemnts were added before!
            for j in tmp:
                if j in adds:
                    added += 1
            
            if added < 2:
                groubs.append(tmp)
                adds = adds + tmp
                
            tmp = []
            added = 0
        c2 += 1
    j = 0
    for i in d2:
        for k in range(len(i)):
            if j == 2:
                if i[k] == "1" and "3" not in adds:
                    tmp.append("3")
                    groubs.append(tmp)
                    
                    adds.append("3")
                    tmp = []
            elif j == 3:
                if i[k] == "1" and "2" not in adds:
                    tmp.append("2")
                    groubs.append(tmp)
                    
                    adds.append("2")
                    tmp = []
            elif j == 6:
                if i[k] == "1" and "7" not in adds:
                    tmp.append("7")
                    groubs.append(tmp)
                    
                    adds.append("7")
                    tmp = []
            elif j == 7:
                if i[k] == "1" and "6" not in adds:
                    tmp.append("6")
                    groubs.append(tmp)
                    
                    adds.append("6")
                    tmp = []
            else:
                if i[k] == "1" and str(j) not in adds:
                   
                    tmp.append(str(j))
                    groubs.append(tmp)
                    
                    adds.append(str(j))
                    tmp = []
            j += 1
    
    for i in groubs:
        c1 = 0 
        for j in i:
            c2 = 0
            for x in adds:
                if j == x:
                    c2 += 1
            
            if c2 > 1:
                c1 += 1
        
        if c1 < len(i):
            filterd.append(i)
    
    groubs = []
    
    for i in range(len(filterd)):
        for j in range(len(filterd[i])):
            tmp = dtob(int(filterd[i][j]))
            
            for k in range(3-len(str(tmp))):
                tmp = '0' + tmp
            
            filterd[i][j] = tmp
            
    res = ""
    for i in filterd:
        b1 = '-1'

        if len(i) == 2:
            if i[0][0] == i[1][0]:
                b1 = i[0][0]
            
                if b1 == "0":
                    res = res + '~' + arr2[0]
                else:
                    res = res + arr2[0]
                
            if i[0][1] == i[1][1]:
                b1 = i[0][1]
            
                if b1 == "0":
                    res = res + '~' + arr2[1]
                else:
                    res = res + arr2[1]
                
            if i[0][2] == i[1][2]:
                b1 = i[0][2]
            
                if b1 == "0":
                    res = res + '~' + arr2[2]
                else:
                    res = res + arr2[2]
                
            res = res + "+"
        elif len(i) == 4:
            if i[0][0] == i[1][0] and i[0][0] == i[2][0] and i[0][0] == i[3][0]:
                b1 = i[0][0]
            
                if b1 == "0":
                    res = res + '~' + arr2[0]
                else:
                    res = res + arr2[0]
                
            if i[0][1] == i[1][1] and i[0][1] == i[2][1] and i[0][1] == i[3][1]:
                b1 = i[0][1]
            
                if b1 == "0":
                    res = res + '~' + arr2[1]
                else:
                    res = res + arr2[1]
                
            if i[0][2] == i[1][2] and i[0][2] == i[2][2] and i[0][2] == i[3][2]:
                b1 = i[0][2]
            
                if b1 == "0":
                    res = res + '~' + arr2[2]
                else:
                    res = res + arr2[2]
                    
            res = res + "+"
        else:
            for j in i:
                n = 0
                if j == "0":
                    res = res + "~" + arr2[n]
                else:
                    res = res + arr2[n]                
                n += 1
                
            res = res + "+"
                
            
    return res[0:-1]

print(kmaper("~A.C+~A.B+A.~B.C+B.C"))
