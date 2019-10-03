#This script generates Brainoof to print arbitrary strings to the terminal.
#It is designed to optimise the code for shortness, but the code isn't as optimal as a human could make it and it comes with some overhead.
#TODO: Swap block method for multipass method

def TextToBF(string): #The input function
    return IntListToBF(list(map(ord, string)))

def IntListToBF(intListIn): #The main processing function
    intList = ToBlocks(intListIn) #Break the input list up into blocks
    differences = [[list(map(lambda n: n - x, block)) for x in range(min(block), max(block) + 1)] for block in intList] #Get a list of the differences to all possible base integers (what the counter will count to) for all blocks
    distances = [[sum(map(abs, diff)) for diff in block] for block in differences] #Sum the differences into the total distance, which is a measure for the amount of +s and -s that will have to be added.
    for i in range(len(distances)): #Weigh the distances for loop overhead
        base = min(intList[i])
        for j in range(len(distances[i])):
            distances[i][j] += sum(GetDivisors(base + j)) + 5 * len(GetDivisors(base + j)) #The sum of all prime factors, which is a measure for +s and -s, plus 5 times the amount of factors, which is the amount of characters needed for loops (one loop comes with 5 characters '[><-]' of overhead)
    ns = [block.index(min(block)) for block in distances] #Find the optimal base integers for each block
    output = "" #Prepare the output
    for i in range(len(distances)): #For every block
        output += BFGenerator(differences[i][ns[i]], ns[i] + min(intList[i])) #Add the fully functional code for that block to the output
    return output

def ToBlocks(intList): #Breaks the integer list into blocks where groups are too far apart in value
    blocks = []
    base = 0
    for i in range(1, len(intList)): #For every element
        divisors = GetDivisors(intList[i]) #Get its divisors
        if sum(divisors) + 5 * len(divisors) < abs(intList[i] - (sum(intList[base:i]) // (i - base))): #If the overhead for making a new block is less than the cost of keeping it in the current block
            blocks.append(intList[base:i]) #Store the old block
            base = i #Set the new block
    blocks.append(intList[base:])
    return blocks

def BFGenerator(diffList, base): #Generates the actual code
    if len(diffList) == 0:
        return ""
    divisors = GetDivisors(base)
    output = "+" + ">+" * (len(diffList)-1) + "<" * (len(diffList) - 1)
    for i in divisors:
        output = "+" * i + "[>" + output + "<-]" #Add another layer to the counters
    output += ">" * (len(divisors) - 1)
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