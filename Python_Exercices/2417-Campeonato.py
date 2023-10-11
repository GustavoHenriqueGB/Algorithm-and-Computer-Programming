cv, ce, cs, fv, fe, fs = map(int, input().split())
cp = cv * 3 + ce
fp = fv * 3 + fe

if cp == fp:
    if cs == fs:
        print('=')
    elif cs > fs:
        print('C')
    elif cs < fs:
        print('F')
elif cp > fp:
    print('C')
elif cp < fp:
    print('F') 