

def isValid(str_char):
    stack=[]
    bracket={')':'(', ']':'[', '}':'{'}  #{'key':'value'}

    for char in str_char:
        if char in bracket.values():
            stack.append(char)
        elif char in bracket:
            if not stack or stack.pop() != bracket[char]:
                return False
    return len(stack)==0





char=str(input("enter bracket: "))
print(isValid(char))