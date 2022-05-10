#coding=utf-8
import sys
import os
from   os.path import abspath, dirname
sys.path.append(abspath(dirname(__file__)))
import tkinter
import tkinter.filedialog
from   tkinter import *
import Fun
ElementBGArray={}  
ElementBGArray_Resize={} 
ElementBGArray_IM={} 

def Button_6_onCommand(uiName,widgetName):
    UserName=Fun.GetText(uiName,"Entry_3")
    PassWord=Fun.GetText(uiName,"Entry_5")
    Fun.MessageBox("UserName:"+UserName+"   PassWord:"+PassWord)
def Button_7_onCommand(uiName,widgetName):
    root=Fun.GetElement(uiName,"root")
    root.destroy() 
