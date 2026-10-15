import re

def validate_student_id(student_id):
    """
    ตรวจสอบรูปแบบรหัสนักศึกษา มทร.อีสาน (RMUTI)
    รูปแบบ: ตัวเลข 11 หลัก ตามด้วยเครื่องหมายขีด (-) และตัวเลข 1 หลัก (Check Digit)
    
    Args:
        student_id (str): ข้อความรหัสนักศึกษาที่ต้องการตรวจสอบ
        
    Returns:
        bool: คืนค่า True หากรูปแบบถูกต้องตามกำหนด, คืนค่า False หากรูปแบบผิด
    """
    # อธิบาย Pattern ของ Regex:
    # ^       : เริ่มต้นข้อความ
    # \d{11}  : ต้องเป็นตัวเลข (0-9) จำนวนพอดี 11 หลัก
    # -       : ต้องตามด้วยเครื่องหมายขีด 1 ตัว
    # \d{1}   : ต้องตามด้วยตัวเลข (0-9) อีกพอดี 1 หลัก
    # $       : สิ้นสุดข้อความ (ห้ามมีตัวอักษรอื่นต่อท้ายอีก)
    pattern = r"^\d{11}-\d{1}$"
    
    # ใช้ re.match เพื่อเช็คว่า student_id ตรงกับ pattern หรือไม่
    if re.match(pattern, student_id):
        return True
    else:
        return False

# --- ตัวอย่างการใช้งาน 3 กรณี ---

# กรณีที่ 1: รูปแบบถูกต้อง
id1 = "63332110339-5"
print(f"รหัส {id1}: {validate_student_id(id1)}")  # ผลลัพธ์: True

# กรณีที่ 2: ผิดเพราะลืมใส่ขีด หรือจำนวนหลักไม่ครบ
id2 = "633321103395" 
print(f"รหัส {id2}: {validate_student_id(id2)}")  # ผลลัพธ์: False

# กรณีที่ 3: ผิดเพราะมีตัวอักษรปน หรือรูปแบบไม่ใช่ตัวเลข
id3 = "63332110ABC-5"
print(f"รหัส {id3}: {validate_student_id(id3)}")  # ผลลัพธ์: False
# เพิ่มบรรทัดทดสอบต่อท้ายโค้ดที่ AI ให้มา
print(validate_student_id("63332110339-5"))  # ควรได้ True
print(validate_student_id("63332110339"))    # ไม่มี check digit -- ผลเป็นอะไร
print(validate_student_id("6333211033-5"))   # ตัวเลขขาด 1 ตัว -- ผลเป็นอะไร
print(validate_student_id("AB332110339-5"))  # มีตัวอักษรนำหน้า -- ผลเป็นอะไร
print(validate_student_id(""))               # string ว่าง -- ผลเป็นอะไร
