distance = float(input("กรุณากรอกระยะทาง (หน่วยเป็นกิโลเมตร): "))
time = float(input("กรุณากรอกเวลาที่ใช้ในการเคลื่อนที่ (หน่วยเป็นชั่วโมง): "))

if distance > 0 and time > 0:

    velocity = distance / time


    print(f"อัตราเร็วคือ {velocity:.2f} กิโลเมตรต่อชั่วโมง")
else:
    print("กรุณากรอกค่าระยะทางและเวลาที่มากกว่า 0")


