	知识点概述	说明	知识点描述

#######################
	hava维测步骤:	hava用例运行	hava维测步骤:
1.当一个用例出错以后，要看这个用例在本地运行是否通过，本地运行需要配置环境，包括在android.xml中配置SN号，设为当前手机的SN号;然后，在jython中新建一个运行配置名为mntn，配置运行入口为kempt/start.py文件，运行参数为work_block和selected_file_path。配置好以后，选中case中的某一个脚本，运行是选mntn运行。
2.先看hava平台的运行脚本是基于哪个平台的，本次平台是芝加哥平台，所以需要曼哈顿手机，运行后，如果没有错误，说明可能是环境问题。
3、看hava上的日志，日志怎么看，需要先看代码，代码中如果执行false就记录下日志，如果执行pass就不会记录日志。
4.找到hava平台记录日志的地方，为Log/dmsg.log，这个log是在运行该脚本的。
点进去这个任务，对应了一台电脑，电脑上对应了两个单板，然后找到任务对应的单板。
5、putty连接到执行任务的电脑，找到mntn目录，里面又有两个日子目录，找到对应单板的日志目录，根据hava上log找到dmsg.log文件。
6.使用scp命令，将日志复制到自己的编译云上去。
6、在自己的云上，根据报的错误来看dmsg日志，报错找不到关键字pref，搜索pref确实没有找到，找到负责perf解析的负责人张琪，最后定位为log被冲掉了。
7.然后hava上定位问题，状态为closed，描述为dmsg日志被冲，填上对应的单号(以前遇到同样问题，所以已经有单号了)。

#######################
		hava代码提交	hava代码合并步骤新:
1.repo sync 更新代码
2.然后进入到mntn目录，看是否有分支，使用命令git branch，否则就要新建分支;
3.git add文件，git commit文件，如果错了可以使用reset撤销提交，提交的的单号固定，描述就写你为什么提交，如果是新代码就是feature，如果是修复bug就是debugfix;
4.然后repo上传你提交的代码;

#######################
		hava用例上线	hava用例上线的步骤:
1.配置jekins时，一个任务一般跑所有的用例，但是配置四个shell时，是为了可以同时跑这么多个，而不是一个一个跑;
2.有一个设备是单独给我用的，所以，在该设备上配置了一个任务跑所有要验证的用例，一个任务每天跑，所以有很多任务;
3.我需要统计所有任务，即jekins每天下发同样的任务，所以多了很多相同的任务！
4.把每个任务的运行结果导出来，把每个用例和运行结果复制到同一张表里面;每天都通过的用例上线;


#######################
		hava用例上线统计	hava用例上线统计:
1.导出全部用例，统计出全部成功的，筛选出全部失败的;统计是插入函数count(区域，值)，区域为整行，值为TRUE或者FAIL，计算出单行的;然后，格式刷其他行的;
2.用例编号mntn_startup_001.py，用例描述是启动日志，用例结果是fail，成功次数14，失败次数为1，失败原因是没找到关键字，进展是2018/5/31暂无进展，状态是pass(上线)或者cancel(取消);
3.选中一行或者某一列，按ctrl+alt+L可以筛选数据，筛选出FAIL的正行标红，筛选出PASS的全部标绿;
4.有多的用例，需要删除的，这里irq的用例不要了，还有一种类型的用例也不早要了。ctrl+alt+L选中后，筛选中关键字为irq的，全部删除;
5.然后添加上统计，特性，该特性总共多少，通过多少，失败多少;最后总结说明重复用例删除了;
6.日志丢失了，无法分析，解决办法:找到result bundle，里面失败用例在前，成功用例在后，一般日志保存在跑的第一个用例里面，所以要么是第一个失败的用例里面，要么是第一个成功的用例里面;


#######################
		hava问题分析	hava问题分析:
1.任务一:设备在线，但是fastboot oem boot起不来;
2.任务二:设备不在线，挂掉了，startup_mntn_0006执行后单板挂掉了。最后林俊杰定位为用例问题，用例中watch_dog中第十三和十四位该改成0;
3.任务三:设备在线，查看dmesg log都是空的。那怎么办，在执行了adb命令后突然就killed了，那有可能是超时了，看看用例开始执行时间，到最后挂掉的时间，一共花了4个小时，因为设置了最长执行时间，所以超时了;
4.任务四:设备在线，但是log目录下是空的，没有找到dmesg log，看用例中，如果找到关键字就通过，如果没有找到关键字就把日志记录到dmesg中，但是这里teardown部分写的log是只生成一个目录，没有往目录里写日志文件，那设计用例是不是有问题？



#######################
		hava用例修改	hava用例修改:
有一个dmesg日志被冲的问题，找不到reset复位关键字的时候，就去其他地方找？？所以应该怎么修改？？

#######################
	hava维测步骤:		hava维测步骤:
1.当一个用例出错以后，要看这个用例在本地运行是否通过，本地运行需要配置环境，包括在android.xml中配置SN号，设为当前手机的SN号;然后，在jython中新建一个运行配置名为mntn，配置运行入口为kempt/start.py文件，运行参数为work_block和selected_file_path。配置好以后，选中case中的某一个脚本，运行是选mntn运行。
2.先看hava平台的运行脚本是基于哪个平台的，本次平台是芝加哥平台，所以需要曼哈顿手机，运行后，如果没有错误，说明可能是环境问题。
3、看hava上的日志，日志怎么看，需要先看代码，代码中如果执行false就记录下日志，如果执行pass就不会记录日志。
4.找到hava平台记录日志的地方，为Log/dmsg.log，这个log是在运行该脚本的。
点进去这个任务，对应了一台电脑，电脑上对应了两个单板，然后找到任务对应的单板。
5、putty连接到执行任务的电脑，找到mntn目录，里面又有两个日子目录，找到对应单板的日志目录，根据hava上log找到dmsg.log文件。
6.使用scp命令，将日志复制到自己的编译云上去。
说明:scp命令可以把远程拷到本地，或者把本地拷到远程，例如，把远程test1文件拷到本地/temp目录，scp root@host1:/tmp/test1 /tmp
7、在自己的云上，根据报的错误来看dmsg日志，报错找不到关键字pref，搜索pref确实没有找到，找到负责perf解析的负责人张琪，最后定位为log被冲掉了。
8.然后hava上定位问题，状态为in process，描述为dmsg日志被冲，填上对应的单号(以前遇到同样问题，所以已经有单号了)。

#######################
	hava问题分析:		hava问题分析:
1.任务一:设备在线，但是fastboot oem boot起不来;
2.任务二:设备不在线，挂掉了，startup_mntn_0006执行后单板挂掉了。最后林俊杰定位为用例问题，用例中watch_dog中第十三和十四位该改成0;
3.任务三:设备在线，查看dmesg log都是空的。那怎么办，在执行了adb命令后突然就killed了，那有可能是超时了，看看用例开始执行时间，到最后挂掉的时间，一共花了4个小时，因为设置了最长执行时间，所以超时了;
4.任务四:设备在线，但是log目录下是空的，没有找到dmesg log，看用例中，如果找到关键字就通过，如果没有找到关键字就把日志记录到dmesg中，但是这里teardown部分写的log是只生成一个目录，没有往目录里写日志文件，那设计用例是不是有问题？



#######################
	hava用例上线统计:		hava用例上线统计:
1.导出全部用例，统计出全部成功的，筛选出全部失败的;统计是插入函数count(区域，值)，区域为整行，值为TRUE或者FAIL，计算出单行的;然后，格式刷其他行的;
2.用例编号mntn_startup_001.py，用例描述是启动日志，用例结果是fail，成功次数14，失败次数为1，失败原因是没找到关键字，进展是2018/5/31暂无进展，状态是pass(上线)或者cancel(取消);
3.选中一行或者某一列，按ctrl+alt+L可以筛选数据，筛选出FAIL的正行标红，筛选出PASS的全部标绿;
4.有多的用例，需要删除的，这里irq的用例不要了，还有一种类型的用例也不早要了。ctrl+alt+L选中后，筛选中关键字为irq的，全部删除;
5.然后添加上统计，特性，该特性总共多少，通过多少，失败多少;最后总结说明重复用例删除了;
6.日志丢失了，无法分析，解决办法:找到result bundle，里面失败用例在前，成功用例在后，一般日志保存在跑的第一个用例里面，所以要么是第一个失败的用例里面，要么是第一个成功的用例里面;


#######################
	CI配置	jekins配置mntn的CI组件	
1.somke_flag的值配置为kirin710_4_9_pkg_drv_device_dev3_usb_device_sne.txt
或者
kirin710_4_9_pkg_drv_device_dev3_usb_device_udp.txt
配置规则为，版本+组内CI组件级选项+类型;
2.版本号哪里看呢？
首先浏览器打开版本下载的地方，要找到平台，是Miami还是Boston，然后找到CI中写的分支，在分支下选择一个有RE_COMPILE的分支，代表是编译的分支，在编译分支下面看版本，选一个编译时间比较长的，表示已经编译完了，在下面找到版本名kirin710_4_9_pkg;
3.平时看护的hava和这次新建的冒烟是不一样的，平时看护的hava是代码合入之后的拦截，冒烟是开发自己触发，出了问题自己负责的;是冒烟还是压测，是有配置信息CI还是其他来判断，CI代表冒烟;所以，冒烟的任务名一般叫DRV_CI；
4、然后在jekins上新建任务，首先是任务名，任务名一定是小组名，比如是DRV_DEV&BOOTLOADER，然后是平台MIAMI，然后是终端类型，比如是UDP还是SNE，然后是要测试的CI特性比如是BLACKBOX_NOC_ECALL这些;
5、然后是tmss用例路径，找到hava平台上对应的Miami平台定义的用例路径，复制到jekins中;
6、还有代码运行位置为run_pakage=/mntn/qtandroid目录;


#######################
	hava代码合并步骤新:		hava代码合并步骤新:
1.repo sync 更新代码
2.然后进入到mntn目录，看是否有分支，使用命令git branch，否则就要新建分支;
3.git add文件，git commit文件，如果错了可以使用reset撤销提交，提交的的单号固定，描述就写你为什么提交，如果是新代码就是feature，如果是修复bug就是debugfix;
4.然后repo上传你提交的代码;

#######################
	平台的区分		**平台的区分
miami 6260
chicago 960
boston 970
atlanda 980

#######################
	gcov覆盖率提升的事情		gcov覆盖率提升的事情
1.打开覆盖率数据显示界面，选择时间，选择dev2组，显示;
2、找到孔飞-底软驱动，ST当前这一列，点进去，再点进去，就看到具体覆盖了哪些文件，包括覆盖的文件、未覆盖的文件、不在责任田的文件、不需要跑的文件;其中，不在责任田的文件要把它移进去;
3、把没有覆盖的.c文件复制到notepad++中，搜索mntn关键字，找出哪些是属于mntn的，然后根据ddrdump_kernel.c来看，是不是ddrdump的用例没有上，以此类推;
4、如果用例上了，但是覆盖率还是没有，就要看是否有cogv文件和codn文件，下载今天最新的运行后的压缩包，来看;打开压缩包后，打开一个.html文件，就可以看到该文件的覆盖率;因为hava平台每天运行完用例后，自动就把gcov上传了，担心的是没有把gcov上传上去;
5、如果用例上了，运行后的压缩包下载下来也有cogv和codn文件，还是没有覆盖到，那就要看主线代码，vendor/../cfg.txt文件中，是否配置了.c文件，+代表该文件存在，-表示该.c文件不存在;


#######################
	blackbox代码框架学习		*blackbox代码框架学习
1、从rdr_core.c文件看起;
2、然后看hisi_app.c文件;
3、rdr_core中的init在hisi_app中的init之前;
4、主要看见个流程，pstore中日志，打印bbox_main关键字的启动后流程和;kmsgcat-log中，打印带有bootcheck关键字的复位流程;
5、复位流程从can not. ..start boot开始，到boot done结束，中间是打印关键字boot check;
6、快捷键
6.1、;+s，光标所在函数，查找该函数所在位置;
6.2、;+f+s，光标不在要查找的函数上，输入cs find s，然后输入要查找的函数，可以查找出全部相关函数;
6.3、shit+#，光标所在关键字，高亮所有对应相同的关键字;
6.4、ctrl+]，光标所在函数，跳转到该函数定义的位置;
6.5、ctrl+T，返回上一步;
6.6、快捷键左、下、上、右，对应h、j、k、l，加上ctrl+w就可以在不同的窗口下切换;

#######################
	gcov中fastboot数据适配		fastboot数据适配
1、首先找到已经配置好的jekins，第一行，都以这个为模板;
2、需要配置4个shell，现在维测的gcov只有三个shell，第一个shell是git_download，用来下载日志等;第二个是git_cov，运行生成kernel_obj;第三个是git_fast，运行生成fastboot_obj；还有一个是……
3、所以，在适配gcov fastboot时，所有执行fastboot boot、fastboot reboot、fastboot oem boot命令时，都要先把导出数据来，导出位置必须放在qtandroid下载，相对路径的git下面;

代码逻辑
1、判断version，提需求加一个COMM或者GCOV？还有Sysconfig中获取version，我这里代码里没有？
2、判断fastboot命令，我这里log path路径并不知道？怎么一会是GCOV目录一会是get_GCOV目录？

			fastboot数据适配，代码编写遇到的问题:
1、pylib下一个log.py，里面是EXECUTE类，里面包含执行EXE(cmd)的函数；
2、在pylib下添加一个GcovFastboot.py文件，里面是GcovFastbootDump类，类里面要写处理fastboot的命令，如果是fastboot命令，就需要执行EXECUTE里面的EXE(cmd)来处理fastboot命令。
3、所以，这样问题是？
GcovFastboot.GcovFastbootDump类里面，要调用log.EXECUTE里面的EXE(cmd)方法；而log.EXECUTE.printEXE又要调用GcovFastboot.GcovFastbootDump里面的方法。不能两个文件相互导入对方吧？
4、处理办法
4.1、方法一。GcovFastboot.GcovFastbootDump里面不执行log.EXECUTE.EXE(cmd)方法，只是处理完fastboot命令，合成要导出数据的命令fastboot oem memorydump，然后log.EXECUTE中调用处理好的fastboot oem memorydump命令；
4.2、方法二。把log.EXECUTE.EXE(cmd)方法，直接当参数，传入到GcovFastboot.GcovFastbootDump里面，直接使用传入的EXEXE(cmd)方法执行fastboot oem memorydump命令；
5、总的来说，就是把log.EXECUTE当成主对象，把GcovFastboot.GcovFastbootDump当成被调用的对象！

#######################
	hava压力测试100次		hava压力测试100次

1、startup.sh中修改case_path为/case/mntn/kerneldump021；
2、在android中修改，是本地执行还是蝴蝶执行，只有本地执行才有local run number，就是运行次数；所以要修改android.xml中为LOCAL，运行次数为100；然后执行startup.sh运行；
3、hava平台有一个qta_git更新，是存放脚本和更新android.xml的地方；

#######################
	gcov手动生成报告		gcov中kernel手动生成报告
1、执行adb shell ecall read_u32 0来触发panic复位，然后执行fastboot oem boot进入安卓，执行.bat文件来抓取数据生成一个.tar.gz文件；
2、解压.tar.gz文件，搜索mntn_file来找到gcda文件。然后找到对应版本的编译包，在image/lib/gcov_en.tar.gz文件，解压，搜索mntn_file关键字，找到gcno文件；
说明:在烧写的镜像包里如果只搜索gcno关键字有很多gcno，如果只搜索mntn_file关键字，只搜索到temp_mntn_file.gcno文件
3、把gcno、gcda文件上传到编译云，通过window把文件放在编译云服务器99上，然后使用scp命令，把文件复制到目标电脑，先在目标电脑/home/get_gcov_data/clv1.2/下建一个gcov_kernel文件夹。然后使用命令:
scp gc* root@100.100.100.225:/home/get_gcov_data/clv1.2/
4、到目标电脑225上，进入clv1.2/gcov_kernel文件夹，然后执行一个gc -o . -c *的命令，在执行一个result的命令，这样就产生对应的result。使用scp命令将result复制到自己的编译云99上，通过window来查看报告。


gcov中fastboot手动生成报告
1、首先执行fastboot watchdog enable命令，然后用get_fastboot_data.sh命令来导出重启之前的数据。
2、然后再执行fastboot oem boot命令，来进入安卓。
说明: fastboot oem boot之前，要执行一个fastboot init的命令。
3、然后再用get_fastboot_data.sh导出数据.tar.gz文件
4、把多次导出的tar.gz文件，全部放到gcov_get_data/gcov_cl1.2下面，然后执行source gcov.sh命令，就生成了对应的报告；

#######################
	编写的watchdog001用例		编写的watchdog001用例
测试步骤
1、执行fastboot watchdog ap enable
2、adb shell
       dmesg>>dmesg.txt
3、adb pull dmesg.txt /home/dmesg.txt
4、查看dmesg.txt中是否有关键字click no 3

实现脚本watchdog_mntn_test_0001
1、init部分
androidCase.init
watchdog.init
2、setup部分
BootToAndroid
deletekmsg
3、testStep部分
self.pass = false
if whetherInAndroid:
    RebootBootloader
    if whetherResetSuccessfully:
       enable(watchdog enable)
       BootToAndroid
    if whetherBootsuccessfully:
      self.pass = seachkey(click no 3)
 checkpoint(self.pass,true)

4、teardown
bootToAndroid
savekmsglog



#######################
	coresight用例实现re使用		正则表达式使用1
1.1、coresight用例，中遍历/sys/date/plateforms/etm8000.etm节点，通过adb shell ls -l命令，查看文件权限。第一个位置，d表示目录，-表示普通文件，l表示链接文件;接着是文件所属用户权限、文件组权限、其他用户权限;
1.2、这里只看文件所属用户权限，如果是r--就只cat，如果是rw-就cat再把cat的值写进去，如果是-w-就echo 0x1进去;
1.3、正则表达式使用匹配字符串里面是否包括[rw]读或者写操作，如果包括，再继续处理;

正则表达式使用2
2.1、在处理责任人表时，使用re.relace(fomat，new_fomat,value)
就是将结尾的空格或者\n\r换行;
2.2、正则表达式匹配history.log中最后一行中的16位日期\d{8}-\d{8}，然后查找日期对应的文件;

#######################
	hava kernel数据适配		hava kernel数据适配
pla3-pylib下，有utils-commutils类，是所有用例类的父类，调用gcovdump用来导出数据; gcovdump文件有gcov导出日志命令基本方法:log中printEXE也调用gcovdump中方法;


#######################
	linux下上一级目录		linux下上一级目录
1、gcov/git/lcov1.1.2/下，lcov1.1.2下有bin;
2、gcov/git/get_gcov_data，下有get_report.sh文件;
3、在gcov/git/get_gcov_data下，执行gcov/git/lcov1.12/bin下文件，可以写成:
../lcov1.12/bin来执行;

#######################
	正则表达式group和groups		import struct
regex = re.compile((?P<head1>hello\w*)--(?P<head2>hello\w*))
str = '''hello1--hello2ddd hello3dd--hello4444444 
hello777 
'''
match_result = regex.match(str)
findall_result = regex.findall(str)
 
print group:,match_result.group()
print groups:,match_result.groups()
print findall:,findall_result
显示结果：
group: hello1--hello2ddd
groups: ('hello1', 'hello2ddd')
findall: [('hello1', 'hello2ddd'), ('hello3dd', 'hello4444444')]
