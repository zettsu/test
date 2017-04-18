Vagrant.configure(2) do |config|

    config.vm.box = "bento/debian-8.5"
    config.vm.network "forwarded_port", guest: 5000, host: 5000
    config.vm.synced_folder "~/TaskManager", "/home/vagrant/TaskManager", owner: "www-data", group: "www-data", :mount_options => ["dmode=777","fmode=777"]
    config.vm.provision "shell", inline: <<-SHELL

    mkdir /home/vagrant/TaskManager
    sudo apt-get update

    sudo apt-get install python
    sudo apt-get install virtualenv

    #composer
    php -r "copy('https://getcomposer.org/installer', '/tmp/composer-setup.php');"
    sudo php /tmp/composer-setup.php --install-dir=/usr/local/bin --filename=composer
    #composer

    SHELL
end