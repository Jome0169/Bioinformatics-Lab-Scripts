fastq_to_fasta -i C10_S1_forward_paired.fq -o C10_FWD.fasta
sed -r s/\([1-2]:[N]:[0]:[A-Z][A-Z]*\)//g C10_FWD.fasta > C10_FWD1.fasta
fastq_to_fasta -i C10_S1_reverse_paired.fq -o C10_REV.fasta
sed -r s/\([1-2]:[N]:[0]:[A-Z][A-Z]*\)//g C10_REV.fasta > C10_REV1.fasta
fastq_to_fasta -i C4_S4_forward_paired.fq -o C4_FWD.fasta
sed -r s/\([1-2]:[N]:[0]:[A-Z][A-Z]*\)//g C4_FWD.fasta > C4_FWD1.fasta
fastq_to_fasta -i C4_S4_reverse_paired.fq -o C4_REV.fasta
sed -r s/\([1-2]:[N]:[0]:[A-Z][A-Z]*\)//g C4_REV.fasta > C4_REV1.fasta
python Wheaver.py C10_FWD1.fasta C10_REV1.fasta C10_full.fasta
head -n 8000000 C10_full.fasta > C10_head.fasta
python Wheaver.py C4_FWD1.fasta C4_REV1.fasta C4_full.fasta
head -n 8000000 C4_full.fasta > C4_head.fasta
python NumberEr.py C10_head.fasta C4_head.fasta
cat C10_head.fasta C4_head.fasta1 > C10_C4.fasta 
python /bigdata/pabster212/RepeatExplorer/seqclust_cmd.py -s C10_C4.fasta -f 4 -d Viridiplantae -c 9 -v C10_C4_output
