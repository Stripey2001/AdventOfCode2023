Input = []
LineReader = open("Input.txt","r")
for line in LineReader:
    Input.append(line[:-1])

Total = 0
for Card in Input:
    Value = 0
    Card = Card.split(": ")[1]
    Card = Card.split(" | ")
    Card[0] = Card[0].split(" ")
    Card[1] = Card[1].split(" ")
    for i in range(0,len(Card[0])):
        for j in range(0,len(Card[1])):
            if Card[0][i]=="":
                break
            else:
                if Card[0][i] == Card[1][j]:
                    if Value == 0:
                        Value = 1
                    else:
                        Value = Value*2
    Total+=Value
print(Total)
