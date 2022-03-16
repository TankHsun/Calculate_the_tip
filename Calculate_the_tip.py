#計算小費與總金額
def Calculate(prize,rate):
	tip = round(prize * (rate / 100))   #round四捨五入
	total =  tip + prize
	print('在費率', rate, '%的狀況下，小費為', tip)
	print('總金額：', total)


prize = int(input('共消費多少?'))
rate = int(input('費率為多少?'))
Calculate(prize,rate)