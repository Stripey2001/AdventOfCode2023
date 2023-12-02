Input = []
LineReader = open("input.txt","r")
for line in LineReader:
    Input.append(line[:-1])
    
Sum=0
for Game in Input:
    Possible = True
    Game=Game.split(": ")
    ID=Game[0][5:]
    Sets=Game[1].split("; ")
    for i in range(0,len(Sets)):
        Sets[i]=Sets[i].split(", ")
        for j in range(0,len(Sets[i])):
            Sets[i][j] = Sets[i][j].split(" ")
            if Sets[i][j][1] == "red":
                if int(Sets[i][j][0])>12:
                    Possible = False
            elif Sets[i][j][1] == "green":
                if int(Sets[i][j][0])>13:
                    Possible = False
            elif Sets[i][j][1] == "blue":
                if int(Sets[i][j][0])>14:
                    Possible = False
    if Possible:
        Sum+=int(ID)
print(Sum)
