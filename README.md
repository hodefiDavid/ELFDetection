# ELFDetection

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
