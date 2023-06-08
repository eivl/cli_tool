# `awsome-user-cli`

Awsome CLI user management tool.

**Usage**:

```console
$ awsome-user-cli [OPTIONS] COMMAND [ARGS]...
```

**Options**:

* `--install-completion`: Install completion for the current shell.
* `--show-completion`: Show completion for the current shell, to copy it or customize the installation.
* `--help`: Show this message and exit.

**Commands**:

* `create`: Create a new user with USERNAME.
* `delete`: Delete a user with USERNAME.
* `delete-all`: Delete ALL user with USERNAME.
* `init`: Initialize the user database.

## `awsome-user-cli create`

Create a new user with USERNAME.

**Usage**:

```console
$ awsome-user-cli create [OPTIONS] USERNAME
```

**Arguments**:

* `USERNAME`: [required]

**Options**:

* `--help`: Show this message and exit.

## `awsome-user-cli delete`

Delete a user with USERNAME.

If --force is not used, will ask for confirmation.

**Usage**:

```console
$ awsome-user-cli delete [OPTIONS] USERNAME
```

**Arguments**:

* `USERNAME`: [required]

**Options**:

* `--force / --no-force`: Fore deletion without confirmation.  [required]
* `--help`: Show this message and exit.

## `awsome-user-cli delete-all`

Delete ALL user with USERNAME.

If --force is not used, will ask for confirmation.

**Usage**:

```console
$ awsome-user-cli delete-all [OPTIONS]
```

**Options**:

* `--force / --no-force`: Fore deletion without confirmation.  [required]
* `--help`: Show this message and exit.

## `awsome-user-cli init`

Initialize the user database.

**Usage**:

```console
$ awsome-user-cli init [OPTIONS]
```

**Options**:

* `--help`: Show this message and exit.
