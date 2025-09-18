print("請選擇轉換類型: length / temperatur / weight")
x=input("輸入類型 :")
if x =="length":
    y=int(input("請輸入數值 :"))
    print(x,"公里","=",y*0.621371,"英里")
    print(x,"英里","=",y*1.609344,"公里")
elif x== "temperatur":
    y=int(input("請輸入數值 :"))
    print(x,"攝氏","=",(y*9/5)+32,"華氏")
    print(x,"華氏","=",(y-32)*5/9,"攝氏")
elif x=="weight":
    y=int(input("請輸入數值 :"))
    print(x,"公斤","=",y*2.20462,"磅")
    print(x,"磅","=",y*0.453592,"公斤")
    