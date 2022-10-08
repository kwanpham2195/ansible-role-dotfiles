# ansible-role-dotfiles

Confguration of dotfiles on a Linux based environment

- Clone dotfile repository
- Create symlinks via rcup
- Create global .gitconfig

## Test

Run `molecule test` for testing this role via Docker

## Requirements

## Role Variables

| Variable                           | Description                           | default                                 |
| ---------------------------------- | ------------------------------------- | --------------------------------------- |
| dotfiles_repo_url                  | URL of repo to clone for use with RCM | https://github.com/Allaman/dotfiles.git |
| gitconfig.name                     | Name of global git config             | Michael                                 |
| gitconfig.username                 | Username of global git config         | allaman                                 |
| gitconfig.mail                     | Mail of global git config             | allaman@rootknecht.net                  |
| gitconfig.credential_cache         | Cache git credentials                 | true                                    |
| gitconfig.credential_cache_timeout | How long to store git credentials     | 3600                                    |
| gitconfig.delta                    | Use delta as git diff enhancement     | true                                    |
| gitconfig.neovim_remote            | Use NeoVim as global diff tool        | true                                    |

## Dependencies

- ansible-role-basic

## Example Playbook

```
---
- name: Playbook
  hosts: localhost
  connection: local
  pre_tasks:
    - set_fact:
        dotfiles_path: "{{ ansible_env.HOME }}/.dotfiles"
        gitconfig:
          name: infratest
          username: test
          mail: max.mustermann@example.com
          credential_cache: "false"
          credential_cache_timeout: 600
          delta: "false"
          neovim_remote: "false"
  roles:
    - ansible-role-dotfiles
```

## License

MIT
