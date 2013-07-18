def p():
    draw, balance = map (float,raw_input().split())
    if draw % 5 == 0 and (draw + 0.5) <= balance:
        balance -= draw + 0.5

    print "%.2f" %balance
    
p()
