import math

def angle_with_x_axis(x1, y1, x2, y2):
    
    vector_OA = [x1, y1]
    vector_OB = [x2, y2]
    # Обчислення кутів між відрізками OA і OB та віссю ОХ
    angle_OA = math.degrees(math.atan2(vector_OA[1], vector_OA[0]))
    angle_OB = math.degrees(math.atan2(vector_OB[1], vector_OB[0]))
    # Перетворення кутів у відсотки від 0 до 100
    angle_OA_percent = (angle_OA + 360) % 360 * 100 / 360
    angle_OB_percent = (angle_OB + 360) % 360 * 100 / 360
    return angle_OA_percent, angle_OB_percent
def main():  
    x1, y1 = map(float, input("Введіть координати точки A (x1, y1): ").split())
    x2, y2 = map(float, input("Введіть координати точки B (x2, y2): ").split())
    
    angle_OA_percent, angle_OB_percent = angle_with_x_axis(x1, y1, x2, y2)
    print(f"Кут між відрізком OA та віссю ОХ: {angle_OA_percent:.2f}%")
    print(f"Кут між відрізком OB та віссю ОХ: {angle_OB_percent:.2f}%")
    
    if angle_OA_percent > angle_OB_percent:
        print(f"Кут між відрізком OA являється більшим та віссю ОХ: {angle_OA_percent:.2f}%")
    elif angle_OA_percent < angle_OB_percent:
        print(f"Кут між відрізком OB являється більшим та віссю ОХ: {angle_OB_percent:.2f}%")
    else:
        print("Відрізки OA та OB утворюють однаковий кут з віссю ОХ.")
if __name__ == "__main__":
    main()