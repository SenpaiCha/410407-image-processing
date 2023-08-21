class BMI:
    def __init__(self) -> None:
        self.weight = int(input('Please enter your weight (kg): '))
        self.hight = int(input('Please enter your hight (cm): '))
        self.Calculate_BMI()

    def Calculate_BMI(self):
        self.cm = self.hight / 100
        self.bmi = self.weight / (self.cm * 2)

        if self.bmi < 18.5:
            print('คุณผอมเกินไป')
        elif self.bmi >= 18.5 and self.bmi <= 24.9:
            print('คุณอยู่เกณฑ์เหมาะสม นํ้าหนักตัวปกติ')
        elif self.bmi >= 25 and self.bmi <= 29.9:
            print('คุณน้ำหนักเกิน แต่ยังไม่เรียกว่าอ้วน')
        elif self.bmi >= 30 and self.bmi <= 30.9:
            print('คุณอ้วนแล้ว!')
        elif self.bmi > 40:
            print('คุณอ้วนเกินไป อันตรายมาก!!!!')

BMI()




