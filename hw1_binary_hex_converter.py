while True:
    try:
        n = int(input())
        bi = " "
        a = n
        while n > 0:
            bi = str(n % 2) + bi
            n //= 2
        print(bi)
        hex_digit = "0123456789ABCDEF"
        h = ""
        while a > 0:
            r = a % 16
            h = hex_digit[r] + h
            a //= 16
        print(h)
    except EOFError:
        break
