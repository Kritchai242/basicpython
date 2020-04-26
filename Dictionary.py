scores = {
    'john': 1200,
    'chai': 2000,
    'too': 3000
}
print(scores)
print(scores['chai'])
# การเพิ่ม Dictionary เหมือน list
scores['chit'] = 5000
print(scores)
# การสร้าง Dictionary ว่าง
points = {}
# เพิ่มค่าเข้า Dictionary
points['a'] = 20.5
points['b'] = 30.2
points['c'] = 50.5
print(points)
# loop แสดงค่าของ Dictionary
for k, v in scores.items():
    print(k, v)
