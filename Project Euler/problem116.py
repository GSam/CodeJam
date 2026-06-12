def count_combinations(n, k):
    # dp[i] stores the number of ways to tile a row of length i
    dp = [0] * (n + 1)
    
    # Base cases: for lengths less than k, only 1 way exists (all black)
    for i in range(k):
        dp[i] = 1
        
    # Fill the DP table using the recurrence relation
    for i in range(k, n + 1):
        dp[i] = dp[i-1] + dp[i-k]
        
    # Subtract 1 to exclude the configuration with zero colored tiles
    return dp[n] - 1

def solve_euler_116(n=50):
    red_ways = count_combinations(n, 2)
    green_ways = count_combinations(n, 3)
    blue_ways = count_combinations(n, 4)
    
    return red_ways + green_ways + blue_ways

if __name__ == "__main__":
    # Test with n=5 to verify with the example
    assert solve_euler_116(5) == 12
    print("Example test passed.")
    
    # Solve for n=50
    result = solve_euler_116(50)
    print(f"Total replacement ways for length 50: {result}")
