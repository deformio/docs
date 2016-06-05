# CLI Reference

Deform command line client (CLI) allows you talk to and operate Deform using the command line interface. It talks to the Deform using the public API.
Source code could be found here [https://github.com/deformio/cli-deform](https://github.com/deformio/cli-deform).

## Installation

    $ pip install cli-deform

## Commands

```
$ deform

Usage: deform [OPTIONS] COMMAND [ARGS]...

  Command-line client for Deform.io

Options:
  -h, --help  Show this message and exit.

Commands:
  collection       Collection manipulation commands
  collections      Collections manipulation commands
  confirm          Confirms email by code
  current-project  Outputs a current project
  document         Document manipulation commands
  documents        Documents manipulation commands
  login            Authenticates against the API
  logout           Logs out current user
  project          Project manipulation commands
  projects         User's projects
  settings         CLI settings
  signup           Creates an account
  use-project      Sets a current project
  version          Outputs the client version
  whoami           Outputs the current user
```

Every command has a help option:

```bash
$ deform signup -h

Usage: deform signup [OPTIONS]

  Creates an account

Options:
  -e, --email TEXT
  -p, --password TEXT
  -h, --help           Show this message and exit.
```
