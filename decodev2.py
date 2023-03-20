
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

sectors = 1

# 输入      区分乐谱和  子乐谱等
# 在这个函数里   区分模块乐谱和多声部乐谱
def inputs():
    res = []
    temp1 = []
    enviro = {}
    parts = {}
    while True:     # 先过滤掉注释 和空行
        a = input()
        if a == "stop":
            break
        if ( not a.startswith('!') ) and ( not  a.isspace() ) and (a):
            temp1.append(a)
    
    # print("去掉注释")
    # print(temp1)
    
    # 处理环境
    sign = 0
    for i in temp1:
        if i == ":setEnvironment":
            sign = 1
            continue
        elif i == "finish":
            sign = 0
            break

        if sign == 1:
            # print(i)
            # print(i.split('='))
            enviro[i.split('=')[0]] = i.split('=')[1]

    # 处理段落
    parts_name = ''
    for i in temp1:
        # 控制sign来决定是否添加
        if i.startswith(':') and i.split('=')[0] == ":create":
            sign = 1
            parts_name = i.split('=')[1]
            parts[parts_name] = []
            continue
        elif i == "finish":
            sign = 0

        if sign == 1:                   # 添加
            for j in i.split():
                parts[parts_name].append(j)


    # 处理主谱
    main_name = 0
    for i in temp1:
        if i.startswith('-') and i.split('=')[0] == "-main":
            sign = 1
            main_name = int(i.split('=')[1])    #获取序号
            res.append([])
            continue
        elif i == "finish":
            sign = 0

        if sign == 1:
            for j in i.split():
                res[main_name].append(j)

         
    return res , enviro , parts
    # return temp1



# 解析最小单元   返回一个 list  这个list需要处理成多个字符  不能直接用
def minimum_decode(strs):  # 接受一个str
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

    # 解析 C*4              这个功能需要砍掉 因为不需要在这里解析
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


# 最大解析   解析输入的最初乐谱  解析成多段格式化的乐谱以方便解析   
# 返回一个以list为子元素的list
# 在这个函数里先解析*这种符号
# 将模块化的章节放入
def maxmum_decode(lists , parts):    # 将乐谱拆分 parts是子段落 用于解释标识符
    #在这里先把*号去除掉
    pass

# 解析函数
def decode():
    pass

def printRes(lists):
    pass


if __name__ == "__main__":
    main , envir , parts = inputs()
    print(main)
    print(envir)
    print(parts)
    # print(inputs())
    for i in main:
        maxmum_decode(i)