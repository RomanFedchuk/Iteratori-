def make_summator():
    total = 0
    def add_to_sum(value):
        nonlocal total
        total += value
        return total
    return add_to_sum


summator = make_summator()
print(summator(10))  # 10
print(summator(5))   # 15
print(summator(20))  # 35