import numpy as np
import sys

#coin change given denomination and goal
def coinChange(arr, index, goal):
    memo = np.zeros((goal + 1, len(arr) + 1))
    return coin(arr,len(arr)-1,goal, memo)

def coin(arr, index, goal,memo):
    if goal < 0 or index < 0:
        return 0
    elif goal == 0:
        return 1
    else:
        if memo[goal][index] > 0:
            return memo[goal][index]
        else:
            memo[goal][index] = coin(arr, index, goal-arr[index],memo) + coin(arr, index-1, goal,memo)
            return memo[goal][index]

#using DP find the ways
def ways(arr, goal):
    memo = [0]*(goal+1)
    memo[0] = 1
    for i in range(goal+1):
        for j in arr:
            if i-j >=0:
                memo[i] += memo[i-j]
    return memo[goal]

#using DP find the ways to get change
def denom(arr, goal):
    memo = [0] * (goal + 1)
    memo[0] = 1
    for j in arr:
        for i in range(goal + 1):
            if i - j >= 0:
                memo[i] += memo[i - j]
    return memo[goal]

#minimum no. of coins
def minCoin(arr, goal):
    memo = [sys.maxsize]*(goal+1)
    memo[0] = 0
    for i in range(1,goal+1):
        for j in arr:
            if i >= j:
                if memo[i-j] != sys.maxsize:
                    memo[i] = min(memo[i], memo[i-j]+1)
    return memo[goal]

def main():
    arr = [7,3,2]
    goal = 60
    print (minCoin(arr, goal))
    # print (int(coinChange(arr,len(arr)-1,goal)))
    # print (ways(arr, goal))
    # print(denom(arr, goal))

if __name__ == "__main__":
    main()