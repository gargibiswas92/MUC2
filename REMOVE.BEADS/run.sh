#!/bin/csh

echo "Enter the number of sugars you want to keep:"

read number

echo "Enter the name of .gro file:"

read gro

echo "Enter the name of the .top file:"

read top

python mod_structure.py $gro $number
python mod_topology.py $top $number
python mod_index.py $number
python index_group_red.py
python mod_top_sod_red.py MOD_top.top 
