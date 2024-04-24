f = open("/Users/kingson/Downloads/fall_2023/CS350/hw1/hw1_src/src/build/server-output.txt")
data = f.read().split("\n")[2:]
data = data[0:500]
modified_data = []
for i in data:
  modified_data += [i.split(",")]

for i in range(len(modified_data)):
  for j in range(1, len(modified_data[0])):
    modified_data[i][j] = float(modified_data[i][j])
print(modified_data[0])

sum = 0
for i in modified_data:
  sum += i[1]

print(sum)