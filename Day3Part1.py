Input = []
LineReader = open("input.txt","r")
for line in LineReader:
    Input.append(line)

def CheckAdjacent(i,j,Input):
    try:
        if Input[i-1][j-1].isnumeric()==False:
            if Input[i-1][j-1]!=".":
                return True
    except:
        a=0
    try:
        if Input[i-1][j].isnumeric()==False:
            if Input[i-1][j]!=".":
                return True
    except:
        a=0
    try:
        if Input[i-1][j+1].isnumeric()==False:
            if Input[i-1][j+1]!=".":
                return True
    except:
        a=0
    try:
        if Input[i][j-1].isnumeric()==False:
            if Input[i][j-1]!=".":
                return True
    except:
        a=0
    try:
        if Input[i][j+1].isnumeric()==False:
            if Input[i][j+1]!=".":
                return True
    except:
        a=0
    try:
        if Input[i+1][j-1].isnumeric()==False:
            if Input[i+1][j-1]!=".":
                return True
    except:
        a=0
    try:
        if Input[i+1][j].isnumeric()==False:
            if Input[i+1][j]!=".":
                return True
    except:
        a=0
    try:
        if Input[i+1][j+1].isnumeric()==False:
            if Input[i+1][j+1]!=".":
                return True
    except:
        a=0
    return False

Digits=[]
i=0
while i < len(Input):
    j=0
    while j< len(Input[i]):
        Adjacent=False
        Digit=0
        if Input[i][j].isnumeric():
            Digit=int(Input[i][j])
            if CheckAdjacent(i,j,Input):
                Adjacent = True
            if Input[i][j+1].isnumeric():
                j+=1
                Digit=Digit*10+int(Input[i][j])
                if CheckAdjacent(i,j,Input):
                    Adjacent = True
                if Input[i][j+1].isnumeric():
                    j+=1
                    Digit=Digit*10+int(Input[i][j])
                    if CheckAdjacent(i,j,Input):
                        Adjacent = True
            if Adjacent:
                Digits.append(Digit)
        j+=1
    i+=1
    
print(Digits)
print(sum(Digits))
