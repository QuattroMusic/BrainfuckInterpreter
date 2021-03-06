# Brainfuck Interpreter

A general brainfuck interpreter featuring a secondary "debug" mode.

### Features

When executing the code, it can be specified if you want the _"classic"_ output, 
or the _"special"_ output.

- Classic: by specifying `is_ascii = True` you can get a standard brainfuck interpreter output
  
- Special: by default (or with `is_ascii = False`), instead of converting from the
number to the character, the program will return the exact number on that cell
  
### Some examples

```python
import BrainfuckInterpreter as bf
print(bf.evaluate("++++."))
# output
# 4
```
```python
import BrainfuckInterpreter as bf
#example with inputs
code = ",."
inputs = [5]
print(bf.evaluate(code,inputs))
# output
# 5
```
```python
import BrainfuckInterpreter as bf
code = "++++++++[>++++[>++>+++>+++>+<<<<-]>+>+>->>+[<]<-]>>.>---.+++++++..+++.>>.<-.<.+++.------.--------.>>+.>++."
print(bf.evaluate(code,is_ascii=True))
# output
# Hello World!
```
```python
import BrainfuckInterpreter as bf
code = """
program that sum the cell 1 and 2
,> input 1 on the first cell
,< input 2 on the second cell
sum
[->>+<<]>
[->+<]>
.
"""
inputs = [5,9]
print(bf.evaluate(code,inputs))
# output
# 14
```
