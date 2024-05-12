import tkinter as tk
from ast_generator import ASTGenerator
from tkcode import CodeEditor
import matplotlib.pyplot as plt
import networkx as nx

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.code_entry = CodeEditor(self)
        self.code_entry.pack(side="top")

        self.ast_button = tk.Button(self)
        self.ast_button["text"] = "Generate AST"
        self.ast_button["command"] = self.generate_ast
        self.ast_button.pack(side="top")

        self.execute_button = tk.Button(self)
        self.execute_button["text"] = "Execute Code"
        self.execute_button["command"] = self.execute_code
        self.execute_button.pack(side="top")

        self.quit = tk.Button(self, text="QUIT", fg="red",
                              command=self.master.destroy)
        self.quit.pack(side="bottom")

        self.ast_text = tk.Text(self)
        self.ast_text.pack(side="top")

    def generate_ast(self):
        code = self.code_entry.get('1.0', 'end-1c')
        G, error = ASTGenerator.generate(code)
        self.ast_text.delete('1.0', tk.END)
        if G is not None:
            pos = nx.spring_layout(G)
            labels = nx.get_node_attributes(G, 'label')
            nx.draw(G, pos, labels=labels, with_labels=True)
            plt.show()
        else:
            self.ast_text.insert(tk.END, error)

    def execute_code(self):
        code = self.code_entry.get('1.0', 'end-1c')
        try:
            exec(code)
        except Exception as e:
            self.ast_text.delete('1.0', tk.END)
            self.ast_text.insert(tk.END, str(e))
