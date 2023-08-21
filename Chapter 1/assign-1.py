weight = int(input('Please enter your weight (kg): '))
hight = int(input('Please enter your hight (cm): '))

cm = 100 / hight

bmi = weight / (cm * 2)

if bmi < 18.5:
    print('คุณผอมเกินไป')
elif bmi >= 18.5 and bmi <= 24.9:
    print('คุณอยู่เกณฑ์เหมาะสม นํ้าหนักตัวปกติ')
elif bmi >= 25 and bmi <= 29.9:
    print('คุณน้ำหนักเกิน แต่ยังไม่เรียกว่าอ้วน')
elif bmi >= 30 and bmi <= 30.9:
    print('คุณอ้วนแล้ว!')
elif bmi > 40:
    print('คุณอ้วนเกินไป อันตรายมาก!!!!')
