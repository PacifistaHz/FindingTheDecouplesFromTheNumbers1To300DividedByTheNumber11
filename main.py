array=list()
for number in range(1,301):
    oddsSum=0
    evensSum=0
    number=str(number)
    for i in range(0,len(number)):
        if i % 2 == 0:
            evensSum+=int(number[i])
        else:
            oddsSum+=int(number[i])
    if abs(evensSum - oddsSum) % 11 == 0:
        array.append(number)
print(*array,sep="\n")