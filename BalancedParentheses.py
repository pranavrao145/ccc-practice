open_list = ["[", "{", "("]
close_list = ["]", "}", ")"]


def check(x):
    stack = []
    for i in x:
        if i in open_list:
            stack.append(i)
        elif i in close_list:
            closeindex = close_list.index(i)
            if (len(stack) > 0) and (open_list[closeindex] == stack[len(stack) - 1]):
                stack.pop()
            else:
                return "unbalanced"
    if len(stack) == 0:
        return "balanced"
    elif len(stack) > 0:
        return "unbalanced"


a = check(input("Enter a string of parentheses: "))
print(f"That string is {a}.")
