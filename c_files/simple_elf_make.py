import subprocess
import os
import fnmatch
output_directory = '/home/david/ELFDetection/ELFDetection/output/'

# Create the output directory if it doesn't already exist
subprocess.run(['mkdir', '-p', output_directory])
i = 0 
source_file = '/home/david/ELFDetection/ELFDetection/c_files/f1.c'
s = source_file.split('/')[-1]
# Generate the output filename based on the input filename
output_file =  output_directory+s[:-2] + 'elf'
try:
# Run the gcc command to compile the source file into an ELF file
    subprocess.run(['gcc', '-g', '-Wall', '-o', output_file, source_file])
except:
    i+=1

print(i) 