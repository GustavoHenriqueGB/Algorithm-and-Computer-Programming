while True:
    H1, M1, H2, M2 = map(int, input().split())

    if H1 == 0 and M1 == 0 and H2 == 0 and M2 == 0:
        break

    else:
        M1 = H1 * 60 + M1 
        M2 = H2 * 60 + M2
        Mfinal = M2 - M1

        if M2 - M1 < 0:
            Mfinal += 60 * 24

        print(Mfinal)
    
    