# root

[![Source Code](https://img.shields.io/badge/github-source%20code-blue?logo=github&logoColor=white)](https://github.com/rolehippie/root) [![Build Status](https://img.shields.io/drone/build/rolehippie/root/master?logo=drone)](https://cloud.drone.io/rolehippie/root) [![License: Apache-2.0](https://img.shields.io/github/license/rolehippie/root)](https://github.com/rolehippie/root/blob/master/LICENSE) 

Ansible role to configure the system root user. 

## Sponsor 

[![Proact Deutschland GmbH](https://proact.eu/wp-content/uploads/2020/03/proact-logo.png)](https://proact.eu) 

Building and improving this Ansible role have been sponsored by my employer **Proact Deutschland GmbH**.

## Table of content

* [Default Variables](#default-variables)
  * [root_bashit](#root_bashit)
  * [root_castles](#root_castles)
  * [root_castles_force](#root_castles_force)
  * [root_ohmyzsh](#root_ohmyzsh)
  * [root_password](#root_password)
  * [root_shell](#root_shell)
  * [root_sshkeys](#root_sshkeys)
* [Dependencies](#dependencies)
* [License](#license)
* [Author](#author)

---

## Default Variables

### root_bashit

Install bash-it repo

#### Default value

```YAML
root_bashit: false
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

### root_ohmyzsh

Install oh-my-zsh repo

#### Default value

```YAML
root_ohmyzsh: false
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

## Dependencies

* None

## License

Apache-2.0

## Author

[Thomas Boerger](https://github.com/tboerger)
