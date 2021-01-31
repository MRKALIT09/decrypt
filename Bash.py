#PROGRAM DECRYPT BY MANDO XPLOIT
#module
from os import system, remove

file=input('FILE => ')

openfile=open(file, 'r')

readfile=openfile.read()

openfile.close()

newcode=readfile.replace('eval', 'echo')

outfile=input('OutPut => ')

newfile=open(outfile, 'w')

newfile.write(newcode)

newfile.close()

system('touch tools.sh')

system('bash'+outfile+' => tools.sh')

remove(outfile)

system('mv -f tools.sh '+outfile)

print('SUCCES DECRYPT | FILE TERSIMPAN '+outfile)

