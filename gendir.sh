#!/usr/bin/env bash
dirExsists(){
echo ""
	if [ -d $1 ]
	then
		echo "[O.K] Found $1"
	else
		echo "[Error]: Can't find $1, Creating directory"
		mkdir -p $1
	fi
}

dir="./"
catFolders="binary crypto stego reversing web misc forensics osint"
eventName=$1
projectDir=$dir$eventName
dirExsists $projectDir

for name in $catFolders; do
    mkdir -pv $projectDir"/"$name && touch $projectDir"/"$name"/.gitkeep"
done;
