zp = float(input())
proc = float(input())
print("Размер подоходного налога на сумму:", str(zp * (proc/100)))
print("Сумма, получаемая на руки:", str(zp - zp*(proc/100)))