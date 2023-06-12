gmx editconf -f SUG.100.gro -c -d 2 -o center.gro -bt cubic

gmx insert-molecules -ci sod.pdb -nmol 1 -box 10 10 10 -o chx_box.gro

gmx solvate -cp center.gro -cs chx_box.gro -o box.gro -p SUG.100.top -maxsol 2019

(number of maximum solvent molecules will depend upon the number of charged sugar moatoms)

(now you modify the topology file, by including the SOD atoms, you will also have to remove the last line from the topology file, because the SOD ions will be included in the system)

python mod_top_sod.py SUG.100.top 48469 50488

(48469 is the index of the last sugar bead, 50488 is the index of the last sodium ion + 1)

(now create a index file using the following code)

python index_sys.py 48469 50487

gmx grompp -f minim.mdp -c box.gro -p MOD.top -o minim.tpr -maxwarn 2 -n index_file.ndx

gmx mdrun -s minim.tpr -noddcheck -v -deffnm minim

gmx grompp -f mdrun1.mdp -c minim.gro -p MOD.top -o mdrun.tpr -maxwarn 2 -n index_file.ndx

gmx mdrun -s mdrun.tpr -noddcheck -v -deffnm mdrun

gmx trjconv -s mdrun.tpr -f mdrun.xtc -o mdnoPBC.xtc -pbc mol -center

gmx trjconv -s mdrun.tpr -f mdnoPBC.xtc -dt 5 -o traj.pdb

