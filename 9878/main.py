from math import log

file=open("input.txt","r")
write=open("output.txt","w")
data=file.read()
dataString=data.split(" ")

def math_operation(x):
    p=3.62*log(x+2.3)
    k=p**3
    return [x,p,k]


result=math_operation(float(dataString[0]))
write.write(f"{result[0]} {result[1]} {result[2]}")
    

file.close()
write.close()