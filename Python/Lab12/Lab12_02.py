import customtkinter as ctk

def calculate_bmi():

    w_txt = ent_weight.get().strip()

    h_txt = ent_height.get().strip()


    # Basic validation

    try:

        weight = float(w_txt)

        height_cm = float(h_txt)

        if weight <= 0 or height_cm <= 0:

            raise ValueError("must be positive")

    except:

        lbl_result.configure(text="Result: กรุณากรอกตัวเลขให้ถูกต้อง (kg, cm)")

        return


    height_m = height_cm / 100.0

    bmi = weight / (height_m * height_m)


    lbl_result.configure(text=f"Result: BMI = {bmi:.2f}")

# ----- App -----

ctk.set_appearance_mode("dark")        # "light" / "dark" / "system"

ctk.set_default_color_theme("blue")    # "blue" / "green" / "dark-blue"


app = ctk.CTk()

app.title("BMI Calculator")

app.geometry("380x520")


# Main frame (like a card)

frame = ctk.CTkFrame(app, corner_radius=16)

frame.pack(padx=20, pady=20, fill="both", expand=True)


# Configure grid: 2 columns

frame.grid_columnconfigure(0, weight=1)

frame.grid_columnconfigure(1, weight=2)


# Row 0: Title (span 2 cols)

lbl_title = ctk.CTkLabel(frame, text="BMI Calculator", font=("Arial", 26, "bold"))

lbl_title.grid(row=0, column=0, columnspan=2, pady=(20, 25))




# Optional: press Enter to calculate

app.bind("<Return>", lambda e: calculate_bmi())

# Row 1: Weight label + entry

lbl_weight = ctk.CTkLabel(frame, text="น้ำหนัก (kg)", font=("Arial", 16))

lbl_weight.grid(row=1, column=0, padx=(20, 10), pady=10, sticky="w")


ent_weight = ctk.CTkEntry(frame, placeholder_text="เช่น 60", height=38)

ent_weight.grid(row=1, column=1, padx=(10, 20), pady=10, sticky="ew")


# Row 2: Height label + entry

lbl_height = ctk.CTkLabel(frame, text="ส่วนสูง (cm)", font=("Arial", 16))

lbl_height.grid(row=2, column=0, padx=(20, 10), pady=10, sticky="w")


ent_height = ctk.CTkEntry(frame, placeholder_text="เช่น 170", height=38)

ent_height.grid(row=2, column=1, padx=(10, 20), pady=10, sticky="ew")


# Row 3: Button (span 2 cols)

btn_calc = ctk.CTkButton(frame, text="Calculate BMI", height=42,
command=calculate_bmi)

btn_calc.grid(row=3, column=0, columnspan=2, padx=20, pady=(20, 20),
sticky="ew")


# Row 4: Result (span 2 cols)

result_box = ctk.CTkFrame(frame, corner_radius=16)

result_box.grid(row=4, column=0, columnspan=2, padx=20, pady=(10, 20),
sticky="nsew")


lbl_result = ctk.CTkLabel(result_box, text="Result: --", font=("Arial", 18))

lbl_result.pack(padx=20, pady=60)


app.mainloop()