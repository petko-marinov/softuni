# Task 6 - Balanced Parentheses
parentheses = [x for x in input()]
stack = []
balanced = True
pairs = {
    '{': '}',
    '[': ']',
    '(': ')',
}

for ch in parentheses:
    if ch in '({[':
        stack.append(ch)
    else:
        if len(stack) == 0:
            balanced = False
            break

        last_opening_bracket = stack.pop()
        if pairs[last_opening_bracket] != ch:
            balanced = False
            break

if balanced:
    print('YES')
else:
    print('NO')
