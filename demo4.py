import matplotlib.pyplot as plt
import numpy as np

x=np.linspace(-3,3,50)
y1=2*x+1
y2=x**2

plt.figure(num=3,figsize=(5,6))
plt.plot(x,y2)
plt.plot(x,y1,color='red',linewidth=1.0,linestyle='--')
plt.xlim((-1,2))
plt.ylim((-2,3))
plt.xlabel('x')
plt.ylabel('y')

plt.xticks(np.linspace(-1,2,5))
plt.yticks([-2,-1.8,0,1.5,3],\
         [r'$really\ bad$',r'$bad$',r'$normal$',r'$good$',r'$perfect$'])

ax=plt.gca()##获取坐标轴信息,gca=get current axic
ax.spines['right'].set_color('none')##设置右边框颜色为无
ax.spines['top'].set_color('none')

ax.xaxis.set_ticks_position('bottom')##位置有bottom(left),top(right),both,default,none
ax.yaxis.set_ticks_position('left')##定义坐标轴是哪个轴，默认为bottom(left)

ax.spines['bottom'].set_position(('data',0 ))##移动x轴，到y=0
ax.spines['left'].set_position(('data',0))##还有outward（向外移动），axes（比例移动，后接小数）

plt.show()