list = [198, 232, 816, 200, 1536, 300, 6144, 984, 51200, 570, 92160, 1200, 565248, 756, 1474560, 800, 6291456, 1782, 65536000]
ascii = ""
for i in range(0,19):
    if(((i+1)&1)!=0):
        ascii += chr(int(list[i]/pow(2,i+1)))
    else:
        ascii += chr(int(list[i]/(i+1)))
print(ascii)