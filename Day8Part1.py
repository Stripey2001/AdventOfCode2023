Input = []
LineReader = open("Input.txt","r")
for line in LineReader:
    Input.append(line[:-1])
    
Directions = Input[0]
Location=[]
Right=[]
Left=[]
Current="AAA"

for i in range(2,len(Input)):
    Location.append(Input[i][:3])
    Left.append(Input[i][7:10])
    Right.append(Input[i][12:15])
    
Moves=0
while Current!="ZZZ":
    if Directions[Moves%len(Directions)]=="L":
        Current = Left[Location.index(Current)]
    else:
        Current = Right[Location.index(Current)]
    Moves+=1
print(Moves)
