# name of student: Milan Sebes
# number of student: 99067157
# purpose of program: to give the change
# function of program: to calculate the change
# structure of program: 

toPay = int(float(input('Amount to pay: '))* 100) # asks how much you need to pay
paid = int(float(input('Paid amount: ')) * 100) # asks how much you've paid
change = paid - toPay # it calculates the change

if change > 0: 
  coinValue = 500
  
  while change > 0 and coinValue > 0: 
    nrCoins = change // coinValue 

    if nrCoins > 0: 
      print('return maximal ', nrCoins, ' coins of ', coinValue, ' cents!' ) # print how much coins you can choose
      nrCoinsReturned = int(input('How many coins of ' + str(coinValue) +  ' cents did you return? ')) # it'll ask how much you want to get
      change -= nrCoinsReturned * coinValue #

# comment on code below:
    if coinValue == 500:
      coinValue = 200
    elif coinValue == 200:
      coinValue = 100
    elif coinValue == 100:
      coinValue = 50
    elif coinValue == 50:
      coinValue = 20
    elif coinValue == 20:
      coinValue = 10
    elif coinValue == 10:
      coinValue = 5
    elif coinValue == 5:
      coinValue = 2
    elif coinValue == 2:
      coinValue = 1
    else:
      coinValue = 0

if change > 0: # if there isn't enough change then it will print 'change not returned'
  print('Change not returned: ', str(change) + ' cents')
else:
  print('done')