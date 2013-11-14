#!/bin/bash

#echo $#
if [ "$#" = "2" ]; then
	echo "Pessoa:" $1
	echo "Ficheiro:" $2

	rm -i deliver.txt
	grep $1, $2 > deliver.txt
	chmod 666 deliver.txt
	echo "Resultado no ficheiro deliver.txt com " `wc -l deliver.txt` "linhas" 
else
	echo "First argument - person name"
	echo "Second argument - file name"
fi
