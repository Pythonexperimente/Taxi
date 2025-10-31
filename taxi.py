import tkinter as tk

from tkinter import simpledialog


km = simpledialog.askstring("Input", "Geben sie die KM an:")
euro = 3.00 * float(km)
print("Die berechnung erfolgte erfolgreich.")
tk.messagebox.showinfo("Ergebnis", f"Die Kosten für {km} KM betragen {euro} Euro.")

print("Dieses Programm ist OpenSource und ist in Editor usw. editierbar für ihr Unternehmen.")
