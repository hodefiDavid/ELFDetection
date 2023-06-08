# ELFDetection

[![License](https://img.shields.io/badge/license-MIT-blue.svg)](https://opensource.org/licenses/MIT)

## Description

The ELF Detection project is designed to identify and classify ELF
(Executable and Linkable Format) files within a given dataset.
The system utilizes machine learning techniques to accurately recognize
ELF files and differentiate them from other file formats. 
The project aims to provide a reliable tool for security analysts,
software developers, and system administrators to efficiently process and analyze ELF files.

We downloaded a dataset of ELF files containing malicious files from the VirusShare archive.
In order to add ELF files ourselves, we learned how to create them and added our own files to the dataset.
Here is a link to download the dataset: https://archive.org/download/virusshare_malware_collection_000

We started with several machine learning algorithms and tried to see how to extract information from them

to analyze the files in the best possible way. We executed the ELF files using elftools, which is the function for their execution.

We created JSON files for each of the ELF files so that we could read their data more conveniently.
We wrote a function that expresses each value list of features from the file and converts it.

We used "readelf" on Linux and created a TXT file describing each ELF file.

We scanned the various features, and from them, we ran our machine learning algorithm to identify the malicious components.

## The Features

We utilized the following features during the classification process:

count_distinct_strings_in_elf: This feature involved counting the number of distinct strings present in the ELF file, providing insights into the variety and complexity of the file's contents.

get_strtab_type: By extracting the string table type from the ELF file, we gained information about the purpose and usage of the strings stored in the file.

get_gotplt_size: The Global Offset Table/Procedure Linkage Table (GOT/PLT) size was determined, offering valuable details about the size and complexity of the file's dynamic linking structure.

get_section_header_size: This feature involved obtaining the size of the section header, which helps understand the organization and layout of different sections within the ELF file.

get_file_entropy: The file entropy was calculated, providing a measure of the file's randomness and complexity. This feature can indicate whether the file exhibits characteristics of obfuscation or encryption.

get_section_header_count: The count of section headers in the ELF file was extracted. This information assists in understanding the number and types of sections present in the file.

count_ips_in_elf: This feature involved counting the occurrences of IP addresses within the ELF file, which can provide insights into potential network-related activities or communication within the malware.

get_elf_size: The size of the ELF file was determined, which gives an indication of the overall file size and complexity.

count_urls_in_elf: This feature involved counting the number of URLs present within the ELF file, which can indicate potential network-related behavior or communication channels used by the malware.

These features were incorporated into the machine learning algorithms to enhance the classification and detection of malicious components within the ELF files.


## Contributing

David Hodefi- https://github.com/hodefiDavid
Haim Willinger- https://github.com/ChaimW25

## License

This project is licensed under the [MIT License](https://opensource.org/licenses/MIT). Refer to the [LICENSE](LICENSE) file for more information.




