#using error handling..

try:
    print ("Reading file content:")
    with open("sample.txt","rt") as file_read:
        i = 1
        line = file_read.readline()
        while line!="":
            print(f"Line {i}: {line.rstrip()}")
            i +=1
            line = file_read.readline()
except FileNotFoundError:
    print("Error: The file 'sample.txt' was not found")





#without using error handling

# import os
# if os.path.exists("sample.txt"):
#     print ("Reading file content:")
#     with open("sample.txt","rt") as file_read:
#         i = 1
#         line = file_read.readline()
#         while line!="":
#             print(f"Line {i}: {line.rstrip()}")
#             i +=1
#             line = file_read.readline()
# else:
#     print("Error: The file 'sample.txt' was not found")