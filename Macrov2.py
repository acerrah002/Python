import tkinter as tk
from tkinter import messagebox
import pyautogui
import threading
import time
import keyboard  # Ensure you have this installed: pip install keyboard

class AutoClickerGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Python Auto-Clicker")
        self.root.geometry("300x450")
        
        self.positions = []
        self.is_running = False

        # --- UI Elements ---
        self.label = tk.Label(root, text="Mouse Positions:", font=('Arial', 12, 'bold'))
        self.label.pack(pady=5)

        self.listbox = tk.Listbox(root, height=10, width=30)
        self.listbox.pack(pady=5)

        self.btn_record = tk.Button(root, text="Record Position (F8)", command=self.add_position, bg="#e1f5fe")
        self.btn_record.pack(fill='x', padx=20, pady=2)

        self.btn_delete = tk.Button(root, text="Remove Selected", command=self.remove_position, bg="#ffebee")
        self.btn_delete.pack(fill='x', padx=20, pady=2)

        self.btn_start = tk.Button(root, text="START CLICKING", command=self.start_clicking, bg="#c8e6c9")
        self.btn_start.pack(fill='x', padx=20, pady=10)

        self.btn_stop = tk.Button(root, text="STOP (ESC)", command=self.stop_clicking, bg="#ffcdd2")
        self.btn_stop.pack(fill='x', padx=20, pady=2)

        # --- Global Hotkeys ---
        # F8 to record, ESC to stop
        keyboard.add_hotkey('f8', self.add_position)
        keyboard.add_hotkey('esc', self.stop_clicking)
        
    def add_position(self):
        # This can now be triggered by F8 even if the window is minimized
        pos = pyautogui.position()
        self.positions.append(pos)
        # Use root.after to update GUI from a background hotkey safely
        self.root.after(0, lambda: self.listbox.insert(tk.END, f"X: {pos.x}, Y: {pos.y}"))

    def remove_position(self):
        selected = self.listbox.curselection()
        if selected:
            idx = selected[0]
            self.listbox.delete(idx)
            self.positions.pop(idx)

    def start_clicking(self):
        if not self.positions:
            messagebox.showwarning("Warning", "Record some positions first!")
            return
        
        if not self.is_running:
            self.is_running = True
            print("Clicking started...")
            self.click_thread = threading.Thread(target=self.run_click_loop, daemon=True)
            self.click_thread.start()

    def run_click_loop(self):
        while self.is_running:
            for pos in self.positions:
                if not self.is_running: 
                    break
                pyautogui.click(pos.x, pos.y)
                time.sleep(0.01) 

    def stop_clicking(self):
        if self.is_running:
            self.is_running = False
            print("Emergency Stop: Clicking Halted.")

if __name__ == "__main__":
    root = tk.Tk()
    app = AutoClickerGUI(root)
    root.mainloop()
