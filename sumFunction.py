# This function sums all the same powered polynomials so that way we can calculate better.
def sumUpPolynomials(function):
    #Sorting the function by power
    print(function)
    function.sort(key= lambda function:(function[-1],function[function.index("x")]),reverse=True)
    i = 0
    function.append("end")
    # Adding up all the same powered symbols
    # Problem with adding all the same powers we gotta find a new way to do it i believe you you can do it be calm and relax
    # everything will be alright bro u got this!
    while True:  
        if(function[i][-1] == function[i+1][-1] and not function[i+1] == "end"):
            functionIConstant = function[i][function[i].index("x")-2::-1]
            functionIIConstant = function[i+1][function[i+1].index("x")-2::-1]
            print(f"functon1Cons={functionIConstant[::-1]}\nfunction2Cons={functionIIConstant[::-1]}")
            function[i] = f"{str(int(functionIConstant[::-1]) + int(functionIIConstant[::-1]))}{function[i][function[i].index('x') -1:]}"
            del function[i+1]
            i -= 1
    
        elif(function[i+1] == "end"):
            del function[i+1]
            break
        i+=1
    # for i in range(len(function)):
    #     print(f"function={function}\ni={i}\nfunction[i]={function[i]}\nfunction[-1]{function[-1]}")
    #     if(function[i+1] != function[-1]):
    #         for j in range(len(function[i])):
    #             if(function[i][j] == function[i+1][j] and function[i][j].isalpha() and function[i+1][j].isalpha() and function[i][-1] == function[i+1][-1]):
    #                 function[i] = f"{int(function[i][0])+int(function[i+1][0])}{function[i][1:]}"
    #                 function.remove(function[i+1])
    #                 i = 0
    #     else:
    #         break
    print(f"function={function}")
    return function  