def is_balanced(value):
    x = []
    length = len(value)
    if length == 1 or length % 2 == 1:
        return False
    
    for i in value:
        if is_open(i):
            x.append(i)
        else:
#             print(x)
            if is_match(x[-1], i):
                del x[-1]
            else: 
                return False
    return not x

def is_open(value):
    if value in ('{', '[', '('):
        return True
    return False

def is_match(first, second):
    if first == '{' and second == '}':
        return True
    elif first == '[' and second == ']':
        return True
    elif first == '(' and second == ')':
        return True
    return False

print("Expected: True")
print("Actuals : {}".format(is_balanced("{()[{}]}")))
print()

print("Expected: True")
print("Actuals : {}".format(is_balanced("{[]{()}}")))
print()

print("Expected: True")
print("Actuals : {}".format(is_balanced("{[({})]}")))
print()

print("Expected: False")
print("Actuals : {}".format(is_balanced("{[({})]")))
print()

print("Expected: False")
print("Actuals : {}".format(is_balanced("[({})]}")))
print()

print("Expected: False")
print("Actuals : {}".format(is_balanced("[")))
print()

print("Expected: False")
print("Actuals : {}".format(is_balanced("}")))
print()

print("Expected: False")
print("Actuals : {}".format(is_balanced("[{}{}(]")))
print()
