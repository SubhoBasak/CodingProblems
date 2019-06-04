# Solution part

def max_cur(arr, cur): # arr = 2D array represent the exchange table
    if cur in arr[0]:
        indx = arr[0].index(cur)
        op_cur = arr[0][indx] #store the output currencu in which given currency
                              #will be changed to get the max anount
        mx = arr[indx+1][indx]
        for i in range(1, len(arr)):
            if arr[i][indx] > mx:
                mx = arr[i][indx]
                op_cur = arr[0][i-1]
        return op_cur, mx
    else:
        print('this currenct is not available in this table !')
        return None, None


# Testing part

arr = [['inr', 'usd', 'prk'],
       [1, 69.21, 0.47],
       [0.014, 1, 0.0068],
       [2.11, 146.04, 1]]

currency, amount = max_cur(arr, 'SSD')

print('Currency : ', currency)
print('Amount : ', amount)
