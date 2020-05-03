ansible-role-dotfiles
=========

Confguration of dotfiles on a Linux based environment

- Installs RCM
- Clone dotfile repository
- Create symlinks via rcup
- Create global .gitconfig

Requirements
------------

Following programs must be in the path:

- awk
- make
- git

When running on Arch Linux they are installed by this role. (Sudo permissions required)

Role Variables
--------------


| Variable| Description | default |
|---------|-------------|---------|
| dotfiles_repo_url | URL of repo to clone for use with RCM | https://github.com/Allaman/dotfiles.git |
| gitconfig.name | Name of global git config | Michael |
| gitconfig.username | Username of global git config | allaman |
| gitconfig.mail | Mail of global git config | allaman@rootknecht.net |
| gitconfig.credential_cache | Cache git credentials | true |
| gitconfig.credential_cache_timeout | How long to store git credentials | 3600 |
| gitconfig.diff_so_fancy | Use diff-so-fancy as global pager tool | true |
| gitconfig.neovim_remote | Use NeoVim as global diff tool | true |

Dependencies
------------

No dependencies

Example Playbook
----------------

```
---
- name: Playbook
  hosts: localhost
  connection: local
  roles:
    - ansible-role-dotfiles
```

License
-------

MIT
