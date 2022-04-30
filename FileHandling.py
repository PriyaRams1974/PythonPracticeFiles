# File Handling
# # open(filename, mode)
# f = open("samplefile.txt", 'r')
# print(f.read(10))
# print(f.read())
#
# f.close()
# ==========
# open(filename, mode)
# try:
#     f = open("samplefile.txt", 'r')
#     print(f.readline())
#     print(f.readline())
# finally:
#     f.close()
# =================
# with open("samplefile.txt", 'r') as f:
#     # f = open("samplefile.txt", 'r')
#     print(f.readline())
#     print(f.readline())
#==========================
# with open("samplefile.txt", 'w') as f:
#     f.write("python is awesome")
#     f.write("Python is my favourite language")
#==========================
# with open("samplefile123.txt", 'w') as f:
#     f.write("python is awesome\n")
#     f.write("Python is my favourite language")

# #==========================
# with open("samplefile123.txt", 'a') as f:
#     f.write("\nAppend mode used python is awesome\n")
#     f.write("Append mode used Python is my favourite language")

# #==========================
# with open("newfile.txt", 'w') as f:
#     lines = ("JS is also awesome!!!", "\nJS is my second favourite language")
#     print(f.writelines(lines))

# #==========================
# with open("newfile.txt", 'r') as f:
#     print(f.readlines())
#==========================
import os
os.remove("samplefile.txt")