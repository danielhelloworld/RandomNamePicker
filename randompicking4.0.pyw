import tkinter as tk
from tkinter import messagebox, filedialog
import random
import os
import subprocess
import sys

class RandomNamePicker:
    def __init__(self):
        self.names = []
        self.remaining_names = []

        self.root = tk.Tk()
        self.root.title("随机点名器")
        self.root.overrideredirect(True)  # Remove window border and title bar
        self.root.wm_attributes("-alpha", 0.6)  # Set window opacity
        self.root.wm_attributes("-topmost", 1)  # Set window to stay on top
        self.window1 = tk.Tk()
        self.window1.title("随机点名器")
        self.window1.overrideredirect(True)  # Remove window border and title bar
        self.window1.wm_attributes("-alpha", 0.6)  # Set window opacity
        self.window1.wm_attributes("-topmost", 1)  # Set window to stay on top
        self.label = tk.Label(self.root, text="", font=("Arial", 0))
  
        self.start_button = tk.Button(self.root, width=5, height=2, text="点名", font=("冬青黑体简体中文 W6", 13), command=self.pick_random_name, state=tk.DISABLED)
        self.start_button.pack(pady=0)
        self.start_button1 = tk.Button(self.window1, width=5, height=2, text="点名", font=("冬青黑体简体中文 W6", 13), command=self.pick_random_name, state=tk.DISABLED)
        self.start_button1.pack(pady=0)

        self.file_path = os.path.join(os.path.expanduser("~"), "Documents", "names.txt")
        self.load_names()
        

        self.root.bind("<ButtonPress-1>", self.start_move)
        self.root.bind("<B1-Motion>", self.on_move)
        self.root.bind("<Button-3>", self.right_click)
        self.window1.bind("<ButtonPress-1>", self.start_move1)
        self.window1.bind("<B1-Motion>", self.on_move2)
        self.window1.bind("<Button-3>", self.right_click)

        self.root.update()  # Update window dimensions after widgets are packed
        self.window_width = self.root.winfo_width()  # Get initial window width
        self.window_height = self.root.winfo_height()  # Get initial window height
        self.window1.update()  # Update window dimensions after widgets are packed
        self.window1_width = self.window1.winfo_width()  # Get initial window width
        self.window1_height = self.window1.winfo_height()  # Get initial window height

        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        screen_width1 = self.window1.winfo_screenwidth()
        screen_height1 = self.window1.winfo_screenheight()

        m = 0 #screen_width1 - self.window1_width  # Right edge of the screen
        n = screen_height1 - 100 - self.window1_height  # 100 pixels above the bottom
        x = screen_width - self.window_width  # Right edge of the screen
        y = screen_height - 100 - self.window_height  # 100 pixels above the bottom

        self.root.geometry("+{}+{}".format(x, y))  # Set window position
        self.window1.geometry("+{}+{}".format(m, n))  # Set window position




        self.root.mainloop()
        self.window1.mainloop()
        
    def load_names(self):
        if os.path.exists(self.file_path):
            with open(self.file_path, "r", encoding="utf-8") as file:
                self.names = file.read().splitlines()
            if self.names:
                self.remaining_names = self.names.copy()
                self.start_button.config(state=tk.NORMAL)
                self.start_button1.config(state=tk.NORMAL)
                self.label.config(text="")
            else:
                messagebox.showinfo("提示", "文件为空，请右键点名导入姓名")
        else:
            messagebox.showinfo("提示", "欢迎使用随机点名器。")
            self.create_file()



    def pick_random_name(self):
        if self.remaining_names:
            random_index = random.randint(0, len(self.remaining_names) - 1)
            random_name = self.remaining_names.pop(random_index)

            custom_box = tk.Toplevel(self.root)
            custom_box.title("恭喜!!!")

            custom_font = ("冬青黑体简体中文 W3", 20)
            custom_font1 = ("冬青黑体简体中文 W6", 15)
            label1 = tk.Label(custom_box, text="恭喜！！！", font=custom_font1)
            label = tk.Label(custom_box, text=random_name, font=custom_font)
            label1.pack(padx=20, pady=10)
            label.pack(padx=20, pady=10)

            custom_box.overrideredirect(True)
            screen_width = self.root.winfo_screenwidth()
            screen_height = self.root.winfo_screenheight()
            box_width = custom_box.winfo_reqwidth()
            box_height = custom_box.winfo_reqheight()
            x_position = (screen_width - box_width) // 2
            y_position = (screen_height - box_height) // 2
            custom_box.geometry(f"+{x_position}+{y_position}")

            ok_button = tk.Button(custom_box, text="OK", command=custom_box.destroy, height=2, width=10)
            ok_button.pack(pady=10)

            if not self.remaining_names:
                self.remaining_names = self.names.copy()

    def start_move(self, event):
        self.x = event.x
        self.y = event.y

    def on_move(self, event):
        deltax = event.x - self.x
        deltay = event.y - self.y
        x = self.root.winfo_x() + deltax
        y = self.root.winfo_y() + deltay
        self.root.geometry("+{}+{}".format(x, y))
    def start_move1(self, event1):
        self.m = event1.x
        self.n = event1.y

    def on_move2(self, event1):
        deltam = event1.x - self.m
        deltan = event1.y - self.n
        m = self.window1.winfo_x() + deltam
        n = self.window1.winfo_y() + deltan
        self.window1.geometry("+{}+{}".format(m, n))
    def right_click(self,event):
            custom_box = tk.Toplevel(self.root)
            custom_box.title("选项")

            custom_font = ("冬青黑体简体中文 W3", 20)
            custom_font1 = ("冬青黑体简体中文 W6", 15)
            label1 = tk.Label(custom_box, text="选项", font=custom_font1)
            #label = tk.Label(custom_box, text=random_name, font=custom_font)
            label1.pack(padx=20, pady=10)
            #label.pack(padx=20, pady=10)

            custom_box.overrideredirect(True)
            screen_width = self.root.winfo_screenwidth()
            screen_height = self.root.winfo_screenheight()
            box_width = custom_box.winfo_reqwidth()
            box_height = custom_box.winfo_reqheight()
            x_position = (screen_width - box_width) // 2
            y_position = (screen_height - box_height) // 2
            custom_box.geometry(f"+{x_position}+{y_position}")
            
            modification_button = tk.Button(custom_box, text="管理姓名", command=self.manage_names, height=2, width=10)
            modification_button.pack(pady=5)
            import_button = tk.Button(custom_box, text="姓名源文件", command=self.open_names_txt_folder, height=2, width=10)
            import_button.pack(pady=5)
            refresh_button = tk.Button(custom_box, text="重置姓名列表", command=self.refresh_namelist, height=2, width=10)
            refresh_button.pack(pady=5)
            close_button = tk.Button(custom_box, text="关闭软件", command=self.close_window, height=2, width=10)
            close_button.pack(pady=5)
            back_button = tk.Button(custom_box, text="返回", command=custom_box.destroy, height=1, width=10)
            back_button.pack(pady=10)            
            
              


           
    def open_names_txt_folder(self):
    # 获取当前脚本所在的文件夹路径

        #script_folder = os.path.dirname(os.path.abspath(__file__))
    
    # 拼接 names.txt 的完整路径
        #names_txt_path = os.path.join(script_folder, "names.txt")
        names_txt_path = self.file_path
    # 检查 names.txt 文件是否存在
        if os.path.exists(names_txt_path):
        # 获取 names.txt 文件所在的文件夹路径
            names_folder = os.path.dirname(names_txt_path)
        
        # 使用系统默认的文件管理器打开该文件夹
            try:
                if os.name == "nt":  # 如果是 Windows 系统
                    subprocess.Popen(["notepad", names_txt_path], shell=True)
                elif os.name == "posix":  # 如果是类 Unix 系统
                    subprocess.Popen(["xdg-open", names_folder])
            except Exception as e:
                print("无法打开文件夹:", e)
        else:
            print("文件 'names.txt' 不存在")
            



    def create_file(self):
        with open(self.file_path, "w", encoding="utf-8") as file:
            file.write("")
        messagebox.showinfo("提示", f"文件已创建：{self.file_path}")

    def close_window(self):
        self.root.destroy()
        sys.exit()
    
    def refresh_namelist(self):
        self.remaining_names = self.names.copy()
        self.load_names()
        messagebox.showinfo("提示" , "已重置列表")

    def manage_names(self):
        self.manage_window = tk.Toplevel(self.root)
        self.manage_window.title("管理姓名列表")
        self.manage_window.geometry("300x400")

        self.name_listbox = tk.Listbox(self.manage_window)
        self.name_listbox.pack(fill=tk.BOTH, expand=True)

        for name in self.names:
            self.name_listbox.insert(tk.END, name)

        self.entry_frame = tk.Frame(self.manage_window)
        self.entry_frame.pack(pady=15)

        self.name_entry = tk.Entry(self.entry_frame)
        self.name_entry.pack(side=tk.LEFT, padx=5)


        self.add_button = tk.Button(self.entry_frame, text="添加", command=self.add_name)
        self.add_button.pack(side=tk.LEFT, padx=5)

        self.delete_button = tk.Button(self.entry_frame, text="删除", command=self.delete_name)
        self.delete_button.pack(side=tk.LEFT, padx=5)

        self.save_button = tk.Button(self.manage_window, text="保存", command=self.save_names)
        self.save_button.pack(pady=10)

    def import_names(self):
        file_path = filedialog.askopenfilename(title="选择姓名文件", filetypes=(("文本文件", "*.txt"), ("所有文件", "*.*")))
        if file_path:
            with open(file_path, "r", encoding="utf-8") as file:
                self.names = file.read().splitlines()
            if self.names:
                self.remaining_names = self.names.copy()
                self.start_button.config(state=tk.NORMAL)
                self.label.config(text="")
            else:
                messagebox.showinfo("提示", "文件为空，请选择一个包含姓名的文件。")
        else:
            messagebox.showinfo("提示", "未选择文件，请选择一个包含姓名的文件。")


    
    def add_name(self):
        name = self.name_entry.get().strip()
        if name:
            self.names.append(name)
            self.name_listbox.insert(tk.END, name)
            self.name_entry.delete(0, tk.END)

    def delete_name(self):
        selected_indices = self.name_listbox.curselection()
        for index in selected_indices[::-1]:
            self.name_listbox.delete(index)
            del self.names[index]

    def save_names(self):
        with open(self.file_path, "w", encoding="utf-8") as file:
            file.write("\n".join(self.names))
        self.remaining_names = self.names.copy()
        self.start_button.config(state=tk.NORMAL)
        self.manage_window.destroy()
        messagebox.showinfo("提示", "姓名列表已保存。")        
        
        



# 创建随机点名器对象
random_name_picker = RandomNamePicker()
