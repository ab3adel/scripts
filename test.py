def gcd (num1,num2):
    lst1=[]
    lst2=[]
    gcd_num=0
    for i in range(2,num1):
        if (num1 % i == 0):
            lst1.append(i)
    for i in range(2,num2):
        if (num2 % i == 0):
            lst2.append(i)
    if num1 > num2:
        for i in lst2:
            if (i in lst1):
                gcd_num=i    
    else :
        for i in lst1:
            if (i in lst2):
                 gcd_num=i 
    return  [gcd_num,lst1,lst2]
print(gcd(480,120))                 



    
                
            


