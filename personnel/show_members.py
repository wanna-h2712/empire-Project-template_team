# =====================================================
#  personnel/show_members.py — คนรับผิดชอบ: ______________________
#  หน้าที่: แสดงรายชื่อลูกน้องทั้งหมดในแฟมิลี่
# =====================================================
from data import family_members

def show_members():
    for member in family_members:
        print(member)
    pass
if __name__ == "__main__":
    show_members()   # ต้องเห็น Tony กับ Luigi คนละบรรทัด
