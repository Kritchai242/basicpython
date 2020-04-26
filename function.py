# การสร้าง Fuction แบบไม่มีการ Return Value
def hello(name):
    print(f"hello {name}")


# เรียกใช้ Fuction Hello()
hello('chai')
# การสร้าง Fuction แบบมีการ Return Value


def area(width, height):
    total = width*height
    return total


# เรียกใช้ Fuction area()
print("พื้นที่ทั้งหมด", area(5, 8))
print(area(12.9, 8.7))

# fucntion แบบมีค่าเริ่มต้น


def show_info(name="", salary=0.00):
    print(f"name:{name}")
    print(f"salary:{salary}")


# การแสดงผลข้อมูลจาก Function
show_info()
print()
show_info('chai', 12000)
