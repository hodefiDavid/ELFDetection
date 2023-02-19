import subprocess

# Define the list of source files and the output directory
source_files = ['f1.c'] #, '/f2.c', '/f3.c'
output_directory = 'output/'

# Create the output directory if it doesn't already exist
subprocess.run(['mkdir', '-p', output_directory])

# Compile each source file into an ELF file using gcc
for source_file in source_files:
    # Generate the output filename based on the input filename
    output_file = output_directory + source_file[:-2] + 'elf'
    
    # Run the gcc command to compile the source file into an ELF file
    subprocess.run(['gcc', '-g', '-Wall', '-o', output_file, source_file])