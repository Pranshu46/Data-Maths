from collections import Counter
import csv
with open('Hieght-Weight.csv', newline='') as f:
    reader = csv.reader(f)
    file_Data = list(reader)
file_Data.pop(0)

new_Data = []
for i in range(len(file_Data)):
    n = file_Data[i][1]
    new_Data.append(float(n))

data = Counter(new_Data)
mode_data_for_range ={
    '50-60 ' :0 ,
    '60-70'  :0 ,
    '70-80'  :0 ,
}

for height, occurence in data.items():
    if 50 < float(height) < 60 :
        mode_data_for_range["50-60"] += occurence
    elif 60 < float(heigt) < 70 :
        mode_data_for_range["60-70"] += occurence
    elif 70 < float(heigt) < 80 :
        mode_data_for_range["70-80"] += occurence

mode_range,mode_occurence = 0,0
for range, occurence in mode_data_for_range.items():
    if occurence > mode_occurence:
        mode_range, mode_occurence = [int(range.split("-")[0]), int(range.split("-")[1])], occurence
mode = float((mode_range[0] + mode_range[1]) / 2)
print (mode)