def calculate_average_quality(quality_string):
    total_quality_score = 0
    for quality_char in quality_string:
        total_quality_score += (ord(quality_char) - 33)
        
    average_quality_score = total_quality_score / len(quality_string)
    return average_quality_score 

def read_fastq_file():
    file = open("sample.fastq", "r")
    total_reads = 0
    total_bases = 0
    passed_reads = 0
    failed_reads = 0
    output_file = open("filtered.fastq", "w")

    read_id = file.readline().strip()
    
    while read_id:
        dna_sequence = file.readline().strip()
        separator = file.readline().strip()
        quality_string = file.readline().strip()
        
        average_quality_score = calculate_average_quality(quality_string)
        total_reads += 1
        total_bases += len(dna_sequence)
       
        if average_quality_score >= 30:
            passed_reads += 1
            print("Read", (total_reads), "Average Quality:", average_quality_score, "PASS")
            output_file.write(read_id + "\n" + dna_sequence + "\n" + separator + "\n" + quality_string + "\n")
        else:
            print("Read", (total_reads), "Average Quality:", average_quality_score, "FAIL")
            failed_reads += 1
        
        read_id = file.readline().strip()

    print("Total Reads:", total_reads)
    print("Total Bases:", total_bases)
    print("Passed:", passed_reads)
    print("Failed:", failed_reads)
    if total_reads > 0:
        average_read_length = total_bases / total_reads
        print("Average Read Length:", average_read_length)
    else:
        print("No reads found in the FASTQ file.")
    file.close()
    output_file.close()
read_fastq_file()