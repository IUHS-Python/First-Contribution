secret_number= 6
i =0
print("Guess the number ... (0-10)")
while  i < 3 :
       i+=1
       x = int(input('Guess : '))
       if  x==secret_number :
           print('you win..')
           break
       else :
           print(f'You have only {3-i} chance ')
