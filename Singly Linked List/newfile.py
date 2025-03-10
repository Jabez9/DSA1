#!/usr/bin/python3
import os

file_path = input("Enter the file name: ")

if os.path.exists(file_path):
    choice = input("File exists. Do you want to overwrite it? (y/n): ").strip().lower()
    if choice != "y":
        print("Exiting...")
        exit()
    print("File exists")

with open(file_path, "w") as f:
    f.write("#!/usr/bin/python3\n")
    print(f"File {file_path} created successfully")
