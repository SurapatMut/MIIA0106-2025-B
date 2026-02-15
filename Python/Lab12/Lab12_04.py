import customtkinter as ctk
import random

class SmartDashboard(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Smart IoT Dashboard Pro")
        self.geometry("450x600")

        # --- State Variables ---
        self.fan_status = False
        self.light_status = False  # เพิ่มตัวแปรสถานะไฟ
        self.temp_value = 0.0

        self.setup_ui()
        self.update_sensor()

    def setup_ui(self):
        self.grid_columnconfigure((0, 1), weight=1)

        # Title
        self.title_label = ctk.CTkLabel(self, text="Smart Home System", font=("Arial", 26, "bold"))
        self.title_label.grid(row=0, column=0, columnspan=2, padx=20, pady=30)

        # Temperature Display (Sensor)
        self.temp_label = ctk.CTkLabel(self, text="Temperature: --°C", font=("Arial", 22))
        self.temp_label.grid(row=1, column=0, columnspan=2, padx=20, pady=10)

        # --- Fan Control Section ---
        self.fan_label = ctk.CTkLabel(self, text="FAN: OFF", font=("Arial", 16), text_color="gray")
        self.fan_label.grid(row=2, column=0, padx=20, pady=5)
        
        self.btn_fan = ctk.CTkButton(self, text="Turn ON Fan", command=self.toggle_fan, fg_color="#2ecc71")
        self.btn_fan.grid(row=3, column=0, padx=10, pady=10)

        # --- Light Control Section (เพิ่มใหม่) ---
        self.light_label = ctk.CTkLabel(self, text="LIGHT: OFF", font=("Arial", 16), text_color="gray")
        self.light_label.grid(row=2, column=1, padx=20, pady=5)
        
        self.btn_light = ctk.CTkButton(self, text="Turn ON Light", command=self.toggle_light, fg_color="#f1c40f", text_color="black")
        self.btn_light.grid(row=3, column=1, padx=10, pady=10)

        # Status Bar
        self.status_bar = ctk.CTkLabel(self, text="System Ready", font=("Arial", 12))
        self.status_bar.grid(row=4, column=0, columnspan=2, pady=40)

    def toggle_fan(self):
        self.fan_status = not self.fan_status
        if self.fan_status:
            self.fan_label.configure(text="FAN: ON", text_color="blue")
            self.btn_fan.configure(text="Turn OFF Fan", fg_color="red")
            self.status_bar.configure(text="Living Room FAN is now ON")

        else:
            self.fan_label.configure(text="FAN: OFF", text_color="gray")
            self.btn_fan.configure(text="Turn ON Fan", fg_color="green")
            self.status_bar.configure(text="Living Room FAN is now OFF")
    def toggle_light(self):
        """ ฟังก์ชันควบคุมการเปิด-ปิดไฟ """
        self.light_status = not self.light_status
        if self.light_status:
            self.light_label.configure(text="LIGHT: ON ", text_color="yellow")
            self.btn_light.configure(text="Turn OFF Light", fg_color="red", text_color="white")
            self.status_bar.configure(text="Living Room Light is now ON")
        else:
            self.light_label.configure(text="LIGHT: OFF", text_color="gray")
            self.btn_light.configure(text="Turn ON Light", fg_color="green", text_color="white")
            self.status_bar.configure(text="Living Room Light is now OFF")

    def update_sensor(self):
        self.temp_value = random.uniform(25, 35)
        self.temp_label.configure(text=f"Temperature: {self.temp_value:.2f}°C")

        # เปลี่ยนสีอุณหภูมิถ้าสูงเกิน 30 องศา
        if self.temp_value > 30:
            self.temp_label.configure(text_color="red")
        else:
            self.temp_label.configure(text_color="white")

        self.after(2000, self.update_sensor) # อัปเดตทุก 2 วินาที

if __name__ == "__main__":
    ctk.set_appearance_mode("Dark")
    app = SmartDashboard()
    app.mainloop()