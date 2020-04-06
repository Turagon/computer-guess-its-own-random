import random as r

def ran_num() :
    bottom = input("Please set the bottom of the range : ")
    bottom = input_num(bottom)
    ceiling = input("Please set the ceiling of the range : ")
    ceiling = input_num(ceiling)
    if bottom > ceiling :
        bottom, ceiling = ceiling, bottom
    ran_answer = r.randint(bottom, ceiling)
    return ran_answer, bottom, ceiling

def input_num(number_input) :
    default_value = False
    while default_value == False :
        try :
            number_input == int(number_input)
            if int(number_input) > 0 :
                default_value = True
            else :
                print("Invalid value! Can't be negative.")
                number_input = input("Please input again : ")
                continue
        except :
            print("Invalid value! Should be integer.")
            number_input = input("Please input again : ")
            continue
    number_input = int(number_input)
    return number_input

def ai_guess(ran_answer, bottom, ceiling) :
    times = 0
    default_value = False
    while default_value == False :
        ai = (bottom + ceiling)//2
        if ai > ran_answer :
            ceiling = ai
            times += 1
        elif ai < ran_answer :
            bottom = ai
            times += 1
        else :
            default_value = True
    return ai, times 

def main() :
    ran_answer, bottom, ceiling = ran_num()
    ai, times = ai_guess(ran_answer, bottom, ceiling)
    print("The AI guessed the number is "+str(ai))
    print("The AI spent "+str(times)+" times")
    print("The answer is "+str(ran_answer))

main()
