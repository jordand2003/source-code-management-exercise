def gcd(a: int, b: int) -> int:
	if a < 0 or b < 0:
		print("No negative number allowed!")
		return
	if b == 0:
		return a
	else:
		return gcd(b,a%b);

print(gcd(-48, 18))
print(gcd(54, 24))
print(gcd(48, 18))
print(gcd(101, 10))
print(gcd(0, 0))