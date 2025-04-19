import numpy as np

def matrix_operations():
    print("Matrix Calculator using NumPy")
    print("\nEnter the dimensions and elements of the matrices.")

    # Input for the first matrix
    rows1 = int(input("Enter the number of rows for Matrix 1: "))
    cols1 = int(input("Enter the number of columns for Matrix 1: "))
    print(f"Enter the elements for Matrix 1 ({rows1}x{cols1}):")
    matrix1 = np.array([list(map(float, input().split())) for _ in range(rows1)])

    # Input for the second matrix
    rows2 = int(input("Enter the number of rows for Matrix 2: "))
    cols2 = int(input("Enter the number of columns for Matrix 2: "))
    print(f"Enter the elements for Matrix 2 ({rows2}x{cols2}):")
    matrix2 = np.array([list(map(float, input().split())) for _ in range(rows2)])

    print("\nSelect an operation to perform:")
    print("1. Add Matrices")
    print("2. Subtract Matrices")
    print("3. Multiply Matrices")
    print("4. Transpose a Matrix")
    choice = int(input("Enter your choice (1-4): "))

    if choice == 1:
        if matrix1.shape == matrix2.shape:
            result = np.add(matrix1, matrix2)
            print("Addition Result:\n", result)
        else:
            print("Error: Matrices must have the same dimensions for addition.")
    elif choice == 2:
        if matrix1.shape == matrix2.shape:
            result = np.subtract(matrix1, matrix2)
            print("Subtraction Result:\n", result)
        else:
            print("Error: Matrices must have the same dimensions for subtraction.")
    elif choice == 3:
        if cols1 == rows2:
            result = np.dot(matrix1, matrix2)
            print("Multiplication Result:\n", result)
        else:
            print("Error: Number of columns in Matrix 1 must equal the number of rows in Matrix 2 for multiplication.")
    elif choice == 4:
        print("Transpose of Matrix 1:\n", np.transpose(matrix1))
        print("Transpose of Matrix 2:\n", np.transpose(matrix2))
    else:
        print("Invalid choice.")

# Run the function
matrix_operations()
