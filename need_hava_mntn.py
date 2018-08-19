序号	时间	问题	实现

**1
	2018/6/1	
dmesg日志被冲的异常
	

1、在startup_mntn_test_0002.py中找，因为用例调用了searchKey方法，searchKey方法在util.py中，在searchKey中先使用adb shell dmesg，在dmesg中找关键字，找不到就在/data/log/android_logskmsgcat-log中面找，最后返回结果;kmsgcat日志中要找到时间突变的位置，只找从结尾开始到时间突变为止的内容;
2、全局查找，在.Get()判断下面中，有search方法，添加查找kmsgcat日志的方法;
3.然后需要在startup_mntn_test_0002用例启动的时候，需要做删除kmsgcat-log日志的操作，以免之前的日志对现在的测试有影响，在pylib/startup.py中添加删除日志的操作;


	2018/6/1	
关闭狗测试等待时间不够
	
修改了startup_mntn_test_0006,在安卓开启和关闭狗时，代码为if show: sleep(5)，因为fastboot重启需要等待5秒，然后用例就pass了;

	2018/6/1	
hava平台用例失败分析方法


	
hava问题分析:
1.任务一:设备在线，但是fastboot oem boot起不来;
2.任务二:设备不在线，挂掉了，startup_mntn_0006执行后单板挂掉了。最后林俊杰定位为用例问题，用例中watch_dog中第十三和十四位该改成0;
3.任务三:设备在线，查看dmesg log都是空的。那怎么办，在执行了adb命令后突然就killed了，那有可能是超时了，看看用例开始执行时间，到最后挂掉的时间，一共花了4个小时，因为设置了最长执行时间，所以超时了;
4.任务四:设备在线，但是log目录下是空的，没有找到dmesg log，看用例中，如果找到关键字就通过，如果没有找到关键字就把日志记录到dmesg中，但是这里teardown部分写的log是只生成一个目录，没有往目录里写日志文件，那设计用例是不是有问题？


**2
	2018/6/20	hava用例utils.py中SearchKey找关键字方法修改	hava用例utils.py中SearchKey方法修改
错误：
错误1：突变位置判处
 utils.py中找关键字方法修改，突变位置错误，因为突变位置是时间变成0,所以当前行为0是正常的，上一行时间不为0时，为大于0的时间，当前行小于上一行，就是突变了;

错误2：文件不存在，try..catch不起作用
查找关键字utils.py，try...catch不起作用，因为subprocess.Popen(shell=True，cmd,stuout=subprocess.PIPE，stderr=subprocess.stdout)，这句子进程的错误也会输出，当找不到kmsgcat-log时，不会报出异常，所以这样写错误;另外，debug运行不会出错，正常运行就出错了，因为debug运行时读文件时已经生成了，正常运行比较快，读文件时文件还没有生成;

错误3：执行命令没考虑多个单板
utils.py中找关键字方法，一个单板和多个单板的问题，不要自己写subprocess.Popen执行命令，要用自带的self.EXE(cmd)方法，自带方法将命令处理过，将fastboot和adb命令加了sn号;

	2018/6/20	关键字标签改变	关键字由ecall]t=0xffff变成ecall][blackbox]t=0xffff;用例中，修改了ecall中关关键字，ecall]t=0xffff为ecall]\S*t=0xffff;
	2018/6/20	
hisi_logs/ap_log/dmesg_ramops_0文件不生成的问题，是因为生成这个文件时，cpu没有拿到锁;	
知识点1:Linux Kernel之spin_lock之ARM64实现

函数arch_spin_lock()实现：
static inline void arch_spin_lock(arch_spinlock_t *lock){
 unsigned int tmp;
 arch_spinlock_t lockval, newval;
 asm volatile(
 ARM64_LSE_ATOMIC_INSN(
 prfm pstl1strm, %3\n
1: ldaxr %w0, %3\n
 add %w1, %w0, %w5\n
 stxr %w2, %w1, %3\n
 cbnz %w2, 1b\n,
 mov %w2, %w5\n
 ldadda %w2, %w0, %3\n
 __nops(3)
 )
 eor %w1, %w0, %w0, ror #16\n
 cbz %w1, 3f\n
 sevl\n
2: wfe\n
 ldaxrh %w2, %4\n
 eor %w1, %w2, %w0, lsr #16\n
 cbnz %w1, 2b\n
3:
 : =&r (lockval), =&r (newval), =&r (tmp), +Q (*lock)
 : Q (lock->owner), I (1 << TICKET_SHIFT)
说明1:cbnz是不等于zero，cbz是等于zero;1b表示back到第一步，3f表示调到front的第3步;这就是cpu获取锁的循环，如果没有得到锁，一直在这里循环;



	2018/6/20	hisi_logs/ap_log/dmesg_ramops_0文件不生成的问题，是因为生成这个文件时，cpu没有拿到锁;	知识点2：中断级别
EL0、EL1、EL2、EL3中断级别中，数字越大，级别越高;应用程序中断的级别为EL0,最低;复位的中断级别为EL3,最高，当发生这个中断后，cpu就不管其他的了;
	2018/6/20	hisi_logs/ap_log/dmesg_ramops_0文件不生成的问题，是因为生成这个文件时，cpu没有拿到锁;	知识点3：狗是什么？
多核中，有多多个cpu，但每个cpu同时只能做一件事，遛狗只有cpu0做这件事；执行adb shell ecall rea_u32 0执行复位，就是让cpu0一直在循环里没有出来，这样cpu0就没法遛狗，这种情况下cpu出现真死和假死，如果是假死就重新去唤醒cpu，一般是真死，如果是真死，狗就直接去按电源，所以就出现单板重启出现复位；

**3
	2018/6/20	sarchkey方法中supprocess.Popen中有参数stderr不会抛出异常；
单独写的执行命令的方法错误，系统自带的self.EXE(cmd)方法中有sn号；	hava用例utils.py中SearchKey方法修改
1. utils.py中找关键字方法修改，突变位置错误，因为突变位置是时间变成0,所以当当前行是正常的，上一行时间为0时，当前行小于上一行，就是突变了;

2.查找关键字utils.py，try...catch不起作用，因为subprocess.Popen(shell=True，cmd,stuout=subprocess.PIPE，stderr=subprocess.stdout)，这句子进程的错误也会输出，当找不到kmsgcat-log时，不会报出异常，所以这样写错误;另外，debug运行不会出错，正常运行就出错了，因为debug运行时读文件时已经生成了，正常运行比较快，读文件时文件还没有生成;

3.utils.py中找关键字方法，一个单板和多个单板的问题，不要自己写subprocess.Popen执行命令，要用自带的self.EXE(cmd)方法，自带方法将命令处理过，将fastboot和adb命令加了sn号;

4.修改了ecall中关关键字，ecall]t=0xffff为ecall]\S*t=0xffff;

**4
		hava解决问题:dmesg_ramops_0文件不生成的问题；	维测hava查看hisi_logs/ap_log/dmesg_ramops_0文件不生成的问题，是因为生成这个文件时，cpu没有拿到锁;

1.Linux Kernel之spin_lock之ARM64实现
函数arch_spin_lock()实现：
static inline void arch_spin_lock(arch_spinlock_t *lock)
{
 unsigned int tmp;
 arch_spinlock_t lockval, newval;
 asm volatile(
 prfm pstl1strm, %3\n
1: ldaxr %w0, %3\n
 add %w1, %w0, %w5\n
 stxr %w2, %w1, %3\n
 cbnz %w2, 1b\n,
 /* LSE atomics */
 mov %w2, %w5\n
 ldadda %w2, %w0, %3\n
 __nops(3)
 )
 sevl\n
2: wfe\n
 ldaxrh %w2, %4\n
 eor %w1, %w2, %w0, lsr #16\n
 cbnz %w1, 2b\n
3:
 : =&r (lockval), =&r (newval), =&r (tmp), +Q (*lock)
 : Q (lock->owner), I (1 << TICKET_SHIFT)
 : m





			说明1:cbnz是不等于zero，cbz是等于zero;1b表示back到第一步，3f表示调到front的第3步;这就是cpu获取锁的循环，如果没有得到锁，一直在这里循环;
2.EL0、EL1、EL2、EL3中断级别中，数字越大，级别越高;应用程序中断的级别为EL0,最低;复位的中断级别为EL3,最高，当发生这个中断后，cpu就不管其他的了;
3.狗是什么？多核中，有多多个cpu，但每个cpu同时只能做一件事，一个cpu在3ms就要把所有的进程跑一遍，遛狗只要每6s遛一次就可以，遛狗只有cpu0做这件事；执行adb shell ecall rea_u32 0执行复位，就是让cpu0一直在循环里没有出来，这样cpu0就没法遛狗，这种情况下cpu出现真死和假死，如果是假死就重新去唤醒cpu，一般是真死，如果是真死，狗就直接去按电源，所以就出现单板重启出现复位；

**5
	2018/8/15		fastboot数据适配
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
