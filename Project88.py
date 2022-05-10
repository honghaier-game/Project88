#coding=utf-8
#import libs 
import sys
import Project88_cmd
import Project88_sty
import Fun
import os
import tkinter
from   tkinter import *
import tkinter.ttk
import tkinter.font
#Add your Varial Here: (Keep This Line of comments)
#Define UI Class
class  Project88:
    def __init__(self,root,isTKroot = True):
        uiName = self.__class__.__name__
        Fun.Register(uiName,'UIClass',self)
        self.root = root
        Fun.Register(uiName,'root',root)
        style = Project88_sty.SetupStyle()
        if isTKroot == True:
            root.title("Form1")
            Fun.CenterDlg(uiName,root,300,160)
            root['background'] = '#efefef'
        Form_1= tkinter.Canvas(root,width = 10,height = 4)
        Form_1.place(x = 0,y = 0,width = 300,height = 160)
        Form_1.configure(bg = "#efefef")
        Form_1.configure(highlightthickness = 0)
        Fun.Register(uiName,'Form_1',Form_1)
        #Create the elements of root 
        Label_2 = tkinter.Label(Form_1,text="账号",width = 10,height = 4)
        Fun.Register(uiName,'Label_2',Label_2)
        Fun.SetControlPlace(uiName,'Label_2',20,20,80,23)
        Label_2.configure(relief = "flat")
        Entry_3_Variable = Fun.AddTKVariable(uiName,'Entry_3','')
        Entry_3 = tkinter.Entry(Form_1,textvariable=Entry_3_Variable)
        Fun.Register(uiName,'Entry_3',Entry_3)
        Fun.SetControlPlace(uiName,'Entry_3',120,24,160,23)
        Entry_3.configure(relief = "sunken")
        Label_4 = tkinter.Label(Form_1,text="密码",width = 10,height = 4)
        Fun.Register(uiName,'Label_4',Label_4)
        Fun.SetControlPlace(uiName,'Label_4',20,50,80,23)
        Label_4.configure(relief = "flat")
        Entry_5_Variable = Fun.AddTKVariable(uiName,'Entry_5','')
        Entry_5 = tkinter.Entry(Form_1,textvariable=Entry_5_Variable)
        Fun.Register(uiName,'Entry_5',Entry_5)
        Fun.SetControlPlace(uiName,'Entry_5',120,54,160,23)
        Entry_5.configure(relief = "sunken")
        Entry_5.configure(show = "*")
        Button_6 = tkinter.Button(Form_1,text="确定",width = 10,height = 4)
        Fun.Register(uiName,'Button_6',Button_6)
        Fun.SetControlPlace(uiName,'Button_6',146,103,60,23)
        Button_6.configure(command=lambda:Project88_cmd.Button_6_onCommand(uiName,"Button_6"))
        Button_7 = tkinter.Button(Form_1,text="退出",width = 10,height = 4)
        Fun.Register(uiName,'Button_7',Button_7)
        Fun.SetControlPlace(uiName,'Button_7',220,103,60,23)
        Button_7.configure(command=lambda:Project88_cmd.Button_7_onCommand(uiName,"Button_7"))
        #Inital all element's Data 
        Fun.InitElementData(uiName)
        #Add Some Logic Code Here: (Keep This Line of comments)


#Create the root of Kinter 
if  __name__ == '__main__':
    root = tkinter.Tk()
    MyDlg = Project88(root)
    root.mainloop()
