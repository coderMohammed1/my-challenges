# this will generate all combination of (chars array) from 1 to n 
import string

def pureb(n):
    chars = list(string.ascii_lowercase)
    l = len(chars)
    
    x = 1
    while x <= n:
        c = []
        
        for i in range(x):
            c.append([0, 0])
        
        for i in range(l ** x):
            for k in range(x):
                if c[k][0] == l:
                    c[k][0] = 0
                
                if c[k][1] == l ** (x - (k + 1)):
                    c[k][1] = 0
            
                print(chars[c[k][0]], end="")
                
                c[k][1] += 1
                
                if c[k][1] == l ** (x - (k + 1)):
                    c[k][0] += 1
            
            print()
        
        x += 1

pureb(2)
