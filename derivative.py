from inputCorrection import correctInput
from sumFunction import sumUpPolynomials
from outputCorrection import correctOutput,outputForReadability

#Calculating the derivative in this function
def deriv(function):
    function = correctInput(function)
    function = sumUpPolynomials(function)

    i=0
    while True:
        if(i < len(function)):
            #This is the real derivative function 
            print(function)
            function[i] = f"{int(function[i][-1]) * int(function[i][0:function[i].index('x')-1])}{function[i][function[i].index('*'):-1]}{int(function[i][-1])-1}"
        else:
            break
        i+=1
    
    function = correctOutput(function)
    return function

