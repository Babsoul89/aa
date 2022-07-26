# demoDict.py
# 사전식 구조


color = {"apple":"red", "banana":"yellow"}
print(color)
print(len(color))
print(color["apple"])
color["cherry"] = "red"
print(color)
del color["apple"]
print(color)
for kv in color.items():
    print(kv)

print("---key---")
for key in color.keys():
    print(key)

