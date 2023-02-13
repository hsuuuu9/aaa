# -*- mode: ruby -*-
# vi: set ft=ruby :

# All Vagrant configuration is done below. The "2" in Vagrant.configure
# configures the configuration version (we support older styles for
# backwards compatibility). Please don't change it unless you know what
# you're doing.
Vagrant.configure("2") do |config|
  config.vm.box = "bento/ubuntu-20.04"
  # 共有フォルダの設定（ホストOSとゲストOS間のファイル同期実施）
  config.vm.synced_folder ".", "/vagrant",  create: true, owner: "vagrant", group: "vagrant"

  config.vm.define "bot" do |server|
    # 仮想マシンのホスト名とIPアドレスを設定
    server.vm.hostname = "bot"
    server.vm.network :private_network, ip: "192.168.56.0"

    # VirtualBoxのGUI上の名前を設定
    server.vm.provider "virtualbox" do |vb|
      vb.gui = true
      vb.name = config.vm.box.gsub(/\//, "_") + "_" + server.vm.hostname
      vb.cpus   = 4       # CPU 割り当て
      vb.memory = "8096"  # メモリ割り当て
      vb.customize [
        "modifyvm"          , :id,
        "--vram"            , "256",
        "--clipboard"       , "bidirectional",
        "--accelerate3d"    , "on",
        "--hwvirtex"        , "on",
        "--nestedpaging"    , "on",
        "--largepages"      , "on",
        "--ioapic"          , "on",
        "--pae"             , "on",
        "--paravirtprovider", "kvm",
      ]
    end


    config.vm.provision "shell", inline: <<-SHELL
      apt-get -y update
      apt-get -y upgrade
      apt-get -y install ubuntu-desktop
      apt -y install software-properties-common
      apt-add-repository --yes --update ppa:ansible/ansible
      apt -y install ansible
    SHELL
     # Ansibleを利用したプロビジョニング実施
    server.vm.provision "ansible_local" do |ansible|
      ansible.playbook = "playbook.yml"
    end
  end
end

# すべて終わったら、リロードすること。
