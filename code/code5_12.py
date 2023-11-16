def input_scores(name):
    print(f"{name}さんの試験結果を入力してください")
    network = int(input("ネットワークの得点は? >> "))
    database = int(input("データベースの得点は? >> "))
    security = int(input("セキュリティの得点は? >> "))
    scores = [network,database,security]

def calc_average(scores):
    avg = sum(scores) / len(scores)
    print(f"平均点は{avg}です")

input_scores("浅木")
calc_average(scores)