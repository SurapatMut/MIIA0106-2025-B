import customtkinter as ctk

def toggle_light():
    # ตรวจสอบสีปัจจุบัน ถ้าเป็นสีเทา (ปิด) ให้เปลี่ยนเป็นเหลือง (เปิด)
    if label.cget("text_color") == "gray":
        label.configure(text_color="yellow")
        print("Light ON!")
    else:
        label.configure(text_color="gray")
        print("Light OFF!")

app = ctk.CTk()
app.title("Smart Home")
app.geometry("300x200")

# เพิ่มสีเริ่มต้นเป็นสีเทา (ไฟปิดอยู่)
label = ctk.CTkLabel(app, text="Living Room", font=("Arial", 24), text_color="gray")
label.pack(pady=(20, 10))

button = ctk.CTkButton(app, text="Toggle Light", command=toggle_light)
button.pack(pady=20)

app.mainloop()