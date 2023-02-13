# 環境構築

## in ubuntu

```
apt install vagrant
```

```
vagrant plugin install vagrant-vbguest
```

```
sudo /sbin/vboxconfig
```

## windows

https://www.kkaneko.jp/tools/win/windows_vagrant.html
こちらを参考に

# 起動方法

```
vagrant up --provider=virtualbox
```

起動後、ID: vagrant PASS: vagrant
でログイン可能。
ログイン後、sudo reboot で再起動後、GUI が動作するようになる。

# 構成について

- 過去バージョンの chrome が使用されている。

- 起動時に ansible によって自動で構成が作成される。

  - 中に入って、ローカルで実行したいときは

  ```
  ansible-playbook -c local -i localhost, playbook.yml
  ```

  - 手動でディスプレイ先を変えたいときは、

  ```
  export DISPLAY=:0.0
  ```

# トラブルシューティング

- ファイル共有が上手くされない

  ゲストエディションをプラグインで更新する。

  ```
  vagrant plugin install vagrant-vbguest
  ```

- 以下のエラーが出る
  VBoxManage.exe: error: Details: code E_FAIL (0x80004005), component SessionMachine, interface IMachine, callee IUnknown
  　ローカルにディレクトリが残ってしまっている
