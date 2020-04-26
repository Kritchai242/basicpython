print("-----------------")
print("#Summation Program")
print("# Tytpe 'Exit' to end program")
print("-----------------")

# ตัวใว้เก็บผลรวม
sumdata = 0
count = 1
while True:
    data = input("Enter Number {count}:")
    # ตรวจว่าผู้ใช้ป้อน 'Exit'
    if data == "exit":
        break
    # การหาผลรวม
    count = count+1
    sumdata += int(data)
print(count)
print(f"Sum is data{sumdata}")
