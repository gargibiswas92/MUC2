echo "Enter the name of the starting .gro file:"

read gro

echo "enter the name of the initial topology file:"

read top

echo "Enter the name of modified topology file (with ions):"

read mod_top

echo "Enter the name of the index file:"

read index

echo "Enter the name of the mdrun.mdp file:"

read mdrun

echo "Enter the name of the mimim.mdp file:"

read minim

echo "Enter the structure of the solvent molecule:"

read sol_name

echo "Enter the maximum number of solvent to be added in the box:"

read sol_num

echo "Enter the distance of the box edge from the protein in nm:"

read edge

gmx editconf -f "$gro" -c -d $edge -o center.gro -bt cubic
gmx insert-molecules -ci sod.pdb -nmol 10000 -box $edge $edge $edge -o chx_box.gro
gmx solvate -cp center.gro -cs chx_box.gro -o box.gro -p "$top" -maxsol $sol_num
gmx grompp -f "$minim" -c box.gro -p "$mod_top" -o minim.tpr -maxwarn 3 -n "$index"
gmx mdrun -s minim.tpr -noddcheck -v -deffnm minim
gmx grompp -f "$mdrun" -c minim.gro -p "$mod_top" -o mdrun.tpr -maxwarn 3 -n "$index"
