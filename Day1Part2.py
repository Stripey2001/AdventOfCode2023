Input = []
LineReader = open("input.txt","r")
for line in LineReader:
    Input.append(line)

def CheckIfNum(line,i):
    if line[i].isnumeric():
        return line[i]
    try:
        if line[i:i+3]=="one":
            return 1
    except:
        return 0
    try:
        if line[i:i+3]=="two":
            return 2
    except:
        return 0
    try:
        if line[i:i+5]=="three":
            return 3
    except:
        return 0
    try:
        if line[i:i+4]=="four":
            return 4
    except:
        return 0
    try:
        if line[i:i+4]=="five":
            return 5
    except:
        return 0
    try:
        if line[i:i+3]=="six":
            return 6
    except:
        return 0
    try:
        if line[i:i+5]=="seven":
            return 7
    except:
        return 0
    try:
        if line[i:i+5]=="eight":
            return 8
    except:
        return 0
    try:
        if line[i:i+4]=="nine":
            return 9
    except:
        return 0
    return 0

def FirstNum(Text):
    for i in range(0,len(Text)):
        if int(CheckIfNum(Text,i))>0:
            return str(CheckIfNum(Text,i))
            
def LastNum(Text):
    for i in range(len(Text)-1,-1,-1):
        if int(CheckIfNum(Text,i))>0:
            return str(CheckIfNum(Text,i))

Values=[]

for j in range(0,len(Input)):
    Values.append(int(FirstNum(Input[j])+LastNum(Input[j])))
print(sum(Values))
