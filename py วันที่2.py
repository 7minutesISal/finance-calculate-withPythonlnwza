
fruits = ("มะม่วง", "ส้ม", "องุ่น", "ทุเรียน")
fruit_price = (50, 60, 100, 200)
total_sale = (10, 20, 30, 40)
people = 1
openshop = True
grand_total = 0
total_kg = [0, 0, 0, 0]
sales_history1 = []
sales_history2 = []
current_stock = []
stock = ["100\n", "50\n", "30\n", "20\n"]
with open ("stock.txt", "w", encoding="utf-8") as t:
        t.writelines(stock)
        print("(เตรียมของแล้ว)")
with open ("stock.txt", "r",) as t:
        for i in range(4):
            data = t.readline()
            cleandata = data.strip()
            current_stock.append(float(cleandata))
def calculate_discount(total, total_sale):
        if total > 800 :
                total_sale10 = total - total_sale[3]
        elif total > 600 :
                total_sale10 = total - total_sale[2]
        elif total > 400 :
                total_sale10 = total - total_sale[1]
        elif total > 200 :
                total_sale10 = total - total_sale[0]
        else:
                total_sale10 = total
        print(f"ราคาทั้งหมดรวมส่วนลด: {total_sale10} บาท")
        return total_sale10

while openshop :
    print("ลูกค้าคนที่",people)
    name = input("ซื่อลูกค้า(พิม 0 ปิดร้าน):")

    if name == "0":
        print("ปิดละ")
        openshop = False
        break
    print("--- รายการสินค้าวันนี้ ---")
    for i in range(4):
        print(i+1, ".", fruits[i], "ราคา", fruit_price[i], "บาท")
    print("stockที่มีตอนนี้--")
    for i in range(4):
        print(i+1, ".", fruits[i], "ตอนนี้มี", current_stock[i], "กิโล")

    while True:
            try :        
                customer = int(input("เลือกผลไม้ : ")) - 1

                if -1 <= customer <= 3 :
                        break
                else:
                        print("ไม่มีกลับไปเลือกใหม่!!")
            except ValueError:
                print("⚠️ กรุณาใส่เป็น 'ตัวเลข' 1, 2, 3 หรือ 4 เท่านั้นครับ!")

    if customer == -1:
        print("ร้านปิดแล้ว")
        openshop = False
        break

    choice = fruits[customer]
    pricechoice = fruit_price[customer]

    print(f"คุณเลือก: {choice}")
    while True:
            try:
                kg = float(input("จำนวนกิโลกรัม : "))
                if kg > current_stock[customer]:
                        print(f"ของไม่พอเว้ย (เหลือแค่{current_stock[customer]} กก.)")
                else:
                        break
            except ValueError:
                print("กรุณาใส่แค่ตัวเลขเท่านั้นนะจ๊ะ")

    current_stock[customer] = current_stock[customer] - kg
    print(f"หัก เหลือ: {current_stock[customer]}กิโล")
    total = pricechoice * kg

    total_kg[customer] = total_kg[customer] + kg

    print(f"ราคาทั้งหมด: {total} บาท")
    final_price = calculate_discount(total, total_sale)

    member = input("มีสมาชิกมั้ย(y/n): ")
    if member == "y" :
        final_price = final_price * 0.95
        print("ลดเพิ่ม 5% สำหรับสมาชิกเรียบร้อย!")
    elif member == "n" :
        member1 = input("สนใจเป็นสมาชิกมั้ย(y/n): ")
        if member1 == "y" :
            print("โอเค ทำแบบนี้")
            final_price = final_price * 0.95
            print("ลดเพิ่ม 5% สำหรับสมาชิกเรียบร้อย!")
        elif member1 == "n" :
            print("โอเค")
    print(f"ยอดที่ต้องชำระจริง: {final_price} บาท")
    record = f"ลูกค้าคนที่{people}: ซื้อ{choice}{kg}กิโล ยอด {final_price} บาท"
    sales_history1.append(record)

    current_sale = {
        "customer" : name,
        "fruit" : choice,
        "weight" : kg,
        "price" : final_price
    }
    sales_history2.append(current_sale)

    grand_total = grand_total + final_price

    print("\n--- 🧾 ประวัติการขาย (แบบแยกข้อมูล) ---")
    for row in sales_history2:
        print(f"คุณ {row['customer']} จ่ายทั้งหมด {row['price']} บาท")

    vat = grand_total * 0.07
    final_price = grand_total + vat

    print(f"\n📢 สรุปยอดหลังรวมภาษี 7%")
    print(f"ยอดก่อน vat:{grand_total} บาท")
    print(f"ภาษีมูลค่าเพิ่ม (7%): {vat:.2f} บาท")
    print(f"ยอดรวมสุทธิที่ต้องนำส่ง: {final_price:.2f} บาท")
    people = people + 1

    if people > 4 :
        openshop = False
        print("ชู่วไป!!ร้านปิดละ")
        break
if openshop == False :
    print(f"สรุปยอดขายวันนี้: {grand_total} บาท")
if openshop == False:
    print("\n=== สรุปยอดขายสินค้าวันนี้ ===")
    for i in range(4):
        print(f"{fruits[i]} ขายได้ทั้งหมด: {total_kg[i]} กิโลกรัม")

if openshop == False :
    print("ประวัติขายวันนี้")
    for row in sales_history1 :
        print(row)

if openshop == False :
    allprice = []
    for row in sales_history2 :
        allprice.append(row['price'])
    if len(allprice) > 0:
        vipprice = max(allprice)
        print(f"ยอดสูงสุดวันนี้: {vipprice:.2f}บาท")
        for row in sales_history2:
            if row['price'] == vipprice:
                print(f"ลูกค้าที่จ่ายหนักสุดคือ: {row['customer']}")
    else:
        print("ยังไม่มีใครซื้อเลย")

if openshop == False :
    if len(sales_history2) > 0:
        search_name = input("ชื่อลูกค้าที่ต้องการหา:")
        found = False

        for row in sales_history2:
            if row["customer"] == search_name:
                print(f"พบข้อมูล: คุณ {row['customer']} ซื้อ {row['fruit']} ไปทั้งหมด {row['price']} บาท")
                found = True

        if not found:
            print("ไม่มีโว้ย")
    else:
        print("ไม่มีชื่อให้หา")

with open ("report.txt","w", encoding="utf-8") as f:
    f.write(f"สรุปยอดขายรวมวันนี้: {grand_total} บาท\n")
    f.write("-" * 30 + "\n")
    for row in sales_history2:
        line = f"คุณ {row['customer']} ซื้อ {row['fruit']} ยอด {row['price']} บาท\n"
        f.write(line)

with open ("report.txt","r", encoding="utf-8") as b:
    data = b.read()

    print("📖 ดึงข้อมูลจากสมุดบัญชีออกมาได้ดังนี้:")
    print(data)

with open("stock.txt", "w", encoding="utf-8") as t:
    new_stock_list = []
    for s in current_stock:
        new_stock_list.append(str(s) + "\n")
    t.writelines(new_stock_list)
