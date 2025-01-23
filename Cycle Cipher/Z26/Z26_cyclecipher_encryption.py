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

def encryption_one_round(plaintext,key_string,start_point,direction):
    ciphertext=[]
    current=int(start_point)
    if direction==1:

        for byte in plaintext:
            current=(current+int(byte))%len(key_string)
            ciphertext.append(key_string[current])

    elif direction==-1:

        for byte in plaintext:
            current=(current-int(byte))

            if current<0:
                current+=len(key_string)

            ciphertext.append(key_string[current])

    return bytearray(ciphertext)

def print_byte(byte_array):
    for byte in byte_array:
        print(byte,end=" ")
    print()
    return 0

file_path=sys.argv[1]
try:
    with open(file_path, "rb") as input_file:
        g = input_file.read()
        byte_in_Z26=[]

        byte_in_Z256 = bytearray(g)

        for byte in byte_in_Z256:
            byte_in_Z26.append(byte-65)
        b=bytearray(byte_in_Z26)

    input_file.close()
    
#Read the key file -----------------------------------------------------------------------------------------------------------------------

    file_key=sys.argv[3]
    key=read_key(file_key)

#-----------------------------------------------------------------------------------------------------------------------------------------
    
#Encryption ------------------------------------------------------------------------------------------------------------------------------

    plaintext=b

    for i in range(len(key)):
        key_string=key[i][0]
        start_point=key[i][1]
        direction=key[i][2] 
        ciphertext=encryption_one_round(plaintext,key_string,start_point,direction)

        plaintext=ciphertext

#Print file ------------------------------------------------------------------------------------------------------------------------------

    cipher_file=sys.argv[2]
    ciphertext_in_Z26=[]
    for byte in ciphertext:
        ciphertext_in_Z26.append(byte+65)
        
    ciphertext_in_Z26=bytearray(ciphertext_in_Z26)

    f=open(cipher_file,"ab")
    f.write(ciphertext_in_Z26)
    f.close()

except FileNotFoundError:
    print('File not found')


