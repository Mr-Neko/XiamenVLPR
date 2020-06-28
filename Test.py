import pickle
import time
import datetime
import xlrd
import xlwt
'''
timestamp = 1438432280
timeArray = time.localtime(timestamp)
print(type(timeArray))
print(timeArray.tm_min)

'''

'''
def longest_time(lists: list):
    temp_list = sorted(lists, key=lambda x: x[0])
    maxs = 0
    work = 0
    flags = 0
    home = 0
    length = len(temp_list)
    print(temp_list)
    for i in range(1, length):
        temps = time.localtime(int(temp_list[i][0]))
        if temps.tm_hour < 7:
            continue
        elif flags == 0:
            home = i
            flags = 1
        elif int(temp_list[i][0]) - int(temp_list[i-1][0]) > maxs:
            maxs = int(temp_list[i][0]) - int(temp_list[i-1][0])
            work = i
            print(work)
    print(maxs)
    print(temp_list[home][0], temp_list[work][0])
    return [temp_list[home][1], temp_list[work][1]]


with open("2015\\Time\\MinETime.pkl", "rb") as f:
    temps = pickle.load(f)
with open("2015\\Space\\MinESpace.pkl", "rb") as f:
    tempt = pickle.load(f)

temp = []
for i in range(len(temps["0801"]["闽EFH388"])):
    temp.append([])
    temp[-1].append(temps["0801"]["闽EFH388"][i])
    temp[-1].append(tempt["0801"]["闽EFH388"][i])

print(longest_time(temp))
MinDTime = {}
with open("D:\\Python\\Datas\\Data_VLPR\\VLPR\\2016\\Bayonet20161021", encoding="utf-8") as file_obj:
    for line in file_obj:
        lines = line.split(",")
        if "闽D" in lines[8]:
            continue
        else:
            if lines[8] in MinDTime:
                continue
            else:
                MinDTime.setdefault(lines[8], [])
print(len(MinDTime))
'''

'''
with open("2016\\Infer.pkl", 'rb') as f:
    test = pickle.load(f)
print(len(test))
for i in list(test.keys()):
    if test[i][1] < 25200 or test[i][1] > 34200 or test[i][3] < 61200 or test[i][3] > 72000:
        test.pop(i)

print(test)
print(len(test))

with open("2016\\InferTest.pkl", "wb") as f:
    pickle.dump(test, f, pickle.HIGHEST_PROTOCOL)
'''
with open("2016\\InferTest.pkl", "rb") as f:
    test = pickle.load(f)

sheet = dict()
workbook = xlrd.open_workbook("所有设备信息.xls")
worksheet = workbook.sheet_by_index(0)
row = worksheet.nrows
equipment = []
for i in range(1, row):
    equipment.append(worksheet.row_values(i)[1])
    sheet[worksheet.row_values(i)[1]] = [worksheet.row_values(i)[3], worksheet.row_values(i)[4]]
key = list(test.keys())

book = xlwt.Workbook(encoding="utf-8", style_compression=0)
sheets1 = book.add_sheet('home', cell_overwrite_ok=True)
sheets2 = book.add_sheet('work', cell_overwrite_ok=True)
for i in range(len(test)):
    home = test[key[i]][0]
    work = test[key[i]][2]
    sheets1.write(i, 0, sheet[home][0])
    sheets1.write(i, 1, sheet[home][1])
    sheets2.write(i, 0, sheet[work][0])
    sheets2.write(i, 1, sheet[work][1])

book.save("Infer_Position.xls")





