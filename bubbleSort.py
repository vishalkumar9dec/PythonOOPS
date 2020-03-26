

def sort(ele):
    for i in range(len(ele)-1, 0, -1):
        for j in range(i):
            if ele[j] > ele[j+1]:
                temp = ele[j]
                ele[j] = ele[j+1]
                ele[j+1] = temp



ele = [4,6,2,7,8,1]

sort(ele)
print(ele)