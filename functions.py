def rectangle_fit_oriented(cont_x: float, cont_y: float,
                           tile_x: int, tile_y: int) -> int:
     total_vertical: int = cont_x // tile_x
     total_horizontal: int = cont_y // tile_y
    
     remaining_vertical: float = cont_x % tile_x
     remaining_horizontal: float = cont_y % tile_y
    
     extra_vertical: int = (remaining_horizontal // tile_x) * (cont_x // tile_y)
     extra_horizontal: int = (remaining_vertical // tile_y) * (cont_y // tile_x)
    
     return int(total_vertical * total_horizontal + max(extra_vertical, extra_horizontal))

def rectangle_fit(cont_x: float, cont_y: float, 
                  tile_x: int, tile_y: int) -> int:
     return max(rectangle_fit_oriented(cont_x, cont_y, tile_x, tile_y),
                rectangle_fit_oriented(cont_x, cont_y, tile_y, tile_x))

# === Other Functions ===

def isosceles_fit_oriented(cont_x: float, cont_y: float, 
                           tile_x: int, tile_y: int) -> int:
     total_fit: int = 0

     subcont_y: float = tile_y
     subcont_x: float = cont_x

     while True:
          subcont_x -= tile_y * cont_x / cont_y
          if subcont_x < tile_x:
               break
          
          total_fit += rectangle_fit(subcont_x, subcont_y, tile_x, tile_y)
     
     return int(total_fit)

def isosceles_fit(cont_x: float, cont_y: float,
                  tile_x: int, tile_y: int) -> int:
       return max(isosceles_fit_oriented(cont_x, cont_y, tile_x, tile_y),
                     isosceles_fit_oriented(cont_x, cont_y, tile_y, tile_x))

def intersection_fit(cont_x: float, cont_y: float,
                     tile_x: int, tile_y: int) -> int:
     
     total_fit_vertical: int = 0
     total_fit_horizontal: int = 0

     total_fit_vertical += 2 * rectangle_fit(cont_x / 2, cont_y, tile_x, tile_y)
     total_fit_vertical += rectangle_fit(cont_x / 2, 3 * cont_y / 2, tile_x, tile_y)

     total_fit_horizontal += 2 * rectangle_fit(cont_x, cont_y / 2, tile_x, tile_y)
     total_fit_horizontal += rectangle_fit(3 * cont_x / 2, cont_y / 2, tile_x, tile_y)
     
     return max(total_fit_vertical, total_fit_horizontal)

# Example calls
print("[1]", isosceles_fit(100, 100, 1, 1))
print("[2]", isosceles_fit(100, 100, 2, 2))
print("[3]", isosceles_fit(100, 100, 99, 1))
print("[4]", intersection_fit(100, 100, 1, 1))
print("[5]", intersection_fit(2, 4, 6, 1))
print("[6]", intersection_fit(2, 4, 3, 1))