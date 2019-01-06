#-*- coding:utf-8 -*-

import wx
from wx import MenuItem, NO_BORDER
from view.boxevent import *
from wx.lib.sized_controls import border
import Image


class BoxPanel(wx.Panel):
    topmap = [{"name":"online parse","func":onlineParseEvent},
              {"name":"offline parse","func":printfunc},
              {"name":"online delete","func":printfunc}
              ]
    
    def __init__(self,frame):
        wx.Panel.__init__(self,frame)
        self.frame = frame
        self.setSizerInfo()
    
    def setSizerInfo(self):
        box = wx.BoxSizer(wx.VERTICAL)
        top_box = self.getTopSizer()
        mid_box = self.getMidSizer()
        bot_box = self.getBottomSizer()
        #分割空间
        box.Add((-1,5))
        box.Add(top_box,flag=wx.RIGHT)
        #分割空间
        box.Add((-1,5))
        box.Add(mid_box,proportion=1,flag=wx.EXPAND|wx.ALL)
        #分割空间
        box.Add((-1,5))
        box.Add(bot_box,proportion=1,flag=wx.EXPAND|wx.ALL)
        self.SetSizer(box)
       
       
    def getTopSizer(self):
        #StaticText和TextCtrl不是同一类型
        #所以StaticText的flag=wx.RIGHT
        #TextCtrl的flag=wx.EXPAND。否则会相互影响
        top_box = wx.BoxSizer(wx.HORIZONTAL)
        for top_item in BoxPanel.topmap:
            name = top_item.get("name")
            func = top_item.get("func")
            top_text = wx.Button(self,id=-1,label=" "+name+" ",style=NO_BORDER)
            top_text.SetBackgroundColour("#BE9F6")
            if func:
                self.frame.Bind(wx.EVT_BUTTON, func, top_text)
            top_box.Add(top_text,flag=wx.RIGHT,border=5)
        return top_box
    
    #proportion=1需要定义，组件才会窗口自适应
    def getMidSizer(self):
        mid_box = wx.BoxSizer(wx.HORIZONTAL)
        mid_text =wx.TextCtrl(self,size=(-1,400),style=wx.TE_MULTILINE)
        mid_box.Add(mid_text,proportion=2,flag=wx.EXPAND,border=5)
        return mid_box
    
    
    def getBottomSizer(self):
        bot_box = wx.BoxSizer(wx.HORIZONTAL)
        #左边monitor
        left_sizer = wx.BoxSizer(wx.VERTICAL)
        left_text = wx.TextCtrl(self,id=-1,size=(-1,90))
        left_static_text = wx.StaticText(self,-1,"Monitor")
        left_sizer.Add(left_static_text,border=5)
        left_sizer.Add(left_text,proportion=1,flag=wx.EXPAND,border=5)
        #右边Info
        right_sizer = wx.BoxSizer(wx.VERTICAL)
        right_static_text = wx.StaticText(self,-1,"Info")
        right_text = wx.TextCtrl(self,id=-1,size=(-1,90))
        right_sizer.Add(right_static_text,border=5)
        right_sizer.Add(right_text,proportion=1,flag=wx.EXPAND,border=5)
        #把monitor和info添加进去
        bot_box.Add(left_sizer,proportion=1,flag=wx.EXPAND)
        bot_box.Add(right_sizer,proportion=1,flag=wx.EXPAND)
        return bot_box






class BoxFrame(wx.Frame):
    menuMap = [{"first":"file",
                "second":[ {"name":"save","func":printfunc},
                           {"name":"exit","func":printfunc},
                          ],
                },
               {"first":"more",
                "second":[{"name":"problem","func":printfunc,},
                          {"name":"about us","func":printfunc,},
                           ]
                },
               ]
    
    def __init__(self):
        wx.Frame.__init__(self,None,-1,"HIBBOX",(200,100),(800,640))
        #设置菜单
        self.setMenuInfo()
        #设置panel
        BoxPanel(self)
      
    def setMenuInfo(self):
        menu_bar = wx.MenuBar()
        for item in BoxFrame.menuMap:
            #设置一键菜单栏
            first_name = item.get("first")
            first_menu = wx.Menu()
            menu_bar.Append(first_menu, first_name)
            #设置二级菜单栏
            second_list = item.get("second")
            for se_item in second_list:
                second_menu = wx.MenuItem(first_menu,-1,text=se_item.get("name"), kind = wx.ITEM_NORMAL)
#                 BoxPanel.menu_list.append(second_menu)
                first_menu.Append(second_menu)
                #二级菜单绑定事件
                self.Bind(wx.EVT_MENU,se_item.get("func"),second_menu)
        self.SetMenuBar(menu_bar)
        
        
    
        
        

class BoxApp(wx.App):
    
    def OnInit(self):
        box_frame = BoxFrame()
        box_frame.Center()
        box_frame.Show(show=True)
        return True
    

if __name__ == "__main__":
    box_app = BoxApp()
    box_app.MainLoop()
    