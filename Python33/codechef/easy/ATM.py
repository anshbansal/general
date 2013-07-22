def p():
    draw, balance = map(float, input().split())
    if not(draw % 5) and (draw + 0.5) <= balance:
        balance -= draw + 0.5

    print(balance)
    
p()
