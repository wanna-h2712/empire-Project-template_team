# =====================================================
#  personnel/remove_member.py — คนรับผิดชอบ: ______________________
#  หน้าที่: ลบลูกน้องออกจากแฟมิลี่ตามชื่อ
# =====================================================
from data import family_members

def remove_member(target_name):
    for member in family_members:
        if member["name"].lower() == target_name.lower():  
            family_members.remove(member)
            print("สั่งเก็บสำเร็จ")
            return True
        return False

#   - หาคนที่ชื่อตรงกับ target_name (ไม่สนตัวพิมพ์ใหญ่/เล็ก) แล้วลบออกจาก family_members
#   - ลบสำเร็จ -> return True | ไม่เจอ -> return False
    # TODO: เขียนโค้ดตรงนี้
    pass


# ทดสอบเฉพาะไฟล์ตัวเอง: พิมพ์  python -m personnel.remove_member
if __name__ == "__main__":
    print(remove_member("TONY"))   # ครั้งแรกต้องได้ True
    # print(remove_member("Luigi"))   # ครั้งที่สองต้องได้ False (ลบไปแล้ว)
    print(family_members)           # ต้องเหลือแค่ Tony
