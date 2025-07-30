import tkinter as tk
from tkinter import messagebox,filedialog
from utils import generate_question
class App:
    def __init__(self,root):
        self.root=root
        root.title("小学生出题工具")
        root.geometry("400x300")
        #设置题目的数量
        tk.Label(root,text="请输入题目数量:").pack(anchor='w',padx=20,pady=5)
        self.num_entry=tk.Entry(root)
        self.num_entry.pack(anchor='w',padx=20,pady=5)
        self.num_entry.insert(0,"100")
        #设置操作类型
        tk.Label(root,text="请选择操作类型:").pack(anchor='w',padx=20,pady=5)
        self.ops={
           '加法':'+',
           '减法':'-',
           '乘法':'*',
           '除法':'÷',
        }
        self.vars={}
        for name in self.ops:
            var=tk.BooleanVar(value=True)
            tk.Checkbutton(root,text=name,variable=var).pack(anchor='w',padx=20,pady=5)
            self.vars[name]=var
        #生成题目按钮
        tk.Button(root,text="生成题目",bg="lightblue",command=self.generate).pack(pady=20)
        #显示题目
