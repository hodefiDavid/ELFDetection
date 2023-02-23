import subprocess
import os
import fnmatch

# # Set the root directory path where you want to search for C files
root_dir = "/home/david/ELFDetection/ELFDetection/c_files"

# # Use os.walk() to traverse the directory tree recursively and get all C files
c_files = []
for root, dirs, files in os.walk(root_dir):
    for file in files:
        if fnmatch.fnmatch(file, "*.c"):
            c_files.append(os.path.join(root, file))

# # Print the list of C file names
# print(c_files)

source_files = c_files
# source_files = ['/home/david/ELFDetection/ELFDetection/c_files/f1.c']
# Define the list of source files and the output directory
# with open('/home/david/ELFDetection/ELFDetection/c_files/output.txt', 'r') as f:
#     for line in f:
#         # Do something with each line
#         s = line.strip('\n')
#         source_files.append(s)
# source_files = [] #, '/f2.c', '/f3.c'


output_directory = '/home/david/ELFDetection/ELFDetection/output/'

# Create the output directory if it doesn't already exist
subprocess.run(['mkdir', '-p', output_directory])
i = 0 
# Compile each source file into an ELF file using gcc
for source_file in source_files:
    # Generate the output filename based on the input filename
    s = source_file.split('/')[-1]
    output_file =  output_directory + s[:-2] + 'elf'
    try:
    # Run the gcc command to compile the source file into an ELF file
        subprocess.run(['gcc', '-g', '-Wall', '-o', output_file, source_file])
    except:
        i+=1

print(i) 