# 割り勘データを入力
def int_input(text):
    return int(input(f"{text}を入力してください >>"))

# 割り勘を計算
# 幹事の支払額の計算
def calc_payment(amount,people=2):
    dnum = amount / people
    pay = dnum // 100 * 100
    if dnum > pay:
        pay = pay + 100
    payorg = amount - pay * (people - 1)
    return int(pay),int(payorg)

# 結果の表示
def show_payment(pay,payorg,people=2,):
    print("*** 支払額 ***")
    print(f"1人あたり{pay}円({people}人)、幹事は{payorg}円です")


amount = int_input("支払い総額")
people = int_input("参加人数")
pay,payorg = calc_payment(amount,people)
show_payment(pay,payorg,people)