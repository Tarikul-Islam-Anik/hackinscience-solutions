for i in range(1, 10):
    for j in range(1, 10):
        for k in range(1, 10):
            for l in range(1, 10):
                if str(i) in '158' and str(j) in '158' and str(k) in '158' and str(l) in '158':
                    pin = f'{i} {j} {k} {l}'
                    if all(x in pin for x in '158'):
                        print(pin)
