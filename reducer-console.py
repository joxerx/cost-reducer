def goexit():
    while True:
        answer = input("Завершить ввод? y/n: ").lower()
        if answer == "y":
            return True
        elif answer == "n":
            return False
        else:
            print("Ответ может быть: \r\n y - да, завершить; \r\n n - нет, продолжить ввод")
            continue


def getfloat(msg):
    while True:
        try:
            res_value = float(input(msg))
            if res_value < 0:
                print("Значение должно быть больше нуля")
                continue
            return res_value
        except ValueError:
            print("Неверный ввод")
            continue


def getinteger(msg):
    while True:
        try:
            res_value = int(input(msg))
            if res_value < 0:
                print("Значение должно быть больше нуля")
                continue
            return res_value
        except ValueError:
            print("Неверный ввод")
            continue


def decrease_average_cost(cur_price, wanted_percent, deals_count):
    spent = 0
    quantity = 0
    for i in range(deals_count):
        spent += purchase_price[i] * purchases_amount[i]
        quantity += purchases_amount[i]

    start_average_price = spent/quantity
    average_price = start_average_price

    print("Начальная средняя стоимость: " + str(start_average_price))

    new_quantity = 0
    while average_price > start_average_price * (1 - (wanted_percent / 100)):
        spent += cur_price
        quantity += 1
        average_price = spent/quantity
        new_quantity += 1
        if average_price > start_average_price:
            res = "При указанной текущей цене невозможно снизить среднюю стоимость покупки"
            return res
    res = "Чтобы добиться желаемого результата необходимо приобрести " + str(new_quantity) + " единиц по текущей стоимости"
    return res


print("Нужно ввести информацию обо всех сделках по интересуемому активу. Чтобы прекратить ввод, отправьте 0.")
purchase_price = []
purchases_amount = []
deals_counter = 0
while True:
    while True:
        price = getfloat("Цена покупки №" + str(deals_counter + 1) + ": ")
        if price > 0:
            purchase_price.append(price)
            break
        elif price == 0:
            if goexit():
                break
            else:
                continue
    if len(purchase_price) == len(purchases_amount):
        break
    while True:
        amount = getinteger("Количество №" + str(deals_counter + 1) + ": ")
        if amount > 0:
            purchases_amount.append(amount)
            deals_counter += 1
            break
        elif amount == 0:
            if goexit():
                purchase_price.pop()
                break
            else:
                continue
    if len(purchase_price) != len(purchases_amount):
        break

current_price = getfloat("Текущая стоимость: ")
decrease_percent = getfloat("На сколько процентов нужно снизить среднюю стоимость: ")
print(decrease_average_cost(current_price, decrease_percent, deals_counter))

