时间	需求类型	需求详情		问题		代码实现
2018/3/22	
Hibbox需求

	
1、弹框增加数据分析平台链接；
2、ftp_log.log中增加debug字段；
	
问题>>>>>：

	
status:closed
1、责任人查询错误。
读取excel表格，步长不应该为5，儿应该为4，导致读取到责任人数据不对；
2、解析lpm3.bin出问题。
它数据本身有问题，跟工具无关；
	
实现>>>>>：
	
panel画板和textctrl元素绑定bind事件时，id不能重复，这里id设置为-1,系统会自动分配id

2018/4/3	
Hibbox需求
	
CONN版本适配
	
问题>>>>>：

	
status:in process
1、多个bbox解析问题
hibbox无法同时解析多个版本的bbox.bin函数，因为每次解析时是传入的文件夹，应该改成以单个文件传入的方式，一个文件解析完了，再解析另外一个，不能同时解析多个，这样变量共用，会出问题
	
实现>>>>>：
	
版本兼容性技巧：
1、用一个类专门存版本信息，版本信息的数据结构要清晰：
hibbox_version0=0x20
hibbox_version1=0x21
hibbox_version1=0x22
ap_version9=9
ap_vrsion10=10
version={hibbox_version0:{xxx,xxx,xxx,xxx},
         hibbox_version1:{
          ap_version9:{xxx,xxx},
          ap_version10:{xxx,xxx}
          },
         hibbox_version2:{xxxx,xxxx,xxx,xxx}
         }
2、要向上兼容,要用大于等于：
if version>=hibbox_version0：
elif version>=hibbox_version1:
else:




2018/4/25	
dump需求
	
1、dump增加删除日志功能；
2、dump增加生成责任人blame.txt，生成上传日志ftp_log.log；
	
问题>>>>>：

	
status:in process
hiBbox中ftp_log中生成责任人desc、责任人工号num有问题
	
实现>>>>>：
	
1、读取excel时，将第一个行做为标题，单独存放在一个列表：
title=[type,desc,existsub,miami,chicago,boston]
其中，boston型号为3670，miami为6260
2、re匹配功能，匹配os.walk下所有文件

						需求1*
删除日志功能直接在dump.py中修改，增加remove参数，执行命令：
-s=0123ABCDEF remove all    #可以删除全部日志
-s=0123ABCDEF remove hisi_logs,lpm3  #可以选择性的删除hisi_logs,lpm3日志
						
需求2*
1、在util下存放一个configs/responser.xls表，表中包括主类型、子类型，新增加一个xlstopy.py文件，将responser.xls转化为responser.py文件，responser.py存放resetType数据和subResetType数据；
2、使用gtsheet.py文件来查询responser.py文件中的数据；
3、使用blame.py文件来读取/data/hisi_log/history.log文件的最后一行，将最后一行的数据分离出来，通过gtsheet.py来查询responser.py中责任人数据，然后写入blame.txt中；
3、使用keyinfo.py文件中，设置各种ip、sn号、die_id、rom、ddr信息，然后生成base_log.log文件；
4、使用keyinfo.py文件中信息和获取blame中数据，合成一个ftp_log.log文件；

						
import os
cmd=
map=[ 
    {name:data,             arg:('adb shell cat /data/a.txt|grep aa ',),func:delData($arg$) },
    ]
def delData(cmd):
    print come delData
    print os.system(cmd)
for i in map:
    if i.get(name):
        if i.get(arg):
            #cmd的格式为'adb shell cat /data/a.txt|grep aa '
            #当列表中只有一个元素时，执行.join方法没有任何变化
            cmd+='\''+'\',\''.join(i.get(arg))+'\''
            cmd=i.get(func).replace($arg$,cmd)
            eval(cmd)

2018/5/25	Hibbox需求	
hibbox2.0项目hibbox工具适配:
1、IRQ中diaginfo;
2、top_head.txt适配excetion_trace;
3、top_head.txt适配area_s;
	
问题>>>>>：

	
status:closed
1、bbox.bin应该二进制方式打开文件；
2、c语言结构体中使用char存放int类型，节省空间；
3、area_s中fomat为QI4X，必须有4X进行补齐；
	
实现>>>>>：
	
hibbox适配diaginfo:
修改ap/hook_head.py和comm/version.py文件，增加diaginfo信息

						
hibbox适配林俊杰的bbox.bin：
1、林俊杰给的bbox.bin文件解析报错，说读取的struct.unpack时提示字符串长度不够258。
2.定位到解析area_s时出的错误
2.1通过lseek找fd起始位置，通过read以后，在lseek看文件位置，可以看到开始位置是224(即E0)，calsize函数执行长度为272，这里意思是area_s数据占17行，每行16字节，16*17就是272啊，最后读完后文件位置为224+272=496(即1F0)，代表是没有错的！
2.2.既然没有错，是为什么呢？解析之前的bbox.bin就没有问题呢？最后找到是文件打开方式不对，二进制打开才行！
3.还有内核中会用char存int
u8类型可能是假字符串，它是把int存在char中，为了省空间。存了一个\x1f，实际1f是31，使用方法ord(\x1f)就等于31，31就是数字1的IISC码，字符1转成数字1就是用ord(\1f)-ord(0)???
4.area_s的format格式为QI4x，4x为自动补齐！否则会影响clear_text的解析！


						
修改了责任人表中异常复位类型对应的责任人

						
miami平台，所有版本670都改成了710

						
hibbox导出vendor日志功能已经有了


						
其他功能修复：
1、增加top_head.txt中解析area_s;
2、NOC增加NOC 980.py

						
debug设置保存后，不再弹框提示：
使用configparse模块，配置文件保存在configs/debug.conf

		hibbox2.0项目hibbox工具适配（补充）		问题：
1、检测不到平台，不弹框显示；
2、检测到平台，使其检测到平台；		bbox2.0项目hibbox版本适配及发布:
1.适配IRQ中diaginfo，且IRQ中个模块数据新增i_rdx和count字段；
2.新增boardid获取平台，解决miami从670修改到710后产生的检测不到平台的问题；另外，把所有涉及到670的都改成710;
3.解决，识别不到平台，不弹框显示的问题
3.1如何查看版本号
看版本号，比如当前版本为kirin970，打开bbox.bin文件，划到九千多的位置，就是版本号了，直接将970改成710就是成功修改了版本号了。
3.2、检查get_var的PLAT_FORM变量，当离线解析bbox.bin文件时，如果选择了平台，就会调用get_var中的set_plat_form方法，所以当PLAT_FORM有值时，说明已经手动设置过，判断手动设置的平台是否在定义的平台信息中;如果没有值，就弹框提示没有平台;
注意:PLAT_FORM是全局变量，所以弹框选择后是一直有值的，所以，下次弹框前要把值清零！！！


其他修改:
NOC 980适配

工具发布:
1、parse_script.py中about.py修改版本号为2.7.3；
2、parse_script.py中update.log中，增加版本修改日志；
3.使用ftp.py修改服务器上的version;
2018/5/27	
dump需求

	
dump中保持跟hibbox工具一致：
1、导出/data/vendor/log日志，删除vendor日志;
2、miami平台670变成710；
3、异常复位责任人修改；
	
问题>>>>>：

	
closed:
1、导出vendor日志后，目录为/18_vendor_log，多了一个斜杠；
2、linux版本中dump脚本没有更新，打包错误；elf.fastboot变量没有定义就使用；
3、无法导出vendor日志。dump.py中ddrdump方法中，ELEM.ANDROID_VERSION版本没有获取，根据版本过滤的args参数没有vendor，所以后面没有导出vendor日志；

	
实现>>>>>：
	1、打包错误：
1.1、vendor日志无法导出，因为打包错误，linux上代码没有更新，需要把代码放在linux上，然后网络映射到本地；
1.2、dump导出fastboot日志报错，因为self.fastboot变量没有定义就使用;

2、vendor日志缺失
2.1、修改了logitems中变量后并没有成功导出，把8.1.0改成P版本还是没有导出vendor日志;
2.2、dump中do方法中getlog中，因为在过滤ANDROID_VERSION=P时，此时ANDROID_VERSION还是默认值N，此时过滤出来的cmdplist是不对的，所以把ANDROID_VERSION的判断提前；
4.2、需要把ELEM.ANDROID_VERSION的判断提前到dump.py中，在ddrdump方法中添加判断版本的方法，但是在fastboot模式是不能执行adb get property来获取版本8.1.0的，所以，如果是fastboot模式，必须先进去到adb来判断版本，然后再导日志;
4.3.在dump.py中增加，ddrdump中，如果是fastboot状态就重启到adb下，获取版本号，并设置ELEM中版本号;.然后根据memory还是kernel或者是没有参数，这里只说kernel的条件下，根据版本号来过滤参数args，此时版本号已经为8.1.0的P版本，过滤的参数就包含了vendor日志;之前就是版本不对，导致参数过滤不到vendor日志;

2018/6/20	工具难题	之前曾经工作中遇到最大的几个问题	
问题>>>>>：

	之前曾经工作中遇到最大的几个问题:
1.hibbox中全选;
2.hibbox跟数据库的兼容问题;
3.hibbox用pyintaller或者py2.exe打包;
4.dump工具在hava平台，因为日志太大卡死的问题;是因为执行命令时，如果命令不成功就一直等待，需要另外开一个线程subprocess.popen来执行命令;		
2018/6/29	Hibbox需求	林俊杰cupidle.txt、lrq.txt、cup_on_off.txt等文件转换	
问题>>>>>：

	ftp_log.log中换行符在数据中间：
在sql.py中像ftp_log.log中添加了数据，在另外一个中blame和ftp_log方法中有写入数据，调用这两个写入的地方在utf_addr_version中		1、ftp.py被打包成了ftp.exe执行，系统调用config/ftp.exe，而不是调用ftp.py；整个hibbox项目用py2打包，只有ftp.py用pyinstaller打包；
2018/7/8	Hibbox需求	林俊杰Exception解析	
问题>>>>>：

	1、copy.deepcopy的使用？
class类中全局变量，是所有对象共用的，每个类都可以对全局变量进行修改；如果要每个对象的全局变量互不影响，需要使用copy.deepcopy。

2、数据是否写满：
在parse_one_cpu时，要根据头部的self.full来判断文件是否写满。如果写满了取数据的次数为(0,self.maxnum)，并且读取的全部数据需要重新排序，即datalist=datalist[self.rear:]+datalist[:self.rear]；如果没有写满，取数据的次数为(0,self.rear)；		底软C代码中，数据结构u8、u16、u32分别代表：
u8 是 unsigned char
u16 是 unsigned short
u32 是 unsigned int
						Python 十进制转二进制、八进制、十六进制
dec = int(input(输入数字：))

print(十进制数为：, dec)
print(转换为二进制为：, bin(dec))
print(转换为八进制为：, oct(dec))
print(转换为十六进制为：, hex(dec))
执行以上代码输出结果为：
输入数字：5
十进制数为：5
转换为二进制为： 0b101
转换为八进制为： 0o5
转换为十六进制为： 0x5
						extrace解析
1.Apexc 0x200大小、BL31exc 0x100大小，数据结构一样；BL31smc 0x3F00大小；
2.它们的头部都是一样的，使用hisiap_ring_buffer这个结构来存放；只是数据单元部分有点区别；
3.APexc、BL31exc是分cpu的，BL31smc是不分cpu的；
4.通过shift.BBOX_SHIFT.shift(EXTRACE)方法来获取基地址0x7c000；
5.然后开始解析，需要在hisiap_ring_buffer这个类里面添加解析方法，方法为parse，传入一个对象，对象包含参数addr、offset，读取的数据存放到hisiap_ring_buffer，这样头部就初始化好了；根据头部信息来解析这个数据段；

						repr() 函数将对象转化为供解释器读取的形式extrace解析
						ord()函数主要用来返回对应字符的ascii码，chr()主要用来表示ascii码对应的字符他的输入时数字，可以用十进制，也可以用十六进制。
						Exception适配遇到的问题
1、struct.unpack中使用X补全
1.1补全的例子
  string = 'test astring'  
 format = '5s 4x 3s'  
 print struct.unpack(format, string) # ('test ', 'ing')  
1.2 在smc中为什么要5X补全
smc的数据结构是u64、u8、u8、u8和一个union中包含u64或者u32，只包含其中一个；
2、deep.copy的使用？？
3、在解析中ringbuffer和ringbuffer_with_id_count两个类，两个类中都有perse_to_head和perse_one_cpu方法，所以这两个方法是公共的，所以最好用继承的方式来用，而不要重复写这个方法；
4、在parse_one_cpu时，要根据头部的self.full来判断文件是否写满。如果写满了取数据的次数为(0,self.maxnum)，并且读取的全部数据需要重新排序，即datalist=datalist[self.rear:]+datalist[:self.rear]；如果没有写满，取数据的次数为(0,self.rear)；
5.round方法可以保留小数点后面几位，round(num,num_digits)，num_digits是四舍五入保留的小数位；
6.zip函数可以将多个列表压缩为字典；

2018/7/8	Hibbox需求	袁旦，ftp.log生成后不删除	
问题>>>>>：

	ftp.py修改后，需要重新打包成ftp.exe		1.ftp这一块的问题
1.1、ftp.py中，发送消息message中，引入了pika第三方库，所以要用pyinstaller打包成ftp.exe，因为使用.py时，参数不能太长，有长度限制！
1.2、注释掉ftp中os.path.exists('ftp.log')后，运行hibbox还是没有产生ftp.log文件；是因为没有将ftp.py重新打包成ftp.exe，hibbox运行中实际调用的ftp.exe，而不是调用ftp.py文件！

2018/7/17	Hibbox需求	林俊杰，kerneldump解析	
问题>>>>>：

	seg的结构体就是u64 addr、u64 size，这个seg的size不包含seg头部的大小		kerneldump解析
1、在viewttool/figure.py中，kerneldump在导出时，首先去看kerneldump有几个，因为一个kerneldump文件不能大于500M，导出后又把多个kerneldump文件合并成一个kerneldump文件；
2、kerneldump是从1000地址开始的，kerldump的头中包含seg表示seg的个数，size表示seg的大小，是所有seg还是单个seg大小？size应该是所有seg的大小，这个size是不包含kerneldump的头的！
3、seg的结构体就是u64 addr、u64 size，这个seg的size不包含seg头部的大小；
2018/8/17	Hibbox需求	林俊杰，lpm3.bin解析	
问题>>>>>：

	1、数据格式是
cpu0、cpu1……cpun
ls0-sp-0、ls0-sp-1……ls0-sp-n
ls1-sp-0、ls1-sp-1……ls1-sp-n
2、08 0a c5 c5中，最左边的0不能舍掉		lpm3.bin解析
1、u64位是8字节，u32是4字节；
2、Python中file.read(number)，这里number代表的是字节；
3、要解析的结构体
struct{
u32 acore_pc[CPU_CORE_NUM*2];
u32 acore_ls0_p[CPU_CORE_NUM*2]；
u32 acore_ls1_p[CPU_CORE_NUM*2]；
}
4、修改的文件lmp3/lmp3_parse.py文件。fomat的格式是Q*8，数据格式是
cpu0、cpu1……cpun
ls0-sp-0、ls0-sp-1……ls0-sp-n
ls1-sp-0、ls1-sp-1……ls1-sp-n
5、分三次读出数据
cpu = struct.unpack(fomat,file.read(struct.caculsize(fomat)))
ls0 = struct.unpack(fomat,file.read(struct.caculsize(fomat)))
ls1 = struct.unpack(fomat,file.read(struct.caculsize(fomat)))
6、corename为(cpu,ls0,ls1)，需要将corename和cpu、ls0、ls1数据一一对应起来，所以使用zip函数将他们压缩起来。
((cpu,cpu),(ls0,ls0),(ls1,ls1))
7、然后根据cpu数据的高八位、低八位来来判断cpu是否异常，来决定是否显示后面的ls0和ls1的数据。
						hibbox无法导出data/log/logservice下文件
1、原因:logservice下文件的文件名中包含空格，导致在puITem函数中，执行'adb shell ls -l /data/log'后，得到的所有文件为:
-xxx ……  04:46  Ea218 xy.zip
因为在处理这行数据的时候，直接split()，就导致Ea218 xy.zip被split开了，所以没有导出来；
2、linux系统中，还有软链接文件。通过ls执行后，显示是:
lxxxxx …… 04:46 kmsgcat-log-ln -> kmsgcat-log
3、处理办法，是通过ls -l /查看根目录来确认文件名重第几列开始的，然后从那一列开始获取文件名。
						hibbox中出现离线解析出现unkown
1、原因:是因为13_data_log中，reaility中有一个history.log文件，且该文件格式不对，所以出现unkown。
2、处理:在getHistorylog函数中，将查找文件的范围改成仅在hisi_logs下查找。
						ftp_log.log上传到大数据平台

一、接口规则
1、每组数据，键值之间用三个分号隔开key:::value
2、多组数据用分号隔开
key:::value;key:::value;key:::value;key:::value
3、ftp_log.log结尾换行
4、key值不能为中文，key值不为空；value值可为中文，value值可为空；key和value中不能包含回车、分号、冒号

二、可能存在的异常
1、ftplog中存在key:::value数据对，key值不为空、value为空的情况。这里需要容错处理;
						2018/8/25修改记录
1、lpm3解析
2、hibbox同时导出hisi_logs 和  data_log，弹框显示unkown问题？
是因为，getHisilog函数里面查找history.log的目录范围为整个Log0.9目录，修改查找范围为Log0.9+04_hisi_logs目录。
3、无法导出/data/log/LogService日志？
因为LogService日志中包含空格。ls -l命令显示，包含转义EL\ test.zip，将ls -l |cat管道cat输出后，转义字符就没有了。
然后，导出时添加双引号，如adb pull /data/log/EL\ test.zip d:\EL test.zip。
4、ftp_log.log参数行重复问题？
fp.seek只用于读数据，不影响写入数据。r+用于读写，但是读了以后，要fp.seek(0)才可以写，否则报错；w+用于读写，但是写的时候，会把原本的内容清空。
						ftplog上传到大数据平台的测试
1、使用adb shell ecall read_u32命令触发panic复位
2、在使用tombsone或者anr或者drop触发；
3、使用hibbox工具导出完整日志，打包成压缩包；
4、在大数据平台在线解析，解析完成，没有出现解析异常；
						2018/8/25修改记录
1、lpm3解析
2、hibbox同时导出hisi_logs 和  data_log，弹框显示unkown问题？
是因为，getHisilog函数里面查找history.log的目录范围为整个Log0.9目录，修改查找范围为Log0.9+04_hisi_logs目录。
3、无法导出/data/log/LogService日志？
因为LogService日志中包含空格。ls -l命令显示，包含转义EL\ test.zip，将ls -l |cat管道cat输出后，转义字符就没有了。
然后，导出时添加双引号，如adb pull /data/log/EL\ test.zip d:\EL test.zip。
4、ftp_log.log参数行重复问题？
fp.seek只用于读数据，不影响写入数据。r+用于读写，但是读了以后，要fp.seek(0)才可以写，否则报错；w+用于读写，但是写的时候，会把原本的内容清空。
