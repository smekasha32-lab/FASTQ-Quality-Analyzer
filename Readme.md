# FASTQ Quality Analyzer

## Overview

The FASTQ Quality Analyzer is a Python-based bioinformatics tool that processes sequencing reads stored in FASTQ format. It calculates read statistics, converts ASCII quality characters into Phred quality scores, identifies high- and low-quality reads, and generates a filtered FASTQ file containing only high-quality sequences.


## Features

- Read FASTQ input files

- Parse sequencing records

- Count total reads

- Count total bases

- Calculate average read length

- Convert ASCII quality characters to Phred quality scores

- Calculate average quality score for each read

- Classify reads as PASS or FAIL using a quality threshold

- Count passed and failed reads

- Generate a filtered FASTQ file containing only high-quality reads

- Generate a dictionary of the ouput quality control data for further use

- Calculate pass rate for reads in the input file

---

## Bioinformatics Background

FASTQ is one of the standard file formats used for storing sequencing data produced by next-generation sequencing platforms.

Each sequencing read contains four lines:

1. Read identifier

2. DNA sequence

3. Separator (+)

4. ASCII encoded quality scores

Quality characters are converted into Phred quality scores using:

```

Phred Score = ASCII Value − 33

```

Higher Phred scores indicate greater confidence in each base call.

---

## Example Input

```

@Read1

ATCGATCG

+

IIIIIIII

@Read2

ATCGATCG

+

!!!!!!!!

```

---

## Example Output

```

Read 1 Average Quality: 40.0 PASS

Read 2 Average Quality: 0.0 FAIL

Total Reads: 2

Total Bases: 16

Passed: 1

Failed: 1

Average Read Length: 8

Pass Rate: 50.0 %

```

---

## Project Structure

```

bioinformatics-fastq-quality-analyzer/

│

├── fastq_quality_analyzer.py

├── sample.fastq

├── filtered.fastq

└── README.md

```

---

## Skills Demonstrated

- Python

- File handling

- Functions

- Loops

- Conditional statements

- FASTQ parsing

- Phred quality scoring

- Bioinformatics preprocessing

- Data filtering

- Dictionary formation

---