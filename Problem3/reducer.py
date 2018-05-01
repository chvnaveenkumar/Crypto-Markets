#Reading the content of the file
s = open_sort_output = open("sort_output.txt","r")
r = write_reducer_output = open("reducer_output.txt", "w")
f = open("final_OP.csv", "w")

#initialiastion
thisKey = ""
thisMaxCounter = 0.0

#for loop to refine the data by removing the extra spaces 
for line in s:
  data = line.strip().split('\t')

#assigning the values to crypto_name and open values 
  crypto_name,openVal = data

  if thisKey != crypto_name:
    if thisKey != '':
      # output the last key value pair result
      r.write(thisKey + '\t' + str(thisMaxCounter)+'\n')

    # start over when changing keys
    thisKey = crypto_name 
    thisMaxCounter = 0
  
  # apply the aggregation function
  #print(str(openVal) + "---" +str(thisMaxCounter)+"-----"+ str(openVal  > thisMaxCounter))
  if float(openVal) > thisMaxCounter:
    thisMaxCounter = float(openVal)

# output the final entry when done
if float(openVal) > thisMaxCounter:
    thisMaxCounter = float(openVal)
r.write(thisKey + '\t' + str(thisMaxCounter)+'\n')

s.close()
r.close()