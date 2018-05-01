f=open("cryptodata.csv","r") #opening cryptodata.csv file 
o=open("aftermapper.txt","w")#opening mapper output file
for line in f:
    datalist=line.strip().split(",") # This will remove extra spaces and splits the data with coma   
    slug,symbol,name,date,ranknow,open,high,low,close,volume,market,close_ratio,spread=datalist #data is assigned to all the variables 
    o.write(name.replace(' ', '')+"\t"+high+"\n")  #this will write data to mapper output by removing spaces and appending high value 
    print name.replace(' ','')+"\t"+high #output will be printed on the console 
f.close() #data file is closed 
o.close() #output file is closed