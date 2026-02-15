import customtkinter as ctk
import random

class SmartDashboard(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Smart IoT Dashboard")
        self.geometry("400x500")

        # TODO(A1): สร้างตัวแปรสถานะพัดลม
        self.fan_status = None

        # TODO(A2): ตัวแปรอุณหภูมิ
        self.temp_value = 0.0

        # TODO(A3): เรียกสร้าง UI
        self.setup_ui()

        # TODO(A4): เริ่มอ่าน sensor
        self.update_sensor()

    def setup_ui(self):
        # TODO(B1): Title Label
        self.title_label = ctk.CTkLabel(self, text="IoT Dashboard", font=("Arial", 24, "bold"))
        self.title_label.grid(row=0, column=0, padx=20, pady=30)
        # TODO(B2): Label อุณหภูมิ
        self.temp_label = ctk.CTkLabel(self, text="Temperature: --°C", font=("Arial", 20))
        self.temp_label.grid(row=1, column=0, padx=20, pady=10)
        # TODO(B3): Label FAN Status
        self.fan_label = ctk.CTkLabel(self, text="FAN: OFF", font=("Arial", 18), text_color="gray")
        self.fan_label.grid(row=2, column=0, padx=20, pady=10)
        # TODO(B4): Toggle Button
        self.btn_toggle = ctk.CTkButton(self, text="Turn ON Fan", command=self.toggle_fan, fg_color="green")
        self.btn_toggle.grid(row=3, column=0, padx=20, pady=30)
        pass

    def toggle_fan(self):
        # TODO(C1): OFF -> ON
        # TODO(C2): ON -> OFF
        self.fan_status = not self.fan_status
        
        if self.fan_status:
            self.fan_label.configure(text="FAN: ON", text_color="blue") 
            self.btn_toggle.configure(text="Turn OFF Fan", fg_color="red")
        else:
            self.fan_label.configure(text="FAN: OFF", text_color="gray")
            self.btn_toggle.configure(text="Turn ON Fan", fg_color="green")
        pass

    def update_sensor(self):
        # TODO(D1): random.uniform(25,35)
        self.temp_value = random.uniform(25, 35)
        # TODO(D2): update label
        self.temp_label.configure(text=f"Temperature: {self.temp_value:.2f}°C")
        # TODO(D3): ถ้า >30 สีแดง
        if self.temp_value > 30:
            self.temp_label.configure(text_color="red") # Red
        else: 
            self.temp_label.configure(text_color="white") 
        # TODO(D4): self.after(1000, self.update_sensor)
        self.after(1000, self.update_sensor)
        pass

if __name__ == "__main__":
    ctk.set_appearance_mode("System")
    ctk.set_default_color_theme("blue")
    app = SmartDashboard()
    app.mainloop()
