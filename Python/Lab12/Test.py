import customtkinter as ctk
import random

class SmartDashboard(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Smart IoT Dashboard v2")
        self.geometry("400x550")

        # --- State Variables ---
        self.fan_status = False
        self.light_status = False
        self.temp_value = 0.0

        self.setup_ui()
        self.update_sensor()

    def setup_ui(self):
        self.grid_columnconfigure((0, 1), weight=1)

        # Row 0: Title
        self.title_label = ctk.CTkLabel(self, text="🌡️ Smart Home", font=("Arial", 24, "bold"))
        self.title_label.grid(row=0, column=0, columnspan=2, padx=20, pady=25)

        # Row 1: Temperature Sensor
        self.temp_label = ctk.CTkLabel(self, text="Temp: --°C", font=("Arial", 20))
        self.temp_label.grid(row=1, column=0, columnspan=2, padx=20, pady=10)

        # --- Row 2-3: Control Buttons ---
        # Fan Button
        self.btn_fan = ctk.CTkButton(self, text="Toggle FAN", command=self.toggle_fan, fg_color="#3498db")
        self.btn_fan.grid(row=2, column=0, padx=10, pady=20)

        # Light Button
        self.btn_light = ctk.CTkButton(self, text="Toggle LIGHT", command=self.toggle_light, fg_color="#f1c40f", text_color="black")
        self.btn_light.grid(row=2, column=1, padx=10, pady=20)

        # --- Row 4-5: Status Display (2 บรรทัด) ---
        # บรรทัดที่ 1: สถานะพัดลม
        self.status_fan = ctk.CTkLabel(self, text="Fan Status: OFF", font=("Arial", 16), text_color="gray")
        self.status_fan.grid(row=4, column=0, columnspan=2, pady=5)

        # บรรทัดที่ 2: สถานะไฟ
        self.status_light = ctk.CTkLabel(self, text="Light Status: OFF", font=("Arial", 16), text_color="gray")
        self.status_light.grid(row=5, column=0, columnspan=2, pady=5)

    def toggle_fan(self):
        self.fan_status = not self.fan_status
        if self.fan_status:
            self.status_fan.configure(text="Fan Status: RUNNING 🌀", text_color="#3498db")
            self.btn_fan.configure(fg_color="#e74c3c", text="Stop FAN")
        else:
            self.status_fan.configure(text="Fan Status: OFF", text_color="gray")
            self.btn_fan.configure(fg_color="#3498db", text="Start FAN")

    def toggle_light(self):
        self.light_status = not self.light_status
        if self.light_status:
            self.status_light.configure(text="Light Status: ON 💡", text_color="#f1c40f")
            self.btn_light.configure(fg_color="#e74c3c", text="Turn OFF", text_color="white")
        else:
            self.status_light.configure(text="Light Status: OFF", text_color="gray")
            self.btn_light.configure(fg_color="#f1c40f", text="Turn ON", text_color="black")

    def update_sensor(self):
        self.temp_value = random.uniform(25, 35)
        self.temp_label.configure(text=f"Temperature: {self.temp_value:.2f}°C")
        
        # แจ้งเตือนผ่านสีถ้าอุณหภูมิสูง
        if self.temp_value > 30:
            self.temp_label.configure(text_color="#e74c3c")
        else:
            self.temp_label.configure(text_color="white")

        self.after(2000, self.update_sensor)

if __name__ == "__main__":
    ctk.set_appearance_mode("Dark")
    app = SmartDashboard()
    app.mainloop()