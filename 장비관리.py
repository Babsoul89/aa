# 장비관리.py

device = {"CPU":5, "GrapicCard":10, "Ram":20}
print(device)
print(len(device))
print(device["CPU"])

#입력
device["Mainboard"] = 30

#삭제
del device["CPU"]

#수정
device["GrapicCard"] = 11
print(device)

#파이썬은 참조를 복사해서 전달
#Pass by reference
device2 = device
device2["Ram"] = 35
print(device)
print(device2)

