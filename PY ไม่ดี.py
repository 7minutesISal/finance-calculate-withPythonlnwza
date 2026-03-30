
# สร้างตัวแปรไว้เช็คว่าร้านยังเปิดอยู่ไหม
shop_open = True
count = 1

while shop_open:
    print(f"\n--- ลูกค้าคนที่ {count} ---")
    print("\n--- ยินดีต้อนรับสู่ร้านผลไม้ (กด '0' ที่จำนวนเพื่อปิดร้าน) ---")
    
    fruit_name = "มะม่วง"
    price_per_kg = 50
    
    # รับค่าเป็น float ตามที่คุณเพิ่งเรียนมา
    amount = float(input(f"ซื้อ{fruit_name} กี่กิโลกรัม? : "))

    # เงื่อนไขพิเศษ: ถ้าพิมพ์ 0 ให้ปิดลูป (ปิดร้าน)
    if amount == 0:
        shop_open = False
        print("กำลังปิดระบบร้านค้า... สวัสดีครับ")
        break # คำสั่งออกจากลูปทันที

    # ส่วนการคำนวณเดิมของคุณ
    total_price = price_per_kg * amount
    discount = 10
    totaldiscount = total_price - discount
    
    print(f"ยอดรวมหลังหักส่วนลด: {totaldiscount} บาท")
    if totaldiscount >= 200:
        print("ยินดีด้วย! คุณได้รับส่วนลดพิเศษเพิ่ม 20 บาท")
        totaldiscount = totaldiscount - 20
    else:
        print("ซื้อเพิ่มอีกนิด เพื่อรับส่วนลดพิเศษครั้งหน้านะ!")
    print("ราคาที่ต้องจ่ายจริงคือ:", totaldiscount, "บาท")
    print("-" * 30)
    count = count + 1
    if count > 5:
        shop_open = False
        print("กำลังปิดระบบร้านค้า... สวัสดีครับ")
        break # คำสั่งออกจากลูปทันที
