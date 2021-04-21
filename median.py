import csv
with open('Hieght-Weight.csv', newline='') as f:
    reader = csv.reader(f)
    file_Data = list(reader)
file_Data.pop(0)

new_Data = []
for i in range(len(file_Data)):
    n = file_Data[i][1]
    new_Data.append(float(n))


n = len(new_Data)
new_Data.sort()
if n % 2 == 0:
    median1 = float(new_Data[n//2])
    median2 = float(new_Data[n//2-1])
    median = (median1 + median2)/2

else:
    median = new_Data[n//2]

print(median)