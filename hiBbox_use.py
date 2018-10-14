1、	工具介绍


2、	工具使用
2.1在线导出fastboot和kernel状态下的手机日志；
2.2解析二进制的bin文件；
2.3离线解析日志；
2.4在线删除日志；

3、	日志存放位置

4、	常见问题
4.1 在线解析，提示“找不到设备”?
原因：环境问题，在DOS窗口下执行“fastboot devices”和“adb devices”能显示设备，在线解析却提示“找不到设备”，一般是因为fastboot.exe或者adb.exe放在了C:\windows\system32下面；
解决办法：需要将fastboot.exe或者adb.exe放在其他位置，例如，放在d:\tools\下，并将d:\tools\添加到path环境变量；

4.2 导出fastboot日志，提示“get boarded failed”，或者提示“Log0.9_12345ABCDF_20180906/00_ddrdump/fastbootlog.bin don’t find”?
原因：烧写的版本不支持fastboot 导出日志。DOS下， fastboot oem ddrdump show执行失败，说明版本不支持fastboot导出日志；或者 fastboot oem ddrdump show执行成功，但是fastboot oem memory fastbootlog d:\fastbootlog.bin失败，也说明版本不支持fastboot导出日志；
解决办法：版本需要root；

4.3 导出 fastboot 日志为0kb ?
原因：烧写的版本不支持fastboot 导出日志。fastboot oem ddrdump show查看可导出的日志，手动执行导出，例如，fastboot oem memory bbox d:\bbox.bin，手动导出的d:\bbox.bin也为0KB；
解决办法：版本需要root；

4.4、导出kernel日志，hisi_logs缺少history.log?
原因：查看total_file_num.txt，查找hisi_logs关键字，看看有没有导出history.log文件，发现没有记录history.log文件，说明手机里面没有生成！为了验证这种想法，手动在手机/data/hisi_logs下创建一个history.log，然后再用hibbox工具导出，发现导出了history.log，所以是因为手机没有生成所以没有导出，不是hibbox工具问题！

4.5 android.log导出问题？
O版本上？

4.6离线解析日志，提示“找不到history.log”?
离线解析的时候，选择路径要选到Log0.9_xxxx 下面，否则hibbox工具找不到history.log，就没办法再离线解析了；
