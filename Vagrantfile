
Vagrant.configure("2") do |config|
  config.vm.box = "generic/ubuntu2010"
  config.vm.network "private_network", ip: "192.168.56.10"
  config.vm.provider "virtualbox" do |vb|
    config.vm.synced_folder "app/", "/home/vagrant/app/"
end
