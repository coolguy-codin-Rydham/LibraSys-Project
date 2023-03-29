# file=open("rscbf.txt","r")
# li=file.readlines()
# strdicttobeused=li[0]
# dicttobeused=eval(strdicttobeused)
# print(strdicttobeused)
# print(type(strdicttobeused))
# a="hello"
# dicttobeused["abs"].append(a)
# print(dicttobeused)

# # print(type(dicttobeused))
# # sum1=dicttobeused["abs"]+dicttobeused["qw"]
# # print(sum1)
# # dicttobeused["huihui"]=9090
# # dicttobeused["hahah"]=7654
# # print(dicttobeused)
# # dicttobeused=str(dicttobeused)
# # file=open("rscbf.txt","w")#! if line 16 and 18 missed then new dic added not exixting changed
# # file.write("%s"%(dicttobeused))
# # file=open("rscbf.txt","r")
# # # a=str({"abc":123,"abgg":98765})
# # # print(type(a))
# # # b=eval(a)
# # # print(b)


# a={18:19,13:14}
# print(a[18])

li=[]
import time as t
import datetime as dt
curr=dt.datetime.now()
curr2=t.strftime("%d.%m.%y")
new=curr+dt.timedelta(days=30)
print(curr2 ,"\n",new)
li.append(curr)
print(li)
a=li[0]+dt.timedelta(days=37)
print(a)