fastq_to_fasta -i C3_S3_forward_paired.fq -o C3_FWD.fasta
sed -r s/\([1-2]:[N]:[0]:[A-Z][A-Z]*\)//g C3_FWD.fasta > C3_FWD1.fasta
fastq_to_fasta -i C3_S3_reverse_paired.fq -o C3_REV.fasta
sed -r s/\([1-2]:[N]:[0]:[A-Z][A-Z]*\)//g C3_REV.fasta > C3_REV1.fasta
fastq_to_fasta -i C6_forward_paired.fq -o C6_FWD.fasta
sed -r s/\([1-2]:[N]:[0]:[A-Z][A-Z]*\)//g C6_FWD.fasta > C6_FWD1.fasta
fastq_to_fasta -i C6_reverse_paired.fq -o C6_REV.fasta
sed -r s/\([1-2]:[N]:[0]:[A-Z][A-Z]*\)//g C6_REV.fasta > C6_REV1.fasta
python Wheaver.py C3_FWD1.fasta C3_REV1.fasta C3_full.fasta
head -n 8000000 C3_full.fasta > C3_head.fasta
python Wheaver.py C6_FWD1.fasta C6_REV1.fasta C6_full.fasta
head -n 8000000 C6_full.fasta > C6_head.fasta
python NumberEr.py C3_head.fasta C6_head.fasta
cat C3_head.fasta C6_head.fasta1 > C3_C6.fasta 
python /bigdata/pabster212/RepeatExplorer/seqclust_cmd.py -s C3_C6.fasta -f 4 -d Viridiplantae -c 9 -v C3_C6_output
