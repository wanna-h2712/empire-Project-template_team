# =====================================================
#  weapon_shop/equip_item.py — คนรับผิดชอบ: อัยมี่
#  หน้าที่: ซื้อและสวมใส่อาวุธให้ลูกน้อง (เช็คเงื่อนไข 2 อย่างก่อน)
# =====================================================

def equip_item(person, weapon):
#   - เช็คเงิน: เงินของ person ไม่พอราคา weapon -> ซื้อไม่ได้
#   - เช็คอาวุธ: person มีอาวุธอยู่แล้ว (equipment ไม่ใช่ "ไม่มี") -> ใส่เพิ่มไม่ได้
#   - ผ่านทั้งคู่ -> หักเงิน, เปลี่ยน equipment เป็นชื่ออาวุธ, บวก bonus เข้า power
#   - return {"status": True/False, "message": ข้อความบอกผล}
    # TODO: เขียนโค้ดตรงนี้
    dict_weapon = {"status": True, "message": "ระบบทำงาน"}

    if person["money"] >= weapon["price"] :
        if person["equipment"] == "ไม่มี" :
            person["money"] = (int(person["money"] - weapon["price"]))
            print(person["money"]) 
            person["equipment"] = weapon["name"]
            person["power"] = (int(person["power"] + weapon["bonus"]))
            return dict_weapon
        else :
            return"ไม่สามารถสวมใส่ได้"
    else :
       return "เงินไม่พอ"
# family_members = [
#     {"name": "Tony", "age": 35, "role": "Hitman", "power": 7, "money": 5000000, "equipment": "ไม่มี"},
#     {"name": "Luigi", "age": 28, "role": "Hitman", "power": 4, "money": 150000, "equipment": "ไม่มี"}
# ]
# weapons_catalog = {
#     "1": {"name": "สนับมือ", "price": 10000, "bonus": 2},
#     "2": {"name": "ปืนพก 9mm", "price": 50000, "bonus": 5},
#     "3": {"name": "ปืนกล Thompson", "price": 150000, "bonus": 10}
# }
# ทดสอบเฉพาะไฟล์ตัวเอง: พิมพ์  python -m weapon_shop.equip_item
if __name__ == "__main__":
    vito = {"name": "Vito", "money": 60000, "power": 5, "equipment": "ไม่มี"}
    gun = {"name": "ปืนพก 9mm", "price": 50000, "bonus": 5}

    print(equip_item(vito, gun))   # ต้องได้ status True
    # print(vito)                    # เงินเหลือ 10000, power เป็น 10, equipment เป็นปืน
    # print(equip_item(vito, gun))
    # print(vito)   # ครั้งที่สองต้องได้ "มีอาวุธอยู่แล้ว"
