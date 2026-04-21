def edit_distance(a, b):
    dp = []

    # create table with 0
    for i in range(len(a)+1):
        row = []
        for j in range(len(b)+1):
            row.append(0)
        dp.append(row)

    # fill first row and column
    for i in range(len(a)+1):
        dp[i][0] = i
    for j in range(len(b)+1):
        dp[0][j] = j

    # main logic
    for i in range(1, len(a)+1):
        for j in range(1, len(b)+1):

            if a[i-1] == b[j-1]:
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = 1 + min(
                    dp[i-1][j],     # delete
                    dp[i][j-1],     # insert
                    dp[i-1][j-1]    # replace
                )

    return dp[len(a)][len(b)]


# input from user
a = input("Enter first string: ")
b = input("Enter second string: ")

#output
result = edit_distance(a, b)
print("Minimum operations required:", result)
