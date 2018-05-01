# opening the file with read mode
open_file = open("sort_output.txt","r")
# opening the file with write mode
write_reducer_output = open("reducer_output.txt", "w")
# setting values to default no string values
currency_Name = ""
high_key_name =""
high_value=0.00
min_high_value = 0.00 # Initalizing min_high_value,min_high_key_name and status
min_high_key_name = "" 
status = True

# checking the input for every line
for line in open_file:
  data = line.strip().split('\t')
  bitcoin_Name, Price= data
  if status: 
    min_high_value = Price # Setting the minimum high value to price
    status = False
  if Price < min_high_value: # verifying the comparision of price value with min high value
     min_high_value = Price 
     min_high_key_name = bitcoin_Name
        
# verifying the bitcoin name and checking with non currency name
  if bitcoin_Name != currency_Name:
    # writing the onto the output file
    if high_value < Price:
        high_key_name = bitcoin_Name
        high_value = Price
    if currency_Name:  
      #print str(high_key_name)+","+high_value    
      write_reducer_output.write('Name of Bitcoin: '+str(high_key_name) + " Least high value: " + str(high_value)+'\n')
      # initializing the values to default values once done with a type of currency
    currency_Name = bitcoin_Name
    high_value=0.0

  # writing the final outcome to the output file
# closing the opened files.
write_reducer_output.write("\n\nName of Bitcoin: {0}\t Least high value of all the currencies: {1}\t".format(min_high_key_name,min_high_value))
print "\n\nName of Bitcoin: {0}\t Least high value of all the currencies: {1}\t".format(min_high_key_name,min_high_value)

open_file.close()
write_reducer_output.close()

''' read_file = open("sort_output.txt","r") # reading sort output
write_file = open("reducer_output.txt", "w") # writing to reducer output

min_high_value = 0.00 # Initalizing min_high_value,min_high_key_name and status
min_high_key_name = "" 
status = True
old_price = 0.00
high_value = 0.00
high_key_name=""

for line in read_file.readlines(): # reading each value from sor_output file
    data = line.strip().split("\t") # split the data by tab space
    if len(data) == 2: 
        bitcoin_name, Price = data # reading data into bitcoint_name and Price
        if status: 
            min_high_value = Price # Initalizing current value to Price
            status = False
        if Price < min_high_value: # cheking condition, if the current value is less than the exiting value
            min_high_value = Price 
            min_high_key_name = bitcoin_name
        s = bitcoin_name
        if s == bitcoin_name:
            if high_value < Price:
                high_key_name = s
                high_value = Price
    print "\n\nName of Bitcoin: {0}\t Least high value: {1}\t".format(high_key_name,high_value)
    high_value = 0.00
    s=bitcoin_name
write_file.write("\n\nName of Bitcoin: {0}\t Least high value: {1}\t".format(min_high_key_name,min_high_value))
print "\n\nName of Bitcoin: {0}\t Least high value of all the bitcoin: {1}\t".format(min_high_key_name,min_high_value)
read_file.close() # closing read_file
write_file.close() # closing write_file
 '''

''' 
Previous code using Data Structures

bitcoint_list = [] 
highest_avg=[]
bitCoin_Name =[]

read_file = open("sort_output.txt","r")
write_file = open("reducer_output.txt", "w")

for line in read_file.readlines():
    data = line.strip().split("\t")
    if len(data) == 2: #condition to check if data has 2 columns 
        bitcoint_name, Price = data #column values are assigned to bitcoin_name and price 
        bitcoint_list.append(bitcoint_name) 
bitcoin_unique = set(bitcoint_list) #this will set the unique values to the bitcoin_uique 
sort_list = sorted(bitcoin_unique) #bitcoin_unique values are sorted
read_file.close()

for bitcoint_names in sort_list: # for each value in sort_line new price_list,total_price,count are created.
    price_list =[]
    total_price = 0
    count = 0
    read_file = open("sort_output.txt","r")  
    for line in read_file.readlines(): 
        data = line.strip().split("\t")
        if len(data) == 2:
            bitcoint_name, Price = data
            s = bitcoint_name
            if s == bitcoint_names:
                price_list.append(float(Price))
                count = count + 1
                total_price = total_price + float(Price)
    highest_avg.append(min(price_list)) #this will append highest_avg value with price_list 
    bitCoin_Name.append(bitcoint_names) #this will append bitCoin_Name with bitcoint_names
    write_file.write("Name of Bitcoin: {0}\t Least value: {1}\t\n".format(bitcoint_names,min(price_list))) #least values of the 
    print "Name of Bitcoin: {0}\t Least value: {1}\t".format(bitcoint_names,min(price_list))
    del price_list
    del total_price
write_file.write("\n\nName of Bitcoin: {0}\t Least high value: {1}\t".format(bitCoin_Name[highest_avg.index(min(highest_avg))],min(highest_avg)))
print "\n\nName of Bitcoin: {0}\t Least high value: {1}\t".format(bitCoin_Name[highest_avg.index(min(highest_avg))],min(highest_avg))
read_file.close()
write_file.close() '''