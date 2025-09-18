print("請選擇轉換類型")
print("1: 公里 -> 英里")
print("2: 英里 -> 公里")
print("3: 攝氏 -> 華氏")
print("4: 華氏 -> 攝氏")
print("5: 公斤 -> 磅")
print("6: 磅 -> 公斤")
x=int(input("請輸入選項 (1-6) :"))
if x==1 :
    y=int(input("請輸入數值 :"))
    print("結果",y*0.621371,"公里")
elif x==2:
    y=int(input("請輸入數值 :"))
    print("結果",y*1.609344,"英里")
elif x==3:
    y=int(input("請輸入數值 :"))
    print("結果",(y*9/5)+32,"°F")
elif x==4:
    y=int(input("請輸入數值 :"))
    print("結果",(y-32)*5/9,"°C")
elif x==5:
    y=int(input("請輸入數值 :"))
    print("結果",y*2.20462,"磅")
elif x==6:
    y=int(input("請輸入數值 :"))
    print("結果",y*0.453592,"公斤")
    