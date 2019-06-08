class BalancedParenthesis:

    # Passing parameters directly to the Init method.
    def __init__(self, parentheses):
        # 2 Lists as the computer cant recognize open and close parenthesis.
        open_parentheses = ['(', '[', '{']
        close_parentheses = [')', ']', '}']

        # Empty stack to store the open parenthesis and pop them too.
        my_stack = []
        # A cute and lovely flag variable.
        count = 0

        # Loop through the input string.
        for i in parentheses:
            # If its a open parenthesis, store it in the stack.
            if i in open_parentheses:
                my_stack.append(i)
            # If its a close parenthesis, pop the open parenthesis from the stack.
            elif i in close_parentheses:
                in_stack = my_stack.pop()

                # Check the indexes of the open and close parenthesis.
                open_index = open_parentheses.index(in_stack)
                close_index = close_parentheses.index(i)

                # If theyre' same, set count as zero and continue the For loop.
                if open_index == close_index:
                    count = 0
                # Nor, the input string is un-balanced, set count as zero and break-exit the loop.
                else:
                    count = 1
                    break

        # Count must be zero and as well as the stack must be empty.
        # If we use 'or' here, anyone being True, will give us the final result as True.
        # AND-  0 0- 0
        #       1 0- 0
        # OR-   1 0- 1- And this is the problem.
        print((count == 0) and (len(my_stack)) == 0)

    # Implementing Joses' solution with a dash of my own!
    @staticmethod
    def jose_balanced_parenthesis(parenthesis):
        open_parentheses = set('([{')
        # A set- Makes sure we make only one lookup when checking for matching parenthesis.
        matches = set(
                        [
                            ('(', ')'),
                            ('[', ']'),
                            ('{', '}')
                        ]
                      )
        # We know why all these are used.
        my_stack = []
        count = 0

        # Iterating over the input parameter.
        for i in parenthesis:
            # If we get a open parenthesis, we append to the stack.
            if i in open_parentheses:
                my_stack.append(i)

            # If its not a open parenthesis,
            elif i not in open_parentheses:

                # When we get a close parenthesis without any open parenthesis,
                # there would be nothing to pop from stack and check it.
                # So break-exit the loop.
                if len(my_stack) == 0:
                    count = 1
                    break

                # Nor,
                else:
                    # Get the open parenthesis from the stack.
                    in_stack = my_stack.pop()
                    # Construct a tuple in the form of (open parenthesis, close parenthesis).
                    test_tuple = (in_stack, i)

                    # If the constructed tuple is in matches, continue.
                    if test_tuple in matches:
                        count = 0
                    # Nor break exit the loop.
                    else:
                        count = 1
                        break

        # The stack must be empty and as well as the count must be equal to zero.
        print((len(my_stack) == 0) and (count == 0))


'''
ObjectBalancedParentheses = BalancedParenthesis("[](){([[[]]])}")  # True.
ObjectBalancedParentheses = BalancedParenthesis("[]")  # True.
ObjectBalancedParentheses = BalancedParenthesis("[](){([[[]]])}")  # True.
ObjectBalancedParentheses = BalancedParenthesis("()(){]}")  # False.
ObjectBalancedParentheses = BalancedParenthesis("[](){([[[]]])}(")  # False.
ObjectBalancedParentheses = BalancedParenthesis("[{{{(())}}}]((()))")  # True.
ObjectBalancedParentheses = BalancedParenthesis("[[[]])]")  # False.
print("***** From Geeks for Geeks: *****")
ObjectBalancedParentheses = BalancedParenthesis("{[]{()}}")  # True.
ObjectBalancedParentheses = BalancedParenthesis("[{}{}(]")  # False.
'''
# Joses' implementation.
ObjectBalancedParentheses = BalancedParenthesis

print(ObjectBalancedParentheses.jose_balanced_parenthesis("[](){([[[]]])}"))  # True.
print(ObjectBalancedParentheses.jose_balanced_parenthesis("[]"))  # True.
print(ObjectBalancedParentheses.jose_balanced_parenthesis("[](){([[[]]])}"))  # True.
print(ObjectBalancedParentheses.jose_balanced_parenthesis("()(){]}"))  # False.
print(ObjectBalancedParentheses.jose_balanced_parenthesis("[](){([[[]]])}("))  # False.
print(ObjectBalancedParentheses.jose_balanced_parenthesis("[{{{(())}}}]((()))"))  # True.
print(ObjectBalancedParentheses.jose_balanced_parenthesis("[[[]])]"))  # False.
print(ObjectBalancedParentheses.jose_balanced_parenthesis("{[]{()}}"))  # True.
print(ObjectBalancedParentheses.jose_balanced_parenthesis("[{}{}(]"))  # False.

print(ObjectBalancedParentheses.jose_balanced_parenthesis("]]{{]]}}"))  # False.
