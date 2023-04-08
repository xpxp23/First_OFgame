#!/usr/bin/python
#coding:utf-8
 
#python 写的扫雷游戏
 
 
import sys
import random
 
class MineSweeping():
  #扫雷主程序
  def __init__(self,row = 8 ,line= 8,mineNum = 15):
    self.row = row
    self.line = line
    self.score = 0 #分数
    self.mineNum = mineNum
    self.xy_list = [[0 for i in range(self.line)] for i in range(self.row)]
 
  def initData(self):
    # 初始化状态值
    # 游戏开始的时候状态值为清零(再重新设置状态值)
    self.xy_list = [[0 for i in range(self.line)] for i in range(self.row)]
    # 设置雷的数量
    maxMine = self.mineNum
    while maxMine > 0 :
      num_x = random.randint(0,self.row-1)
      num_y = random.randint(0,self.line-1)
      if self.xy_list[num_x][num_y] == 0:
        self.xy_list[num_x][num_y] = 1
        maxMine -= 1
 
  #获取x坐标
  def get_pos(self,str_pos):
    #获取x坐标
    while 1:
      try:
        num_x = raw_input(str_pos)
        if int(num_x) in range(self.line) and num_x :
          break
        else:
          print u'输入无效值'
      except:
        pass
    return int(num_x)
 
  #进行扫雷
  def mine_clear(self,x,y):
    # 设置显示进行扫过的数目
    # 设置数字
    # 0 表示扫过的雷
    # 1 表示类
    # 2 表示扫过的类
 
    #获取坐标的数字
    pos = self.xy_list[x][y]
    if pos == 0 :
      self.xy_list[x][y] = 2
      return 0
    elif pos == 2 :
      return 2
    else:
      return 1
 
  #界面的显示
  def mineFace(self,state):
    #显示界面的内容
    #设置游戏的状态
    #1 表示运行的状态
    #2 表示输出的状态
    #3 表示游戏结束的状态
    #4 表示游戏获得了完胜
    if state == 1:
      print '+=================+'
      print '   Game start  '
      print '+=================+'
      tt = ' #'
      print '**************************'
      for i in range(self.line):
        str_t = ''
        for t in xrange(self.row):
          str_t += tt
        print "|%s|"%(str_t,)
      print '**************************'
      print 'Please input values of x,y(0-7):'
    #刷新用户界面
    if state == 2:
      tt = ' #'
      print '**************************'
      for i in range(self.line):
        str_t = ''
        for t in xrange(self.row):
          if self.xy_list[i][t] == 2:
            str_t += str(self.xy_list[i][t]).rjust(2)
          else:
            str_t += tt
        print "|%s|"%(str_t,)
      print '**************************'
    if state == 3:
      print '**************************'
      for i in range(self.line):
        str_t = ''
        for t in xrange(self.row):
          if int(self.xy_list[i][t]) != 1:
            str_t += ' 2'
          else:
            str_t += ' *'
        print "|%s|"%(str_t,)
      print '**************************'
 
    if state == 4:
      tt = ' #'
      print '**************************'
      for i in range(self.line):
        str_t = ''
        for t in xrange(self.row):
          if self.xy_list[i][t] == 2:
            str_t += str(self.xy_list[i][t]).rjust(2)
          else:
            str_t += ' @'
        print "|%s|"%(str_t,)
      print '**************************'
 
 
  def MainLoop(self):
    #创建游戏主循环
 
    #创建界面的运行
    self.mineFace(1)
    self.score = 0
    self.initData()
    #print self.xy_list
 
 
    # 进入主循环
    while 1:
      #获取坐标的位置
      x = self.get_pos(' X = ')
      y = self.get_pos(' Y = ')
      num = self.mine_clear(x,y)
      #判断是不过的了完胜
      win = True
      for i in self.xy_list:
        if 0 in i:
          win = False
          break
      if win:
        num = 4
 
      #执行刷新界面的函数
      if num == 0:
        self.mineFace(2)
        self.score += 10
      elif num == 2:
        print u'这个位置已经被排过了,证实没有雷'
      elif num == 1:
        print '+=================+'
        print '   Game over  '
        print '+=================+'
        print u'分数 : ', self.score
        self.mineFace(3)
        # 是不是进行下一句
        next = raw_input(u'是够进行下一局:Y or N ')
        if next.upper().startswith('Y'):
          print u'下一局开始'
          self.nextGame()
        else:
          print '>>> Game exit'
          break
      else:
        self.score += 10
        print u'恭喜您获得的完全的胜利'
        print u'分数 : ', self.score
        self.mineFace(4)
        next = raw_input(u'是够进行下一局:Y or N ')
        if next.upper().startswith('Y'):
          print u'下一局开始'
          self.nextGame()
        else:
          print '>>> Game exit'
          break
 
  # 下一局初始化信息
  def nextGame(self):
    self.mineFace(1)
    self.score = 0
    self.initData()
 
 
if __name__ == '__main__':
  mi = MineSweeping(10,10,20)
  mi.MainLoop()
  sys.exit()
