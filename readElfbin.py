import struct



# Open the ELF file in binary mode

with open('/home/david/elf/VirusShare_ELF_20140617/VirusShare_5bf5255431526b0684737d663b7af46d', 'rb') as f:

    # Read the ELF header

    elf_header = f.read(52)
     # Read the section header table offset from the ELF header
    section_header_offset = struct.unpack('I', elf_header[32:36])[0]
    # Read the section header size from the ELF header
    section_header_size = struct.unpack('H', elf_header[46:48])[0]
    # Seek to the section header table
    f.seek(section_header_offset)
    # Read each section header from the file
    section_headers = []
    for i in range(0, 10):
        section_header_data = f.read(section_header_size)
        section_header = struct.unpack('IIQQQQIIQQ', section_header_data)
        section_headers.append(section_header)

        # Do something with the section headers
    print(section_headers)

