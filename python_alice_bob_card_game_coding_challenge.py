
from itertools import combinations_with_replacement, permutations
import sys
for line in sys.stdin:
    found = False
    line = line.strip()
    operandsList = list(combinations_with_replacement(list(['+', '-', '*']), r=4))
    givenInputs = list(permutations(line.split(" ")))

    for operands in operandsList:
        for ip in givenInputs:
            evalString = '{ip0} {op0} {ip1} {op1} {ip2} {op2} {ip3} {op3} {ip4}'.format(
                                                                                        ip0 = ip[0],
                                                                                        ip1 = ip[1],
                                                                                        ip2 = ip[2],
                                                                                        ip3 = ip[3],
                                                                                        ip4 = ip[4],
                                                                                        op0 = operands[0],
                                                                                        op1 = operands[1],
                                                                                        op2 = operands[2],
                                                                                        op3 = operands[3])

            if abs(eval(evalString)) == 42:
                # print(evalString, eval(evalString))
                found = True
                break

    if not found:
        print('NO')
    else:
        print('YES')