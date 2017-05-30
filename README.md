
# ZCamp2017 Chef vs Ansible Demo Repository

Demo repository for our #zcamp2017 session on Chef vs. Ansible

## Development Environment

Use [Linus Kitchen v0.3](https://github.com/tknerr/linus-kitchen/releases/tag/v0.3) which has both Chef and Ansible toolchains installed

## Chef Demo

Generate a new Chef cookbook:
```
$ chef generate cookbook myapp_chef
$ cd myapp_chef
```

Lint check via `foodcritic`:
```
$ foodcritic .
```


## Ansible Demo

Generate a new Ansible role:
```
$ molecule init role --role-name myapp_ansible
$ cd myapp_ansible
```

Lint check via `ansible-lint`:
```
$ ansible-lint molecule/default/playbook.yml
```
