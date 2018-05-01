read_file = open("sort_output.txt","r") # reading sort output
write_file = open("reducer_output.txt", "w") # writing to reducer output
#new variable is created 
max_high_value = 0.00
#new variable is created 
max_high_key_name = ""
#new variable is Status is created 
status = True
#total variable is created
total = 0.0
#Variable count is created
count = 0
#Variable check is created
check = ""
#Variable avg is created
avg = 0.00
#Variable avg_bit_coin_name is created
avg_bit_coin_name = ""
#Variable avg_bitcoin_value is created
avg_bitcoin_value = 0.00
#Reading each line from the input file
for line in read_file.readlines(): 
    #splits the data
    data = line.strip().split("\t")
    #Checks if length of the data is two
    if len(data) == 2:
        # reading data into bitcoint_name and Price
        bitcoin_name, Price = data 
        #Checks if status exists
        if status:
            max_high_value = float(Price)
            #Assigning Status to false
            status = False 
            check = bitcoin_name
            avg_bitcoin_value = 0
            #checks bitcoin not equal to check
        if bitcoin_name != check:
          #  Checks avg_bitcoin_value is less than total/count:
            if avg_bitcoin_value < total/count:
                avg_bit_coin_name = check
                avg_bitcoin_value = total/count
            #Caluclating the average
            avg = total/count
            #writing the output 
            write_file.write("\n\nName of Bitcoin: {0}\t Avg value: {1}\t".format(max_high_key_name,total/count))
            print "\n\nName of Bitcoin: {0}\t AVG value: {1}\t".format(max_high_key_name,total/count)
            max_high_key_name = ""
            #Assigning check variable to bitcoin_name
            check = bitcoin_name
            max_high_value = float(Price)
            total = 0.0
            count = 0
            #increasing the count by one
        count = count + 1
        total = total + float(Price)
        #Checks price is greater than max_high_value
        if Price > max_high_value:
            max_high_value = float(Price)
            max_high_key_name = bitcoin_name 
#print the output
print "\n\nName of Bitcoin: {0}\t AVG high value: {1}\t".format(avg_bit_coin_name,avg_bitcoin_value)
write_file.write("\n\nName of Bitcoin: {0}\t AVG high value: {1}\t".format(avg_bit_coin_name,avg_bitcoin_value))
#Closing the read file
read_file.close()
#CLosing the written file
write_file.close()