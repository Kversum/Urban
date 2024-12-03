def calculate_structure_sum(data):
    var = 0
    if isinstance(data, int) or isinstance(data, float):
        return data
    elif isinstance(data, dict):
        for k in data.items():
            var += calculate_structure_sum(k)
        return var
    elif isinstance(data, tuple):
        for i in data:
            var += calculate_structure_sum(i)
        return var
    elif isinstance(data, str):
        return len(data)
    elif isinstance(data, list):
        for i in data:
            var += calculate_structure_sum(i)
        return var
    elif isinstance(data, set):
        for i in data:
            var += calculate_structure_sum(i)
        return var
    else:
        return 0


data_structure = [
  [1, 2, 3],
  {'a': 4, 'b': 5},
  (6, {'cube': 7, 'drum': 8}),
  "Hello",
  ((), [{(2, 'Urban', ('Urban2', 35))}])
]


result = calculate_structure_sum(data_structure)

print(result)