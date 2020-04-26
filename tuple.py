number = (5, 8, 13, 24, 7, 16)  # ใช้ () สำหรับ tuple
Mixed = (10, 25, [5, 4, 3], 75, True, 'Krichai')
print(number[2])
print(Mixed[2])
print(Mixed[2][1])
# ลองเปลี่ยนแปลงค่าสมาชิก ไม่สามารถเปลี่ยนได้
number[2] = 10
print(number)
