file=open(' Fileprogram.txt','w')
file.write("hi i am silvia.")
file.write("\ncurrently i am doing  my internship in python django at inmakes. ")
file.close()


file=open(' Fileprogram.txt','r')
content=file.read()
print(content)
file.close()

file=open(' Fileprogram.txt','a')
file.write("\npython is simple to learn ")
file.close()