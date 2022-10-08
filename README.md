# ansible-role-dotfiles

Confguration of dotfiles on a Unix based environment

- Clone dotfile repository
- Create symlinks via rcup

## Test

Run `molecule test` for testing this role via Docker

## Requirements

## Role Variables

| Variable          | Description                           | default                                                             |
| ----------------- | ------------------------------------- | ------------------------------------------------------------------- |
| dotfiles_repo_url | URL of repo to clone for use with RCM | https://github.com/Allaman/dotfiles.git                             |
| dotfiles_path     | Path to the cloned repo               | {{ ansible_env.HOME }}/workspace/github.com/allaman/public-dotfiles |

## Dependencies

## Example Playbook

```
---
- name: Playbook
  hosts: localhost
  connection: local
  pre_tasks:
    - set_fact:
        dotfiles_path: "{{ ansible_env.HOME }}/.dotfiles"
  roles:
    - ansible-role-dotfiles
```

## License

MIT
