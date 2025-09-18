import tkinter as tk
from tkinter import ttk, messagebox
import subprocess

class PredictiveMaintenanceGUI(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("IoT Predictive Maintenance Demo")
        self.geometry("450x220")
        self.create_widgets()

    def create_widgets(self):
        ttk.Label(self, text="IoT Predictive Maintenance Demo", font=("Arial", 16)).pack(pady=10)

        self.run_button = ttk.Button(self, text="Run Prediction", command=self.run_prediction)
        self.run_button.pack(pady=10)

        self.status_label = ttk.Label(self, text="Status: Idle")
        self.status_label.pack(pady=10)

        self.exit_button = ttk.Button(self, text="Exit", command=self.destroy)
        self.exit_button.pack(pady=10)

    def run_prediction(self):
        self.status_label.config(text="Status: Running prediction...")
        self.update()

        try:
            # Replace 'main.py' with your actual script name for prediction
            subprocess.run(["python3", "Stream_IoT_Prediction_Dashboard_plotly.py"], check=True)
            self.status_label.config(text="Status: Prediction completed")
            messagebox.showinfo("Prediction Finished", "Prediction completed successfully!\nCheck generated plots.")
        except subprocess.CalledProcessError:
            self.status_label.config(text="Status: Prediction failed")
            messagebox.showerror("Error", "Prediction failed. Check console for errors.")

if __name__ == "__main__":
    app = PredictiveMaintenanceGUI()
    app.mainloop()
