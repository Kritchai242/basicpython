# import ทั้งหมดทุก Function ใน Module
#import numbers

# # # เรียกใช้งาน
# print(numbers.factorial(5))
# print(numbers.fibonacci(100))

# import บาง Function ใน Module
# from numbers import factorial
# print(numbers.factorial(5))

# # import ทุก Function ใน Module
# from numbers import *
# print(numbers.factorial(5))
# print(numbers.fibonacci(100))

# import ทุก Function และเปลี่ยนชื่อ
from numbers import factorial as fa, fibonacci as fi
# การเรียกใช้งาน
d = input("factoril number:")
print(fa(int(d)))
print(fi(int(d)))
