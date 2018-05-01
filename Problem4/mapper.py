#opening the file cryptodata with the access to reading access
input_file=open("cryptodata.csv","r")
#opening the file mapper_gopi.txt with the writing access
output_file=open("mapper_gopi.txt","w")
#iterating through all the lines of the input data
for line in input_file:
    #separating the data with the reference of ,
    data=line.strip().split(",")
    #copying the list of values of the data onto a list
    slug,symbol,bitcoin_name,date,ranknow,open_value,high,low,close_value,volume,market,close_ratio,spread=data
    # writing the required columns onto the output file
    output_file.write(bitcoin_name+"\t"+open_value+"\t"+close_value+"\n")
# closing the files 
input_file.close()
output_file.close() 