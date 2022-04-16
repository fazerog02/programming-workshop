YASEGATA = 18.5
HUTUU = 25

print("身長[cm]を入力してください")
shintyou = float(input())
shintyou = shintyou / 100  # BMIは身長[m]で計算するので，[cm]->[m]に直す

print("体重[kg]を入力してください")
taijuu = float(input())

bmi = taijuu / (shintyou * shintyou)
print("あなたのBMIは「" + str(bmi) + "」です")

print("あなたの体型は", end="")
if bmi < YASEGATA:
    print("やせ型です")
elif bmi < HUTUU:
    print("普通体型です")
else:
    print("肥満です")
