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
operands = r"[\+\-\*\/\^\%]"

value = left+r"*("+digit+r"|"+tag+r")"+right+r"*"
unit = r"("+value+r"|("+operands+value+r"))*"

dig=r"\d+(\.\d+)?";

regex_all = r"^"+value+r"("+operands+value+r")*$"
print(regex_all)
valid_pattern = re.compile(regex_all)

def evaluate(expression, story):
    expression = expression
    namespace = math_namespace
    try:
        #print(regex_all)
        #print("Vyraz: "+expression)
        if valid_pattern.match(expression):
            print("VALID",end=" ")
            expression = "("+expression+")"
            while(True):
              expression=re.sub(r'('+dig+'!)', "("+r'\1'+")", expression)
              expression=re.sub(r'('+dig+'\^('+digit+'))', "("+r'\1'+")", expression)
              #print("expression:"+expression)
              oldexpr=expression
              subexpr=re.sub(r'(.*)(\([^\(\)]+\))(.*)', r'\2', expression)
              subexpr = re.sub(r'('+dig+')\^('+digit+')', "pow("+r'\1'+","+r'\3'+")", subexpr)
#              subexpr = re.sub(r'('+dig+')!', "factorial("+r'\1'+")", subexpr)
              subexpr = re.sub(r'\|('+digit+')\|', "(fabs("+r'\1'+"))", subexpr)
              subresult = eval(subexpr, namespace)
              subresult = int(subresult) if int(subresult) == float(subresult) else round(float(subresult),8)
              expression=re.sub(r'(.*)(\([^\(\)]+\))(.*)', r'\1'+"\""+str(subresult)+"\""+r'\3', expression)
              expression=re.sub("\""+str(subresult)+"\"",str(subresult), expression)
              if (oldexpr==expression):
                break

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
