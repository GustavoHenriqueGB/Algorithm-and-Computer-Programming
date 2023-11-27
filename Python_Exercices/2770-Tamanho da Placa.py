while True:

    try:
        x, y, m = map(int, input().split())

        for i in range(0,m):
            xi, yi = map(int, input().split())

            if xi <= x and yi <= y or xi <= y and yi <= x:
                print('Sim')

            else:
                print('Nao')

                
    except EOFError:
        break