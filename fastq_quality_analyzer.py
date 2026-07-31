def calculate_average_quality(quality_string):            # Calculate the average quality score of a FASTQ read
    total_quality_score = 0
    for quality_char in quality_string:
        total_quality_score += (ord(quality_char) - 33)
        
    average_quality_score = total_quality_score / len(quality_string)
    return average_quality_score 

def read_fastq_file(input_filename, output_filename):         
    file = open(input_filename, "r")
    total_reads = 0
    total_bases = 0
    passed_reads = 0
    failed_reads = 0
    output_file = open(output_filename, "w")

    read_id = file.readline().strip()
    
    while read_id:                                         # Read the FASTQ file in chunks of 4 lines (read ID, DNA sequence, separator, quality string)
        dna_sequence = file.readline().strip()
        separator = file.readline().strip()
        quality_string = file.readline().strip()
        
        average_quality_score = calculate_average_quality(quality_string)
        total_reads += 1
        total_bases += len(dna_sequence)
       
        if average_quality_score >= 30:                    # Regard reads as passed or failed reads based on quality treshold
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
    if total_reads > 0:                                   # Calculate average read length if reads are present
        average_read_length = total_bases / total_reads
        print("Average Read Length:", average_read_length)
    else:
        print("No reads found in the FASTQ file.")
    file.close()
    output_file.close()
    
    return {                                              # Return a dictionary with the statistics
    "total_reads": total_reads,
    "total_bases": total_bases,
    "passed_reads": passed_reads,
    "failed_reads": failed_reads,
    "average_read_length": average_read_length
    }
stats = read_fastq_file("sample.fastq", "filtered.fastq")

pass_rate = (                                            # Calculate the pass rate of reads based on quality
    stats["passed_reads"] / stats["total_reads"]
) * 100
print("Pass Rate:", pass_rate, "%")

if stats["failed_reads"] > 100:                          # Check if failed reads exceed threshold
    print("Warning: Many reads failed quality control.")


