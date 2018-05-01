newinput = open("aftermapper.txt","r") # a new input file with mapper output is opened  
newoutput=open("sort_output.txt","w") # a new output of the sorted file is opened with write privilage

data = newinput.readlines() #new lines from data file is fed to 'data' 
data.sort() # all the values in the data are sorted here
for line in data:
    newoutput.write(line)
newinput.close()
newoutput.close()