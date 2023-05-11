#!/bin/bash

#20219025_Aswin_Subhash

echo "Shell script to sum n numbers"

echo "Enter the total number of no.s to be added: "
read n

s=0
i=0

echo "Enter numbers to be added: "
while [ $i != $n ]
do
    read a
    s=`expr $s + $a`
    i=`expr $i + 1`
done

echo "The sum is : $s"
