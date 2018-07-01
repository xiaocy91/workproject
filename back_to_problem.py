

#############################

	**1	2018/4/22	
hibbox
	
西安研发：李伟
miami平台产品JSN，用Hibox抓取dump，是空的
	
问题：版本问题
状态：closed
原因:是user版本的问题，fasboot锁了。由于研发阶段，测试手机都是user版本的，出了问题没法抓日志；



#############################

	**2	2018/4/22	
hibbox
	
袁旦：
hibbox抓包时，30_baselog概率性不生成
	
问题：使用问题
状态：closed
原因：没有导完日志,因为dump中bbox.bin没有解析出来，所有日志不完整。



#############################

	**3	2018/4/25	
hibbox
	

西安：蔡志鹏
hibbox工具打开后，提示找不到设备，但是设备已经连接好了

	
问题：环境问题
状态：closed
原因：fastboot、adb环境变量没设置好，用hibbox中的fastboot重新设置了环境变量就好了



#############################

	
**4
	2018/5/9	
hibbox
	
程利华：
1、hibbox清除log，会把snoop目录清楚掉？
2、用工具导出/data/vendor/log目录，和手动导的不一样？
	
问题：工具（没有提需求）
状态：in process
原因：
1、导出日志会全部导出，不仅仅为snoop；
2、清楚日志全部清楚，包括snoop日志；



#############################

	
**5
	2018/5/14	
hibbox
	
秦永恒
  rom中(0x15,samsang)，(0x11，toshiba),(0x45,sandisk)，为什么0x11没有解析出来？对应的hibbox文件为utfs_ddr_.py文件！

	
问题：工具（没有提需求）
状态：in process
原因：ufs_addr_.py文件对rom的解析有错误



#############################

	
**6
	2018/6/1	
hibbox
	
西安研发：李伟
fastboot导出的文件都是0kb,且fastboot oem ddrdump show命令可以使用，只是导出来的文件是空的，且烧写的软件版本是eng版本？？？
	
问题：版本问题
状态：closed
原因：目前miami平台有问题，终端把fastboot锁了，所以fastboot不能导日志；



#############################

	
**7
	2018/6/22	hibbox	hibbox工具导出fastboot日志为0kb	6月1号下午之前的fastboot宏锁了


#############################

	
**8
	2018/6/26	dump	dump工具导日志没有生成01_android_log	dump工具，在m版本中，13_data_log下有android_log后，就不在生成01_android_log了，而hibbox工具会生成。


#############################

	
**9
	2018/6/27	hibbox	hibbox解析phoenix和orlando平台bbox.bin文件出错	原因是加入orlando中断表时，中断号有一个写成了412~427，这里中断号必须是一个一个单独的，不能这样写在一起;
