def generate_pascal_triangle_row(n):
    row = [1]  
    
    for i in range(1, n + 1):
        next_row = [1]  
        
        for j in range(1, i):
            next_row.append(row[j - 1] + row[j])  
            
        next_row.append(1)  
        row = next_row
    
    return row
n = int(input("Введіть номер рядка трикутника Паскаля: "))

pascal_row = generate_pascal_triangle_row(n)
print(f"Рядок {n} трикутника Паскаля: {pascal_row}")
