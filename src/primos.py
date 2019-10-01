num = int(input())
numinicio = 1
quant = 0
while True:
    if numinicio > 1:
        for i in range(2,numinicio):
            if (numinicio % i) == 0:
                break
        else:
            print(numinicio)
            quant += 1
    if (quant == num):
        break
    else:
        numinicio += 1
    



    
