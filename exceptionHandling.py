a = 5
b = 'p'

try:
    print("Connection Opened")
    print(a/b)
except ZeroDivisionError as e:
    print("Raised zero division exception : " , e)

except Exception as e:
    print('Raised Exception', e)
finally:
    print('Connection Closed')


print('Bye')