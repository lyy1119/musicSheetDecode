
import time
    # ---   --   -        +    ++   +++
C = [-20 , -13 , -6 , 1 , 8 , 15 , 22]
D = [-19 , -12 , -5 , 2 , 9 , 16 , 23]
E = [-18 , -11 , -4 , 3 , 10 , 17 , 24]
F = [-17 , -10 , -3 , 4 , 11 , 18 , 25]
G = [-16 , -9 , -2 , 5 , 12 , 19 , 26]
A = [-15 , -8 , -1 , 6 , 13 , 20 , 27]
B = [-14 , -7 , 0 , 7 , 14 , 21 , 28]
spare = 29

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

def count_num(astr , tarCh):
    res = 0
    for i in astr:
        if i == tarCh:
            res = res + 1
    return res

# 解析最小单元   返回一个 list  这个list需要处理成多个字符  不能直接用
def minimum_decode(strs):  # 接受一个str
    #返回一个 list 子解析 解析一个最小单元  #+C*4
    """
    先解析 #
    再解析 -+
    再解析 C*4
    """

    res = ''
    # lens = len(strs.split("#"))

    
    addtion = 0

    # 解析#号
    if '#' in strs:    #说明有#号
        # print("有#号")
        addtion = 0.5
        str1 = strs.split("#")[1]
    else :
        str1 = strs

    #解析 - +
    lenA = len(str1.split("-"))
    lenB = len(str1.split("+"))
    puls_num = 0
    minu_num = 0

    puls_num = count_num(str1 , '+')
    minu_num = count_num(str1 , '-')

    if puls_num != 0:
        address = puls_num + 3
        str2 = str1.split("+")[puls_num]
    elif minu_num != 0:
        str2 = str1.split("-")[minu_num]
        address = 3 - minu_num
    else:
        address = 3
        str2 = str1




    # 解析 C*4              这个功能需要砍掉 因为不需要在这里解析
    if str2 == '0':
            res = spare
    else:
        res = trans[str2][address]+addtion
        # print(res)
    
    return res


# 最大解析   解析输入的最初乐谱  解析成多段格式化的乐谱以方便解析   
# 返回一个以list为子元素的list
# 在这个函数里先解析*这种符号
# 将模块化的章节放入
def maxmum_decode(alist):    # 将乐谱拆分
    res = []
    temp1 = []
    # 在这里先把*号去除掉

    # 先切分放到一个temple中
    for i in alist:
        if len(i.split('*')) == 1:
            temp1.append([i , 1])
        else:
            temp1.append([i.split('*')[0] , i.split('*')[1]])
    # 现在 存储格式为 [符号 , 次数]
    # 查找最小的次数
    min = 1
    for i in temp1:
        if float(i[1]) < min:
            min = float(i[1])
    
    # 已经找到最小的数
    print(min)
    global times
    if times < int(1/min):
        times = int(1/min)

    for i in temp1:
        i[1] = float(i[1]) * times


    # print(temp1)



    
    for i in temp1:
        for j in range(int(i[1])):
            res.append(i[0])

    return res  


def sign_decode(alist , parts):  # 解释特殊标识符
    res = []
    for i in alist:
        res.append(i)
        if i.startswith('='):   # =开头表示模块化乐谱
            res.remove(i)
            res.extend(parts[i.split('=')[1]])

    return res


def decode_and(alist):
    temp = []
    for i in alist:
        if '&' in i:
            temp.append(i.split('&'))
        else:
            temp.append(i)
    
    maxlength = 0
    for i in temp:
        if type(i) == str:
            if maxlength < 1:
                maxlength = 1
        else:
            if len(i) > maxlength:
                maxlength = len(i)
    
    # print(maxlength)
    res = []
    for i in range(maxlength):
        res.append([])

    for i in temp:
        if type(i) == str:
            for j in range(maxlength):
                res[j].append(i)
        elif type(i) == list:
            length = len(i)
            for j in range(length):
                res[j].append(i[j])
            for j in range(length , maxlength):
                res[j].append('0')
    
    return res




# 解析函数
def decode():
    pass


def PrintSoundTrack(lists):
    address = 1
    for i in lists:
        print("soundTrack%d = " % address, end='')
        print(i)
        address = address + 1

def SaveSoundTrack(lists , enviro):
    with open("output" , "w") as f:
        # 输出基本信息
        f.write("生成时间:\t%s\n" % time.asctime())
        if "speed" in enviro.keys():
            # 如果环境变量中有speed
            f.write("乐谱速度:\t%d\n" % (int(enviro["speed"])*times))
            f.write("(原速度:\t%s)\n" % enviro["speed"])
        else:
            f.write("速度倍数:\t%d\n" % times)
            
        f.write("\n")

        address = 1
        for i in lists:
            f.write("soundTrack%d = " % address)
            # f.write(i)
            f.write('[')
            for j in i:
                f.write("%.1f," % j)
            f.write(']')
            f.write('\n')
            address = address + 1



if __name__ == "__main__":

    # 输入
    main , envir , parts = inputs()

    # ==============处理结构化乐谱 循环解释获得结构化的乐谱的真实内容=========
    # 处理parts
    for i in parts.keys():
        parts[i] = maxmum_decode(parts[i])
    # 循环解释part
    for i in parts.keys():
        parts[i] = sign_decode(parts[i] , parts)
    # ===================================================================



    # ====================循环解释main 将main中的parts展开=================
    # 先解析* 再解析parts
    sign_decoded_main = []
    for i in main:
        sign_decoded_main.append(sign_decode(maxmum_decode(i) , parts))
    # print(sign_decoded_main)
    # ====================================================================
    

    # =======================生成纯字符的谱子 将&符号解析=====================
    base_sign_main_pre = []
    for i in sign_decoded_main:
        base_sign_main_pre.append(decode_and(i))
    # 整理谱子
    base_sign_main = []
    for i in base_sign_main_pre:
        if type(i) == list:
            for j in i :
                base_sign_main.append(j)
    # ==================================================================== 

    # =======================生成由数字构成的声道============================
    soundtracks = []
    address = 0
    for i in base_sign_main:
        soundtracks.append([])
        for j in i:
            # print(minimum_decode(j))
            soundtracks[address].append(minimum_decode(j))
        address = address + 1
    # ====================================================================



    # =========================环境变量控制================================
    if "print_on_cmd" in envir.keys():
        if int(envir["print_on_cmd"]) != 0:
            PrintSoundTrack(soundtracks)
    if "output_off" in envir.keys():
        if int(envir["output_off"]) != 0:
            pass
    else:
        SaveSoundTrack(soundtracks , envir)
    # ==================================================================
