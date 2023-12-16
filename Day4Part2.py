Input = []
LineReader = open("Input.txt","r")
for line in LineReader:
    Input.append(line[:-1])

Total = 0
Cards=[]
for i in range(0,len(Input)):
    Cards.append(1)
for i in range(0,len(Input)):
    Value=0
    Input[i] = Input[i].split(": ")[1]
    Input[i] = Input[i].split(" | ")
    Input[i][0] = Input[i][0].split(" ")
    Input[i][1] = Input[i][1].split(" ")
    for j in range(0,len(Input[i][0])):
        for k in range(0,len(Input[i][1])):
            if Input[i][0][j]=="":
                break
            else:
                if Input[i][0][j] == Input[i][1][k]:
                    Value+=1
    j=1
    while j <= Value:
        Cards[i+j]=Cards[i+j]+Cards[i]
        j+=1
print(Cards)
print(sum(Cards))
