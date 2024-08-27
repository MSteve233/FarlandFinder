import copy
from turtle import pos
MinNum=0
MaxNum=0
#初始化程序
MinNum=int(input("最小边界值:"))
MaxNum=int(input("最大边界值:"))
while True:
    Posi=(MinNum+MaxNum)//2#计算坐标值
    BorS=input(f"{Posi}，大(b)还是小(s)?:")
    if BorS == "b":
        MaxNum=copy.deepcopy(Posi)
    else:
        MinNum=copy.deepcopy(Posi)