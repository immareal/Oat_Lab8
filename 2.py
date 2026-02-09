from datetime import datetime
from pythainlp.util import num_to_thaiword
from gtts import gTTS
months_th = [
    "มกราคม",
    "กุมภาพันธ์",
    "มีนาคม",
    "เมษายน",
    "พฤษภาคม",
    "มิถุนายน",
    "กรกฎาคม",
    "สิงหาคม",
    "กันยายน",
    "ตุลาคม",
    "พฤศจิกายน",
    "ธันวาคม"
]

now = datetime.now()

year = num_to_thaiword(now.year + 543)
month = months_th[now.month - 1]
day = num_to_thaiword(now.day)
hour   = num_to_thaiword(now.hour)
minute = num_to_thaiword(now.minute)

dayth = ["จันทร์","อังคาร","พุธ","พฤหัส","ศุกร์","เสาร์","อาทิตย์"]
date = dayth[now.weekday()]

name = input("กรอกชื่อของท่าน : ")

text = f'สวัสดีคุณ{name} วันนี้วัน{date}ที่ {day} {month} ปีพุธศักราช {year} ขณะนี้เวลา {hour} นาฬิกา {minute} นาที วันนี้เป็นวันครบรอบวันเกิดของคุณ ขอให้คุณมีความสุขมากๆนะครับ'

tts_th = gTTS(text, lang='th')
tts_th.save('media1.mp3')
