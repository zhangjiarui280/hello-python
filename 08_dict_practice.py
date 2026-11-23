# 字典计数的手动实验：看字典怎么一步步变化
counts = {}
print(counts)

counts["INFO"] = 1
print(counts)

counts["ERROR"] = 1
print(counts)

counts["INFO"] = counts["INFO"] + 1
print(counts)
