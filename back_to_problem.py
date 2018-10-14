	序号	时间	工具	问题	原因及解决方法


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
	2018/6/22	hibbox	hibbox工具导出fastboot日志为0kb	miami平台，6月1号下午之前的fastboot宏锁了


#############################

	
**8
	2018/6/26	dump	dump工具导日志没有生成01_android_log	dump工具，在m版本中，13_data_log下有android_log后，就不在生成01_android_log了，而hibbox工具会生成。


#############################

	
**9
	2018/6/27	hibbox	hibbox解析phoenix和orlando平台bbox.bin文件出错	原因是加入orlando中断表时，中断号有一个写成了412~427，这里中断号必须是一个一个单独的，不能这样写在一起;


#############################

	
**10
	2018/7/8	hibbox	导出hisi_logs/memorydump失败	问题：版本问题
状态：closed
导出hisi_logs/memorydump失败，在getlog中有提示adb shell pull memorydump 失败，说明没有权限导出memorydump文件！


#############################

	
**11
	2018/7/8	hibbox	hisi_logs下没有产生history.log	问题：版本问题
状态：closed
hisi_logs下没有产生history.log？查看total_file_num.txt，查找hisi_logs关键字，看看有没有导出history.log文件，发现没有记录history.log文件，说明手机里面没有生成！为了验证这种想法，手动在手机/data/hisi_logs下创建一个history.log，然后再用hibbox工具导出，发现导出了history.log，所以是因为手机没有生成所以没有导出，不是hibbox工具问题！


#############################

	
**12
	2018/7/12	hibbox	手机黑屏下，发现只导出了fastboot下日志，没有正常启动的kernel日志	
问题：版本问题
状态：closed
手机是黑屏状态，然后导日志，发现只导出了fastboot下日志，没有正常启动的kernel日志。是不是工具的问题导致没有导出日志？
通过get_log.log文件，查看导出日志，手机开始是fastboot状态，让后进入kernel等待180秒，最后导出结束。因为没有等到进入kernel，所以没有导出日志，不是工具的问题。


#############################

	
**13
	2018/8/7	??	??	要记录的问题
1、dump工具导出日志，dump done 不代表日志导出完成了，还要在等会。因为主线程走完了，子线程还在导;
2、dump工具直接执行dump log info kernel data-log导出日志，为什么报出save kernel failed的错误？
3、hibbox导出日志，无法导出13_data_log/LogService下的文件。
4、日志离线解析中，reliabilty/apperace下有hisitory.log，且其中的记录的复位未知，导致出现unknown！
5、上次版本验证中，hibbox无法导出日志。trace工具解析有问题？


#############################

	
**14
	2018/10/8			hibbox解决问题:
1、多个单板连接导出日志报错;
1.1、因为导出日志时，有一个ls -l的命令cmd，直接调用的subprocess执行命令cmd，没有replace替换sn号;

2、miami平台新型号手机，无法导出日志;
2.1、因为需要添加MRK型号;

3、fastboot环境变量的问题.
3.1获取环境变量存放到变量里面，变量中没有fastboot.exe，就把configs下的fastboot64存放到里面，变量里面就有了fastboot64的环境变量，但是执行的命令确不对了，还是执行的fastboot devices，而不是执行的fastboot64 devices; 所以，相当于还是用的运行者电脑自己的fastboot命令，没有用到fastboot64命令；
3.2、所以，在两个个单板连接，然后选择SN号时，出现了三个设备，其中一个是fastboot。需要在执行selectplatform之前，检查设备fastboot devices改成fastboot64 devices.

解决办法: c:/windows/system32下面的adb.exe和fastboot.exe没有生效，hibbox工具有时候会调用不到，但是在dos窗口下，执行确可以！adb.exe和fastboot.exe尽量不要放在c:/windows/system32下面。
