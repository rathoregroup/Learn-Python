price = int(input())
if price>=300:
    print(price-price*0.3)
elif price>=200 and price<300:
    print(price-price*0.2)
elif price>=100 and price<200:
    print(price-price*0.1)
elif price>=0 and price<100:
    print(price-price*0.05)
else:
    print(price)
    