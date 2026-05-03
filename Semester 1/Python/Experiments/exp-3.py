def compare_tuples(tuples_list):
    results = []

    for a, b in tuples_list:
        comparison_results = {
        'Equal': a == b,
        f'{a} is Greater': a > b,
        f'{a} is Lesser': a < b}

    results.append(comparison_results)

    return results


input_tuples = [(5, 4), (8, 8), (11, 10)]
print(compare_tuples(input_tuples))