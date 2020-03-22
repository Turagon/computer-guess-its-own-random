import random as r
rang = int(input("Please set the ceiling of the range :"))
num = r.randint(1,rang)
print("The random number is ", num)
g_num = r.randint(1,rang)
n = 1
if g_num == num :
    print("Congratulations! Hole in one!!!")


while True :   
    if g_num > num :
        g_num1 = r.randint(1, g_num)
        if g_num1 < num :
            g_num = r.randint(g_num1,g_num)
        elif g_num1 > num :
            g_num = r.randint(1, g_num1)
                 
    if g_num < num :
        g_num1 = r.randint(g_num,rang)
        if g_num1 > num :
            g_num = r.randint(g_num, g_num1)
        elif g_num1 < num :
            g_num = r.randint(g_num1, rang)
    n = n + 1
            
    if g_num == num :
        print("Congratulations ! The computer guess number is", g_num)
        print("The computer tried ", n, " times")
        break
   
    
