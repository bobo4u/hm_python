def invest(amount,rate,time):
    print('principal amount:{}'.format(amount))
    for t in range(1,time+1):
        amount = amount * (1 + rate)
        print('year {}: ${}'.format(t,amount))

invest(50,0.05,10)

invest(100,0.05,10)
