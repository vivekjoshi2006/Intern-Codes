import tkinter as tk 
import numpy as np

def read_matrix(text):
    try:
        rows = text.strip().split("\n")
        matrix = [list(map(float, row.split())) for row in rows]
        return np.array(matrix)
    except: return None

def show_result(result):
    result_box.delete("1.0", tk.END)
    if isinstance(result, str): result_box.insert(tk.END, result)
    else:
        for row in result: result_box.insert(tk.END, "  ""  ".join(str(x) for x in row) + "\n")

def add():
    A, B = read_matrix(matA.get("1.0", tk.END)), read_matrix(matB.get("1.0", tk.END))
    if A is None or B is None or A.shape != B.shape: show_result("Error: Invalid input or size mismatch!")
    else: show_result(A + B)

def subtract():
    A, B = read_matrix(matA.get("1.0", tk.END)), read_matrix(matB.get("1.0", tk.END))
    if A is None or B is None or A.shape != B.shape: show_result("Error: Invalid input or size mismatch!")
    else: show_result(A - B)

def multiply():
    A, B = read_matrix(matA.get("1.0", tk.END)), read_matrix(matB.get("1.0", tk.END))
    if A is None or B is None or A.shape[1] != B.shape[0]: show_result("Error: Cannot multiply matrices!")
    else: show_result(np.dot(A, B))

def transpose():
    A = read_matrix(matA.get("1.0", tk.END))
    if A is None: show_result("Error: Invalid matrix!")
    else: show_result(A.T)

def determinant():
    A = read_matrix(matA.get("1.0", tk.END))
    if A is None or A.shape[0] != A.shape[1]: show_result("Error: Determinant needs square matrix!")
    else: show_result(f"Determinant = {np.linalg.det(A):.2f}")

root = tk.Tk()
root.title("Matrix Operations Tool"), root.geometry("800x520"), root.configure(bg="#f4f6ff")

tk.Label(root, text="Matrix Operations Tool", font=("Arial", 18, "bold"), bg="#f4f6ff", fg="#2c3e50").pack(pady=10)
frame = tk.Frame(root, bg="#f4f6ff"); frame.pack()

tk.Label(frame, text="Matrix A", font=("Arial", 12, "bold"), bg="#f4f6ff").grid(row=0, column=0)
matA = tk.Text(frame, width=25, height=8, font=("Consolas", 11)); matA.grid(row=1, column=0, padx=10)

tk.Label(frame, text="Matrix B", font=("Arial", 12, "bold"), bg="#f4f6ff").grid(row=0, column=1)
matB = tk.Text(frame, width=25, height=8, font=("Consolas", 11)); matB.grid(row=1, column=1, padx=10)

btn_frame = tk.Frame(root, bg="#f4f6ff"); btn_frame.pack(pady=10)
btn_style = dict(font=("Arial", 11, "bold"), width=14, bg="#4a69bd", fg="white")

tk.Button(btn_frame, text="Add", command=add, **btn_style).grid(row=0, column=0, padx=5)
tk.Button(btn_frame, text="Subtract", command=subtract, **btn_style).grid(row=0, column=1, padx=5)
tk.Button(btn_frame, text="Multiply", command=multiply, **btn_style).grid(row=0, column=2, padx=5)
tk.Button(btn_frame, text="Transpose A", command=transpose, **btn_style).grid(row=0, column=3, padx=5)
tk.Button(btn_frame, text="Determinant A", command=determinant, **btn_style).grid(row=0, column=4, padx=5)

tk.Label(root, text="Result", font=("Arial", 12, "bold"), bg="#f4f6ff").pack(pady=5)

result_box = tk.Text(root, width=60, height=8, font=("Consolas", 11))
result_box.pack()
root.mainloop()