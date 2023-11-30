while True:
    try:
        string = input()
        new_string = ''
        upper = True

        for i in string:
            
            if i == ' ':
                new_string += ' '

            elif upper:
                new_string += i.upper()
                upper = False

            else:
                new_string += i.lower()
                upper = True

        print(new_string)
    except EOFError:
        break