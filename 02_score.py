# 判断及格（注意 >= 而不是 >）
score = int(input("请输入分数："))

if score >= 90:
    print("优秀")
elif score >= 60:
    print("及格")
else:
    print("不及格")
