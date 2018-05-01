
 # aftermapper_tarun file is opened with read permissions 
o = open("aftermapper_tarun.txt", "r")
# a file named sort_output with write permissions is created 
s = open("sort_output.txt", "w") 

# each line is read from o
lines = o.readlines() 

#all the lines are sorted with this sort() function
lines.sort() 
#all the lines are written into the file sort_output
for line in lines: 
  s.write(line)
 # file aftermapper_tarun.txt is closed 
o.close()
 # file sort_output.txt is closed
s.close()