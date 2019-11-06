"A homemade Brainoof interpreter in Python"

#Constants
cellLength = 8
maxval = 2**cellLength

#Classes
class Interpreter:
    def __init__(self):
        self.commands = {'>':self.IncMemCount, '<':self.DecMemCount
                        ,'+':self.IncCell,     '-':self.DecCell
                        ,'.':self.OutputChar,  ',':self.InputChar
                        ,'[':self.ZeroJump,    ']':self.NonZeroJump}
        self.jumpCount = 0
        self.jumpEnd = {']':-1,'[':1} #Characters that end a jump with the increment of [key]
        self.memory = [0]
        self.i = 0 #Pointer
    
    def Run(self, script):
        self.j = 0 #Program counter
        self.dir = 1 #Program counter increment
        self.jumping = False
        while self.j < len(script):
            char = script[self.j]
            if char in self.commands:
                if self.jumping:
                    if char in self.jumpEnd:
                        self.jumpCount += self.jumpEnd[char]
                        if self.jumpCount == 0:
                            self.jumping = False
                            self.dir = 1
                else:
                    self.commands[char](self.i, self.memory)
            self.j += self.dir #Move program counter

    def IncMemCount(self, i, mem):
        i += 1
        if i == len(mem): mem.append(0) #Add memory at a positive address
        self.i = i
    def DecMemCount(self, i, mem):
        i -= 1
        if i < 0:
            mem.insert(0, 0) #Add memory at a 'negative' adress (simulated by simply incrementing the counter)
            i += 1
        self.i = i

    def IncCell(self, i, mem):
        mem[i] += 1
        if mem[i] == maxval: mem[i] = 0 #Memory overflow
    def DecCell(self, i, mem):
        mem[i] -= 1
        if mem[i] < 0: mem[i] = maxval - 1 #Memory underflow

    def OutputChar(self, i, mem):
        print(chr(mem[i]), end = '', flush = True)
    def InputChar(self, i, mem):
        char = input('')
        if len(char) == cellLength:
            mem[i] = int(char, base = 2) #Allows input in Binary
        elif len(char) == cellLength // 4:
            mem[i] = int(char, base = 16) #Allows input in Hexadecimal
        elif len(char) == 1:
            mem[i] = ord(char) % maxval
        else:
            print("\nInvalid input")
            raise SystemExit

    def ZeroJump(self, i, mem):
        if mem[i] == 0:
            self.jumping = True
            self.dir = 1
            self.jumpCount = 1
    def NonZeroJump(self, i, mem):
        if mem[i] != 0:
            self.jumping = True
            self.dir = -1
            self.jumpCount = -1

class CommandLine:
    def __init__(self):
        self.commands = {'l':self.RunFile, 'i':self.Info, 'h':self.Help
                        ,'r':self.ResetInterpreter, 'q':self.QuitIt, '#':self.Comment
                        ,'f':self.InjectFile, 'w':self.WriteFile}
                        #Command format for commands is always :c argument where c is the command key
    def Listen(self):
        while True:
            command = input("\n> ")
            self.Process(command)
    def Process(self, command):
        if command == "":
            return
        if ';' in command:
            n = command.index(';')
            self.Process(command[:n])
            self.Process(command[n+1:])
        else:
            if command[0] == ':':
                self.commands[command[1]](command)
            else:
                interpreter.Run(command)
    def RunFile(self, command):
        try:
            fileName = command[command.index(' ') + 1:] #Get string after the command
            try:
                with open(fileName) as scriptfile:
                    script = scriptfile.read()
            except:
                print("Could not open file '{}'".format(fileName))
                return
        except:
            print("Could not extract filename, remember to read files with ':l FILENAME' where FILENAME is the name of the file.")
            return
        self.Process(script)
    def InjectFile(self, command):
        try:
            fileName = command[command.index(' ') + 1:] #Get string after the command
            try:
                with open(fileName, 'r') as dataFile:
                    data = dataFile.read()
            except:
                print("Could not open file '{}'".format(fileName))
                return
        except:
            print("Could not extract filename, remember to inject files with ':f FILENAME' where FILENAME is the name of the file.")
            return
        originalIndex = interpreter.i
        for char in data:
            interpreter.memory[interpreter.i] = ord(char) % maxval
            interpreter.IncMemCount(interpreter.i, interpreter.memory)
        interpreter.i = originalIndex
    def WriteFile(self, command):
        try:
            fileName = command.split(' ')[1]
            fileLength = command.split(' ')[2]
        except:
            print("Could not extract filename and/or file length, remember to write files with ':w FILENAME LENGTH' where FILENAME is the name of the file and LENGTH is the amount of memory cells to read.")
            return
        originalIndex = interpreter.i
        try:
            with open(fileName, 'w') as writeFile:
                for i in range(fileLength):
                    writeFile.write(chr(interpreter.memory[interpreter.i]))
                    interpreter.IncMemCount(interpreter.i, interpreter.memory)
        except:
            print("Could not open file {} or an error occured while writing.".format(fileName))
        interpreter.i = originalIndex
    def Comment(self, command):
        pass
    def Info(self, command):
        print("Current memory:\n{}\nCurrent memory pointer: {}".format(interpreter.memory, interpreter.i))
    def Help(self, command):
        print("Commands:\n:h   | Help\n:i   | Memory info\n:#   | Comment\n:l   | Load script\n:f   | Load file into memory\n:w   | Write file from memory\n:r   | Reset interpreter\n:q   | Exit interpreter")
    def ResetInterpreter(self, command):
        global interpreter
        interpreter = Interpreter()
        print("Interpreter reset complete")
    def QuitIt(self, command):
        print("Exiting interpreter...")
        raise SystemExit

#Main execution block
if __name__ == "__main__": #If the current process is a main process started by the user
    print("\nBRIAN | Brainoof Reader, Interpreter And Nothing else\nWritten in Python by Serge Johanns")
    print("\nEnter ':h' for command help", end = "")
    interpreter = Interpreter()
    commandLine = CommandLine()
    commandLine.Listen()
