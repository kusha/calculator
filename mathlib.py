import math
import re
 
math_namespace = vars(math).copy()
math_namespace['__builtins__'] = None
 
# regex_function = r'(\d+!|\d+(\.\d+)?\^\d+|\|[+,-]?\d+(\.\d+)?\|)'
# regex_value = r'((([1-9]\d*|0)(\.\d+)?)|'+regex_function+')'
# regex_operation = r'(\+|\-|\*|\/)'
# regex_all = '^[+,-]?('+regex_value+regex_operation+')*'+regex_value+"$"
digit = r"([\-\+]?\d+(\.\d+)?)"
tag = r"(\#[1-9][0-9]?)"
left = r"[\(\|]"
right = r"[\)\|\!]"
operands = r"[\+\-\*\/\^]"
 
value = left+r"*("+digit+r"|"+tag+r")"+right+r"*"
unit = r"("+value+r"|("+operands+value+r"))*"
 
regex_all = r"^"+value+r"("+operands+value+r")*$"
print(regex_all)
valid_pattern = re.compile(regex_all)
 
def evaluate(expression, story):
    expression = expression
    namespace = math_namespace
    try:
        if valid_pattern.match(expression):
            print("VALID",end=" ")
            expression = re.sub(r'('+unit+')!', "factorial("+r'\1'+")", expression)
            expression = re.sub(r'(\d+(\.\d+)?)\^(\d+)', "pow("+r'\1'+","+r'\3'+")", expression)
            expression = re.sub(r'\|[+,-]?(\d+(\.\d+)?)\|', r'\1', expression)
            # substitution for story
            if re.findall(r'#([1-9][10-99])', expression):
                # print(namespace["story"])
                namespace["story"] = [None] + [float(i[1]) if i[1] is not None else i[1] for i in story]
                print(namespace["story"])
                expression=re.sub(r'#([\d]{1,2})',r'evaluate(story[\1])',expression)
            print("INPUT:", expression, end=" => ")
            result = eval(expression, namespace)
            result = int(result) if int(result) == float(result) else round(float(result),8)
            print("RESULT:", result)
            return str(result)
        return None
    except Exception as e:
        return None