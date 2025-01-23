import random
import sys

#Generate key
def key_generation():
    set_1=[]
    while len(set_1)<26:
        tmp=random.randint(0,25)
        if tmp not in set_1:
            set_1.append(tmp)
    start_point=random.randint(0,25)
    
    dir_ran=random.randint(0,1)
    if dir_ran==0:
        direction=-1
    else:
        direction=1
    return set_1,start_point,direction

#Key generating ------------------------------------------------------------------------------------------------------ 
#Open file
file_key =sys.argv[1]
f=open(file_key,"a")

repetition=int(sys.argv[2])

for k in range(repetition):
    key_string,start_point,direction=key_generation()
    for i in range(len(key_string)):
        f.write(str(key_string[i])+' ')
    f.write('\n')
    f.write(str(start_point))
    f.write('\n')
    f.write(str(direction))
    f.write('\n')

f.close()
#--------------------------------------------------------------------------------------------------------------------------------------------
