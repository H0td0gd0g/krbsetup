# krbsetup


**krbsetup** is a command-line tool that automates the setup of a Kerberos client environment.

When working with Active Directory environments, such as during penetration tests, CTFs, or lab validation, you often need to edit `/etc/hosts`, write `/etc/krb5.conf`, and export environment variables before Kerberos authentication will work. krbsetup takes care of these steps for you so that you can get started quickly and consistently.


```
kali% krbsetup -h

    __          __                 __                  / \__
    |  |--.----.|  |--.-----.-----.|  |_.--.--.-----.  (    @\___
    |    <|   _||  _  |__ --|  -__||   _|  |  |  _  |  /         O
    |__|__|__|  |_____|_____|_____||____|_____|   __| /   (_____/
                                            |__|     /_____/   U

    Kerberos Environment Setup Tool
    Author : H0td0gd0g
    Version : 0.1.0
    =============================================
    
usage: krbsetup [-h] [--debug] {setup,cleanup} ...

Kerberos Environment Setup Tool

positional arguments:
  {setup,cleanup}
    setup          Set up enviroment
    cleanup        clean up settings

options:
  -h, --help       show this help message and exit
  --debug          Show debug messages
```

## Features

- Adds the target host entry to `/etc/hosts`
- Generates a `krb5.conf` for the target realm
- Writes the required environment variables to your shell configuration file (`~/.zshrc` by default)
- Supports both `local` and `remote` setup modes
- Provides a `cleanup` command to remove the settings it has added

## Requirements

- Python 3.14 or later
- [pipx](https://pipx.pypa.io/)

## Installation

We recommend installing krbsetup with pipx, which places the tool in an isolated environment and makes the `krbsetup` command available globally.

```bash
pipx install git+https://github.com/H0td0gd0g/krbsetup
```

To upgrade to the latest version:

```bash
pipx upgrade krbsetup
```

To uninstall:

```bash
pipx uninstall krbsetup
```

## Usage

### Local setup

Please specify the IP address and the fully qualified domain name (FQDN) of the target host.

```bash
krbsetup setup local -i <IP_ADDRESS> -d <FQDN>
```

Example:

```bash
krbsetup setup local -i 10.10.10.100 -d dc01.corp.local
```

In this example, krbsetup derives the following values from the FQDN:

| Item     | Value             |
|----------|-------------------|
| Hostname | `dc01`            |
| Domain   | `corp.local`      |
| Realm    | `CORP.LOCAL`      |

### Remote setup

```bash
krbsetup setup remote -i <IP_ADDRESS>
```

### Cleaning up

To remove the settings added by krbsetup, please run:

```bash
krbsetup cleanup
```

### Debug output

If you would like to see detailed messages, please add the `--debug` option.

```bash
krbsetup setup local --debug -i 10.10.10.100 -d dc01.corp.local
```

## Command Reference

```
krbsetup setup local
  -i, --ip     IP address of the target host (required)
  -d, --fqdn   Fully qualified domain name of the target host (required)
  --debug      Show debug messages

krbsetup setup remote
  -i, --ip     IP address of the target host (required)
  --debug      Show debug messages

krbsetup cleanup
  --debug      Show debug messages
```

You can also run `krbsetup -h` or `krbsetup <command> -h` at any time to display help.

## Configuration

Default paths can be adjusted in `config.toml`.

| Key        | Default      | Description                                   |
|------------|--------------|-----------------------------------------------|
| `shell_rc` | `~/.zshrc`   | Shell configuration file to write variables to |
| `krb5_dir` | `./krbsetup` | Directory where generated files are placed     |

## Notes

- Please run krbsetup as a normal user. Running it as root is intentionally blocked.
- Changes to system files such as `/etc/hosts` require root privileges. Rather than running with elevated privileges itself, krbsetup prints the exact `sudo` commands needed, so that you can review them before running them yourself.
- Please use this tool only against systems that you own or are explicitly authorized to test.

## Author

H0td0gd0g
