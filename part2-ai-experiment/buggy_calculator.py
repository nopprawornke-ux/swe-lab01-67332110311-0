def calculate_grade(scores):
    # แก้ไข: ตรวจสอบก่อนว่าลิสต์ว่างหรือไม่
    if len(scores) == 0:
        return "N/A", 0  # ถ้าไม่มีคะแนน ให้คืนค่าเป็น N/A และเฉลี่ย 0

    total = sum(scores) # ใช้ sum() เพื่อความกระชับ
    average = total / len(scores)
    
    if average >= 80:
        grade = "A"
    elif average >= 70:
        grade = "B"
    elif average >= 60:
        grade = "C"
    elif average >= 50:
        grade = "D"
    else:
        grade = "F"
    return grade, average

# ทดสอบรัน
print(calculate_grade([85, 92, 78, 88, 95])) # ทำงานปกติ
print(calculate_grade([]))                   # จะไม่ Error แล้ว แต่จะได้ ('N/A', 0) แทน
