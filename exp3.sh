#!/bin/sh

#20219025_Aswin_Subhash

echo "Shell script to find factorial of a number"

echo "Enter the number: "
read n

f=1

while [ $n -gt 1 ]
do
  f=$((f * n)) 
  n=$((n - 1))
done

echo $f