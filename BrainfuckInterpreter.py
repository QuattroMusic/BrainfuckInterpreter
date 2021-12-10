def evaluate(string, inputs: tuple or list = (), is_ascii: bool = False) -> str:
    bf = [0]
    cellPos = 0
    evalPos = 0
    usedInput = -1
    output = ""

    while evalPos < len(string):

        char = string[evalPos]

        if char not in ["+", "-", ".", ",", "[", "]", "<", ">"]:
            evalPos += 1
            continue

        if char == "+":
            bf[cellPos] += 1

        elif char == "-":
            bf[cellPos] -= 1

        elif char == ".":
            if is_ascii:
                output += chr(bf[cellPos])
            else:
                output += f"{bf[cellPos]}\n"

        elif char == ",":
            usedInput += 1
            try:
                num = inputs[usedInput]
            except IndexError:
                return "Not enough inputs"

            bf[cellPos] = num

            pass

        elif char == "<":
            cellPos -= 1
            if cellPos < 0:
                bf.insert(0, 0)
                cellPos += 1

        elif char == ">":
            cellPos += 1

            if cellPos > len(bf) - 1:
                bf.append(0)

        elif char == "[":
            if bf[cellPos] == 0:
                current_depth = 1
                while current_depth != 0:
                    evalPos += 1
                    if string[evalPos] == "]":
                        current_depth -= 1
                    if string[evalPos] == "[":
                        current_depth += 1

        elif char == "]":
            current_depth = 1
            while current_depth != 0:
                evalPos -= 1
                if string[evalPos] == "]":
                    current_depth += 1
                if string[evalPos] == "[":
                    current_depth -= 1

            continue

        evalPos += 1

    return output
