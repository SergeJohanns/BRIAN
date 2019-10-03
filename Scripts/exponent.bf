,>,>+<[<[>>>+>+<<<<-]>>>>[<<<<+>>>>-]<[<[>>+>+<<<-]>>>[<<<+>>>-]<<-]<[-]>>[<<+>>-]<<<-]>.

;:# Broken down commented version
,>, Take inputs on cell 0 (base) and 1 (exponent)
>+< Set cell 2 to 1 then go back to cell 1 (prepares it to be the base for repeated multiplication)
[ If the exponent is not 0
    < Go to cell 0
    [>>>+>+<<<<-] Clone it to cells 3 and 4
    >>>> Go to cell 4
    [<<<<+>>>>-] Move it back to cell 0
    < Go to cell 3
    [ If clone of base is not 0
        < Go to cell 2 (the result)
        [>>+>+<<<-] Clone it to cells 4 (add) and 5 (copy)
        Cell 4 is where the temporary computation happens while cell 2 is always one multiplication behind
        >>> Go to cell 5
        [<<<+>>>-] Move it back to cell 2
        << Go back to cell 3
    -] Subtract one from cloned base and repeat loop
    < Go to cell 2
    [-] Set it to 0
    >> Go to cell 4
    [<<+>>-] Move it to cell 2
    <<< Go back to cell 1
-] Subtract 1 from exponent and repeat loop
>. Display result