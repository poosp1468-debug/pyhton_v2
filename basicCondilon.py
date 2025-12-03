apple = 1000
banana = 2000

print("=== ຮ້ານໜາກໄມ້ BorHu ===")
print("1. apple =", apple)
print("2. banana =", banana)

choice = input("ເລືອກສີນຄ່າ (1 ຫຼື 2): ")

while choice not in ["1", "2"]:
    choice = input ("ເລືອກພິດ! ລູກຄ້າເລືອກ 1 ຫຼື 2 :")
if choice == "1":
    item = "apple"
    price = apple
else:
    item = "banana"
    price = banana
    print(f"\ລູກຄ້າເລືອກ {item} ລາຄາ {price}kip")
    money = int(input("ລູກຄ້າໃສ່ຈຳນວນເງິນ: "))
    while money < price:
        print("ເງິນບໍ່ພໍ! ລຸກຄ້າໃສ່ໃໝ່")
        money = int(input("ລູກຄ້າໃສ່ຈຳນວນເງິນ:"))
        change = money - price
        print("\n=== ສະລຸບລາຍການ ===")
        print("ສີນຄ້າ:", item)
        print("ລາຄາ:", price)
        print("ຈຳນວນເງິນທີ່ຈາຍ:", money)
        print("ເງິນທອນ:", change)
        print("ຂອບໃຈທີ່ໃຊ້ບໍລີການ Borhu!")
        print ("447799")
        print ("664411")