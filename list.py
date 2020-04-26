# การสร้างข้อมูลแบบ List
number = [5, 8, 13, 24, 7, 16]
name = ['Jhon', 'Jane', 'Jame', 'Chai']
Mixed = [10, 25, 75, True, 'Krichai']
# การเข้าถึงสมาชิกใน List
print(number[5])
print(name[3])
print(Mixed[2], Mixed[3])
# การนับสมาชิกใน List
print("สมาชิกทั้งหมดชิก", len(number))
# การสร้าง List แบบว่าง
data = []
# การเพิ่มสมาชิกเข้าไปใน List ว่าง
data.append(10)
data.append(15)
data.append(20)
print(data)
# การ Update สมาชิกใน List
data[1] = 12
print(data)
# Function วน Loop อ่านสมาชิกทั้งหมด
for d in number:
    print(d)
# loop หาผลรวมใน List
sum = 0
for s in number:
    sum += s
    print(sum)
