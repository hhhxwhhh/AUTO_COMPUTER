# This file is intentionally left blank.
import random

def generate_question(op_types):
    op=random.choice(op_types)
    a=random.randint(1,99)
    b=random.randint(1,99)
    if op=='+':
        return f"{a} + {b} =  "
    elif op=='-':   
        return f"{a} - {b} =  "
    elif op=='*':
        return f"{a} * {b} =  "
    elif op=='÷':
        b=random.randint(1,9)
        a=random.randint(1,9)*b
        return f"{a} ÷ {b} =  "
