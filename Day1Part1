Input = []
LineReader = open("input.txt","r")
for line in LineReader:
    Input.append(line)

def FirstNum(Text):
    for i in range(0,len(Text)):
        if Text[i].isnumeric():
            return Text[i]
            
def LastNum(Text):
    for i in range(len(Text)-1,-1,-1):
        if Text[i].isnumeric():
            return Text[i]

Values=[]

for j in range(0,len(Input)):
    Values.append(int(FirstNum(Input[j])+LastNum(Input[j])))
print(sum(Values))
