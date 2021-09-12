p_var = {"cm": 0.01, "lbs": 0.45359237, "ft": 0.3048}
weight, wu = input("Weight : ").split()
height, hu = input("Height : ").split()
weight = float(weight)*p_var[wu]
height = float(height)*p_var[hu]
BMI = weight / height**2
if BMI < 18.5:
    print("ผอม")

elif BMI >= 18.5 and BMI < 23.0:
    print("รูปร่างปกติ")

elif BMI >= 23.0 and BMI < 25.0:
    print("รูปร่างอ้วน")

elif BMI >= 25.0 and BMI < 30.0:
    print("อ้วนระดับ 1")

elif BMI >= 30.0:
    print("อ้วนระดับ 2")