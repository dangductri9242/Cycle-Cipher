import sys

def read_key(key_file):
    with open(key_file, "r") as input_file:
        g = input_file.readlines()
        key=[]
        for i in range(0,len(g),3):
            g[i]=g[i].replace(" \n","")
            key_string=list(map(int,g[i].split()))
            g[i+1]=int(g[i+1])
            g[i+2]=int(g[i+2])
            key.append((key_string,g[i+1],g[i+2]))

    input_file.close()
    return key

def reverse_key_pair(key_string):
    reverse_key=[0]*len(key_string)
    for i in range(len(key_string)):
        reverse_key[key_string[i]]=i
    return reverse_key

def decryption_one_round(ciphertext,key_string,start_point,direction):
    plaintext=[]
    ciphertext=ciphertext[::-1]

    reverse_look_up=reverse_key_pair(key_string)

    for i in range(len(ciphertext)-1):
        tmp=direction*(reverse_look_up[ciphertext[i]]-reverse_look_up[ciphertext[i+1]])
        if tmp<0:
            tmp+=len(key_string)
        plaintext.append(tmp)

    tmp=direction*(reverse_look_up[ciphertext[-1]]-start_point)
    if tmp<0:
        tmp+=len(key_string)
    plaintext.append(tmp)

    return bytearray(plaintext[::-1])

def print_byte(byte_array):
    for byte in byte_array:
        print(byte,end=" ")
    print()
    return 0

file_path=sys.argv[1]
try:
    with open(file_path, "rb") as input_file:
        g = input_file.read()
        b = bytearray(g)
    input_file.close()

#Read the key file -----------------------------------------------------------------------------------------------------------------------

    file_key=sys.argv[3]
    key=read_key(file_key)

#-----------------------------------------------------------------------------------------------------------------------------------------
    
# #Decryption ------------------------------------------------------------------------------------------------------------------------------

    ciphertext=b

    key=key[::-1]
    for i in range(len(key)):
        key_string=key[i][0]
        start_point=key[i][1]
        direction=key[i][2] 
        reverse=reverse_key_pair(key_string)
        new_plaintext=decryption_one_round(ciphertext,key_string,start_point,direction)
        ciphertext=new_plaintext

#Print file ------------------------------------------------------------------------------------------------------------------------------

    decrypted_file=sys.argv[2]
    f=open(decrypted_file,"ab")
    f.write(new_plaintext)
    f.close()

except FileNotFoundError:
    print('File not found')


