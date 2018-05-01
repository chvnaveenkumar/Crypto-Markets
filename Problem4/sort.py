open_file = open("mapper_gopi.txt", "r")
sort_output = open("sort_data.txt", "w")

lines = open_file.readlines()
lines.sort()

for line in lines:
  sort_output.write(line)

open_file.close()
sort_output.close()