def tower_builder(n_floors):
    result = []
    width = (n_floors * 2) - 1
    for x in range(1, 2 * n_floors, 2):
        stars = x * '*'
        line = stars.center(width)
        result.append(line)
    return result
