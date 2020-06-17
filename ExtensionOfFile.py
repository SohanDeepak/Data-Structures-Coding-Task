filename = input("Input the Filename: ")
split_name = filename.split('.')
if split_name[1] == "py":
    print("The extension of the file is: 'Python'")
elif split_name[1] == "c":
    print("The extension of the file is: 'C'")
elif split_name[1] == "cpp":
    print("The extension of the file is: 'C++'")
