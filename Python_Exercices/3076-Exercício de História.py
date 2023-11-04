while True:

    try:   
        ano = int(input())
        sec = ano // 100
        if ano % 100 != 0:
            sec += 1
        print(sec)

    except EOFError:
        break