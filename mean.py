import csv
with open('Hieght-Weight.csv', newline='') as f:
    reader = csv.reader(f)
    file_Data =  list(reader)
file_Data.pop(0)

new_Data = []
for i in range (len (file_Data)):
    n = file_Data [i] [1]
    new_Data.append(float(n))

n_num = len(new_Data)
total = 0;

for x in new_Data :
    total +=x

mean = total / n_num
print(mean)