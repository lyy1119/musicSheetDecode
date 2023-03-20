C = [-6 , 1 , 8]
D = [-5 , 2 , 9]
E = [-4 , 3 , 10]
F = [-3 , 4 , 11]
G = [-2 , 5 , 12]
A = [-1 , 6 , 13]
B = [0 , 7 , 14]
spare = 15

trans = {}
trans["C"] = C
trans["D"] = D
trans["E"] = E
trans["F"] = F
trans["G"] = G
trans["A"] = A
trans["B"] = B


times = 1


def Inputs():
    text = ''
    while True:
        a = input()
        if a == "stop":
            break
        text = text + ' ' +a.split(';')[0]
    return text 

def numOfSoundTrack(lists):
    res = 0
    for i in lists:
        num = len(i.split("&"))
        if res < num:
            res = num
    return res


def _decode(strs):  # 接受一个str
    #返回一个 list 子解析 解析一个最小单元  #+C*4
    """
    先解析 #
    再解析 -+
    再解析 C*4
    """

    res = []
    lens = len(strs.split("#"))

    
    addtion = 0

    # 解析#号
    if lens == 2:    #说明有#号
        addtion = 0.5
        str1 = strs.split("#")[1]
    else :
        str1 = strs

    #解析 - +
    lenA = len(str1.split("-"))
    lenB = len(str1.split("+"))

    if lenA == 2:   # 说明有 - 号
        address = 0
        str2 = str1.split("-")[1]
    elif lenB == 2: # 说明有 + 号
        address = 2
        str2 = str1.split("+")[1]
    else :          # 说明无-+号
        address = 1
        str2 = str1

    # 解析 C*4
    # 检查有没有*号
    lenM = len(str2.split("*"))

    if lenM == 2:   #说明有*号
        sign = str2.split("*")[0]       # 音符
        num0 = float(str2.split("*")[1])   # 次数
        # 生成
        # for t in range(times):
        num = int(num0 * times)
        while num:
            #
            if sign == '0':
                res.append(spare)
            else:
                res.append(trans[sign][address]+addtion)    #加入
            num = num - 1
    else:
        #
        for t in range(times):
            if str2 == '0':
                    res.append(spare)
            else:
                res.append(trans[str2][address]+addtion)
    
    return res

def __decode(lists):
    # 处理 多声道 , 多声道表现为list下的一个多元素list
    res = []
    for i in lists:
        for j in _decode(i):
            res.append(j)
    return res



def decode(lists):
    """
    rules:
    C D E F G A B  (必须大写)

    C 代表 1      B 代表 7 

    - 代表低音     + 代表高音

    +C*4 代表高音do 四拍    1 - - -

    #+C*4 代表 升调do 四拍  

    使用&表示同时演奏


    使用; 来分割输入行

    使用空格来分开不同音符

    示例 : "#+C*4 -D #f;"  -> | #+1 - - - | -1 4 |
    """

    # 处理最大复合单元 #F&#C
    res = []
    for i in lists:     #i 是一个str
        sonlist = i.split("&")      # 已经将多声道分开了    sonlist是一个列表
        lens = len(sonlist)
        if lens == 1:
            for k in _decode(sonlist[0]):
                res.append(k)
        else:
            res.append(__decode(sonlist))
    return res


def finalMake(lists , soundtrackNum):
    res = []
    # 初始化
    for i in range(soundtrackNum):
        res.append([])

    for i in lists:
        if type(i) == list:
            add = 0
            k = 0
            for j , k in zip(i , range(soundtrackNum)):
                res[k].append(j)
            for k in range(k , soundtrackNum):
                res[k].append(0)
        else:
            for k in range(soundtrackNum):
                res[k].append(i)
    
    return res
    # 开始正式生成
    
def soundWordDecode():
    text = Inputs()     #简单解析输入
    lists = text.split()    #解析成列表
    soundtrack_num = numOfSoundTrack(lists) #声道数
    print(soundtrack_num)
    final = decode(lists)
    print(final)
    res = finalMake(final , soundtrack_num)
    return res
    # print(res)

def read_jiepai():
    config = input()
    global times
    times = int(config.split("=")[1])


def OutPut(lists):
    for i in lists:
        print(i)
        print(len(i))

if __name__ == "__main__":
    read_jiepai()
    res = soundWordDecode()
    OutPut(res)



    