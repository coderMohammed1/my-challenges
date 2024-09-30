import math
def EEAinv(B,A):
    # A>B
    
    if(A<=B):
        print("A should be grater than B: B mod A")
        return 0
    
    if math.gcd(A,B) != 1:
        print("the Multiplicative invers does not exisist!")
        return 0
    
    table = [[math.floor(A/B),A,B,A%B,0,1,0-1*math.floor(A/B)]] # the first row
    
    p = 0 # a tracker for the previous row 
    c = 1 # a tracker for the current row
    
    while True:
        row = [0, 0, 0, 0, 0, 0, 0]  # new independent row each time
        table.append(row)
        
        table[c][0] = math.floor(table[p][2] / table[p][3]) # quotient (Q)
        table[c][1] = table[p][2]
        
        table[c][2] = table[p][3]
        table[c][3] = table[c][1] % table[c][2] # R
        
        table[c][4] = table[p][5]
        table[c][5] = table[p][6]
        table[c][6] = table[c][4] - table[c][5] * table[c][0]
        
       
        if table[c][3] == 0: # if the remainder is 0 then stop!
            if (table[c][5] < 0):
                table[c][5] = table[c][5] + A
            return table[c][5] # the result
        
        c += 1  
        p += 1  
        
print(f"the result is:{EEAinv(8,21)}")
