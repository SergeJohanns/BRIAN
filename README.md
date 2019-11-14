# BRIAN
 Repository for the BRIAN brainfuck interpreter and auxillary toolset.

## BRIAN.py
 Brian.py is the brainfuck interpreter I wrote for personal use. It has a command line where you can enter code line by line as well as load seperate script files. It also supports injecting files into and writing files from memory.
 
### Using the command line
 Simply running the script is enough to activate the command line. Alternatively, you can import the `CommandLine` class and create a new instance, but note that it relies on a global variable `interpreter` set to an instance of the interpreter class.

### Using just the interpreter
 If you only need an interpreter you can import the class Interpreter with `from BRIAN import Interpreter`. Then you can make a new interpreter object and any time you need to parse a string of code you call `interpreterInstance.Run("CODEINSTRINGFORMAT")`.
 
## TextToBrainoof.py
 TTBf is a script that takes in an arbitrary string and generates a brainfuck script to print it. It is optimised to generate short scripts. It does this by finding an optimal integer (by trying out all of the options in the given context), then adding some multiple of that integer to each cell, in such a way that the result is as close to the needed character as possible. Finally, it performs a string of adjustments.
 
### Using TextToBrainoof.py
 To use TTBf, simply run the script. It will repeatedly prompt the user for a string, then print the corresponding brainfuck code. To use the module as a dependency, import the module and run `TextToBrainoof.TextToBF("ASCIITEXTTOPROCESS")`. The function will return the brainf code in string form.
 
## Scripts
 I also uploaded a few scripts I made while playing around with the language.
 
