#Races=[[7,9],[15,40],[30,200]]
Races=[[46,208],[85,1412],[75,1257],[82,1410]]
Ways=[]
for Race in Races:
    Total=0
    i=1
    while i<Race[0]:
        if(i*(Race[0]-i))>Race[1]:
            Total+=1
        i+=1
    Ways.append(Total)
print(Ways)
