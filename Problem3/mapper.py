
# here a file is been opened with read permission
dataInput = open("cryptodata.csv", "r") 

 # here a file dataoutput is created with write permission
dataOutput = open("aftermapper_tarun.txt", "w")

 # for every line in daatInput, data in "data" variable is refined by removing the extra spaces  
for line in dataInput: 
  data = line.strip().split(",")
  #If condition to check if the data has 13 values in it
  if (len(data) == 13): 
    slug,symbol,name,date,ranknow,open_value,high,low,close,volume,market,close_ratio,spread = data
    #data is written into the dataOutput file
    dataOutput.write(name + "\t" + open_value+ "\n")
#dataInput is closed  
dataInput.close() 
#data output file is closed
dataOutput.close()