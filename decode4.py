
# get inputs from terminal
def inputFromCmd():
    res = []
    while True:     # 接收输入的同时滤掉注释 和空行
        a = input()
        if a == "stop":
            break
        if ( not a.startswith('@') ) and ( not  a.isspace() ) and (a):
            res.append(a)
    return res


# decode eivironments
def decodeEnviro(code):
    print("===Decode EnvironmentSettings===")
    res = {}
    sign = 0
    for i in code:
        if i == ":setEnvironment":
            print("*find settings*")
            sign = 1
            continue
        elif i == "finish" and sign == 1:
            print("*end of environmentsetting*")
            sign = 0
            break

        if sign == 1:
            envir_pair = i.split('=')
            envir_name = envir_pair[0]
            envir_value = envir_pair[1]
            print("-set %s=%s" % (envir_name , envir_value))
            res[envir_name] = envir_value

    print("===Environment Decode Finish===\n")
    return res

def decodeSections(code):
    print("===Decode Section===")
	
    res = {}
    parts_name = ''
    sign = 0
    for i in code:
        # 控制sign来决定是否添加
        if i.startswith(':') and i.split('=')[0] == ":section":
            sign = 1
            parts_name = i.split('=')[1]	# get the name of a section
            print("*find a section named %s*" % parts_name)
            res[parts_name] = []
            continue
        elif i == "finish" and sign == 1:
            sign = 0
		
        if sign == 1:                   # 添加
            for j in i.split():
                res[parts_name].append(j)

    print("===Section Decode Finish===\n")
    return res

def decodeMainSheet(code):
    print("===Decode MainSheet===")

    res = []
    sign = 0
    for i in code:
        if i == ":main":
            print("*find mainsheet*")
            sign = 1
            continue
        elif i == "finish" and sign == 1:
            break

        if sign == 1:
            for j in i.split():
                res.append(j)
	
    print("===MainSheet Decode Finish===\n")
    return res


def basicDecode():
    print("=====Start Basci Decode=====")
    inputsWithRealCode = inputFromCmd()

    # envirs = {}
    envirs		= decodeEnviro(inputsWithRealCode)
    # sections = {'':[]}
    sections	= decodeSections(inputsWithRealCode)
    # main = []
    main		= decodeMainSheet(inputsWithRealCode)
	
    print("=====Basci Decode Finish=====\n")

    print(envirs)
    print(sections)
    print(main)
    print(inputsWithRealCode)
    return envirs , sections , main

if __name__ == "__main__":
    envirs , sections , main = basicDecode()
