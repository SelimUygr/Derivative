def correctOutput(function):
    i = 0
    while True:
        if(i<len(function)):
            #Getting rid of constants
            if((not function[i][-2] == "*") and int(function[i][-2:]) < 0):
                del function[i]
            #If power is 0 we remove all symbolics so constant is better to read
            elif(int(function[i][-1]) == 0):
                function[i] = function[i][0]
            #If power is 1 we remove the power (**1) so symbolic better to read
            elif(int(function[i][-1]) == 1):
                function[i] = function[i][:function[i].index('x')+1]
        else:
            break
        i +=1
    
    function = "+".join(function)
    return function

# This function only for prepare output for humans to read better.
def outputForReadability(function):
    correctOutput(function)
    readable_function = "+".join(function)
    readable_function = readable_function.replace("**","^")
    readable_function = readable_function.replace("*","")
    print(readable_function)

    return function
