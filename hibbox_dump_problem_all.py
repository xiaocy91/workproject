
----------------------------------------

2018/4/25	
hibbox




hibbox工具打开后，提示找不到设备，但是设备已经连接好了


原因是环境问题，fastboot、adb环境变量没设置好，用hibbox中的fastboot重新设置了环境变量就好了



----------------------------------------


2018/5/25 hibbox


检测不到平台



hibbox检测不到平台，因为获取平台的命令执行后无效，需要补充通过boardid方法换算平台的方法



----------------------------------------


2018/5/25 hibbox

hibbox2.0项目hibbox工具适配遇到的问题

1、bbox.bin应该二进制方式打开文件；
2、c语言结构体中使用char存放int类型，节省空间；
3、area_s中fomat为QI4X，必须有4X进行补齐；


原因：
1、bbox.bin文件解析报错，错误提示读取的struct.unpack时提示字符串长度不够258。是因为bbox.bin没有用二进制方式打开，改用二进制打开文件就没有错误了；
2、u8类型可能是假字符串，它是把int存在char中，为了省空间。存了一个"\x1f"，实际1f是31，使用方法ord("\x1f")就等于31，31就是数字1的IISC码，字符1转成数字1就是用ord("\1f")-ord("0")；
3、area_s的format格式为"QI4x"，4x为自动补齐，否则会影响的解析；




----------------------------------------



2018/5/27

无法导出vendor日志

logitems中添加vendor log后仍然没有导出vendor日志

dump中do方法中getlog中，因为在过滤ANDROID_VERSION="P"时，此时ANDROID_VERSION还是默认值N，此时过滤出来的cmdplist是不对的，版本不对导致参数过滤不到vendor日志;所以把ANDROID_VERSION的判断提前，如果是fastboot状态就重启到adb下，获取版本号，并设置ELEM中版本号，根据版本号来过滤参数args，此时版本号已经为P版本，过滤的参数就包含了vendor日志。

----------------------------------------




2018/6/22	hibbox	


hibbox无法导出fastboot日志


hibbox工具导出fastboot日志为0kb	


miami平台，6月1号下午之前的fastboot宏锁了




----------------------------------------


2018/6/26	dump	

dump导出日志中android_log不存在


dump工具导日志没有生成01_android_log	


dump工具，在m版本中，13_data_log下有android_log后，就不在生成01_android_log了，而hibbox工具会生成。




---------------------------------------------

2018/6/27	hibbox
	
适配phoenix和orlando平台

hibbox解析phoenix和orlando平台bbox.bin文件出错	

原因是加入orlando中断表时，中断号有一个写成了"412~427"，这里中断号必须是一个一个单独的，不能这样写在一起;



---------------------------------------------





