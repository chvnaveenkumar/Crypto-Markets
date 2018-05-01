# opening the file sort data with reading access
open_sort_output = open("sort_data.txt","r")
# opening reducer output file with writing access
write_reducer_output = open("reducer_outputInExcel.csv", "w")
# initializing current key to an empty string which can varied upon every type of crypto key
currentKey = ""
write_reducer_output.write('BitCoin Name:,Difference bwn Avg of Open and close value: '+"\n");
# initializing the opening value, count, closing value list to nothing
sum_open_value = 0.0
count = 0
close_valuelsit =[]
sum_close_value = 0.0
# traversing through all the elements of the data and filtering the data as per the requirement.
for line in open_sort_output:
  dataList = line.strip().split('\t')
  bitcoin_Name, open_value,close_value = dataList
# checking the bitcoin name and current key of the verification 
  if bitcoin_Name != currentKey:
    # writing the onto the output file
    if currentKey:      
      write_reducer_output.write(currentKey + ',' + str((sum_open_value/count)-(sum_close_value/count))+'\n')
      # initializing the values to default values once done with a type of currency
    currentKey = bitcoin_Name
    sum_open_value = 0.0
    sum_close_value = 0.0
    count = 0
  # adding the values of opening and closing
  sum_open_value += float(open_value)
  sum_close_value += float(close_value)
  count += 1
  # writing the final outcome to the output file
# write_reducer_output.write('BitCoin Name: ,' + 'Avg of Open value:,'+'Avg of close value: '+'\n')  
write_reducer_output.write(currentKey + ',' + str(sum_open_value/count) +','+str(sum_close_value/count)+'\n')
# closing the opened files.
open_sort_output.close()
write_reducer_output.close()