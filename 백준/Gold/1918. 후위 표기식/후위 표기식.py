import sys
input = sys.stdin.readline

equations = input()
stack = []
res = ''

for e in equations:
    if e.isalpha():
        res += e

    else:
        if e == '(':
            stack.append(e)

        elif e == ')':
            while stack[-1] != '(':
                res += stack.pop()
            stack.pop()

        elif e == '/' or e == '*':
            while stack and (stack[-1] == '/' or stack[-1] == '*'): # 조건 주의
                res += stack.pop()
            stack.append(e)

        elif e == '+' or e == '-':
            while stack and stack[-1] != '(':
                res += stack.pop()
            stack.append(e)

while stack:
    res+=stack.pop()

print(res)