#Opening the file of crypto currency data
c=open("cryptodata.csv","r")
#Opening the file of mapper output
mo=open("aftermapper.txt","w")
#reading each line in file of data
for line in c:
    #separating the data from "," symbol
    datalist=line.strip().split(",")
    #Assigning data to variables data list
    slug,symbol,name,date,ranknow,open,high,low,close,volume,market,close_ratio,spread=datalist
    #Writing data into the file named after_gundu.txt
    mo.write(name.replace(' ', '')+"\t"+high+"\n")
#closing data file
c.close()
# closing the file which is written
mo.close()

