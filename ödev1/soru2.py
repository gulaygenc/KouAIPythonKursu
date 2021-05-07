for i in range(5):
    num = int(input("Enter number: "))
    temp = False
    
    if num == 1:
        print("asal değil")
        break
    else:
        for j in range(2,num):
            if (num % j) == 0:
                temp = True
                break
            else:
                temp = False
    
    if temp == True:
        print("asal değil")
    else:
        print("asal")