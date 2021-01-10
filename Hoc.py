# Initialization an integer variable name num_integer
num_integer = 1000
# Initialization a float variable name num_float
num_float = 3.125
# Initialization a string variable name string_var
string_var = 'Codelearn.io'
# Initialization a boolean variable name boolean_var
boolean_var = True

#Print value of each variable
print(num_integer)
print(num_float)
print(string_var)
print(boolean_var)
# Khai báo biến a và gán giá trị cho a = 5
a = 5
# Khai báo biến b và gán giá trị cho b = 7
b = 7
print("a + b =",a + b)
#hàm type()
name = "Codelearn"
date_of_birth = 2
pi = 3.14

print(type(name))
print(type(date_of_birth))
print(type(pi))
#Bạn chỉ có thể nối 2 chuỗi với nhau chứ không thể nối một chuỗi với 1 số.
# toán tử

#Toán tử cộng 2 giá trị.
7 + 3 = 10
#Toán tử trừ 2 giá trị.
7 - 3 = 4
#Toán tử nhân 2 giá trị.
	7 * 3 = 21
#Toán tử chia 2 giá trị.
7 / 3 = 2.(3)
#Toán tử chia lấy phần nguyên của 2 giá trị.
7 // 3 = 2

10 // 6 = 1
#Toán tử chia lấy phần dư của 2 giá trị.
7 % 3 = 1

10 % 6 = 4

#Toán tử mũ (a**b = ab)	
2 ** 3 = 8

5 ** 7 = 78125
#kiểm tra ký tự có trong chuỗi
print("Code" in "Codelearn")
print("Py" not in "Python")
#kiểm tra chỉ số có cùng đối tượng
a = 5
b = 7
print(a is b)
print(a is not b)

# toán tử quan hệ
a and b
a or b
not a
# lựa chọn
n = int(input())
if n % 2 == 0:
    # Nếu n là số chẵn thì hiển thị ra màn hình n is an even number
    print("n is an even number")
else:
    # Ngược lại, nếu n không là số chẵn thì hiển thị ra màn hình n is an odd number
    print("n is an odd number")
#toán tử 3 ngoi
# Python program to demonstrate nested ternary operator 
a, b = 10, 20

print ("Both a and b are equal" if a == b else "a is greater than b"
		if a > b else "b is greater than a") 
# vòng lặp while
i = 1
while i <= 5:
    print(i)
    i += 1
#vòng lặp for
for i in range(1, 5):
    print(i)

# Tạo ra list để lưu trữ các số nguyên
list1 = [1, 2, 3]
# Tạo ra list để lưu trữ các xâu ký tự
list2 = ["Viet", "Tuan", "Duong"]
# Bạn cũng có thể tạo ra một list lưu trữ các kiểu dữ liệu khác nhau
list3 = [7, 3.5, "Codelearn"]
# truy xuất phần tử
names = ["Viet", "Dung", "Huong"]
print(names[0])
print(names[1])
print(names[2])
#Bạn cũng có thể dùng vòng lặp for để duyệt qua các phần tử của list.
names = ["Viet", "Dung", "Huong"]
for name in names:
    print(name)

#Để thêm một phần tử vào cuối của list bạn dùng hàm append():
lst = []
lst.append(4)
lst.append(3)
lst.append(6)
print(lst)
#nhập list có n phần tử
n = int(input())
lst = []
for i in range(n):
    lst.append(int(input()))
# tính tổng list
answer = 0
for v in lst:
    answer += v

print(answer)
#Đây là hàm trả về số phần tử có trong list
lst = [2, 3, 1]
print(len(lst))

lst = [2, 3, 1]
for i in range(len(lst)):
    print(lst[i])
# hàm max min
lst = [2, 3, 1]
print(max(lst))
print(min(lst))

#Hàm insert :Đây là hàm dùng để thêm một phần tử vào một ví trí trong list
vowels = ['a', 'e', 'i', 'u']
# Chèn xâu 'o' vào vị trí thứ 4 trong list vowels
vowels.insert(3, 'o')
print(vowels)

=>['a', 'e', 'i', 'o', 'u']

#Hàm remove :Hàm này dùng để xóa một phần tử khỏi list:
lst = ['A', 'B', 'C']
lst.remove('A')
print(lst)

=>['B', 'C']

#Hàm pop() được dùng để xóa một phần tử với chỉ số cho trước trong list:

lst = ['A', 'B', 'C']
# Xóa phần tử thứ 2 khỏi list
lst.pop(1)
print(lst)

=>['A', 'C']

#Hàm sort :Hàm này được dùng để sắp xếp các phần tử trong list theo một thứ tự nhất định. Ví dụ:

lst = [4, 5, 3, 7, 6, 1]
# Sắp xếp các phần tử trong list theo thứ tự tăng dần
lst.sort()
print(lst)

=>[1, 3, 4, 5, 6, 7]
# Sắp xếp các phần tử trong list theo thứ tự giảm dần
lst.sort(reverse=True)
print(lst)

=>[7, 6, 5, 4, 3, 1]

#Hàm reverse :Đây là hàm dùng để đảo ngược list:

lst = [4, 5, 3, 7, 6, 1]
lst.reverse()
print(lst)

=>[1, 6, 7, 3, 5, 4]
#Hàm count :Đây là hàm dùng để đếm số lần xuất hiện của một thành phần trong list:

lst = [6, 2, 3, 8, 2]
print(lst.count(2))

=>2
#Hàm clear :Đây là hàm dùng để xóa hết các phần tử bên trong list:

lst = [1, 2, 3]
lst.clear()
print(lst)

=>[]
#Phương thức lower() :Đây là phương thức được dùng để chuyển 1 chuỗi về dạng in thường:

s = "CODELEARN123"
print(s.lower())

=>codelearn123

#Phương thức upper() :Đây là phương thức được dùng để chuyển 1 chuỗi về dạng in hoa:

s = "codelearn123"
print(s.upper())

=>CODELEARN123
#Phương thức isalnum() :
#Đây là phương thức được dùng để kiểm tra xem một xâu có chỉ chứa các ký tự chữ và số hay không.

s = "codelearn2020"
print(s.isalnum())

=>True
s = "codelearn2020.io"
# Kết quả sẽ là False do chuỗi s chứa ký tự .
print(s.isalnum())

=>False

#Phương thức isalpha()
#Phương thức này được dùng để kiểm tra xem một chuỗi có chứa toàn các ký tự chữ không:

s = "codelearn"
print(s.isalpha())
=>True
# Kết quả sẽ là False do chuỗi s chứa số 2020
s = "codelearn2020"
print(s.isalpha())
=>False

#Phương thức isnumeric()
#Phương thức này dùng để kiểm tra xem một xâu có chứa toàn các ký tự số hay không:

s = "2020"
print(s.isnumeric())
=>True
s = "c2020"
print(s.isnumeric())
=>False

#Phương thức split() Phương thức này được dùng để cắt một chuỗi ra
# thành list các chuỗi khác dựa trên một phần tử trong chuỗi đầu vào:

s = "Welcome to Codelearn.io!"
print(s.split(" "))
=>['Welcome', 'to', 'Codelearn.io!']
s = "A1B1C1D1E1"
print(s.split("1"))
=>['A', 'B', 'C', 'D', 'E', '']

#Phương thức join()
#Phương thức này được dùng để nối một tập hợp thành một chuỗi sử dụng kí tự cho trước. Ví dụ:

lst = ["Welcome", "to", "Codelearn.io!"]
print(" ".join(lst))
=>Welcome to Codelearn.io!
lst = ["A", "B", "C"]
print("-".join(lst))
=>A-B-C
#Bạn có thể sử dụng hàm split() và hàm join() để loại bỏ các khoảng trắng thừa trong chuỗi. Ví dụ:

message = "   Welcome   to Codelearn.io!   "
print(" ".join(message.split()))

=>Welcome to Codelearn.io!

#Phương thức replace()
#Phương thức này được dùng để thay thế các chuỗi con tìm thấy thành chuỗi con mới. Ví dụ:

name = "Cod3l3arn"
print(name.replace("3", "e"))
=>Codelearn
# lấy 1 kí tự trong chuỗi
name = "Codelearn"
print(name[0])

=>C

s = 'Python String'
# s[0] là phần tử đầu tiên trong chuỗi
print(s[0])
=>P
# s[-1] là phần tử đầu cuối cùng trong chuỗi
print(s[-1])
=>g
# s[-2] là phần tử đứng trước phần tử cuối cùng trong chuỗi
print(s[-2])
=>n
#Cắt chuỗi trong Python (Slice a string in Python)
s = 'Python String'
print(s[0:2])
=>Py
print(s[3:5])
=>ho
print(s[7:])
=>String
print(s[:6])
=>Python
print(s[7:-4])
=>St






