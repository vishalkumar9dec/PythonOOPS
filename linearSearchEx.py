pos = -1

def search(list1,n):
    for i in range(len(list1)):
        if list1[i] == n:
            globals() ['pos'] = i
            return True
    else:
        return False


list1 = [1,2,3,4,5,6]
n=10

if search(list1,n):
    print('Found at ', pos+1)
else:
    print('Not Found')