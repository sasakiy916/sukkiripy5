def eat(breakfast="トースト",lunch="おにぎり",dinner="カレー",*desserts):
    print(f"朝は{breakfast}を食べました")
    print(f"昼は{lunch}を食べました")
    print(f"晩は{dinner}を食べました")
    for d in desserts:
        print(f"おやつに{d}を食べました")

eat("と","金","負","かかか","じゃじゃじゃ")