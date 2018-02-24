def stock_buy_sell(arr):
    min_ele = arr[0]
    max_diff = 0

    for i in range(1,len(arr)):
        if arr[i] < min_ele:
            min_ele = arr[i]

        if arr[i] - min_ele > max_diff:
            max_diff = arr[i] - min_ele

    return max_diff

def main():
    arr = [7,2,5,10,1,8]
    print (stock_buy_sell(arr))

if __name__ == "__main__":
    main()
