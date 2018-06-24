
##################################
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


##################################
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





##################################
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


##################################
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


##################################
	2018/5/27	
dump需求

	
dump中保持跟hibbox工具一致：
1、导出和删除vendor/log;
2、miami平台670变成710；
3、异常复位责任人修改；
	
问题>>>>>：

	
closed:
1、导出vendor日志后，目录为/18_vendor_log，多了一个斜杠；
2、linux版本中dump脚本没有更新，打包错误；
3、无法导出vendor日志
3.1、dump.py中ddrdump方法中，ELEM.ANDROID_VERSION版本没有获取，根据版本过滤的args参数没有vendor，所以后面没有导出vendor日志；

in process:
1、无法删除vendor日志；
	
实现>>>>>：
	
1.要求增加/data/vendor/log;
2、增加vendor日志的导出，增加vendor日志的删除;
3.但是修改了logitems中变量后并没有成功导出，把8.1.0改成P版本还是没有导出vendor日志;
4.dump中do方法中getlog中，需要修改:
4.1、因为在过滤ANDROID_VERSION=P时，此时ANDROID_VERSION还是默认值N，此时过滤出来的cmdplist是不对的，所以把ANDROID_VERSION的判断提前；
4.2、需要把ELEM.ANDROID_VERSION的判断提前到dump.py中，在ddrdump方法中添加判断版本的方法，但是在fastboot模式是不能执行adb get property来获取版本8.1.0的，所以，如果是fastboot模式，必须先进去到adb来判断版本，然后再导日志;
4.3
4.3.1.在dump.py中增加，ddrdump中，如果是fastboot状态就重启到adb下，获取版本号，并设置ELEM中版本号;
4.3.2.然后根据memory还是kernel或者是没有参数，这里只说kernel的条件下，根据版本号来过滤参数args，此时版本号已经为8.1.0的P版本，过滤的参数就包含了vendor日志;之前就是版本不对，导致参数过滤不到vendor日志;
4.4dump导vendor日志中的错误
4.4.1.vendor日志无法导出，因为打包错误，linux上代码没有更新，需要把代码放在linux上，然后网络映射到本地;
4.4.2.dump导出fastboot日志报错，因为self.fastboot变量没有定义就使用;
4.4.3.dump无法导出日志，因为版本问题，是p版本或者9版本;

