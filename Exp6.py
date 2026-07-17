def matrix_chain_order(dims):
    """
    Matrix Chain Multiplication using Dynamic Programming

    dims: List of matrix dimensions.
    Matrix Ai has dimensions dims[i-1] x dims[i]

    Time Complexity: O(n^3)
    Space Complexity: O(n^2)
    """

    n = len(dims) - 1

    # Cost table
    m = [[0] * (n + 1) for _ in range(n + 1)]

    # Split table
    s = [[0] * (n + 1) for _ in range(n + 1)]

    # l = chain length
    for l in range(2, n + 1):
        for i in range(1, n - l + 2):
            j = i + l - 1
            m[i][j] = float('inf')

            for k in range(i, j):
                cost = (
                    m[i][k]
                    + m[k + 1][j]
                    + dims[i - 1] * dims[k] * dims[j]
                )

                if cost < m[i][j]:
                    m[i][j] = cost
                    s[i][j] = k

    return m, s


def print_optimal_parens(s, i, j):
    """Prints the optimal parenthesization."""

    if i == j:
        return f"A{i}"

    k = s[i][j]

    left = print_optimal_parens(s, i, k)
    right = print_optimal_parens(s, k + 1, j)

    return f"({left} x {right})"


def print_dp_table(m, n):
    """Displays the DP Cost Table."""

    print("\nDP Cost Table m[i][j]:")

    print("{:>6}".format(""), end="")
    for j in range(1, n + 1):
        print("{:>9}".format(f"A{j}"), end="")
    print()

    for i in range(1, n + 1):
        print("{:<6}".format(f"A{i}"), end="")

        for j in range(1, n + 1):
            if j < i:
                print("{:>9}".format("---"), end="")
            else:
                print("{:>9}".format(m[i][j]), end="")

        print()


# ---------------- Main Program ----------------

# Matrix Dimensions:
# A1 = 10 x 30
# A2 = 30 x 5
# A3 = 5 x 60
# A4 = 60 x 10

dims = [10, 30, 5, 60, 10]

n = len(dims) - 1

print("Matrix Dimensions:")
for i in range(n):
    print(f"A{i+1}: {dims[i]} x {dims[i+1]}")

m, s = matrix_chain_order(dims)

print("\nMinimum scalar multiplications:", m[1][n])

print("Optimal parenthesization:",
      print_optimal_parens(s, 1, n))

print_dp_table(m, n)