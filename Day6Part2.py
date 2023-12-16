#Time = 71530
Time = 46857582
#Distance = 940200
Distance = 208141212571410

i=1
Min=0
Max=0
while i<Time:
    if i*(Time-i)>Distance:
        Min=i
        break
    i+=1
i=Time
while i>Min:
    if i*(Time-i)>Distance:
        Max=i
        break
    i+=-1
print(Min,Max)
print(Max-Min+1)
