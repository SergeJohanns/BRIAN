#This script generates Brainoof to print arbitrary strings to the terminal.
#It is designed to optimise the code for shortness, but the code isn't as optimal as a human could make it and it comes with some overhead.
#TODO: Swap block method for multipass method

import math

def TextToBF(string): #The input function
    return IntListToBF(list(map(ord, string)))

def IntListToBF(intListIn): #The main processing function
    n = FindBaseInteger(intListIn)
    coeffList = [[(c+1) + abs(m - ((c+1) * n)) for c in range(math.ceil(m / n))] for m in intListIn]
    coeffList = [coeffs.index(min(coeffs)) + 1 for coeffs in coeffList]
    diffList  = [intListIn[i] - n * coeffList[i] for i in range(len(intListIn))]
    return BFGenerator(diffList, n, coeffList)

def FindBaseInteger(intListIn):
    A = [[x for x in range(0, max(intListIn) - i, i + 1)] for i in range(max(intListIn))] #Get a two-dimensional list [[1,2..k],[2,4..k]..[k]]
    B = []
    i = 0 #Counter for n
    for n in intListIn:
        B.append([]) #Add a two-dimenstional list of the form of A
        j = 0 #Counter for col
        for col in A:
            B[i].append([]) #Add a column to that list
            k = 1 #Counter for elem 
            for elem in col:
                B[i][j].append(k+abs(n-elem))
                k += 1
            j += 1
        i += 1
    B = [[min(col) for col in matrix] for matrix in B] #Select the most efficient coefficient for each letter for each basis integer
    B = [sum([B[j][i] for j in range(len(B))]) for i in range(len(B[0]))] #Sum the costs of every letter assuming the most efficient coefficient for each basis integer
    B = [B[i] + sum(GetDivisors(i + 1)) + 5 * len(GetDivisors(i + 1)) for i in range(len(B))] #Correct the weights for the length of the integer counter construct
    return B.index(min(B)) + 1 #Return the most efficient basis integer

def BFGenerator(diffList, base, coefficients): #Generates the actual code
    print(diffList, base, coefficients)
    #Prepare the basis integer
    if len(diffList) == 0:
        return ""
    divisors = GetDivisors(base)
    output = ""
    for i in coefficients:
        output += "+" * i + ">"
    output = output[:-1] + "[<]" #Cut off the final move command and then move back

    output = ">" + output
    
    for i in divisors:
        output = "+" * i + "[>" + output + "<-]" #Add another layer to the counters
    #Add the adjustments
    output += ">" * len(divisors) #Move to the cell after the last counter (the marking empty cell) and one more
    for i in diffList:
        if i >= 0:
            output += ">" + "+" * i
        else:
            output += ">" + "-" * abs(i)
    output += "[<]>[.>]"
    return output

def GetDivisors(n): #Gets the complete list of prime factors, including duplicates
    divs = SubDivisors(n)
    low = [x for x in divs if x <= 3] #Used to reduce all n < 4 to products to save loop overhead
    high = [x for x in divs if x > 3]
    return Reduce(low) + high

def SubDivisors(n): #Recursive helper function for the GetDivisors function
    if n < 2:
        return []
    for i in range(2, n + 1):
        if n % i == 0:
            return [i] + SubDivisors(n // i)

def Reduce(intList): #Reduces a list of 2s and 3s to minimal (as low as possible) products
    #Assumes the list is sorted, which it is
    out = []
    for i in range(0, len(intList) - 1, 2):
        out.append(intList[i] * intList[i+1])
    if len(intList) % 2 != 0:
        out.append(intList[len(intList) - 1])
    return out

if __name__ == "__main__":
    while True:
        string = input("Text: ")
        if string: #If string is not empty
            print(TextToBF(string))
        else:
            break