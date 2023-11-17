def is_leapyear(year):
    if year % 400 == 0:
        return True
    elif year % 4 == 0 and not year % 100 == 0:
        return True
    return False

# 実行文
while True:
    year = input("西暦を入力(n 入力で終了) >> ")
    
    # 終了処理
    if year == "n":
        break

    # うるう年判定
    if is_leapyear(int(year)):
        print(f"西暦{year}年は、うるう年です")
    else:
        print(f"西暦{year}年は、うるう年ではありません")