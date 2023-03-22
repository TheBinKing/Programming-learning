
#乱序字符串数是指一个字符串的重新排列,
#eg:python ypthon

def find_ruanxu_str(string1,string2):
    dic={}
    for i in string1:
        if dic.get(i):
            dic[i]+=1
        else:
            dic[i]=1
    for i in string2:
        if dic.get(i):
            dic[i]-=1
        else:
            return False


