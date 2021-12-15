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
        str_input = input("\nAnother string? [Y or N]: \n")

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
    isValid = True  # False if expression is invalid
    result = 0

    # Assume expression is valid and evaluate until invalid
    operators = Stack()
    operands = Stack()
    expression_stack = Stack()
    expression_list = []
    expression_count = 0

    # Removing spaces
    for character in expression:
        if character != ' ':
            expression_list.append(character)
    expression = ''.join(expression_list)
    print(expression)

    # Push expression to stack and validate
    i, j = 0, 0
    number=None
    while i < len(expression) and isValid:
        print("i: ", i)
        # For numbers, check for multi-digit numbers and floats
        while expression[i].isdigit() and i < len(expression)-1:
            j = i
            if expression[j+1].isdigit() or expression[j+1] == '.':
                j += 1

            # extract the entire number from the string
            elif i == j:
                number = expression[j]

                # push number to stack
                print("pushed: ", number)
                expression_stack.push(number)
                expression_count += 1
                i += 1
            else:
                number = expression[i:j]
                i = j

                # push number to stack
                print("pushed: ", number)
                expression_stack.push(number)
                expression_count += 1
                i += 1



        # For brackets or operators, just push to stack
        if i < len(expression):
            print("pushed: ", expression[i])
            expression_stack.push(expression[i])
            expression_count += 1
            i += 1

    print("expression_stack: ", expression_stack.getItems())

    # Check validity of expression
    i = 0

    # Copy popped elements into validated stack
    validated_expression_stack = Stack()

    while not expression_stack.isEmpty():

        exp = expression_stack.pop()
        validated_expression_stack.push(exp)
        print("validated: ", exp)

        if not expression_stack.isEmpty():
            next_exp = expression_stack.pop()
            # expression_stack.push(next_exp)
            validated_expression_stack.push(next_exp)
            print("validated: ", next_exp)
        else: next_exp = ' '

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

        elif exp.isalpha():
            isValid = False

        # If expression is invalid
    if not isValid:
        print("The Expression is Illegal.")
        result = -1
    print("Validated stack: ", validated_expression_stack.getItems())
    #  Looking for the first close bracket in the exp
    exp_list = []
    operator_flag = False
    while not validated_expression_stack.isEmpty():
        one_char = validated_expression_stack.pop()
        operator_flag = False
        if one_char != ']' and one_char != '}' and one_char != ')':
            exp_list.append(one_char)
            print(exp_list)
            operator_flag = True
        else:
            while '*' in exp_list:
                # get index of operator
                id = exp_list.index('*')
                operator = exp_list[id]

                # find operands
                op = [exp_list[id-1], exp_list[id+1]]

                # pass to stacktops
                ans = evaluateStackTops(op, operator)

                #  Replace with result
                exp_list[id] = ans
                exp_list.pop(id-1)
                exp_list.pop(id)
                operator_flag = True


            while '/' in exp_list:
                # get index of operator
                id = exp_list.index('/')
                operator = exp_list[id]

                # find operands
                op = [exp_list[id-1], exp_list[id+1]]

                # pass to evaluate
                ans = evaluateStackTops(op, operator)

                # Replace with result
                axp_list[id] = ans
                exp_list.pop(id-1)
                exp_list.pop(id)
                operator_flag = True


            while '+' in exp_list:
                # get index of operator
                id = exp_list.index('+')
                operator = exp_list[id]

                # find operands
                op = [exp_list[id - 1], exp_list[id + 1]]

                # pass to evaluate
                ans = evaluateStackTops(op, operator)

                # Replace with result
                exp_list[id] = ans
                exp_list.pop(id - 1)
                exp_list.pop(id)
                operator_flag = True

            while '-' in exp_list:
                # get index of operator
                id = exp_list.index('-')
                operator = exp_list[id]

                # find operands
                op = [exp_list[id - 1], exp_list[id + 1]]

                # pass to evaluate
                ans = evaluateStackTops(op, operator)

                # Replace with result
                exp_list[id] = ans
                exp_list.pop(id - 1)
                exp_list.pop(id)
                operator_flag = True
    print(exp_list)
    for element in exp_list:
        print(element)
        if element !='(' and element !='[' and element !='{':
            result = element
            print(result)

    return float(result)


# ----------------------------------------------------------

def evaluateStackTops(numbers, operation):
    print("evaluating")
    ans = 0
    numberStack = Stack()

    for num in numbers:
        numberStack.push(num)

    if operation == '+':
        ans = float(numberStack.pop()) + float(numberStack.pop())
    elif operation == '-':
        ans = float(numberStack.pop()) - float(numberStack.pop())
    elif operation == '*':
        ans = float(numberStack.pop()) * float(numberStack.pop())
    elif operation == '/':
        ans = float(numberStack.pop()) / float(numberStack.pop())

    return str(ans)

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
