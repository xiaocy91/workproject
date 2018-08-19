	知识点概述	说明	知识点描述

#######################
	版本验证	第一次版本验证	1、第一个脚本：auto_potest.bat
运行过程：先将imag路径改为要测试的版本的Image路径，然后运行
运行结果：PASS
2、第二个脚本：usb2.0.bat
运行过程：将脚本下case中xloader文件下xml改成EMILY（本次手机使用型号为EMILY）
运行结果：Sdcard执行失败，因为EMILY手机没有Sdcard,然后会使用IDT加载EMILY.xml来烧写单板
问题：为什么一定要把image下除了EMILY.xml的文件删除？？？
3、第三个脚本：usb3.0.bat
运行过程：不需要修改
运行结果：只是做了pull和push操作


#######################
		第二次版本验证	版本验证步骤
1.执行usb2.0，修改case中xloader中路径为emily或者alps，运行后输入image的路径；
问题:usb2.0是基于HIDS工具的，所以要先安装该工具！
2.执行usb3.0前，要把image中没用的xml删除，然后执行，没有失败就成功了；
3.插入sdcard后，执行protest_main以后，没有报错就成功了；
4.执行小绿版操作，连接小绿版播号，看wiki，然后执行uart命令，打开设备管理器，看是否有uart93口，打开sscome串口工具，输入回车，工具会输出打印；
5.再cmd中执行命令后，然后在串口中查看日志，日志打印的东西会多点；
6.执行gevent -l后，拔掉usb才可以休眠，然后再打开屏膜，手动触模，cmd命令窗口可以打印很多东西；
7.枚举升级，使用小绿版，拨号到0011和1000，然后看设备管理中是否出现com1.0口，出现该口以后重启手机，然后IDT烧写升级；
6.验证fastboot的时间，这个不需要连接串口，手机只需要连接usb就可以，这时设备管理器里有PCU_UI端口，打开串口工具sscome，输入at^fblock=1就是锁住了，等于0就是不锁；
8.遇到的问题
8.1ALPS手机，用枚举类型强制升级，升级到fastboot模式就出错了。解决方法:执行IDT-tools-clear usb map data，然后再烧写，速度很慢，但是可以烧写成功；
8.2执行at^fblock以后，导致/data目录没有写权限了。解决办法:锁了旁路以后不要忘记解锁；另外，有的user版本确实没有写权限，此时需要执行adb root和adb amount命令就有root权限了，然后执行push操作。
8.3使用小绿板执行uart命令后，导致无法识别SD卡。解决办法:需要将执行的命令再反着执行一遍。

#######################
	版本验证步骤		版本验证步骤
1.执行usb2.0，修改case中xloader中路径为emily或者alps，运行后输入image的路径；
问题:usb2.0是基于HIDS工具的，所以要先安装该工具！
2.执行usb3.0前，要把image中没用的xml删除，然后执行，没有失败就成功了；
3.插入sdcard后，执行protest_main以后，没有报错就成功了；
4.执行小绿版操作，连接小绿版播号，看wiki，然后执行uart命令，打开设备管理器，看是否有uart93口，打开sscome串口工具，输入回车，工具会输出打印；
5.再cmd中执行命令后，然后在串口中查看日志，日志打印的东西会多点；
6.执行gevent -l后，拔掉usb才可以休眠，然后再打开屏膜，手动触模，cmd命令窗口可以打印很多东西；
7.枚举升级，使用小绿版，拨号到0011和1000，然后看设备管理中是否出现com1.0口，出现该口以后重启手机，然后IDT烧写升级；
6.验证fastboot的时间，这个不需要连接串口，手机只需要连接usb就可以，这时设备管理器里有PCU_UI端口，打开串口工具sscome，输入at^fblock=1就是锁住了，等于0就是不锁；
8.遇到的问题
8.1ALPS手机，用枚举类型强制升级，升级到fastboot模式就出错了。解决方法:执行IDT-tools-clear usb map data，然后再烧写，速度很慢，但是可以烧写成功；
8.2执行at^fblock以后，导致/data目录没有写权限了。解决办法:锁了旁路以后不要忘记解锁；另外，有的user版本确实没有写权限，此时需要执行adb root和adb amount命令就有root权限了，然后执行push操作。
8.3使用小绿板执行uart命令后，导致无法识别SD卡。解决办法:需要将执行的命令再反着执行一遍。

#######################
	版本验证遇到的问题		版本验证遇到的问题
1.脚本问题
dev3/auto_protest脚本，boston选择es

2.trace32使用
trace32版本1.62，双击trace32文件运行，选择boston平台，然后选择ap sumting，右键选择start，然后选择镜像文件/lib/virture文件，这时需要一段时间，解析出来没有乱码;然后，还有linux process和linux  log没有乱码，表示通过;

3.要上电
1000 0011代表uart2

4.user版本IDT只能下载镜像，不能烧写;

版本验证
1.usb2.0测试先改img路径，安装HIDS然后测试;
2.usb3.0直接运行;
3.auto_protest中，把不需要xml文件删除，然后运行直接pass;
4.sd卡存储测试，插入sd卡，测试通过，没有失败的用例;



#######################
	版本验证的问题		版本验证的问题
1、mount命令
mount -t debugfs nodev /dev/debugfs
这是将系统dwbugfs类型数据挂载到/dev/debugfs下；
2、挂载的debugfs下有clk和gpio；
3、PCUI口插上usb就有，用来发命令；uart口插上小绿板才有，用于看uart信息；
4、小绿板有两个usb口，一个用于连接电脑，一个用于连接手机，效果是一样，用哪个口就把开关拨到哪边；
5、trace32的使用，首先选择平台，然后选择导出日志的ddrdump下的kerneldump.bin文件，然后选择烧写镜像的Lib下的vitureLinux文件，就可以开始解析；

#######################
	P版本验证		p版本验证有三个组:
platfom平台组
pmu功耗组
DRV组

1、首先是platform脚本验证
1.1、直接就是main4_N.bat运行，不选M是因为M版本跟P版本的系统目录有点不一样，所以选N；
1.2、刚烧好版本的时候，用hibbox导出手机里的日志，日志里就保存了kmscat-log的日志，里面记录了bootime is;
1.3、运行后选择Dallas平台，然后开始测试5次重启的用例；
1.4、替换中间的一些.apk，怕不是最新的；
1.5、测试有modem的用例，直接注释掉，不运行；
1.6、测试中有个用例运行后卡住了，直接在另外一个cmd窗口，敲带&的命令就可以继续运行；
1.7、测试trace那个地方，不要调用他们的脚本，可以调用dump工具来执行;

2、pmu功耗验证
2.1最后搜集日志就行，看日志是不是都PASS了；
2.2执行中有java的错误，忽视不计；

3、驱动用例的验证
3.1、注释掉usb.bat的用例，打开其他protest.bat用例，usb的用例用原来boston的脚本来跑；
3.2、pcui口可以通过getprory来设置，设置是否有pcui口，或者枚举出其他端口，pcui口只能发送at^fblock命令；
3.3、有一条用例，get config.propry的命令，可以枚举端口，如果手机了解到了电脑，就有android.phone显示；
3.4、测试中有一个rmc.bat的脚本，里面的命令是gevent -l的命令，执行后手动触发手机屏幕；
3.5、uart口要先使能uart shell，然后发su命令root，然后发ls等shell命令；
3.6手动测试一下小绿板的操作；

#######################
	P版本验证		版本验证的问题
1、mount命令
mount -t debugfs nodev /dev/debugfs
这是将系统dwbugfs类型数据挂载到/dev/debugfs下；
2、挂载的debugfs下有clk和gpio；
3、PCUI口插上usb就有，用来发命令；uart口插上小绿板才有，用于看uart信息；
4、小绿板有两个usb口，一个用于连接电脑，一个用于连接手机，效果是一样，用哪个口就把开关拨到哪边；
5、trace32的使用，首先选择平台，然后选择导出日志的ddrdump下的kerneldump.bin文件，然后选择烧写镜像的Lib下的vitureLinux文件，就可以开始解析；

#######################
	P版本验证		p版本验证有三个组:
platfom平台组
pmu功耗组
DRV组

1、首先是platform脚本验证
1.1、直接就是main4_N.bat运行，不选M是因为M版本跟P版本的系统目录有点不一样，所以选N；
1.2、刚烧好版本的时候，用hibbox导出手机里的日志，日志里就保存了kmscat-log的日志，里面记录了bootime is;
1.3、运行后选择Dallas平台，然后开始测试5次重启的用例；
1.4、替换中间的一些.apk，怕不是最新的；
1.5、测试有modem的用例，直接注释掉，不运行；
1.6、测试中有个用例运行后卡住了，直接在另外一个cmd窗口，敲带&的命令就可以继续运行；
1.7、测试trace那个地方，不要调用他们的脚本，可以调用dump工具来执行;

2、pmu功耗验证
2.1最后搜集日志就行，看日志是不是都PASS了；
2.2执行中有java的错误，忽视不计；

3、驱动用例的验证
3.1、注释掉usb.bat的用例，打开其他protest.bat用例，usb的用例用原来boston的脚本来跑；
3.2、pcui口可以通过getprory来设置，设置是否有pcui口，或者枚举出其他端口，pcui口只能发送at^fblock命令；
3.3、有一条用例，get config.propry的命令，可以枚举端口，如果手机了解到了电脑，就有android.phone显示；
3.4、测试中有一个rmc.bat的脚本，里面的命令是gevent -l的命令，执行后手动触发手机屏幕；
3.5、uart口要先使能uart shell，然后发su命令root，然后发ls等shell命令；
3.6手动测试一下小绿板的操作；








#######################
	P版本验证		p版本验证过程，和遇到的问题;
1、平台组
1.1、测试中注释掉了modem测试用例，成功;
1.2、测试中把call GetLog.bat注释掉，改成call dump.exe没有成功，看看是为什么？
1.3、测试trace解析，选择导出日志的kerneldump.bin文件，提示文件不可用;解决办法是，重新操作一遍，然后在重新导出日志;

2、功耗组
2.1、执行过程中，如果出现了sh ＆命令后，就不需要再输入，如果没有出现然后运行卡在那里，就需要重新输入，等待20分钟，搜集日志;不看搜集的日志，运行过程中也能看到结果，出现cpuidle6和cpuidle7失败;

补充测试1、
echo 0> /sys/devices/system/cpu/cpuX/online    ;
cat  /sys/devices/system/cpu/cpuX/online   ；
echo 1> /sys/devices/system/cpu/cpuX/online    ;
cat  /sys/devices/system/cpu/cpuX/online   ；
(X取值为0-7，可选取不同的x值反复测试)

补充测试2、
cat /sys/devices/system/cpu/cpuX/cpuidle/stateY/usage
x为0-7，Y为0-2
这个预期结果是过段时间看下，结果递增；

3、驱动组
3.1在使用dev1.bat测试存储卡的时候，
storage005测试失败，需要补充测试:
在adb shell中执行:
make_ext4fs /dev/block/bootdevice/by-name/reserved5   ；
mkdir /data/test；
mount -t ext4 /dev/block/bootdevice/by-name/reserved5    /data/test；
mount
这里make_ext4fs改成mke2fs;
3.2、测试uart shell命令
fastboot oem uart6osd enable
fastboot oem uart enable
fastboot oem uart ap 6
这里敲回车没有反应，是小绿板有问题，换一个就成功了;
3.3、枚举升级时区分没有内存卡的小绿板

4、验证结束后告知:
Boston V100R001C50B 100预验证，DRV_PLAT、LPM验证PASS，无新增问题，DRV_DEV验证加上DTS2018071811240单点回归验证pass;没有新增问题，报告已经归档;

