# ✅ 1. Sum from 1 to 5
print(1+2+3+4+5)
# ✅ 2. Flowchart (Sum of Odd Numbers 1–100)

# Fill in:

# N ← 1
# S ← 0
# ✅ 3. Odd or Even Program
num = int(input("Enter a positive integer: "))

if num % 2 == 0:
    print("Even number")
else:
    print("Odd number")

# ✅ 4. Decorative Output
n = 5
print('*' * n)
print(('#' + ' ') * n)

# ✅ 5. Name and Address
name = "Md Asif"
address = "Kasna, India"

print(name)
print(address)

# ✅ 6. Arrange Two Integers (Small → Large)
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

if a < b:
    print(a, b)
else:
    print(b, a)

# ✅ 7. Prime & Composite (2–12)
for num in range(2, 13):
    for i in range(2, num):
        if num % i == 0:
            print(num, "Composite")
            break
    else:
        print(num, "Prime")


# ✅ 8. Armstrong Numbers (100–999)
for num in range(100, 1000):
    a = num // 100
    b = (num // 10) % 10
    c = num % 10
    
    if num == a**3 + b**3 + c**3:
        print(num)

# ✅ 9. Add Item to Dictionary
person = {"Mother": "Jane Doe"}
person["Father"] = "John Doe"

print(person)


# ✅ 10. Move Largest Value to Last (No temp variable)
lst = [4, 2, 9, 1, 5]

for i in range(len(lst)-1):
    if lst[i] > lst[i+1]:
        lst[i], lst[i+1] = lst[i+1], lst[i]

print(lst)

# ✅ 11. 2D List → 1D List
a = [[1,2],[3,4],[5,6]]
new_list = []

for row in a:
    for item in row:
        new_list.append(item)

print(new_list)

# ✅ 12. Average Score from Dictionary
maria = {'korean':94, 'english':88, 'math':95, 'science':80}

avg = sum(maria.values()) / len(maria)
print(avg)



# ✅ 13. Deep Copy Dictionary
import copy

school = {'class1':{'student1':'A'}}
school2 = copy.deepcopy(school)

print(school is school2)   # False

# ✅ 14. Extract Math Scores & Find Average (Using zip)
scores = (
    ('Hyun',88,95,90),
    ('Min',90,85,88),
    ('Jin',75,80,85),
    ('Lee',92,90,91)
)

names, eng, math, sci = zip(*scores)

avg_math = sum(math) / len(math)
print(avg_math)