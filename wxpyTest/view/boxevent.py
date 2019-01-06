#-*- coding:utf-8 -*-
from template.onlinediag import OnlineDialog
import wx

def printfunc(event):
    print event
    print "haha"
    

def onlineParseEvent(event):
    online_diag = OnlineDialog()
    online_diag.Bind(wx.EVT_BUTTON, printfunc, online_diag.yes_btn)
    online_diag.ShowModal()
    
    
    
