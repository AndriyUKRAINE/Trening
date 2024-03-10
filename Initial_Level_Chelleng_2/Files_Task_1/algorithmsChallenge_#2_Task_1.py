import numpy as np

def merge_arrays(*arrays):
    merged_array = np.concatenate(arrays)  
    merged_array = np.unique(merged_array)  
    merged_array = merged_array[merged_array % 5 != 0] 
    merged_array = np.sort(merged_array)  
    return merged_array

def main():
    num_arrays = int(input("Введіть кількість масивів: "))
    arrays = []
    for i in range(num_arrays):
        array = np.random.randint(0, 101, np.random.randint(1, 11))  
        arrays.append(array)
        print(f"Масив {i + 1}: {array}")    
    merged_array = merge_arrays(*arrays)
    print("\nОбєднаний масив (по зростанню, унікальні, без кратних 5):", merged_array)
if __name__ == "__main__":
    main()