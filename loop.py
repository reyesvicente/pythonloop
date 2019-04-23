a, b = 1, 1
while a < 5:
    print("a =", a)
    a +=1
    while b < 5:
        print("b =", b)
        if b == 2:
            b = 1
        break
    b +=1
