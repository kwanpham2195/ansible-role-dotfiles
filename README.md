# ansible-role-dotfiles

Confguration of dotfiles on a Unix based environment

- Clone up to two dotfile repositories (one public and one private in my case)
- Create symlinks via rcup

## Test

Run `molecule test` for testing this role via Docker

## Requirements

## Role Variables

| Variable                       | Description                           | default                                                             |
| ------------------------------ | ------------------------------------- | ------------------------------------------------------------------- |
| dotfiles.public.enabled        | Enable public dotfiles                | true                                                                |
| dotfiles.public_repo_url       | URL of repo to clone for use with RCM | https://github.com/Allaman/dotfiles.git                             |
| dotfiles.public.path           | Path to the cloned repo               | {{ ansible_env.HOME }}/workspace/github.com/allaman/public-dotfiles |
| dotfiles.public.excluded_files | List of files that are not symlinked  | README.md, LICENSE, screenshot.png                                  |

In addition, you can specify those variables for `dotfiles.private` as well.

## Dependencies

## Example Playbook

```
---
- name: Playbook
  hosts: localhost
  connection: local
  pre_tasks:
    - set_fact:
        dotfiles:
          public:
            path: "{{ ansible_env.HOME }}/.dotfiles"
  roles:
    - ansible-role-dotfiles
```

## License

MIT
