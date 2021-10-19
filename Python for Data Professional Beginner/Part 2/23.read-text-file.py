# Membaca file hello.txt dengan fungsi read()
print(">>> Membaca file hello.txt dengan fungsi read()")
file = open("hello.txt", "r")
content = file.read()
file.close()
print(content)

# Membaca file hello.txt dengan fungsi readline()
print(">>> Membaca file hello.txt dengan fungsi readline()")
file = open("hello.txt", "r")
first_line = file.readline()
second_line = file.readline()
file.close()
print(first_line)
print(second_line)

# Membaca file hello.txt dengan fungsi readlines()
print(">>> Membaca file hello.txt dengan fungsi readlines()")
file = open("hello.txt", "r")
all_lines = file.readlines()
file.close()
print(all_lines)

# Membaca file hello.txt dengan menerapkan looping
print(">>> Membaca file hello.txt dengan menerapkan looping")
file = open("hello.txt", "r")
for line in file:
    print(line)
