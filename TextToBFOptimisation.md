# Optimising the text to brainf conversion for compact code

## The foundation

The simplest and least compact way to convert text to brainf code is to simply take the ASCII-value *n* of the first character, place that many +-signs, then place '.>' to print and move over one cell and finally repeat it for the next character. This works but causes long and uninteresting code as an output.

## The basis integer

The next step is to find some *n* such that it has the lowest combined ASCII-value-difference with all of the characters in the text, then first write that to every cell that is to be used, then finally adjust all of the cells to get them to the correct value and print them. This produces code that is slightly more compact and interesting to read, but it still results in a long string of +s and -s that is far longer than it needs to be and also far less interesting in terms of code.

## Looping with prime factors

Finally, we can save space on the first value *n* by writing it to a cell using loops and it's prime factors. Such that 21 would be output not by incrementing 21 times but by incrementing 7 times, 3 times. This makes the first block more compact, but doesn't help us save on the later blocks.

## Splitting into blocks

Finally, we can cut down on long ajustment sequences by deetecting when two sections are, on average, far removed in ASCII space, then splitting them up into blocks that have their own basis integer. This would handle situations like uppercase-lowercase conversions without needing ridiculously long strings of +s and -s, and since it means there are now basis integer constructions (and likely print constructions) throughout the code it makes the program look more visually interesting, too. This is the extent of optimisation of the first version of the module.

## Multiple passes

For further optimisation, the earlier idea of a basis integer can be expanded upon by choosing a lower integer and adding it to some cells twice. This would allow one basis integer to cover two regions far apart in ASCII-space without needing long adjustment sequences.
