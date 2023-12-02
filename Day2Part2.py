Input = []
LineReader = open("input.txt","r")
for line in LineReader:
    Input.append(line[:-1])
    
Sum=0
for Game in Input:
    Red=0
    Green=0
    Blue=0
    Game=Game.split(": ")
    ID=Game[0][5:]
    Sets=Game[1].split("; ")
    for i in range(0,len(Sets)):
        Sets[i]=Sets[i].split(", ")
        for j in range(0,len(Sets[i])):
            Sets[i][j] = Sets[i][j].split(" ")
            if Sets[i][j][1] == "red":
                if int(Sets[i][j][0])>Red:
                    Red = int(Sets[i][j][0])
            elif Sets[i][j][1] == "green":
                if int(Sets[i][j][0])>Green:
                    Green = int(Sets[i][j][0])
            elif Sets[i][j][1] == "blue":
                if int(Sets[i][j][0])>Blue:
                    Blue = int(Sets[i][j][0])
    Power = Red*Green*Blue
    Sum+=Power
print(Sum)
