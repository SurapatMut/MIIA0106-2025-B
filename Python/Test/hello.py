#สร้าง function
def inputx():
    x = input("Enter number of x") #string ตัวอักษร
    #ต้อง การ x เป็นตัวเลข
    x = int(x)  # convert string => int,float
    print(f" x = {x}")
    print(f" x+1 = {x+1}")

    if x >50 :
        print("x > 50")
    elif x > 30:
        print("x= 31-50")
    else :
        print("x <= 30")

# output ใช้คำสั่ง print
print("*****************")
print("Hello LAB11 Python")
print("*****************")

# ตัวแปร
x = 10 #int ตัวเลข
y = "20" # string ตัวอักษร
name = "sutit"
z= 1.5 # float ทศนิยม

print("x= ",x)
print("x+1= ",x+1)
#print("x+y= ",x+y) int + string ไม่ได้

print(f"x+1={x+1} and y ={y}")

#เรียกใช้ฟังก์ชัน
inputx()