#Taking the data from the mapper output
newinput = open("aftermapper.txt","r")
#Creating a new file for the output after sorting the data
newoutput=open("sort_output.txt","w")
# variable data is assigned to readlines from the mapper output
data = newinput.readlines()
#data is sorted 
data.sort()
#Now each line in data is read by a variable line
for line in data:
    # data which is read is then written in sorted output file
    newoutput.write(line)
#The input file which is data is closed
newinput.close()
#The file which is written is closed
newoutput.close()