# fastWordHydra
Python code that automates the process of web crawling and brute force attack with hydra.

## Warning
<p><b>DO NOT</b> try to use this command to attack other's computer, use it as a tool to learn or even automate the process of your own work. After all, this tool was created with the intention to learn even more about how brute force attacks work.<br>"with great power comes great responsibility."</p>

## Requirements
<p>In order to use this tool, you should have the following in your device: </p>
-Hydra (sudo apt install hydra -y) <br>
-Root permissions in the terminal that is running the code.

## How it works
<p>Firstly, the program will ask for a URL to curl. <b>DO NOT</b> forget to use "https://", as it is needed. This first part of the code will generate a wordlist that gets all possible passwords with a length greater than 6. </p>
<p>After this, you will be asked if you want or not to run Hydra's brute force (Y to yes and N to to). Please note that if you want to execute Hydra's brute force, you will need the following: </p>
-The possible username that will be used in the authentication; <br>
-The full IpV4 address of the target machine. E.g. 192.168.0.1. <br><br>
<p>On the other hand, if you choose not to run the brute force attack, the program will stop and the generated wordlist will be in the current folder named of "completeWordList.txt". </p>

