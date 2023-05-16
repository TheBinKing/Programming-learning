import numpy
import time
l = []
sl = set()
dl = dict()
r = numpy.random.randint(0, 1000000, 100000)
for i in range(0, 100000):
    l.append(r[i])
    sl.add(r[i])
    dl.setdefault(r[i], 1)
    

#计算通过set来查找的效率
start = time.clock()
for i in range(100000):
    t = i in sl
end = time.clock()
print("time of set is %.5f" % float(end-start))

#计算通过dict的效率
start = time.clock()
for i in range(100000):
    t = i in dl
end = time.clock()
print("time of dict is %.5f" % float(end-start))
#计算通过list的效率
start = time.clock()
for i in range(100000):
    t = i in l
end = time.clock()
print("time of list is %.5f" % float(end-start))