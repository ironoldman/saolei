# -*- coding:utf8 -*-
#测试扫雷
from Tkinter import *
from tkinter import messagebox
from tkinter import ttk
import copy
import random
import time


class saolei(object):

    # 初始化各个按钮，设计两个list来存放格子数据与按钮对象
    # self.boxList 用来存放格子数据，比如坐标，是否为雷或数字，是否已经翻开或标旗
    # self.buttonList 依次用来存放按钮对象
    def __init__(self):
        self.first_click = 1
        self.lattice_number = 480
        self.boom_number = 99
        self.total_b_number = 99]

            self.redFlag_list =[]


            self.neighbor_list = self.cpt8x(self.boxList[arg1])
            #print self.neighbor_list
            for i in self.neighbor_list:
                if self.boxList[i]['status'] == 1:
                    self.redFlag_list.append(i)
            if self.sef_nbr == len(self.redFlag_list):
                for i in self.redFlag_list:
                    if self.boxList[i]['role'] != 9:
                        self.over()
                list3 = list(set(self.neighbor_list) - set(self.redFlag_list))
                for i in list3:
                    if self.boxList[i]['role'] == 0:
                        self.blank8x(self.boxList[i])

                    else:
                        self.buttonList[i].configure(image = self.img,bg = 'LightSkyBlue',)
                        self.buttonList[i].configure(bg = 'gray',text=self.boxList[i]['role'],font=("黑体", 12, "bold"),bd =1,fg = 'black',compound='center')
                        self.boxList[i]['status'] =0
        if self.boom_number == 0:
            self.win()

    #右键事件函数
    def right_hander(self,ev,arg1):

        if self.boxList[arg1]['status'] == 3:
            self.buttonList[arg1].configure(image = self.img2,bg = 'LightSkyBlue',compound ='center')
            self.boxList[arg1]['status'] = 1
            self.boom_number = self.boom_number -1
            self.leishu_s.configure(text = self.boom_number)
            #print self.boom_number



        elif self.boxList[arg1]['status'] == 2:
            self.buttonList[arg1].configure(image = self.img,bg = 'LightSkyBlue')
            self.boxList[arg1]['status'] =3


        elif self.boxList[arg1]['status'] == 1:
            self.buttonList[arg1].configure(image = self.img_wh,compound = 'center')
            self.boxList[arg1]['status'] = 2
            self.boom_number = self.boom_number + 1
            self.leishu_s.configure(text = self.boom_number)
            #print self.boom_number

        if self.boom_number == 0:
            self.win()

    #结束函数
    def over(self,ev = None):
        for i in range(0,len(self.buttonList)):
            if self.boxList[i]['role'] == 9:
                self.buttonList[i].configure(image = self.img_lei,compound ='center')
        messagebox.askokcancel('pt','game over!!')
        self.slfm.quit()

    #胜利函数，总格子数减去雷数如果等于翻开的格子数。就胜利了。
    def win(self,ev = None):
        open_number = 0
        for i in self.boxList:
            if i['status'] == 0:
                open_number = open_number + 1

        if open_number == self.lattice_number - self.total_b_number:
            messagebox.askokcancel('pt','you win!!')
            self.slfm.quit()


    #布雷函数，产生X,Y轴坐标随机数，生成雷，
    def radm_boom(self,nbr,first_blank_list):
        n = 0
        while n < nbr:
            cot = 0
            rx = random.randint(0,15)
            ry = random.randint(0,29)
            #print rx,ry
            cot = rx * 30 + ry
            #print cot
            #print len(self.boxList)
            if self.boxList[cot]['role'] != 9 and cot not in first_blank_list:
                n = n +1
                self.boxList[cot]['role'] = 9


    #调试用，如果发现有问题，固定游戏数据，按照列表方式布雷
    # def radm_boom(self,nbr,c):
    #     for i in range(0,480):
    #         if aaa.testNumber[i] == 9:
    #             self.boxList[i]['role'] = 9

    #此函数用于布完雷后生成雷边上的数字
    def write_nbr(self):
        for i in range(0,len(self.boxList)):
            if self.boxList[i]['role'] != 9:
                neighbor_list = self.cpt8x(self.boxList[i])
                boom = 0
                for n in neighbor_list:
                    if self.boxList[n]['role'] == 9:
                        boom = boom + 1
                self.boxList[i]['role'] =boom


    #通过递归算法对每个空白进行8向数显示，然后进行4向空白显示。如果有空白再递归至函数初始处。
    #一开始是4向计算，后来发现windows扫描是计算周边8个空白显示。故修改为8x
    def blank8x(self,arg1):
        if arg1['role'] == 0 and arg1['status'] != 0:

            x = arg1['cdtX']
            y = arg1['cdtY']

            self.buttonList[x*30+y].configure(bg = 'gray',text='',state = 'disabled',compound='center')
            arg1['status'] = 0
            list8 = self.cpt8x(arg1)
            for i in list8:
                if 0 < self.boxList[i]['role'] < 9 and self.boxList[i]['status'] ==3:
                    self.buttonList[i].configure(image = self.img,bg = 'LightSkyBlue',)
                    self.buttonList[i].configure(bg = 'gray',text=self.boxList[i]['role'],font=("黑体", 12, "bold"),bd = 1,fg = 'black',compound='center')
                    self.boxList[i]['status']=0
            #blk_list=[]
            if x == 0 and y == 0:
                for i in  [(x*30)+(y+1),(x+1)*30+y,(x+1)*30+(y+1)]:
                    self.blank8x(self.boxList[i])


                    #self.buttonList[i].configure(bg = 'gray',text='',fg = 'red',state = 'disabled',compound='center')
            elif x == 0 and y == 29:
                for i in  [(x*30)+(y-1),(x+1)*30+(y-1),(x+1)*30+y]:
                    self.blank8x(self.boxList[i])
                #return  [x-1,(x+1)*30+y]

            elif x == 15 and y == 0:
                for i in  [(x-1)*30+y,(x-1)*30+(y+1),x*30+(y+1)]:
                    self.blank8x(self.boxList[i])
                #return  [(x-1)*30+y,x*30+(y+1)]

            elif x == 15 and y == 29:
                for i in  [(x-1)*30 +(y-1),(x-1)*30+y,x*30+(y-1)]:
                    self.blank8x(self.boxList[i])
                #return [(x-1)*30+y,x*30+(y-1)]

            elif x == 0 and 0<y<29:
                for i in  [x*30+(y-1),x*30+(y+1),(x+1)*30+(y-1),(x+1)*30+y,(x+1)*30+(y+1)]:
                    self.blank8x(self.boxList[i])
                #return [x*30+(y-1),x*30+(y+1),(x+1)*30+y]

            elif x == 15 and 0<y<29:
                for i in  [(x-1)*30+(y-1),(x-1)*30+y,(x-1)*30+(y+1),x*30+(y-1),x*30+(y+1)]:
                    self.blank8x(self.boxList[i])
                #return [(x-1)*30+y,x*30+(y-1),x*30+(y+1)]

            elif y == 0 and 0 <x<15:
                for i in  [(x-1)*30+y,(x-1)*30+(y+1),x*30+(y+1),(x+1)*30+y,(x+1)*30+(y+1)]:
                    self.blank8x(self.boxList[i])
                #return [(x-1)*30+y,x*30+(y+1),(x+1)*30+y]

            elif y == 29 and 0 <x<15:
                for i in  [(x-1)*30+(y-1),(x-1)*30+y,x*30+(y-1),(x+1)*30+(y-1),(x+1)*30+y]:
                    self.blank8x(self.boxList[i])
                #return [(x-1)*30+y,x*30+(y-1),(x+1)*30+y]

            else:
                for i in  [(x-1)*30+(y-1),(x-1)*30+y,(x-1)*30+(y+1),x*30+(y-1),x*30+(y+1),(x+1)*30+(y-1),(x+1)*30+y,(x+1)*30+(y+1)]:
                    self.blank8x(self.boxList[i])
                #return  [(x-1)*30+y,x*30+(y-1),x*30+(y+1),(x+1)*30+y]
        else:
            pass


    #8向计算，此函数返回参数周边格子的数值的列表。
    def cpt8x(self,arg1):
        x = arg1['cdtX']
        y = arg1['cdtY']
        if x == 0 and y == 0:
            return  [(x*30)+(y+1),(x+1)*30+y,(x+1)*30+(y+1)]
        elif x == 0 and y == 29:
            return  [(x*30)+(y-1),(x+1)*30+(y-1),(x+1)*30+y]
        elif x == 15 and y == 0:
            return  [(x-1)*30+y,(x-1)*30+(y+1),x*30+(y+1)]
        elif x == 15 and y == 29:
            return [(x-1)*30 +(y-1),(x-1)*30+y,x*30+(y-1)]
        elif x == 0 and 0<y<29:
            return [x*30+(y-1),x*30+(y+1),(x+1)*30+(y-1),(x+1)*30+y,(x+1)*30+(y+1)]
        elif x == 15 and 0<y<29:
            return [(x-1)*30+(y-1),(x-1)*30+y,(x-1)*30+(y+1),x*30+(y-1),x*30+(y+1)]
        elif y == 0 and 0 <x<15:
            return [(x-1)*30+y,(x-1)*30+(y+1),x*30+(y+1),(x+1)*30+y,(x+1)*30+(y+1)]
        elif y == 29 and 0 <x<15:
            return [(x-1)*30+(y-1),(x-1)*30+y,x*30+(y-1),(x+1)*30+(y-1),(x+1)*30+y]
        else:
            return  [(x-1)*30+(y-1),(x-1)*30+y,(x-1)*30+(y+1),x*30+(y-1),x*30+(y+1),(x+1)*30+(y-1),(x+1)*30+y,(x+1)*30+(y+1)]



def main():
    sl = saolei()
    mainloop()

if __name__ == '__main__':
    main()
