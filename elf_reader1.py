#!/usr/bin/env python3
import sys
from elftools.elf.elffile import ELFFile
elf_name = "/home/david/elf/training-sample"     
print(f"Mapping between segments and sections in the file {elf_name}")
elffile = ELFFile(open(elf_name, 'rb'))
segments = list()
for segment_idx in range(elffile.num_segments()):
    segments.insert(segment_idx, dict())
    segments[segment_idx]['segment'] = elffile.get_segment(segment_idx)
    segments[segment_idx]['sections'] = list()
for section_idx in range(elffile.num_sections()):
    section = elffile.get_section(section_idx)
    for segment in segments:
        if segment['segment'].section_in_segment(section):
            segment['sections'].append(section)
for segment in segments:
    seg_head = segment['segment'].header
    print("Segment:")
    print(f"Type: {seg_head.p_type}\nOffset: {hex(seg_head.p_offset)}\nVirtual address: {hex(seg_head.p_vaddr)}\nPhysical address: {(seg_head.p_paddr)}\nSize in file: {hex(seg_head.p_filesz)}\nSize in memory: {hex(seg_head.p_memsz)}\n")
    if segment['sections']:
        print("Segment's sections:")
        print([(section.name, hex(section['sh_addr'])) for section in segment['sections']], sep=', ', end='\n')
    else:
        print('Segment contains no sections')
    print('\n--------------------------------------------------------------------------------')