def unique_elements(lst) :
    seen = set()
    return [x for x in lst if not (x in seen or seen.add(x))]

numbers = [1, 5, 6, 5, 8, 6, 10, 8, 9]
print(unique_elements(numbers))