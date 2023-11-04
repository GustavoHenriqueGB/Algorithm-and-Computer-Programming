while True:

    try:
        ah, am = map(int,input().split())
        h = ah // 30
        m = am // 6
        print(f'{h:0>2}:{m:0>2}')
        
    except EOFError:
        break