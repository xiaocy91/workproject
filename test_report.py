hibbox工具--功能验证报告

dfx.bin导出修改适配-20181113
一、原因: 因为现在的手机版本不支持dump-emmc，只支持dump-storage，但是configs下的fastboot64工具只支持dump-emmc，所以emmc和storage都用不了，所以要更新fastboot64工具; 更新工具时，要先删除C:/Windows/system32下的fastboot.exe和adb.exe，然后dos下输入where fastboot命令查看哪些地道有，然后把最新的工具添加到环境变量；添加好后，使用fastboot --version来查看工具版本。
二、测试步骤:
1、烧写在支持fastboot  oem dump-storage dfx d:\dfx.bin命令的手机版本(2017-2-8号后的手机版本就开始支持storage命令了)。
2、打开hibbox工具-在线解析，手机进入fastboot状态，勾选dfx选项，点确定后开始导出日志
三、预期结果:
成功导出Log_xxx/00_ddrdump/dfx.bin




conn版本适配-201804
一、原因: bbox中新增CONN数据
二、测试步骤
打开hibbox工具，拖拽bbox.bin文件至工具中进行解析，需要覆盖不同版本的bbox.bin文件，包括0x20、0x21、0x22；
三、预期结果
不同版本bbox.bin可以正确解析，top_head.txt中包含CONN字段和地址



弹框增加数据分析平台链接--201803
二、测试步骤: 
1、没有异常复位时，使用hibbox-在线解析，导出kernel下日志致结束；
2、执行adb shell ecall read_u32 0命令后，出发复位，使用hibbox-在线解析，导出kernel下日志致结束；
三、预期结果
1、导出结束后，弹框提示没有异常复位，并显示大数据平台链接；
2、导出结束后，弹框提示异常复位信息，并显示大数据平台链接；


ftp_log.log中增加debug字段-201803
二、测试步骤
1、打开hibbox-在线解析，会弹框提示“是否为测试人员”；
2、如果是测试人员，选择“是”，然后在线导出kernel下日志；如果不是测试人员，选择“否”，然后导出kernel下日志；
三、预期结果
1、弹出debug弹框，默认为“否”；
2、选择为“是”，在线导出kernel下日志后，Log_xxx/ftp_log.log中记录的debug字段为True；选择“否”后，Log_xxx/ftp_log.log中记录的debug字段为False；



