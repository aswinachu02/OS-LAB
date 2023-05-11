#!/bin/bash

#20219025_Aswin_Subhash

echo "Shell script to check if a string is palindrome or not"
echo "Please enter a string without spaces"
read str

for i in $(seq 0 ${#str})
do 
   rev=${str:$i:1}${rev}
done

if [ "$str" = "$rev" ]
then
   echo "The entered string is palindrome"
else
   echo "It is not palindrome"
fi