working_dir = "//Home//madams//code//cs121//"
first_file = raw_input("Name of file to be read: ")
second_file = raw_input("Name of file to be copied to: ")
file1 = open(working_dir+first_file, "r")
file2 = open(working_dir+second_file, "w")
file2.writelines(first_file)
file2.close()
file1.close()
