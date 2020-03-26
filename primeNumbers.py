num = 23

flag = 0
for i in range(2,num//2):
    if num%i==0:
        flag=1
        break


if flag == 1:
    print('Number is not prime')
else:
    print('number is prime')