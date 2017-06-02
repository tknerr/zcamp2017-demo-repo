
# ZCamp2017 Chef vs Ansible Demo Repository

Demo repository for our #zcamp2017 session on Chef vs. Ansible

## Development Environment

Use [Linus Kitchen v0.3](https://github.com/tknerr/linus-kitchen/releases/tag/v0.3) which has both Chef and Ansible toolchains installed

## Chef Demo

Lint check via `foodcritic`:
```
$ foodcritic .
```

Integration-test the Chef cookbook:
```
$ kitchen converge
$ kitchen verify
$ kitchen destroy
```

## Ansible Demo

Lint check via `ansible-lint`:
```
$ ansible-lint site.yml
```

Integration-test the Ansible role:
```
$ molecule converge
$ molecule verify
$ molecule destroy
```
Executing the Ansible role via Vagrant in Docker:
```
$ vagrant up --provider docker
´´´
