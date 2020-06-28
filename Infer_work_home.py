import pickle
import time


def High_p_creat_forCE(addr: str, k):
    with open(addr, "rb") as f:
        temp = pickle.load(f)
    old = "08"
    count = {}
    Highp = {}
    for i in temp:
        # print(i)
        if i[0:2] == "08" and old == "08":
            for j in temp[i]:
                if k >= len(temp[i][j]) >= 9:
                    if j not in count:
                        count[j] = 1
                    else:
                        count[j] = count[j] + 1
        elif i[0:2] == "09" and old == "08":
            for j in count:
                if count[j] >= 10:
                    Highp[j] = 1
            print(count)
            old = "09"
            count.clear()
            for j in temp[i]:
                if k >= len(temp[i][j]) >= 9:
                    if j not in count:
                        count[j] = 1
                    else:
                        count[j] = count[j] + 1
        elif i[0:2] == "09" and old == "09":
            for j in temp[i]:
                if k >= len(temp[i][j]) >= 9:
                    if j not in count:
                        count[j] = 1
                    else:
                        count[j] = count[j] + 1
        elif i[0:2] == "10" and old == "09":
            for j in count:
                if count[j] >= 10:
                    Highp[j] = 1
            print(count)
            old = "10"
            count.clear()
            for j in temp[i]:
                if k >= len(temp[i][j]) >= 9:
                    if j not in count:
                        count[j] = 1
                    else:
                        count[j] = count[j] + 1
        elif i[0:2] == "10" and old == "10":
            for j in temp[i]:
                if k >= len(temp[i][j]) >= 9:
                    if j not in count:
                        count[j] = 1
                    else:
                        count[j] = count[j] + 1
    for j in count:
        if count[j] >= 10:
            Highp[j] = 1

    f1 = open(addr[0:5] + "\\" + addr[11:15] + "HighP.txt", "w")
    for i in Highp:
        f1.write(i + "\n")
    f1.close()


def High_p_creat_forD(addr: str, k):
    path = []
    count = {}
    Highp = {}
    days = [31, 30, 31]
    with open(addr) as f:
        for lines in f:
            path.append(lines.replace("\n", ""))
    path_count = 0
    for i in days:
        for i1 in range(i):
            with open(path[path_count], "rb") as f:
                temp = pickle.load(f)
            print(path[path_count])
            path_count = path_count + 1
            for m in temp:
                if k >= len(temp[m]) >= 9:
                    if m in count:
                        count[m] = count[m] + 1
                    else:
                        count[m] = 1
        for j in count:
            if count[j] >= 10:
                Highp[j] = 1
        print(len(Highp))
        count.clear()
        print("END")
    f1 = open(addr[0:4] + "\\MinDHighP.txt", "w")
    for i in Highp:
        f1.write(i + "\n")
    f1.close()


# 0是时间 1是设备号 返回推断的内容
def longest_time(lists: list):
    temp_list = sorted(lists, key=lambda x: x[0])
    maxs = 0
    work = 0
    flags = 0
    home = 0
    length = len(temp_list)
    for i in range(1, length):
        temps = time.localtime(int(temp_list[i][0]))
        if temps.tm_hour < 7 or temps.tm_hour > 22:
            continue
        elif flags == 0:
            home = i
            flags = 1
        elif int(temp_list[i][0]) - int(temp_list[i-1][0]) > maxs:
            maxs = int(temp_list[i][0]) - int(temp_list[i-1][0])
            work = i
    return [temp_list[home][0], temp_list[home][1], temp_list[work-1][0], temp_list[work][1]]


def str2time(times: str):
    temp_time = int(times)
    timestramps = time.localtime(temp_time)
    return timestramps.tm_hour*60*60 + timestramps.tm_min*60 + timestramps.tm_sec


def infer_forCE(year, dicts: dict, city):
    infer_C = {}
    count_C = {}
    # 下面的是存储高频车的txt文件地址
    with open(str(year) + "\\Min" + city + "HighP.txt") as f:
        for line in f:
            lines = line.replace("\n", "")
            infer_C.setdefault(lines, [0, 0, 0, 0])
            count_C.setdefault(lines, [])
            count_C[lines].append({})
            count_C[lines].append({})
    # 下面的是闽C和闽E的车辆记录pkl文件
    caddrS = str(year) + "\\Space\\Min" + city + "Space.pkl"
    caddrT = str(year) + "\\Time\\Min" + city + "Time.pkl"
    with open(caddrS, "rb") as f:
        Cs = pickle.load(f)
    with open(caddrT, "rb") as f:
        Ct = pickle.load(f)
    # 调试用print("End1")
    for day in Cs:
        for car in infer_C:
            if car not in Cs[day]:
                continue
            # temp是对车辆记录的处理
            temp = []
            for i in range(len(Cs[day][car])):
                temp.append([])
                temp[-1].append(Ct[day][car][i])
                temp[-1].append(Cs[day][car][i])
            temps = longest_time(temp)
            count_C[car][0].setdefault(temps[1], [0, 0])
            count_C[car][1].setdefault(temps[3], [0, 0])
            if count_C[car][0][temps[1]][0] != 0:
                sums = count_C[car][0][temps[1]][1] * count_C[car][0][temps[1]][0]
                count_C[car][0][temps[1]][0] = count_C[car][0][temps[1]][0] + 1
                count_C[car][0][temps[1]][1] = (sums + str2time(temps[0])) // count_C[car][0][temps[1]][0]
            else:
                count_C[car][0][temps[1]][0] = 1
                count_C[car][0][temps[1]][1] = str2time(temps[0])

            if count_C[car][1][temps[3]][0] != 0:
                sums = count_C[car][1][temps[3]][1] * count_C[car][1][temps[3]][0]
                count_C[car][1][temps[3]][0] = count_C[car][1][temps[3]][0] + 1
                count_C[car][1][temps[3]][1] = (sums + str2time(temps[2])) // count_C[car][1][temps[3]][0]
            else:
                count_C[car][1][temps[3]][0] = 1
                count_C[car][1][temps[3]][1] = str2time(temps[2])
        print(day)
    for i in list(infer_C.keys()):
        infer_C[i][0] = max(count_C[i][0], key=lambda x: x[0])
        infer_C[i][1] = count_C[i][0][infer_C[i][0]][1]
        infer_C[i][2] = max(count_C[i][1], key=lambda x: x[0])
        infer_C[i][3] = count_C[i][1][infer_C[i][2]][1]
        if infer_C[i][0] == infer_C[i][2] or infer_C[i][3] <= infer_C[i][1]:
            infer_C.pop(i)
    dicts.update(infer_C)
    Cs.clear()
    Ct.clear()
    return dicts


def infer_forD(year, dicts: dict):
    infer_D = {}
    count_D = {}
    with open(str(year) + "\\MinDHighP.txt") as f:
        for line in f:
            lines = line.replace("\n", "")
            infer_D.setdefault(lines, [0, 0, 0, 0])
            count_D.setdefault(lines, [])
            count_D[lines].append({})
            count_D[lines].append({})
    caddrS = str(year) + "XiamenSourceS.txt"
    caddrT = str(year) + "XiamenSourceT.txt"
    daddrs = []
    daddrt = []
    with open(caddrS) as f:
        for lines in f:
            daddrs.append(lines.replace("\n", ""))
    with open(caddrT) as f:
        for lines in f:
            daddrt.append(lines.replace("\n", ""))
    # 测试用print("End")
    for addrs, addrt in zip(daddrs, daddrt):
        print(addrs)
        with open(addrs, "rb") as f:
            Ds = pickle.load(f)
        with open(addrt, "rb") as f:
            Dt = pickle.load(f)
        for car in infer_D:
            if car not in Ds:
                continue
            temp = []
            for i in range(len(Ds[car])):
                temp.append([])
                temp[-1].append(Dt[car][i])
                temp[-1].append(Ds[car][i])
            temps = longest_time(temp)
            count_D[car][0].setdefault(temps[1], [0, 0])
            count_D[car][1].setdefault(temps[3], [0, 0])
            if count_D[car][0][temps[1]][0] != 0:
                sums = count_D[car][0][temps[1]][1] * count_D[car][0][temps[1]][0]
                count_D[car][0][temps[1]][0] = count_D[car][0][temps[1]][0] + 1
                count_D[car][0][temps[1]][1] = (sums + str2time(temps[0])) // count_D[car][0][temps[1]][0]
            else:
                count_D[car][0][temps[1]][0] = 1
                count_D[car][0][temps[1]][1] = str2time(temps[0])

            if count_D[car][1][temps[3]][0] != 0:
                sums = count_D[car][1][temps[3]][1] * count_D[car][1][temps[3]][0]
                count_D[car][1][temps[3]][0] = count_D[car][1][temps[3]][0] + 1
                count_D[car][1][temps[3]][1] = (sums + str2time(temps[2])) // count_D[car][1][temps[3]][0]
            else:
                count_D[car][1][temps[3]][0] = 1
                count_D[car][1][temps[3]][1] = str2time(temps[2])
        Ds.clear()
        Dt.clear()
    for i in list(infer_D.keys()):
        infer_D[i][0] = max(count_D[i][0], key=lambda x: x[0])
        infer_D[i][1] = count_D[i][0][infer_D[i][0]][1]
        infer_D[i][2] = max(count_D[i][1], key=lambda x: x[0])
        infer_D[i][3] = count_D[i][1][infer_D[i][2]][1]
        if infer_D[i][0] == infer_D[i][2] or infer_D[i][3] <= infer_D[i][1]:
            infer_D.pop(i)
    dicts.update(infer_D)
    return dicts


year = [2015, 2016]
for i in year:
    test = {}
    infer_forD(i, test)
    infer_forCE(i, test, "C")
    infer_forCE(i, test, "E")
    print(len(test))
    print(test)
    with open(str(i) + "\\Infer.pkl", "wb") as f:
        pickle.dump(test, f, pickle.HIGHEST_PROTOCOL)

