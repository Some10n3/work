# A recursive solution for Rod cutting problem

# Returns the best obtainable price for a rod of length n
# and price[] as prices of different pieces 
def cutRod(price, index, n):
	
	# base case
	if index == 0:
		return n*price[0]
	
	# At any index we have 2 options either
	# cut the rod of this length or not cut 
	# it
	notCut = cutRod(price,index - 1,n)
	cut = float("-inf")
	rod_length = index + 1

	if (rod_length <= n):
		
		cut = price[index]+cutRod(price,index,n - rod_length)

	return max(notCut, cut)

# Driver program to test above functions 
arr = [0, 25, 50, 75, 100]
size = len(arr)
print("Maximum Obtainable Value is ",cutRod(arr, size - 1, size))

# This code is contributed by Vivek Maddeshiya
