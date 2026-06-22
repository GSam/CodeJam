def solve_euler_88(k_limit=12000):
    # The absolute maximum possible minimal product-sum number for k_limit is 2 * k_limit
    max_p = 2 * k_limit

    # min_N[k] will store the minimal product-sum number for a set of size k.
    # Initialize each with its theoretical maximum upper bound.
    min_N = {k: 2 * k for k in range(2, k_limit + 1)}

    # DFS to generate all factorizations with factors >= 2
    # prod: current product
    # sum_val: current sum of the chosen factors
    # count: number of factors chosen so far (m)
    # start: the minimum next factor to choose (ensures non-decreasing order)
    def dfs(prod, sum_val, count, start):
        if count >= 2:
            k = prod - sum_val + count
            if k <= k_limit:
                if prod < min_N[k]:
                    min_N[k] = prod

        for i in range(start, max_p):
            if prod * i > max_p:
                break
            dfs(prod * i, sum_val + i, count+1, i)

    # Start the recursive search
    dfs(1, 0, 0, 2)

    # Sum the UNIQUE minimal product-sum numbers
    unique_minimal_numbers = set(min_N.values())
    return sum(unique_minimal_numbers)

if __name__ == "__main__":
    # Verify with the problem description example (for k <= 6, sum of unique minimal N is 30)
    assert solve_euler_88(6) == 30
    print("Example test passed.")

    # Solve for k <= 12000
    result = solve_euler_88(12000)
    print(f"The sum of all minimal product-sum numbers for 2 <= k <= 12000 is: {result}")
