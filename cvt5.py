def ten_str(n):
	if(n>9 and n<20):
		if(n==10):
			return "Ten"
		if(n==11):
			return "Eleven"
		if(n==12):
			return "Twelve"
		if(n==13):
			return "Thirteen"
		if(n==14):
			return "Fourteen"
		if(n==15):
			return "Fifteen"
		if(n==16):
			return "Sixteen"
		if(n==17):
			return "Seventeen"
		if(n==18):
			return "Eighteen"
		if(n==19):
			return "Nineteen"
	else:
		f1=0
		f2=0
		k=n%10
		if(k!=0):
			f1=1
		if(k==1):
			str1 = "One"
		if(k==2):
			str1 = "Two"
		if(k==3):
			str1 = "Three"
		if(k==4):
			str1 = "Four"
		if(k==5):
			str1 = "Five"
		if(k==6):
			str1 = "Six"
		if(k==7):
			str1 = "Seven"
		if(k==8):
			str1 = "Eight"
		if(k==9):
			str1 = "Nine"
		k=n/10
		if(k!=0):
			f2=1
		if(k==2):
			str2 = "Twenty "
		if(k==3):
			str2 = "Thirty"
		if(k==4):
			str2 = "Fourty"
		if(k==5):
			str2 = "Fifty"
		if(k==6):
			str2 = "Sixty"
		if(k==7):
			str2 = "Seventy"
		if(k==8):
			str2 = "Eighty"
		if(k==9):
			str2 = "Ninety"

		if(f1==0):
			str1 = ""
		if(f2==0):
			str2 = ""
		str_f = str2 + " " + str1
		return str_f

def make_str(n):
	k=n
	str_num = ""
	char_count=0
	while(k>0):
		char_count+=1
		k=k/10

	if(char_count > 3):
		num = n
		str_count1 = ten_str(num/1000)
		str_count2 = ten_str(num%100)
		str_count3 = ten_str((num/100)%10)
		str_num = str_count1 + " Thousand " + str_count3 + " Hundred " + str_count2

	if(char_count == 3):
		num = n
		str_count2 = ten_str(num%100)
		str_count3 = ten_str((num/100)%10)
		str_num = str_count3 + " Hundred " + str_count2

	if(char_count < 3):
		num = n
		str_num = ten_str(num)

	str_num = str_num.lstrip()
	str_num = str_num.rstrip()

	return str_num

a = map(int, raw_input().split(' '))
m = a[0]
n = a[1]
sum1=m
sum2=n
while(sum1 != sum2 and sum1 < 99999 and sum2 < 99999):
	str1 = make_str(m)
	str2 = make_str(n)
	if(m<n):
		sum1 = m
		sum2 = n
	else:
		sum1 = n
		sum2 = m
	#print (sum1, sum2, str1, str2)
	#print (str2>str1)

	if(str1 < str2):
		sum1 = sum1 + m
		sum2 = sum2 + n
	else:
		sum1 = sum1 + n
		sum2 = sum2 + m

	m = sum1
	n = sum2

if(sum1 < 99999 and sum2 < 99999):
	print sum1
else:
	print "Out of bounds"