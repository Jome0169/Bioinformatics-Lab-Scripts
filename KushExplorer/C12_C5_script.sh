fastq_to_fasta -i C12_S2_forward_paired.fq -o C12_FWD.fasta
sed -r s/\([1-2]:[N]:[0]:[A-Z][A-Z]*\)//g C12_FWD.fasta > C12_FWD1.fasta
fastq_to_fasta -i C12_S2_reverse_paired.fq -o C12_REV.fasta
sed -r s/\([1-2]:[N]:[0]:[A-Z][A-Z]*\)//g C12_REV.fasta > C12_REV1.fasta
fastq_to_fasta -i C5_forward_paired.fq -o C5_FWD.fasta
sed -r s/\([1-2]:[N]:[0]:[A-Z][A-Z]*\)//g C5_FWD.fasta > C5_FWD1.fasta
fastq_to_fasta -i C5_reverse_paired.fq -o C5_REV.fasta
sed -r s/\([1-2]:[N]:[0]:[A-Z][A-Z]*\)//g C5_REV.fasta > C5_REV1.fasta
python Wheaver.py C12_FWD1.fasta C12_REV1.fasta C12_full.fasta
head -n 8000000 C12_full.fasta > C12_head.fasta
python Wheaver.py C5_FWD1.fasta C5_REV1.fasta C5_full.fasta
head -n 8000000 C5_full.fasta > C5_head.fasta
python NumberEr.py C12_head.fasta C5_head.fasta
cat C12_head.fasta C5_head.fasta1 > C12_C5.fasta 
python /bigdata/pabster212/RepeatExplorer/seqclust_cmd.py -s C12_C5.fasta -f 4 -d Viridiplantae -c 9 -v C12_C5_output
