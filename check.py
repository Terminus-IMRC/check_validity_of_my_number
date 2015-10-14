#!/usr/bin/env python3

import sys

# c.f. 総務省令第八十五号
# (http://www.soumu.go.jp/main_content/000327387.pdf)

def check_validity_of_my_number(num):
	num = int(num)

	if not (num < 1e12):
		return False

	nums = [0 for i in range(12)]
	for i in range(0, 12):
		nums[i] = num % 10
		num = int(num / 10)

	sum = 0
	for n in range(1, 11 + 1):
		Pn = nums[n]

		if n <= 6:
			Qn = n + 1
		else:
			Qn = n - 5

		sum += Pn * Qn
	
	sum %= 11

	if sum <= 1:
		cd = 0
	else:
		cd = 11 - sum
	
	return cd == nums[0]

def main():
	if len(sys.argv) != 2:
		print('invalid argument', file = sys.stderr)
		exit(1)

	s = sys.argv[1]
	num = int(s)
	print(check_validity_of_my_number(num))

if __name__ == '__main__':
	main()
