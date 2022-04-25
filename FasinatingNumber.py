
def fasinating(n):
    s1 = str(n) + str(n*2) + str(n*3)
    # print('s = ',s1)
    Frequency = [0] * 10
    for i in s1:
        d = int(i)
        Frequency[d]+=1
    for i in range(1,10):
        if(Frequency[i]==0 or Frequency[i]>1):
          return False
    return True

n = 192
x = fasinating(n)
if (x==True):
     print(n, ' is a fasinating no')
else:
     print(n, ' is not a fasinating no')