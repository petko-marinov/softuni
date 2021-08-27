# Task 6. Password validator
import re


def password_validator(my_pass):
    pattern = r'\w'
    pattern_regex = re.search(pattern, my_pass)
    numbers = sum(c.isdigit() for c in my_pass)
    output = []

    if 10 >= len(my_pass) >= 6 and pattern_regex and numbers >= 2:
        output.append("Password is valid")
        return output

    else:
        if len(my_pass) > 10 or len(my_pass) < 6:
            output.append("Password must be between 6 and 10 characters")
        if pattern_regex:
            pass
        else:
            output.append("Password must consist only of letters and digits")
        if numbers < 2:
            output.append("Password must have at least 2 digits")
        return output


messages = input()
print("\n".join(password_validator(messages)))