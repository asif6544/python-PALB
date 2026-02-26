# ✅ 1. Sum from 1 to 5
print(1+2+3+4+5)
# ✅ 2. Flowchart (Sum of Odd Numbers 1–100)
N = 1
S = 0

while N < 100:
    N = N + 2
    S = S + N

print(S)
# ✅ 3. Odd or Even
num = int(input("Enter a positive integer: "))

if num % 2 == 0:
    print("Even")
else:
    print("Odd")
# ✅ 4. Decorative Output
n = 5
print('*' * n)
print(('#' + ' ') * n)
# ✅ 5. Name and Address
name = "Md Asif"
address = "Kasna, India"

print(name)
print(address)
# ✅ 6. Expected Output Program
a = 10
b = 5
print(a + b)
print(a - b)
print(a * b)
print(a / b)
# ✅ 7. Arrange Two Numbers (Small → Large)
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

if a < b:
    print(a, b)
else:
    print(b, a)
# ✅ 8. Compound Conditional Expression
ans = int(input("Enter 0 or 1: "))

if ans == 0:
    print("You entered Zero")
elif ans == 1:
    print("You entered One")
else:
    print("Invalid input")
# ✅ 9. Prime and Composite (2–12)
for num in range(2, 13):
    for i in range(2, num):
        if num % i == 0:
            print(num, "Composite")
            break
    else:
        print(num, "Prime")
# ✅ 10. Armstrong Numbers (100–999)
for num in range(100, 1000):
    a = num // 100
    b = (num // 10) % 10
    c = num % 10
    
    if num == a**3 + b**3 + c**3:
        print(num)
# ✅ 11. Combine Two Lists (Nested Loop)
l1 = ["A", "B", "C"]
l2 = ["1", "2", "3"]

for i in l1:
    for j in l2:
        print(i + j)
# ✅ 12. Add Item to Dictionary
person = {"Mother": "Jane Doe"}
person["Father"] = "John Doe"

print(person)
# ✅ 13. Move Largest Value to Last (Without temp)
lst = [4, 2, 9, 1, 5]

for i in range(len(lst)-1):
    if lst[i] > lst[i+1]:
        lst[i], lst[i+1] = lst[i+1], lst[i]

print(lst)
# ✅ 14. 2D List → 1D List
a = [[1,2],[3,4],[5,6]]
new_list = []

for row in a:
    for item in row:
        new_list.append(item)

print(new_list)
# ✅ 15. Average Score from Dictionary
maria = {'korean':94, 'english':88, 'math':95, 'science':80}

avg = sum(maria.values()) / len(maria)
print(avg)
# ✅ 16. Deep Copy Dictionary
import copy

school = {'class1':{'student1':'A'}}
school2 = copy.deepcopy(school)

print(school is school2)   # Should print False
