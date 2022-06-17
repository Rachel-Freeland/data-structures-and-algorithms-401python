from data_structures.stack import Stack


def multi_bracket_validation(string):
    """
    Argument:
        string
    Return:
        bool
    Returns a boolean value to make sure that each type of bracket
    `()`, `[]`, and `{}` has an opening and closing bracket.
    """

    stack = Stack()
    close_brace = [")", "}", "]"]

    for char in string:
        if stack.is_empty() and char in close_brace:
            return False
        else:
            if char == "(":
                stack.push(")")
            if char == "{":
                stack.push("}")
            if char == "[":
                stack.push("]")

            if char in close_brace:
                if stack.top.value == char:
                    stack.pop()
                else:
                    return False

    return True
