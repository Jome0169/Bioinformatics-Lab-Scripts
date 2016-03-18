#for sampleFile in $(cat sampleList.txt); do awk ‘{print $7}’ $sampleFile >
#		tempCol.txt; paste allSampleTPMfile.txt tempCol.txt > tempTable.txt; mv
#		tempTable.txt allSampleTPMfile.txt; done

for Sample in *TrinityAlignemnt; 
	do homesweet=${PWD##*/}; mv TotalIsoforms.txt ${homesweet}_totalisoforms.txt; cd $Sample ; awk '{print $6}' RSEM.isoforms.results > TempFile.txt ;
			result=${PWD##*/} ;  NewFile=${result%_TrinityAlignemnt}; 
			sed 's/TPM/'"$NewFile"'/g' TempFile.txt >  CuteFile.txt ; mv CuteFile.txt .. ; 
			cd .. ; paste ${homesweet}_totalisoforms.txt CuteFile.txt > temptable.txt; mv temptable.txt ${homesweet}_totalisoforms.txt; 
done
