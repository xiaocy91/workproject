	知识点概述	说明	知识点描述

#######################
	sudo命令		ubuntu系统，sudo命令   #执行命令时，预设身份为root来执行，授予这个权限时会要求输入密码

#######################
	repo使用		repo命令：
repo -u init xxxxx/manifest.git  #初始化
repo sync   #拉代码
repo start <newbranchname>  #创建新的分支
git status  #查看更改过的代码
git add *  #添加修改的代码
git commit *   #提交修改的代码
repo remote add <remotename> <url> #设置远程连接仓库
repo push <remotename>  #向服务器提交项目的代码

#######################
	memory导出dump		fastboot端口下，Hibbox抓ddrdump日志，使用的命令：
fastboot oem memory bbox D:\
说明1：fastboot oem ddrdump show   #显示memory下的ddrdump内存块
说明2：fastboot oem memory xxx D:\   #将memory下的ddrdump内存块导出到D盘

#######################
	存储导出dfx		fastboot导出dfx存储文件：
fastboot oem dump dfx D:\dfx.bin  #将dfx存储导出到D盘文件dfx.bin中

#######################
	mount命令		mount命令：
mount -o <filename.iso>  /mnt/cdrom   #将一个iso镜像文件挂载到/mnt/cdrom下

#######################
	pull\push命令		adb pull <remote> <local>   #从安卓端拉文件到本地
adb push <local> <remote>   #从本地推文件到安卓端

#######################
	py2打包python		下载Python对应版本的py2exe，使用这个工具可以将自己的程序打包成exe文件。使用这个工具需要写一个用于打包的setup.py文件（名称可以自己定，不一定是setup.py），写好后在命令提示符界面cd到这个文件的目录，执行命令“python setup.py py2exe”即可打包完成。下面是自己参考其他网友写的，可供参考：
# _*_ coding: utf-8 _*_
import py2exe
from distutils.core import setup

includes = ['encoding', 'encodings.*']
options = {'py2exe':
        {'compressed': 1,
        'optimize': 2,
        'ascii': 1,
        'includes': includes,
        'bundle_files': 1,
        'dll_excludes': ['MSVCP90.dll'],
        }
      }
 
setup(version='1.0.0',
   description='search file',
   name='search file',
   options=options,
   zipfile=None,
   windows=[{'script': 'core\\tool.py', # 需要打包的程序的主文件路径
        'icon_resources': [(1, 'resource\\icon.ico')], # 程序的图标的图片路径
        }],
   )

#######################
	pyinstaller打包python		进入到pyinstaller文件夹，执行：
python pyinstaller.py -F d:\dump.py
说明：-F表示打包成一个文件

#######################
	一个类继承多个类		比如A、B为父类，A、B都有test()方法：
1、子类为class C(A,B)，此时c=C(),c.test()方法使用的写在前面的A类中test()方法
2、子类为class C(B,A)，此时c=C(),c.test()方法使用的写在前面的B类中test()方法


#######################
	运行文件时，加参数		sys.argv是一个参数列表，sys.argv[0]是文件本身

#######################
	字符串中有且仅有回车\n		字符串中只要有字符就不为空，比如在读文件中，当一行没有数据，只是回车，仍然代表有值：
f = file('poem.txt')
# if no mode is specified, 'r'ead mode is assumed by default
while True:
 line = f.readline()
 if len(line) == 0: # Zero length indicates EOF！！！！！！！！！！！！！！！！！！！！！
  break
 print the len is :%s%len(line)
f.close()

#######################
	函数返回值问题		c语言中函数返回0代表运行正常，返回负数（-1）代表运行失败

#######################
	*args，**kargs		def func(*args,**kargs):
 print args:,args
 print kargs:,kargs
func(1,3,7,all={'k':kkkk,'h':hhhhh})
运行结果：
C:\pythontest>funCan.py
args: (1, 3, 7)
kargs: {'all': {'h': 'hhhhh', 'k': 'kkkk'}}

#######################
	lambda匿名函数
中带if-else		lambda表达式，通常是在需要一个函数，但是又不想费神去命名一个函数的场合下使用，也就是指匿名函数
根据参数是否为1 决定s为yes还是no
>>> s = lambda x:yes if x>=1 else no
>>> s(0)
'no'
>>> s(1)
'yes'

#######################
	map函数		map() 会根据提供的函数对指定序列做映射
s = lambda x:yes if x>=1 else no
print map(s,[0,1,2,3,4])
运行结果：
C:\pythontest>danHangFunc.py
['no', 'yes', 'yes', 'yes', 'yes']

#######################
	filter函数		filter()过滤掉不符合条件的元素，返回由符合条件元素组成的新列表。两个参数，第一个为函数，第二个为序列，序列的每个元素作为参数传递给函数进行判，然后返回 True 或 False，最后将返回 True 的元素放到新列表中。
def filter_fun(n):
 if n>1:
  return True
 else:
  return False
print filter(filter_fun,[0,1,2,3,4])
运行结果：
C:\pythontest>danHangFunc.py
[2, 3, 4]

#######################
	Hibbox中ftp.py使用		1、Hibbox中，找到ftp.py，先注释掉os.path.remove(ftp_log.log)文件，然后再注释掉os.path.remove(zip)；
2、然后再ftp.py同级目录下新建一个configs文件夹；
3、然后将ftp_log.log放在hibbox中一个LOg0.9目录下；
4、然后执行ftp.py 加上参数：
Log0.91234335656566666（日志根目录）  199999199999-2301802(hisi_logs下的时间戳文件)  mylog(产生的压缩包文件名称)  /hava/hibox/phonelog(远程服务器路径)
5、然后看到configs下产生了mylog.zip文件，打开该压缩包，可以看到里面有ftp_log.log；
6、因为之前放入的ftp_log.log中有module、responser等信息，所有压缩包里的ftp_log.log也有相关信息，说明ftp.py文件是没有问题的；
7、Hibbox运行的时候，是调用configs下的ftp.exe文件，一开始是怀疑ftp.exe有问题，而ftp.exe是ftp.py编译出来的，所有ftp.py没有问题就代表ftp.exe没有问题；
8、排除ftp.py没有问题，就看hibbox中，导日志结束时，里面把configs中产生的压缩包复制粘贴一份，以免一会时间后被删除，复制出来的日志压缩包里仍然没有module、responser等信息，说明hibbox本身就没有产生数据，是hibbox的问题；

#######################
	traceback模块		import traceback  
try:  
    1/0  
except Exception,e:  
    traceback.print_exc()  
输出结果是
Traceback (most recent call last):
File test_traceback.py, line 3, in <module>
1/0
ZeroDivisionError: integer division or modulo by zero
这样非常直观有利于调试。

1、traceback.print_exc()跟traceback.format_exc()有什么区别呢？
format_exc()返回字符串，print_exc()则直接给打印出来。
即traceback.print_exc()与print traceback.format_exc()效果是一样的。
2、print_exc()还可以接受file参数直接写入到一个文件。比如
traceback.print_exc(file=open('tb.txt','w+'))
写入到tb.txt文件去。

#######################
	compare beyound对比工具		文本对比工具compare beyound，使用方法：
1、打开compare后，创建一个文件夹的对比，左边选择一个目录，右边选择一个目录；
2、选择一个文件或文件夹，右键-select left file to compare,然后，再右键-compare to 选中的文件；
3、选中两个文件或文件夹，右键-compare;
然后开始对比文件

#######################
	代码合入步骤		提交代码步骤
1.首先进入到hione/vender/tools/hibbox/mntn目录；
2.然后repo sync --no--tags同步最新代码；
3!代码同步后用compare和最新的代码对比；
4.repo start 分支名称，建立一个新的分支；
(repo start branchname，等价于git branch branchname加上git checkout branchname，等价于git -b branch branchname。)
5.将修改过的代码合并到最新拉下来的代码；
6使用git status .来查看修改的文件有哪些；然后逐个把修改过的文件打开，使用stripwhitespace来去除空格；
7，然后git add . 添加修改，再git commit .提交修改；
8.repo upload .来提交当前的代码；
(repo upload等价于git push操作，只是git是直接提交到远程仓库，然后repo是提交到代码审核的服务器上，这个涉及到gerrit框架设计。)
8.提交时需要填写单号，描述就是update hibbox version to V271，如果是开发就填feafure，如果是修改缺陷问题提交代码就填debug，让后保存后就自动提交，如果不保存就不提交；
9如果重新修改后，再次提交，单号不变，但是提交时使用git commit -amend。git commit -amend会在最后一次提交的基础上去提交，不会重新提交新的；

#######################
	编译云使用		1、编译云地址：100.106.198.99，账号：fwx505628，密码：fqh8112;
2、增加一个账号：adduser xwx551895，切换用户：su xwx551895;
3、创建目录
创建目录存放hione代码：mkdir br_hisi_wt_trunk_hione/
进入目录：cd br_hisi_wt_trunk_hione/
4、下载主线代码
初始化repo: repo init -u http://10.141.105.139/platform/manifest.git -b br_hisi_wt_trunk_hione -g open-repo-branch=stable -no-repo-verify
同步代码： repo sync -c --no-tags
5、编译版本
../build/envsetup.sh && choosecombo release kirin970 eng normal all arm64 && make - j162>&1 | tee build.log
6、配置Java环境
export JAVA_HOME = /usr/lib/jvm/java-8-openjdk-amd64
export JRE_HOME = /usr/lib/jvm/java-8-openjdk-amd64/jre
export PATH = $JAVA_HOME/bin:$PATH
vim ~/.basrc
vim ~/.bashrc
/etc/apt/source.list
7、将xwx551895添加到用户组
usermod xwx551895 -aG sudo id xwx551895


#######################
	整合工具参数检验	参数检验模块修改意见	参数模块修改意见:
所有的参数:
-s,-k,-m,-p,-d,-l,-h

1.nargs=*,表示任意多个参数:
parse.add_argument(filename,nargs=*,type=init)
说明1:运用在-m和-k和-p上。不输入参数，值为none; 输入参数，不输入值，值为列表且为空; 输入参数，输入值，值为列表且有值！
2.choices选项
说明:在choices[info,debug,]等选项，来限制输入。且默认值为info。
3.requiem=true为必须参数
说明:在该模块没有用！
4.默认参数
default=默认参数
说明:-l和-d都需要设置默认参数。-l默认为info，-d默认为Log。
4.互斥参数
parse=argparse.ArgumentParser()
group=parse.add_mutually_exclusive_group()
group.add_argument(-a,-aa)
group.add_argument(-b,-bb)
添加互斥组，在组里添加互斥参数
说明:-k和-m和-p之间互斥
5.参数不合法的话。是直接报错，还是什么？自定义异常如下:
class ArgError(Exception):
    def __init__(self):
        self.arg=arg
    def __str__(self):
        return self.arg
然后参数出错了就raise ArgError(arg)。


#######################
	bbox.bin文件结构:	bbox.bin文件结构讲解	bbox.bin文件结构:
1、bbox.bin留给AP的，一共8M，每行是512字节，第一行就是给top_head.txt文件的，其中top_head.txt中，因为是64位的手机，每一个内存就是两个字节;
2.bbox.bin文件整体是，第一行信息，预留，ap，剩下是给AC,NOC这些数据，这一共8M；之后就是给其它数据，LMP、vedio音频、monut摄像;
3.top_head.txt是AP第一行数据解析出来的，version一个字节，music一个字节！等等其它;




#######################
		bbox2.0项目hibbox工具适配-代码修改	bboxbin适配代码修改
1.这次版本还是0x202,只是bboxapversion变成了1000b;之前的版本也是0x202,但是ap版本是1000a;
2.这个current version是怎么用的？
3.head_top.py中修改了ap中IRQ中结构，IRQ中有task_info,cpu_info这些信息，然后本次增加了一个diag_info，diag_info之前是percup的，就是说每个cpu该信息都不一样，都会被记录下来;diag_info不是percup的，信息都是一样、公用的;
4.IRQ中所有的task_info、diag_info都加了r_idx和count字段;
5.代码修改
5.1、在ap/hook_head.py中定义，当前head_ringbuffer_format1_0_B=IIIIII72s，还有head_ringbuffer_format1_0_2和
head_ringbuffer_format1_0_4是之前的;
5.2. 在ap/hook_head.py中定义各个字符串，head_ringbuffer=enum(task,cup,diaginfo,max);
5.3、在ap/hook_ringbuffer.py中，定义head_ringbuffer_struct=(iis,ssii,256s);
5.4、在ap/hook_hea.py文件，hook_ringbuffer_obj={
task_info:task_obj;
cpu_info:cpu_obj;
diag_info:diag_obj;
}
5.5在ap/hook_head.py文件中，有两个对象，一个diag_obj，一个新的diag_with_idx_count的对象，并将值赋予给hook_ringbuffer_obj;
5.6在comm/version.py中，version_manage方法中，根据v_hex版本值来判断，是使用新bufferring的对象，还是旧的ringbuffer对象？？？？？？
5.7在arg_parse.py文件中，直接调用v.hook_format()方法，返回所需要的v对象？？？？？


#######################
		bbox2.0项目hibbox工具适配-bbox二进制文件查看	bbox.bin文件查看方法:
1.根据bbox.bin第一行文件解析出来的top_head.txt文件，找到conn位置，diag位置，文件第一行空间为0x200，然后后面预留0x100,所以ap开始的位置是0x300;
2.比如，现在要找conn在文件中的位置，可以看到conn位置为0x7000b20，所以看conn的位置为0x0000b20开始;
3.看diaginfo时，可以直接在文件中搜索关键词diaginfo，然后diaginfo第一行占用了两行办，然后diaginfo后面的所有数据为256s,因为bbox.bin每行为16个字节，所以diaginfo的数据占16行;

#######################
		其他异常修复	bbox2.0项目hibbox版本其他异常修复:
1.适配IRQ中diaginfo，且IRQ中个模块数据新增i_rdx和count字段；
2.新增boardid获取平台，解决miami从670修改到710后产生的检测不到平台的问题；另外，把所有涉及到670的都改成710;
3.解决，识别不到平台，不弹框显示的问题
3.1如何查看版本号
看版本号，比如当前版本为kirin970，打开bbox.bin文件，划到九千多的位置，就是版本号了，直接将970改成710就是成功修改了版本号了。
3.2、检查get_var的PLAT_FORM变量，当离线解析bbox.bin文件时，如果选择了平台，就会调用get_var中的set_plat_form方法，所以当PLAT_FORM有值时，说明已经手动设置过，判断手动设置的平台是否在定义的平台信息中;如果没有值，就弹框提示没有平台;
注意:PLAT_FORM是全局变量，所以弹框选择后是一直有值的，所以，下次弹框前要把值清零！！！

其他修改:
NOC 980适配


#######################
		工具发布	工具发布:
1、parse_script.py中about.py修改版本号为2.7.3；
2、parse_script.py中update.log中，增加版本修改日志；
3.使用ftp.py修改服务器上的version;

#######################
	fseek和ftell函数	bbox2.0项目适配，解析diaginfo	file.seek()可以将文件游标移动到文件的任意位置，本文具体的file.seek()文件游标移动操作方法、
file.seek()方法标准格式是：seek(offset,whence=0)
 offset：开始偏移量，也就是代表需要移动偏移的字节数。 
 whence：给offset参数一个定义，表示要从哪个位置开始偏移；0代表从文件开头开始算起，1代表从当前位置开始算起，2代表从文件末尾算起。
代码： 
f = open('111.py','rb')
print(f.tell()) #0
f.seek(3) #默认为零，从文件开头
print(f.tell()) #3
f.seek(4,1) #1为从当前位置，移动4个字节
print(f.tell()) #7
f.seek(-4,2) #从文件末尾算，移动4个字节
print(f.tell()) #15
#f.tell()方法告知游标的位置


#######################
	pthon列表排序	使用ConfigParse模块产生
debug.conf	 python语言中的列表排序方法有三个：reverse反转/倒序排序、sort正序排序、sorted可以获取排序后的列表
reverse()方法
      将列表中元素反转排序，比如下面这样
      >>> x = [1,5,2,3,4]
      >>> x.reverse()
      >>> x
      [4, 3, 2, 5, 1]
sort()排序方法
      此函数方法对列表内容进行正向排序，排序后的新列表会覆盖原列表（id不变），也就是sort排序方法是直接修改原列表list排序方法
      >>> a = [5,7,6,3,4,1,2]
      >>> a.sort()
      >>> a
      [1, 2, 3, 4, 5, 6, 7]
      有的时候会需要一个排序好的列表，而又想保存原有未排序列表，他们会这么操作,这个时候问题出现了，变量b得到的是一个空值。那么想要得到排序好的列表，又想保留原列表怎么办呢？
      >>> a = [5,7,6,3,4,1,2]
      >>> b = a.sort()
      >>> print b
      None
sorted()方法
      即可以保留原列表，又能得到已经排序好的列表sorted()操作方法如下：
      >>> a = [5,7,6,3,4,1,2]
      >>> b = sorted(a)
      >>> a
      [5, 7, 6, 3, 4, 1, 2]
      >>> b
      [1, 2, 3, 4, 5, 6, 7]
      sorted()方法可以用在任何数据类型的序列中，返回的总是一个列表形式：
      >>> sorted('iplaypython.com')
      ['.', 'a', 'c', 'h', 'i', 'l', 'm', 'n', 'o', 'o', 'p', 'p', 't', 'y', 'y']

#######################
	浅析Python中的struct模块
		在写简单的socket通信代码时，在网络通信当中，大多传递的数据是以二进制流（binary data）存在的。当传递字符串时，不必担心太多的问题，而当传递诸如int、char之类的基本数据的时候，就需要有一种机制将某些特定的结构体类型打包成二进制流的字符串然后再网络传输，而接收端也应该可以通过某种机制进行解包还原出原始的结构体数据。python中的struct模块就提供了这样的机制，该模块的主要作用就是对python基本类型值与用python字符串格式表示的C struct类型间的转化。基本的pack和unpack：
import struct
import binascii
values = (1, 'abc', 2.7)
s = struct.Struct('I3sf')
packed_data = s.pack(*values)
unpacked_data = s.unpack(packed_data)
print 'Original values:', values
print 'Format string :', s.format
print 'Uses :', s.size, 'bytes'
print 'Packed Value :', binascii.hexlify(packed_data)
print 'Unpacked Type :', type(unpacked_data), ' Value:', unpacked_data
输出：
Original values: (1, 'abc', 2.7) 
Format string : I3sf 
Uses : 12 bytes 
Packed Value : 0100000061626300cdcc2c40 
Unpacked Type : <type 'tuple'>  Value: (1, 'abc', 2.700000047683716)
代码中，首先定义了一个元组数据，包含int、string、float三种数据类型，然后定义了struct对象，并制定了format‘I3sf’，I 表示int，3s表示三个字符长度的字符串，f 表示 float。最后通过struct的pack和unpack进行打包和解包。通过输出结果可以发现，value被pack之后，转化为了一段二进制字节串，而unpack可以把该字节串再转换回一个元组，但是值得注意的是对于float的精度发生了改变，这是由一些比如操作系统等客观因素所决定的。打包之后的数据所占用的字节数与C语言中的struct十分相似。定义format可以参照官方api提供的对照表：
			2、字节顺序
   可以指定大端存储、小端存储等特定的字节顺序，对于底层通信的字节顺序是十分重要的，不同的字节顺序和存储方式也会导致字节大小的不同。在format字符串前面加上特定的符号即可以表示不同的字节顺序存储方式，例如采用小端存储 s = struct.Struct(‘<I3sf’)就可以了。

#######################
	scp命令使用		
1#从远程服务器中下载数据文件到本地主机
如果你想从远程主机host1中的/tmp/目录下拷贝test1 文件到本地主机的/tmp目录，那么可以在本地主机的命令行下面
输入命令：
scp root@host1:/tmp/test1 /tmp
 
#2 从远程服务器中拷贝目录文件到本地主机下面
当你从远程主机中拷贝一个目录的时候，你需要给scp命令传入一个“-r“ 选项，这样scp命令就会将远程主机下面的整个目录的文件都拷贝的本地主机下。
输入下面的命令：
scp -r root@hots1:/tmp  /tmp
这个命令就会把host1主机下的tmp目录拷贝到本地主机的/tmp目录下


#######################
	提交代码步骤		提交代码步骤
1.首先进入到hione/vender/tools/hibbox/mntn目录；
2.然后repo sync --no--tags同步最新代码；
3!代码同步后用compare和最新的代码对比；
4.repo start 分支名称，建立一个新的分支；
(repo start branchname，等价于git branch branchname加上git checkout branchname，等价于git -b branch branchname。)
5.将修改过的代码合并到最新拉下来的代码；
6使用git status .来查看修改的文件有哪些；然后逐个把修改过的文件打开，使用stripwhitespace来去除空格；
7，然后git add . 添加修改，再git commit .提交修改；
8.repo upload .来提交当前的代码；
(repo upload等价于git push操作，只是git是直接提交到远程仓库，然后repo是提交到代码审核的服务器上，这个涉及到gerrit框架设计。)
8.提交时需要填写单号，描述就是update hibbox version to V271，如果是开发就填feafure，如果是修改缺陷问题提交代码就填debug，让后保存后就自动提交，如果不保存就不提交；
9如果重新修改后，再次提交，单号不变，但是提交时使用git commit -amend。git commit -amend会在最后一次提交的基础上去提交，不会重新提交新的；

#######################
	logging模块	python logging 替代print 输出内容到控制台和重定向到文件	1、python logging 替代print 输出内容到控制台和重定向到文件
import logging  
logging.debug('debug message')  
logging.info('info message')  
logging.warning('warning message')  
logging.error('error message')  
logging.critical('critical message')  
输出：
WARNING:root:warning message
ERROR:root:error message
CRITICAL:root:critical message
2、默认情况下python的logging模块将日志打印到了标准输出中，且只显示了大于等于WARNING级别的日志；
3、这说明默认的日志级别设置为WARNING（日志级别等级CRITICAL > ERROR > WARNING > INFO > DEBUG > NOTSET）；

#######################
	二进制文件跳转到指定地址	notepad++中ctrl+g快捷键使用	notepad++中，二进制文件地址定位ce17；ctrl+g可以跳到指定地址；

#######################
	vars函数使用	python查看内置函数和属性的方法	python查看内置函数和属性的方法
dir():默认打印当前模块的所有属性，如果传一个对象参数则打印当前对象的属性
vars():默认打印当前模块的所有属性，如果传一个对象参数则打印当前对象的属性


#######################
	维测工具遇到的问题:		维测工具遇到的问题:
1、 logging模块打印输出到textcontrl控件，将textcontrl对象传入到logging模块，然后输出打印;
2、 wxpython文件拖拽解析的实现;使用drag实现;
3、子线程修改主线程中的图形界面。使用pubsub模块，子线程使用CallAfter发送消息，主线程使用获取消息后更新界面;
4、python报错，keyerror,setmosize
QT designer中mainwindow.ui控件调用
QT designer中帮助文档使用;

#######################
	git使用		repo start brach --all
git cherry-pick  xxx
关于git中cherry-pick的使用，选择一部分提交的代码合并到另一个分支

#######################
	git使用		repo upload 时报错

$ repo upload
如果有多个项目同时进行了改动，为了避免出错，会弹出编辑器显示有改动需要提交的项目列表。将希望提交的分支前的注释去掉，就可以将该项目的分支执行推送动作；
# Uncomment the branches to upload:
#
# project test/test1/:
branch jiangxin ( 1 commit, Mon Oct 25 18:04:51 2010 +0800):
#         4f941239 0.2-dev -> 0.2-jiangxin
#
# project test/test2/:
branch jiangxin ( 1 commit, Mon Oct 25 18:06:51 2010 +0800):
#         86683ece 0.2-dev -> 0.2-jiangxin


#######################
	进程线程相关问题		进程线程相关问题
1、线程或进程间通信
from queue import Queue
q = Queue()
q.put(value)
q.get(value)

2、进程池
from multiprocessing import pool
import qu
p = pool(4)
pool.apply_async

3、线程池
3.1、2.7中使用Threapool，需要pip install Threadpool安装;
3.2、3.0以上内置ThreadpoolExecute;
from concurrent.features import ThreadpoolExecute
pool = ThreadpoolExecute(10)
pool.submit(func,args)


#######################
	问题		问题，重要:
1.0x203在bbox中是怎么改的？

#######################
	线程与进程学习		线程与进程学习
1.线程
from threading import Thread
class MyThread(Thread):
    def __init__(self,func,args,textctrl,que):
        Thread.__init__(self)
         self.func=func
         self.args=args
         self.textctrl = textctrl
         self.que=que

2.线程池
2.1.Python2.7需要安装pip install threadpool，然后导入:
from threadpool import ThreadPool;

2.2.Python3.0以上，自带了ThreadPoolExecutor，需要导入:
from concurrent.features import ThreadPoolExecutor;

2.3.现在学习使用Threadpool:
pool = ThreadPool(4)
requests=pool.makerequests(func,args)
for req in requests:
   pool.putrequest(req)
pool.wait()



#######################
	线程与进程学习		线程与进程学习 
4.进程
from multiprocessing import process
p=process(func,args)
p.start
5.进程池
from multiprocessing import pool
p=pool(4)
for i in range(16):
    p.apply_async(func,args)
p.close()
p.join()

6.线程、线程间通信queue
from Queue import Queue

#######################
	拓展学习	拓展整理下正则表达式，开源日志系统	
做开发就是很忙的，我现在做公司监控系统的开发，交付压力也不小;
主要是你做的东西有点杂，不成系统;
这个测试工具，应该涉及到兼容多个平台，正则匹配和日志处理的东西。可以拓展整理下正则表达式，开源日志系统;

#######################
	hibbox问题严重性		hibbox问题严重性
只要导出日志没出问题;
只要解析没出问题;
其他都是小问题！

#######################
	Excel操作		写Excel我们需要使用第三方库xlwt，和xlrd一样，xlrd表示read xls，xlwt表示write xls

#######################
	wxpython的拖拽的使用：		wxpython的拖拽的使用：
import wx
class FileDropTarget(wx.FileDropTarget):
    def __init__(self, window):
        wx.FileDropTarget.__init__(self)
        self.window = window

    def OnDropFiles(self,  x,  y, fileNames):
        self.window.SetValue(str(fileNames))
class MyFrame(wx.Frame):

    def __init__(self, parent, id):

        wx.Frame.__init__(self, parent, id, title = u'拖放例子', size = (778,494))
        panel=wx.Panel(self)
        textBox=wx.TextCtrl(panel, pos = (50, 50),size =(300, 200))
        dropTarget = FileDropTarget(textBox)
        textBox.SetDropTarget( dropTarget )
if __name__=='__main__':
    app=wx.App()
    frame=MyFrame(parent=None,id=-1)
    frame.Show(True)
    app.MainLoop()

#######################
	C语言中#ifdef，#ifndef和#endif的作用：
1、用于注释掉一段代码
2、防止头文件重复包含		C语言中#ifdef，#ifndef和#endif的作用

1、用于注释掉一段代码
编写程序时，需要看到一系列的调试代码，但是发给客户时，客户不希望看到什么什么OK的代码，所以我们希望能很容易地注释掉这段代码。 
这时需要用到预处理指令 #ifdef 和 #endif ：
#include <stdio.h>
#define CONFIG_DEBUG 
int main(){
    FILE *fp;
    fp=fopen(D:\\DEV\\test.txt,r); 
    if(NULL==fp){
        printf(error!);
    }
#ifdef CONFIG_DEBUG 
    printf(open test.txt ok);
#endif
    return 0;
}
如果文件在那个路径没错的话，将会打印如下信息： 
open test.txt ok
如果不想看到这样的调试信息，注释掉#define CONFIG_DEBUG这句就行。
			2、防止头文件重复包含
a.h
#include <stdio.h>
#include b.h

b.h
#include a.h

c.c
#include a.h
#include b.h
int main(){
    printf(Hello!);
}
如果程序是这样写，编译器就会出现Error #include nested too deeply的错误。 
因为这里 b.h 和 a.h 都互相包含，c.c文件在include的时候重复include了a.h，我们希望c.c文件中执行#include b.h的时候 b.h 能进行判断，如果没有#include a.h则include，如果已经include了，则不再重复定义。

可以将b.h修改为：
#ifndef _A_H
#define _A_H 
#include a.h
#endif

#######################
	copy.copy和copy.deepcopy的使用		1、copy.copy和copy.deepcopy的使用？
copy.copy为浅copy，只复制了第一层数据，子列表是没有copy；copy.deepcopy，复制就不会改变子列表的值了，是因为deepcopy将子列表也复制了一份。
例如：
import copy
list = ['beijing','tianjin','hebei',['neimeng','xinjiang'],'wuhan']
list_copy = copy.deepcopy(list)
list[3][0] = 'taiwan'
print(list)
print(list_copy)
结果显示：
['beijing', 'tianjin', 'hebei', ['taiwan', 'xinjiang'], 'wuhan']
['beijing', 'tianjin', 'hebei', ['neimeng', 'xinjiang'], 'wuhan']

2、class类中全局变量
class类中全局变量，是所有对象共用的，每个类都可以对全局变量进行修改；如果要每个对象的全局变量互不影响，需要使用copy.deepcopy。

#######################
	hibbox发布流程		hibbox发布流程
1、Hibbox新增需求，需要补充测试用例;
2、在update_log.py文件中添加更新日志，在about.py中升下版本号；
3、运行setup.py，将Hibbox.py打包成Hibbox.exe，打包好的文件存放在工程根目录\Hibbox\Hibbox.exe下;
4、确认ftp.py文件是否有修改，修改过后，需要使用Pyinstaller重新打包ftp.py为ftp.exe。打包好的ftp.exe放在ftp.py所在目录下dist\ftp.exe下。
5、将hibbox.exe、configs\ftp.exe、configs\dump.exe、configs\responsibily.xlsx、configs\update.exe文件打包成Hibbox_版本号_日期.rar格式，上传到；
6、使用update_version.py更新hibbox版本；更新版本后需要测试是否会提示自动升级；

#######################
	拖拽文件进去的drop使用		
2、解析的问题
拖拽文件进去的drop使用

#######################
	complie的使用		complie(blackbox_mntn_test_004.py,single)
