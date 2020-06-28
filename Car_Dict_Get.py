import pickle

# 初始的算法测试代码
'''
MinCSpace = {}
MinCTime = {}
MinESpace = {}
MinETime = {}
with open("D:\\Python\\Datas\\Data_VLPR\\VLPR\\2015\\Bayonet20150801", encoding="utf-8") as f:
    MinCTime.setdefault("0801", {})
    MinCSpace.setdefault("0801", {})
    MinETime.setdefault("0801", {})
    MinESpace.setdefault("0801", {})
    for line in f:
        lines = line.split(",")
        if "闽C" in lines[8]:
            if lines[8] in MinCTime["0801"] and lines[10] in MinCTime["0801"][lines[8]]:
                continue
            else:
                MinCSpace["0801"].setdefault(lines[8], []).append(lines[6])
                MinCTime["0801"].setdefault(lines[8], []).append(lines[10])
        elif "闽E" in lines[8]:
            if lines[8] in MinETime["0801"] and lines[10] in MinETime["0801"][lines[8]]:
                continue
            else:
                MinESpace["0801"].setdefault(lines[8], []).append(lines[6])
                MinETime["0801"].setdefault(lines[8], []).append(lines[10])

print(MinCTime)
print(MinETime)


print(MinC)
with open("2015\\MinC.pkl", "wb") as f:
    pickle.dump(MinC, f, pickle.HIGHEST_PROTOCOL)
with open("2015\\MinD.pkl", "wb") as f:
    pickle.dump(MinD, f, pickle.HIGHEST_PROTOCOL)
with open("2015\\MinE.pkl", "wb") as f:
    pickle.dump(MinE, f, pickle.HIGHEST_PROTOCOL)
'''
path2015 = []
path2016 = []
# 读取地址 下面的两个txt应该是最初数据文件的地址
with open("Source2015.txt") as f:
    for line in f:
        path2015.append(line.replace("\n", ""))
with open("Source2016.txt") as f:
    for line in f:
        path2016.append(line.replace("\n", ""))

# 对每个数据处理，闽C、闽E三个月数据做一组，闽D每天一个单独数据
# 需求的部分变量
i = 0
MinCSpace = {}
MinCTime = {}
MinESpace = {}
MinETime = {}
MinDSpace = {}
MinDTime = {}

# 对2016年的闽D 时间空间处理，由于存储格式不同，与闽C 闽E 的处理分开，2015年处理同样修改相关文件名即可

i = 0
for file_path in path2016:
    date = file_path[-4:]
    new_path_space = "2016\\Space\\MinDSpace" + date + ".pkl"
    new_path_time = "2016\\Time\\MinDTime" + date + ".pkl"
    with open(file_path, encoding="utf-8") as file_obj:
        for line in file_obj:
            lines = line.split(",")
            if "闽D" in lines[8]:
                if lines[8] in MinDTime and lines[10] in MinDTime[lines[8]]:
                    continue
                else:
                    MinDSpace.setdefault(lines[8], []).append(lines[6])
                    MinDTime.setdefault(lines[8], []).append(lines[10])
    with open(new_path_space, "wb") as f:
        pickle.dump(MinDSpace, f, pickle.HIGHEST_PROTOCOL)
    with open(new_path_time, "wb") as f:
        pickle.dump(MinDTime, f, pickle.HIGHEST_PROTOCOL)
    MinDSpace.clear()
    MinDTime.clear()
    i += 1
    print(i)
print("End2")


# 20161030的文件编码异常，作为测试补充文件使用
'''
with open("D:\\Python\\Datas\\Data_VLPR\\VLPR\\2016\\Bayonet20161030", encoding="utf-8") as file_obj:
    for line in file_obj:
        lines = line.split(",")
        if "闽D" in lines[8]:
            if lines[8] in MinDTime and lines[10] in MinDTime[lines[8]]:
                continue
            else:
                MinDSpace.setdefault(lines[8], []).append(lines[6])
                MinDTime.setdefault(lines[8], []).append(lines[10])
with open("2016\\Space\\MinDSpace1030.pkl", "wb") as f:
    pickle.dump(MinDSpace, f, pickle.HIGHEST_PROTOCOL)
with open("2016\\Time\\MinDTime1030.pkl", "wb") as f:
    pickle.dump(MinDTime, f, pickle.HIGHEST_PROTOCOL)
MinDSpace.clear()
MinDTime.clear()

print("End2")
'''

# 对2016年的闽C 闽E的时间空间做处理，2015的话修改相关文件地址即可
for file_path in path2016:
    date = file_path[-4:]
    MinETime.setdefault(date, {})
    MinESpace.setdefault(date, {})
    MinCTime.setdefault(date, {})
    MinCSpace.setdefault(date, {})
    with open(file_path, encoding="utf-8") as file_obj:
        for line in file_obj:
            lines = line.split(",")
            if "闽C" in lines[8]:
                if lines[8] in MinCTime[date] and lines[10] in MinCTime[date][lines[8]]:
                    continue
                else:
                    MinCSpace[date].setdefault(lines[8], []).append(lines[6])
                    MinCTime[date].setdefault(lines[8], []).append(lines[10])
            elif "闽E" in lines[8]:
                if lines[8] in MinETime[date] and lines[10] in MinETime[date][lines[8]]:
                    continue
                else:
                    MinESpace[date].setdefault(lines[8], []).append(lines[6])
                    MinETime[date].setdefault(lines[8], []).append(lines[10])
    i = i + 1
    print(i)
print(len(MinESpace))
print(len(MinCSpace))
print(len(MinCTime))
print(len(MinETime))
with open("2016\\Space\\MinCSpace.pkl", "wb") as f:
    pickle.dump(MinCSpace, f, pickle.HIGHEST_PROTOCOL)
with open("2016\\Time\\MinCTime.pkl", "wb") as f:
    pickle.dump(MinCTime, f, pickle.HIGHEST_PROTOCOL)
with open("2016\\Space\\MinESpace.pkl", "wb") as f:
    pickle.dump(MinESpace, f, pickle.HIGHEST_PROTOCOL)
with open("2016\\Time\\MinETime.pkl", "wb") as f:
    pickle.dump(MinETime, f, pickle.HIGHEST_PROTOCOL)


