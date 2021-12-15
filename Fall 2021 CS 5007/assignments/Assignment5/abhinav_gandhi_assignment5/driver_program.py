from Stack import Stack


def isBalanced(expression):
    is_balanced = True  # False if expression is not balanced
    balance_stack = Stack()  # Create an empty stack object

    curly = 0  # Curly bracket pairs
    box = 0  # Box bracket pairs
    brace = 0  # Brace pairs

    # Process the input string to remove spaces
    # Add each character to stack
    for character in expression:
        if character != ' ':
            balance_stack.push(character)

    while not balance_stack.isEmpty():
        # Elements are popped as Last In First Out
        # This inverts the expression and we expect to see closed bracket before open brackets
        element = balance_stack.pop()

        # If a bracket is closed before it is opened, expression is unbalanced
        # If an open bracket is not closed, expression is unbalanced
        # Since expression is inverted due to stack, we check if brackets are opened before they are closed
        # Note: [{]} I am assuming this is balanced but illegal

        if element == '{':
            curly += 1
        elif element == '[':
            box += 1
        elif element == '(':
            brace += 1

        if curly > 0 or box > 0 or brace > 0:
            is_balanced = False

        if element == '}':
            curly -= 1
        elif element == ']':
            box -= 1
        elif element == ')':
            brace -= 1

    if curly < 0 or box < 0 or brace < 0:
        is_balanced = False

    return is_balanced


def query(str_input):
    another_string = False  # True if user wants to enter another string
    user_resp_valid = False  # True when a valid response is entered by user

    # validate user response
    if str_input.upper() == 'Y':
        user_resp_valid = True
    elif str_input.upper() == 'N':
        user_resp_valid = True

    # If user response is invalid, prompt again until a valid response is entered
    while not user_resp_valid:
        print("\nInvalid Response. Please type Y or N.")
        str_input = input("\nAnother string? [Y or N]: ")

        if str_input.upper() == 'Y':
            user_resp_valid = True
        elif str_input.upper() == 'N':
            user_resp_valid = True

    if str_input.upper() == 'Y':
        another_string = True

    elif str_input.upper() == 'N':
        another_string = False

    return another_string


def evaluate(expression):
    result = 0.0
    isValid = True  # False if expression is invalid
    expression_stack = Stack()
    # Assume expression is valid until invalid
    expression_list = []

    # Removing blank spaces in expression
    for character in expression:
        if character != ' ':
            expression_list.append(character)
    expression = ''.join(expression_list)

    bracket_list = ['(', ')', '[', ']', '{', '}']
    operator_list = ['+', '-', '*', '/']

    # Validating the sequence of operators and operands
    for i in range(len(expression_list)):
        if (expression_list[i] == ']' or expression_list == '}' or expression_list[i] == ')') and (expression_list[i-1]
                                                                                                   in operator_list):
            isValid = False

    i = 0
    # Push expression to stack and check additional element validity constraints
    while i < len(expression) and isValid:
        if expression[i] in bracket_list:
            expression_stack.push(expression[i])
            i += 1

        elif expression[i] in operator_list:
            expression_stack.push(expression[i])
            i += 1

        elif expression[i].isalpha():
            # Checking for alphabets/variables in expression
            isValid = False

        else:  # It is a number
            num = ""
            # Number can be single or multi-digit and can have decimal point
            # Accumulate all the digits of the number and then push
            while i < len(expression) and (expression[i].isdigit() or expression[i] == '.'):
                num = num + expression[i]
                i += 1
            expression_stack.push(num)

    # Check validity constraints for operators
    i = 0
    validated_expression_stack = Stack()

    while not expression_stack.isEmpty():
        # Get last item in expression stack
        exp = expression_stack.pop()

        # Push it to the validated stack
        validated_expression_stack.push(exp)
        # print("validated: ", exp)

        if not expression_stack.isEmpty():
            # Get another item from expression stack
            next_exp = expression_stack.pop()

            # Push it to the validated stack
            validated_expression_stack.push(next_exp)
            # print("validated: ", next_exp)

        else:
            # If there are no more elements in expression stack use a white space for rest of the checks
            next_exp = ' '

        # We are now evaluating the expression from right to left
        if exp.isdigit() and (next_exp == ')' or next_exp == '}' or next_exp == ']'):
            isValid = False

        elif (exp == '(' or exp == '[' or exp == '{') and (next_exp == ')' or next_exp == '}' or
                                                           next_exp == ']' or next_exp.isdigit()):
            isValid = False

        elif (exp == '+' or exp == '-' or exp == '*' or exp == '/') and (next_exp == '+' or
                                                                         next_exp == '-' or next_exp == '*' or
                                                                         next_exp == '/' or next_exp == '(' or
                                                                         next_exp == '[' or next_exp == '{'):
            isValid = False

        elif (exp == ')' or exp == '}' or exp == ']') and (next_exp == '+' or next_exp == '-' or next_exp == '*' or
                                                           next_exp == '/'):
            isValid = False

        elif (exp == '}' or exp == ']' or exp == ')') and (next_exp == '{' or next_exp == '[' or next_exp == '('):
            isValid = False

    # If expression is found to be invalid
    if not isValid:
        print("The Expression is Illegal.")
        result = -1
        return result

    # Otherwise evaluate the expression & return result
    # Now our validated stack will pop the expression from left to right
    # We will pop all elements until we see a closed bracket
    # Then evaluate the sub-expression within the bracket
    exp_list = []
    current_exp = Stack()

    while not validated_expression_stack.isEmpty():
        # get an element from stack
        element = validated_expression_stack.pop()

        # If element is not closed bracket
        if element != ']' and element != '}' and element != ')':
            # exp_list.append(element)
            current_exp.push(element)
            # print('cur: ', current_exp.getItems())

        else:  # Element is closed bracket
            # Evaluate sub-expression inside bracket as per operator precedence

            # Match the closed bracket encountered with an open bracket
            open_bracket = ''
            if element == ']':
                open_bracket = '['
            elif element == '}':
                open_bracket = '{'
            elif element == ')':
                open_bracket = '('

            # Pop until matching open bracket and evaluate
            exp_list = []
            popped_element = ''
            while popped_element != open_bracket:
                # Get element from current expression
                popped_element = current_exp.pop()
                # print('cur: ', current_exp.getItems())

                # Store it to exp_list
                exp_list.append(popped_element)

            # Evaluate exp_list
            while '*' in exp_list:
                # get index of operator
                id = exp_list.index('*')
                operator = exp_list[id]

                # find operands
                op = [exp_list[id - 1], exp_list[id + 1]]

                # Evaluate and push to current_exp stack
                current_exp.push(evaluateStackTops(op, operator))
                # print('cur: ', current_exp.getItems())

                # Remove the evaluated operator
                exp_list.pop(id)

            while '/' in exp_list:
                # get index of operator
                id = exp_list.index('/')
                operator = exp_list[id]

                # find operands
                op = [exp_list[id - 1], exp_list[id + 1]]

                # Evaluate and push to current_exp stack
                current_exp.push(evaluateStackTops(op, operator))
                # print('cur: ', current_exp.getItems())

                # Remove the evaluated operator
                exp_list.pop(id)

            while '+' in exp_list:
                # get index of operator
                id = exp_list.index('+')
                operator = exp_list[id]

                # find operands
                op = [exp_list[id - 1], exp_list[id + 1]]

                # Evaluate and push to current_exp stack
                current_exp.push(evaluateStackTops(op, operator))
                # print('cur: ', current_exp.getItems())

                # Remove the evaluated operator
                exp_list.pop(id)

            while '-' in exp_list:
                # get index of operator
                id = exp_list.index('-')
                operator = exp_list[id]

                # find operands
                op = [exp_list[id - 1], exp_list[id + 1]]

                # Evaluate and push to current_exp stack
                current_exp.push(evaluateStackTops(op, operator))
                # print('cur: ', current_exp.getItems())

                # Remove the operator that is evaluated
                exp_list.pop(id)

    # return round(current_exp.pop(), 2)
    return '{:.2f}'.format(float(current_exp.pop()))


def evaluateStackTops(numbers, operation):
    ans = 0.0
    numberStack = Stack()

    for num in numbers:
        numberStack.push(num)

    # Now when we pop the numbers from stack they will in the correct order left to right
    # Evaluate for whatever operation is found
    if operation == '+':
        ans = float(numberStack.pop()) + float(numberStack.pop())
    elif operation == '-':
        ans = float(numberStack.pop()) - float(numberStack.pop())
    elif operation == '*':
        ans = float(numberStack.pop()) * float(numberStack.pop())
    elif operation == '/':
        ans = float(numberStack.pop()) / float(numberStack.pop())

    return ans


def main():
    another_string = True
    print("Please type an arithmetic expression made from unsigned numbers and the operation + - * /. "
          "The expression must be fully parenthesized")

    # While another string is available, prompt user
    while another_string:
        # Prompt user for new expression
        expression = input("\nYour expression: ")

        # Check if expression is balanced or not
        if isBalanced(expression):
            result = evaluate(expression)
            print("The value is " + str(result))

        else:
            print("\nThat is not balanced.")

        # Check if another string
        another_string = query(input("\nAnother string? [Y or N]: "))

    # If no more strings are available print the following
    print("All numbers are interesting.")


if __name__ == "__main__":
    main()

# {{[(12+9)/3]+7.2}*[(6-4)/8]}
