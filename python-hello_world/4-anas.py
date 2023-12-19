import random
negative_last_digit=0
number = random.randint (-10000, 10000)
last_digit = abs(number)%10

#print (number)
#print(last_digit)
if number < 0 :
  negative_last_digit-last_digit*-1
  print("last digit of", number, "is", negative_last_digit)