# Brainf-uck
 Repository for my brainf tools and projects

## BRIAN.py
 Brian.py is the brainf interpreter I wrote for personal use. It has a command line where you can enter code line by line as well as load seperate script files. It also supports injecting files into and writing files from memory.
 
### Using the command line
 Simply running the script is enough to activate the command line. Alternatively, you can import the `CommandLine` class and create a new instance, but note that it relies on a global variable `interpreter` set to an instance of the interpreter class.

### Using just the interpreter
 If you only need an enterpreter you can import the class Interpreter with `from BRIAN import Interpreter`. Then you can make a new interpreter object and any time you need to parse a string of code you call `interpreterInstance.Run("CODEINSTRINGFORMAT")`.
 
## TextToBrainoof.py
 TTBf is a script that takes in an arbitrary string and generates a brainf script to print it. It is optimised for short code, but not optimally so. It breaks the string up into substrings whose characters are near in ASCII space to prevent excessively long adjustments.
 
## Scripts
 I also uploaded a few scripts I made while playing around with the language.
 
