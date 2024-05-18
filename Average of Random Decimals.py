import random
import decimal
a=round(decimal.Decimal(random.randrange(100,10000)/100),2)
b=round(decimal.Decimal(random.randrange(100,10000)/100),2)
c=round(decimal.Decimal(random.randrange(100,10000)/100),2)
d=round(decimal.Decimal(random.randrange(100,10000)/100),2)
e=round(decimal.Decimal(random.randrange(100,10000)/100),2)

Ave=(a+b+c+d+e)/5

print("The Five Numvers are: ", a, ",", b, ",", c, ",", d, ",", e)
print("The Average is ", Ave)