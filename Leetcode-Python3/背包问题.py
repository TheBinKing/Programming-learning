


W = [2,3,4,5] #物品重量（前面的0是为了从0递推）
V = [3,4,5,6] #物品价值 （前面的0是为了从0递推）

n = 4 #物品数量
c = 8 # 背包的总载重量

def pakage_normal(n,b,W,V):
    pakage=[]
    for i in range(n):
        _temp=[]
        for j in range(b+1):
            _temp.append(0)
        pakage.append(_temp)
    for i in range(n):
        for j in range(1,b+1):
            if j < W[i]:
                pakage[i][j]=pakage[i-1][j]
            else:
                pakage[i][j]=max(pakage[i-1][j],pakage[i-1][j-W[i]]+V[i])
    return pakage

print (pakage_normal(n,c,W,V))



