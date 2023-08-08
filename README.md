# root

[![Source Code](https://img.shields.io/badge/github-source%20code-blue?logo=github&amp;logoColor=white)](https://github.com/rolehippie/root)
[![General Workflow](https://github.com/rolehippie/root/actions/workflows/general.yml/badge.svg)](https://github.com/rolehippie/root/actions/workflows/general.yml)
[![Readme Workflow](https://github.com/rolehippie/root/actions/workflows/docs.yml/badge.svg)](https://github.com/rolehippie/root/actions/workflows/docs.yml)
[![Galaxy Workflow](https://github.com/rolehippie/root/actions/workflows/galaxy.yml/badge.svg)](https://github.com/rolehippie/root/actions/workflows/galaxy.yml)
[![License: Apache-2.0](https://img.shields.io/github/license/rolehippie/root)](https://github.com/rolehippie/root/blob/master/LICENSE)
[![Ansible Role](https://img.shields.io/badge/role-rolehippie.root-blue)](https://galaxy.ansible.com/rolehippie/root)

Ansible role to configure the system root user.

## Sponsor

Building and improving this Ansible role have been sponsored by my current and previous employers like **[Cloudpunks GmbH](https://cloudpunks.de)** and **[Proact Deutschland GmbH](https://www.proact.eu)**.

## Table of content

- [Requirements](#requirements)
- [Default Variables](#default-variables)
  - [root_bashit](#root_bashit)
  - [root_bashit_version](#root_bashit_version)
  - [root_castles](#root_castles)
  - [root_castles_force](#root_castles_force)
  - [root_enable_profile_load](#root_enable_profile_load)
  - [root_homeshick_version](#root_homeshick_version)
  - [root_ohmyzsh](#root_ohmyzsh)
  - [root_ohmyzsh_version](#root_ohmyzsh_version)
  - [root_override_zshenv](#root_override_zshenv)
  - [root_password](#root_password)
  - [root_shell](#root_shell)
  - [root_sshkeys](#root_sshkeys)
- [Discovered Tags](#discovered-tags)
- [Dependencies](#dependencies)
- [License](#license)
- [Author](#author)

---

## Requirements

- Minimum Ansible version: `2.10`


## Default Variables

### root_bashit

Install bash-it repo

#### Default value

```YAML
root_bashit: false
```

### root_bashit_version

Version of bash-it to install

#### Default value

```YAML
root_bashit_version: latest
```

### root_castles

List of castles to use

#### Default value

```YAML
root_castles: []
```

#### Example usage

```YAML
root_castles:
  - tboerger/homeshick-base
  - name: tboerger/homeshick-linux
    force: True
```

### root_castles_force

Force castle updates

#### Default value

```YAML
root_castles_force: true
```

### root_enable_profile_load

Enable loading of profile.d within zshenv

#### Default value

```YAML
root_enable_profile_load: true
```

### root_homeshick_version

Version of homeshick to install

#### Default value

```YAML
root_homeshick_version: latest
```

### root_ohmyzsh

Install oh-my-zsh repo

#### Default value

```YAML
root_ohmyzsh: false
```

### root_ohmyzsh_version

Version of bash-it to install

#### Default value

```YAML
root_ohmyzsh_version: latest
```

### root_override_zshenv

Override zshenv provided by system

#### Default value

```YAML
root_override_zshenv: true
```

### root_password

Update root password to this value

#### Default value

```YAML
root_password:
```

### root_shell

Enforce this shell for root

#### Default value

```YAML
root_shell: /bin/bash
```

### root_sshkeys

List of authorized keys

#### Default value

```YAML
root_sshkeys: []
```

#### Example usage

```YAML
root_sshkeys:
  - ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAINaQYR0/Oj6k1H03kshz2J7rlGCaDSuaGPhhOs9FcZfn tboerger@host1
  - ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIC7oOi3qaDtfQVFhPKyd0Wk0C/y+QM71vtln8Rl44NlB tboerger@host2
  - ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIFcPTmdo+7eK+8n2yE7Kx1vyQ4yJwHBngvQOt1MPhKhR tboerger@host3
```

## Discovered Tags

**_root_**


## Dependencies

- None

## License

Apache-2.0

## Author

[Thomas Boerger](https://github.com/tboerger)
