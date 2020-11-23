a=0
for i in range(1,10):
    if i == 5:
        print('----------')
        print("这是i" + str(i))
        continue
    a+=1
    print("这是a"+str(a))