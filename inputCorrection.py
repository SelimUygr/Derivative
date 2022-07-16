def correctInput(function):
    function = function.replace(" ","")
    function = function.split("+")
    for i in range(len(function)):
        #add coefficients to those who seems have not(!)
        if(not function[i][0].isnumeric()):
            function[i] = f"1*{function[i]}"

        #add powers to those who seems have not(!)
        if("**" not in function[i]):
            if(function[i].isnumeric()):
               function[i] = f"{function[i]}*x**0" 
            else:
                function[i] = f"{function[i]}**1"

    
    
    return function



