# 1)შექმენით ფუნქცია რომელსაც გადაეცემა სახელები,თქვენი დავალებაა ტერმინალში გამოიტანოთ კენტ ინდექსზე მდგომი სახელები და შეინახოთ ახალ სიაში
def name1(user_kenti):
    New = ""
    for i in user_kenti:
        if user_kenti.index(i) % 2 ==1:
            New.append(i)
    return New
print(name1(["dato" , "gio" , "tengo"]))



# 2)შექმენით ფუნქცია რომელსაც გადაეცემა სახელები,ზოგი სახელი უნდა იყოს დაწყებული დიდი ასოთი ზოგი კი ჩვეულებრივ პატარა ასოებით უნდა იყოს დაწყებული,თქვენი დავალებაა ახალ სიაშ დაამატოთ მხოლოდ ის სახაელები რომელთა პირველი ასოც არის დიდი
def name(user_name):
    list1 = []
    for i in user_name:
        if i[0] == i.upper():
            list1.append(i)
print(name(["Dato" , "gio" ,"Tengoi" ]))




# 3)შექმენით ფუნქცია რომელსაც გადაეცემა სახელები,ეს სახელები ზოგი მთლინად უნდა იყოს დიდი ასოებით დაწერილი ზოგი კი პატარა,თქვენი დავალებაა ახალ სიაშ დაამატოთ მხოლოდ დიდი ასოებით დაწერილი სახელები

def name(user_name):
    list1 = []
    for i in user_name:
        if i == i.upper():
            list1.append(i)
print(name(["dato" , "gio" ,"tengoi"  "DATO" , "GIO" , "LEKSO"]))


# 4)შექმენით ფუნქცია რომელსაც გადაეცემა სტრინგი,თქვენი დავალებაა რომ ამ სტრინგიდან ამოიღოთ მხოლოდ ხმოვანი ასოები და შეინახოთ ერთად ცვლადში,შემდეგ კი ეს ამოღებული ასოები გადააქციეთ დიდ ასოებათ და ისე დააბრუნეთ
def tx_dd(user_str):
    new = []
    for i in user_str:
        if i in "aeiou":
            new.append(i)
            new.upper()
    return new
print(tx_dd(["dato magaria programireba"]))



# 5)შექმენით ფუნქცია რომელსაც გადაეცემა სტრინგებით სავსე სია,თქვენი დავალებაა ახალ სიაში დაამატოთ მხოლოდ ის სტრინგები რომლებიც იწყებიან დიდ ასოზე და ასევე მათ სიგრძე არის 5 ზე ნაკლები და ასევე ამ სტრინგში არის ერთი ასო მაინც ხმოვანი
def str1(user_str):
    new = []
    for i in user_str:
        if len(i) < 5 and i in "aeiou" and i.capitalize():
            new.append(i)
print(str1(["dato", "Dagaria" ,"raaaaa" , "gio"]))

