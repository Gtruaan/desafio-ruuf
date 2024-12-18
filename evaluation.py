"""
Evaluation and metrics for the rectangle_fit function.
"""
from functions import rectangle_fit


testcases: list[tuple] = [
    (3, 2, 5, 8, 6),
    (1, 2, 2, 4, 4),  # Ruuf
    (1, 2, 3, 5, 7),  # Ruuf
    (2, 2, 1, 10, 0), # Ruuf
    (1, 6, 6, 8, 8),
]

print("Running tests...")
for (tile_x, tile_y, cont_x, cont_y, expected) in testcases:
    result: int = rectangle_fit(cont_x, cont_y, tile_x, tile_y)
    try:
        assert result == expected
        print("Test passed")
    except AssertionError:
        print(f"Test failed: {result} (result) != {expected} (expected)")

print("Calculating average coverage...")
cumulative_coverage: float = 0
valid_tests: int = 0

for cont_x in range(1, 50):
    for cont_y in range(1, 50):
        for tile_x in range(1, 50):
            for tile_y in range(1, 50):
                if tile_x * tile_y <= cont_x * cont_y and not (max(tile_x, tile_y) > max(cont_x, cont_y)):
                    total_area: int = cont_x * cont_y
                    number_of_tiles: int = rectangle_fit(cont_x, cont_y, tile_x, tile_y)
                    
                    if number_of_tiles > 0:     
                        covered_area: int = number_of_tiles * tile_x * tile_y
                        cumulative_coverage += (covered_area / total_area)
                        valid_tests += 1

print(f"Average coverage: {100 * cumulative_coverage / valid_tests:.2f}%")
