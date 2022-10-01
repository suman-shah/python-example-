# Python3 code to check if a given
# number is perfect or not

# Returns true if n is perfect
def isPerfect( n ):
	
	# To store sum of divisors
	sum = 1
	
	# Find all divisors and add them
	i = 2
	while i * i <= n:
		if n % i == 0:
			sum = sum + i + n/i
		i += 1
	
	# If sum of divisors is equal to
	# n, then n is a perfect number
	
	return (True if sum == n and n!=1 else False)

# Driver program
print("Below are all perfect numbers till 10000")
n = 2
for n in range (10000):
	if isPerfect (n):
		print(n , " is a perfect number")
		
# This code is contributed by "Sharad_Bhardwaj".
