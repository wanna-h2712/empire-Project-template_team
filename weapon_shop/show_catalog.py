# =====================================================
#  weapon_shop/show_catalog.py — คนรับผิดชอบ: ฟลุ๊ค______________________
#  หน้าที่: แสดงรายการอาวุธทั้งหมดที่มีขาย
# =====================================================
from data import weapons_catalog

def show_catalog():
#   - print อาวุธทุกชิ้นใน weapons_catalog บรรทัดละชิ้น (รหัส, ชื่อ, ราคา, พลังโบนัส)
    # TODO: เขียนโค้ดตรงนี้
    # print("name : สนับมือ - price : 10000 - bonus: 2")
    # print("name : ปืนพก 9mm - price : 50000 - bonus : 5")
    # print("name : ปืนกล Thompson - price : 150000 - bonus : 10")

    for i in weapons_catalog :
        print(f"{'1'} : {weapons_catalog["1"]}")
        print(f"{'2'} : {weapons_catalog["2"]}")
        print(f"{'3'} : {weapons_catalog["3"]}")
print(show_catalog())


# weapons_catalog = {
#     "1": {"name": "สนับมือ", "price": 10000, "bonus": 2},
#     "2": {"name": "ปืนพก 9mm", "price": 50000, "bonus": 5},
#     "3": {"name": "ปืนกล Thompson", "price": 150000, "bonus": 10}
# }



# ทดสอบเฉพาะไฟล์ตัวเอง: พิมพ์  python -m weapon_shop.show_catalog
# if __name__ == "__main__":
#     show_catalog()   # ต้องเห็นอาวุธครบ 3 ชิ้น


# print (show_catalog())