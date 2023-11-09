line = int(input())
numbers = [int(x) for x in input().split()]
count = 0

for i in range(line):
   for j in range(i+1):
            if numbers[j] > numbers[i]:
                count += 1
print(count)
