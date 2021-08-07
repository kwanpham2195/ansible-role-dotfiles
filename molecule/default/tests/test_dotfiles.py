import os

def test_exist_dotfiles(host):
    home = host.user("root").home
    assert host.file(home+"/.dotfiles").exists

def test_exist_nvim(host):
    home = host.user("root").home
    assert host.file(home+"/.config/nvim/init.lua").exists

def test_exist_nvim_symlink(host):
    home = host.user("root").home
    assert host.file(home+"/.config/nvim/init.lua").is_symlink

def test_exist_gitconfig(host):
    home = host.user("root").home
    assert host.file(home+"/.gitconfig").exists

def test_exist_gitconfig_entry(host):
    home = host.user("root").home
    assert host.file(home+"/.gitconfig").contains("infratest")

