import matplotlib.pyplot as plt
import pandas as pd

asset_tgt = ['000001']
desti_path = 'C:/Users/anton/Desktop/'

headers = ['date', 'tid', 'open', 'high', 'low', 'close', 'volume', 'mid', 'range', 'fac0', 'avg', 's3', 's7', 's14',
           's21', 's35', 's49',
           's75', 's100', 's150', 's200', 's300', 's400', 's500', 's600', 's800', 's1000', 's1500', 's2000', 's3000',
           'ma_close', 'ub', 'lb']

lm_hd = ['s3000', 's2000', 's1500', 's1000', 's800', 's600', 's500', 's400', 's300', 's200', 's150', 's100', 's75',
         's49', 's14', 'ub', 'lb']
sm_hd = ['s1000', 's800', 's600', 's500', 's400', 's300', 's200', 's150', 's100', 's75', 's49', 's14', 'ub', 'lb']


def pic_out(if_mirror):
    plt.style.use('bmh')

    for comm in asset_tgt:
        # for comm in stock_pool_list_result:

        # 读入相关的数据，用DataFrame作为数据承载结构
        comm_t4 = pd.read_csv(desti_path + comm + '_30_t4_out.csv', names=headers, parse_dates=False, index_col='date')

        # 判断是否输出mirror
        comm_t4 = (comm_t4 if if_mirror == False else -comm_t4)

        comm_t4['x'] = 0  # 在数据的最后一列插入0值作为0轴数据
        ts_stamp = comm_t4.index[0]
        # date=list(comm_t4.date[:3000])
        # comm_t4=comm_t4[headers2]
        # rawd3=pd.DataFrame(comm_t4[:3000],index=date,columns=headers2)
        rawd3 = comm_t4[:3000].sort_index(ascending=False)
        rawd1 = comm_t4[:1000].sort_index(ascending=False)

        # 设置y轴的最大最小值
        lm3_uplim = round(max(rawd3[lm_hd].max()) * 1.5)
        lm3_dnlim = round(min(rawd3[lm_hd].min()) * 1.5)
        lm_uplim = round(max(rawd1[lm_hd].max()) * 1.5)
        lm_dnlim = round(min(rawd1[lm_hd].min()) * 1.5)
        sm_uplim = round(max(rawd1[sm_hd].max()) * 1.5)
        sm_dnlim = round(min(rawd1[sm_hd].min()) * 1.5)
        lmpx_uplim = (rawd3['close'].max() * 1.015 if if_mirror == False else rawd3['close'].max() * 0.985)
        lmpx_dnlim = (rawd3['close'].min() * 0.985 if if_mirror == False else rawd3['close'].min() * 1.015)
        smpx_uplim = (rawd1['close'].max() * 1.015 if if_mirror == False else rawd1['close'].max() * 0.985)
        smpx_dnlim = (rawd1['close'].min() * 0.985 if if_mirror == False else rawd1['close'].min() * 1.015)

        # 预设图像的大小、分辨率、背景颜色
        fig = plt.figure();
        fig.subplots_adjust(top=0.96)
        fig.subplots_adjust(bottom=0.04)
        fig.subplots_adjust(left=0.04)
        fig.subplots_adjust(right=0.96)
        ax = fig.add_subplot(111)
        ax.patch.set_facecolor("gainsboro")

        # 设置x轴标签颜色

        axis = plt.gca().xaxis

        for label in axis.get_ticklabels():
            label.set_color("black")
            label.set_fontsize(10)
            label.set_fontweight('bold')

        # plt.figure(figsize=(40,30),dpi=200,facecolor='#87CEEB');
        # plt.grid(True);
        # plt.set_ylabel('Values');
        # plt.right_ax.set_ylabel('Prices');

        # plot各个级别线条以及修改线条参数
        close_px = rawd3.sort_index(ascending=True).close.plot(linewidth=0.7, label='close', color='#767676',
                                                               secondary_y=True)
        close_pxma = rawd3.sort_index(ascending=True).ma_close.plot(linewidth=2, label='ma_close', color='#767676',
                                                                    secondary_y=True)
        s49 = rawd3.sort_index(ascending=True).s49.plot(linewidth=2.3, label='s49', color='#FFFFFF', secondary_y=False)
        s75 = rawd3.sort_index(ascending=True).s75.plot(linewidth=2.3, label='s75', color='#008080', secondary_y=False)
        s100 = rawd3.sort_index(ascending=True).s100.plot(linewidth=2.3, label='s100', color='#FFFF00',
                                                          secondary_y=False)
        s150 = rawd3.sort_index(ascending=True).s150.plot(linewidth=4.5, label='s150', color='#FF0000',
                                                          secondary_y=False)  # original_lwt==4
        s200 = rawd3.sort_index(ascending=True).s200.plot(linewidth=4.5, label='s200', color='#000000',
                                                          secondary_y=False)  # original_lwt==4
        s300 = rawd3.sort_index(ascending=True).s300.plot(linewidth=2.1, label='s300', color='#800080',
                                                          secondary_y=False)
        s400 = rawd3.sort_index(ascending=True).s400.plot(linewidth=2.1, label='s400', color='#800080',
                                                          secondary_y=False)
        s500 = rawd3.sort_index(ascending=True).s500.plot(linewidth=2.1, label='s500', color='#800080',
                                                          secondary_y=False)
        s600 = rawd3.sort_index(ascending=True).s600.plot(linewidth=2.1, label='s600', color='#800000',
                                                          secondary_y=False)
        s800 = rawd3.sort_index(ascending=True).s800.plot(linewidth=2.1, label='s800', color='#993300',
                                                          secondary_y=False)
        s1000 = rawd3.sort_index(ascending=True).s1000.plot(linewidth=4.5, label='s1000', color='#9090FF',
                                                            secondary_y=False)  # original_lwt==4.2
        s1500 = rawd3.sort_index(ascending=True).s1500.plot(linewidth=2.1, label='s1500', color='#FF99CC',
                                                            secondary_y=False)  # original_lwt==1.8
        s2000 = rawd3.sort_index(ascending=True).s2000.plot(linewidth=2.1, label='s2000', color='#FFCC99',
                                                            secondary_y=False)  # original_lwt==1.8
        s3000 = rawd3.sort_index(ascending=True).s3000.plot(linewidth=4.5, label='s3000', color='#FF6600',
                                                            secondary_y=False)  # original_lwt==4.2
        ub = rawd3.sort_index(ascending=True).ub.plot(linewidth=1.8, label='ub', color='#0000FF', secondary_y=False)
        lb = rawd3.sort_index(ascending=True).lb.plot(linewidth=1.8, label='lb', color='#0000FF', secondary_y=False)
        x = rawd3.sort_index(ascending=True).x.plot(linewidth=0.5, label='0_hori', color='#000000', secondary_y=False)

        # 设置y轴轴标签的颜色

        bxis = close_px.yaxis

        for label in bxis.get_ticklabels():
            label.set_color("black")
            label.set_fontsize(10)
            label.set_fontweight('bold')

        cxis = s49.yaxis

        for label in cxis.get_ticklabels():
            label.set_color("black")
            label.set_fontsize(10)
            label.set_fontweight('bold')

        # 设置两条y轴，图标题颜色，字体和大小

        close_px.set_ylabel('Price', fontsize=12, color='k')
        s49.set_ylabel('Values', fontsize=12, color='k')
        s49.set_ylim(lm3_dnlim, lm3_uplim)
        close_px.set_ylim(lmpx_dnlim, lmpx_uplim)
        close_px.grid(True)
        s49.grid(False)
        # plt.xlabel('Date',fontsize=12,fontweight='bold')
        plt.title('demo_000001', fontsize=24, color='b', fontweight='bold')
        # ax.legend(loc='lower center')
        # plt.legend((close_px,close_pxma,s49,s75,s100,s150,s200,s300,s400,s500,s600,s800,s1000,s1500,
        # s2000,s3000,ub,lb),('close','ma_close','s49','s75','s100','s150','s200','s300','s400','s500',
        # 's600','s800','s1000','s1500','s2000','s3000','ub','lb'))

        # 再调整一下x和y的tick的颜色为黑色
        # 把作图区域的大小以及背景颜色调整一下
        # 在读入的csv文件中最后一列插入都是0的值，多少用len
        # 两侧坐标的上下限制DIY设置方式
        # close_px.set_ylim(36000, 50000)
        # s49.set_ylim()

        # 导出图片
        # plt.savefig('C:\\Users\\zp\\Desktop\\pic\\cu.png',dpi=200,facecolor='w')

        fig = plt.gcf()
        fig.set_size_inches(30, 14)

        if if_mirror == True:
            plt.savefig('C:\\Users\\anton\\Desktop\\demo_000001_30.png', format='png', dpi=200,
                        facecolor='lightsteelblue')
        else:
            plt.savefig('C:\\Users\\anton\\Desktop\\demo_000001_a.png', format='png', dpi=200,
                        facecolor='lightsteelblue')

        plt.close()
