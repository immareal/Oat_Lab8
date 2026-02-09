import pyqrcode
import png
import os
stdcode = "68071"

nums = []

while True:
    n = int(input("กรอกตัวเลข (0 เพื่อหยุด): "))
    if n == 0:
        break
    nums.append(n)

print(nums)

for idx, n in enumerate(nums, start=1):
    st = str(n)                     
    number = str(idx).zfill(4)      
    filename = f"{n}{number}.png"  

    qr_code = pyqrcode.create(st)
    qr_code.png(filename, scale=10)

# i = len(nums)
# number = str(i).zfill(4)
# st = nums + str(number)
# qr_code = pyqrcode.create(st)
# filepath = st + ".png"
# qr_code.png(filepath, scale=10)