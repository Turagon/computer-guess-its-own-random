import random as r
num = r.randint(1,100)
print("The random number is ", num)
g_num = r.randint(1,100)
n = 1
if g_num == num :
    print("Congratulations")


while True :   
    if g_num > num :
        g_num1 = r.randint(1, g_num)
        if g_num1 < num :
            g_num = r.randint(g_num1,g_num)
        elif g_num1 > num :
            g_num = r.randint(1, g_num1)
                 
    if g_num < num :
        g_num1 = r.randint(g_num,100)
        if g_num1 > num :
            g_num = r.randint(g_num, g_num1)
        elif g_num1 < num :
            g_num = r.randint(g_num1, 100)
            
    if g_num == num :
        print("Congratulations ! The computer guess number is", g_num)
        break
   
    
