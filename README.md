DEPENDENCIES
1. Hashicorp Vagrant to create manage enviroments
2. VirtualBox or VMWare based on what operating system and cpu you have, to create the virutal machines.

HOW TO RUN ENVIROMENT
1. Ensure you have a virtual box by running the command "vagrant box add generic/ubuntu2010" for windows or "vagrant box add spox/ubuntu-arm" for M1 chip Mac users.
2. Clone the repository into your machine
3. Move to the directory you cloned the repo in with your terminal
4. Run the command "vagrant up"

HOW TO RUN PROJECT
1. Ssh into the virtual machine using "vagrant ssh"
2. Cd into the app folder
3. Run command "python3 main.py" to start the game

