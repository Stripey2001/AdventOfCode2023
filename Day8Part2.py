Input = []
LineReader = open("Input.txt","r")
for line in LineReader:
    Input.append(line[:-1])
    
Directions = Input[0]
Location=[]
Right=[]
Left=[]

for i in range(2,len(Input)):
    Location.append(Input[i][:3])
    Left.append(Input[i][7:10])
    Right.append(Input[i][12:15])
    
Current=[]
for i in range(0,len(Location)):
    if Location[i][2]=="A":
        Current.append(Location[i])

Moves=0
AllZ=False
while not AllZ:
    if Directions[Moves%len(Directions)]=="L":
        for i in range(0,len(Current)):
            Current[i] = Left[Location.index(Current[i])]
    else:
        for i in range(0,len(Current)):
            Current[i] = Right[Location.index(Current[i])]
    AllZ = True
    for i in range(0,len(Current)):
        if Current[i][2]!="Z":
            AllZ=False
    Moves+=1
print(Moves)
