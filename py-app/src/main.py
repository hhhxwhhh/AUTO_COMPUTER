import tkinter as tk
from tkinter import messagebox,filedialog
from utils import generate_question
class App:
    def __init__(self,root):
        self.root=root
        root.title("小学生出题工具")
        root.geometry("400x500")  # 增加窗口高度
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
        tk.Button(root,text="生成题目",bg="lightblue",command=self.generate).pack(pady=10)
        #显示题目
        self.text=tk.Text(root,height=10,width=40)
        self.text.pack(padx=20)
        #保存题目按钮
        tk.Button(root,text="保存题目",bg="lightgreen",command=self.save).pack(pady=10)
        
    def generate(self):
        try:
            num=int(self.num_entry.get())
            if num<=0 or num>10000:
                raise ValueError
        except ValueError:
            messagebox.showerror("错误","请输入正确的题目数量")
            return
        op_types=[self.ops[name] for name,var in self.vars.items() if var.get()]
        if not op_types:
            messagebox.showerror("错误","请至少选择一个操作类型")
            return 
        self.text.delete(1.0, tk.END)
        line = ""
        for i in range(num):
            question = generate_question(op_types)
            line += "{:<12}".format(question)
            if (i + 1) % 3 == 0:
                self.text.insert(tk.END, line + "\n")
                line = ""
        if line:  # 处理最后一行不足3个的情况
            self.text.insert(tk.END, line + "\n")
        #显示生成完成的提示
        messagebox.showinfo("生成成功","题目已生成")
            
    def save(self):
        content=self.text.get(1.0,tk.END).strip()
        if not content:
            messagebox.showerror("错误","请先生成题目")
            return 
        file=filedialog.asksaveasfile(mode='w',defaultextension=".txt")
        if file:
            with open(file,'w',encoding='utf-8') as f:
                f.write(content)
            messagebox.showinfo("保存成功","题目已保存")
            
def main():
    root=tk.Tk()
    app=App(root)
    root.mainloop()
if __name__=="__main__":
    main()