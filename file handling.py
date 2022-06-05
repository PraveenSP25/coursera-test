f =open("my info","r")


f1=open("praven","w")  ## here it check file name it didnt find any file in this name that time it will create file in given name
for data in f:  ## here we copy the data from my info to praveen
    f1.write(data)
