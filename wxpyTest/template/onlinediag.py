#-*- coding:utf-8 -*-

import wx
from wx import Position


class OnlineDialog(wx.Dialog):
    
    def __init__(self):
        wx.Dialog.__init__(self,None,-1,"oneline parse dialog",size=(450,550))
        self.checkmap = {"hisi_logs":"/data/hisi_logs",
                  "memerydump":"/data/hisi_logs/memorydump",
                  "android_logs":"/data/log/android_logs",
                  "pstore":"/data/log/pstore",
                  }
        self.setChecklist()
       
       
    def setChecklist(self):
        box_sizer = wx.BoxSizer(wx.VERTICAL)
        self.list_box = wx.CheckListBox(self,-1,(300,10),(400,500),self.checkmap.values())
        self.yes_btn = wx.Button(self,-1,"Yes",style=wx.YES)
        box_sizer.Add(self.list_box)
        box_sizer.Add(self.yes_btn)
        self.SetSizer(box_sizer)
    
    
    