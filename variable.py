a = 3
b = 4.92
c = "look forward"
print(a)
print(b)
print(c)
print(a, b, c)
x = y = z = 10
j, k = 5, 15
print(x, y, z)
print(j, k)
#boolean
status=False
msg=True
print(status,msg)
#ตัวแปรแสดงผลร่วมกับข้อความ
#ที่ 1
print("ราคาขายต่อชิ้น",b,"บาท")
#ที่2 String interpolation
print("ราคาขายต่อชิ้น %.2f บาท"%b)
print("ราคาขายต่อชิ้น %.2f บาท มีจำนวน %d ชิ้น"%(b,a))
#ที่3 Format String
print(f"ราคาขายต่อชิ้น {b} มีจำนวน {a}")
