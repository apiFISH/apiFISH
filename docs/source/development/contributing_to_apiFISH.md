# Reporting bugs and feature requests

The issue tracking system is available on GitHub in the [apiFISH/apiFISH repository](https://github.com/apiFISH/apiFISH/issues).

## For documentation reviewer

### 1. Clone *apiFISH* repository

Create a folder where you want to install *apiFISH* and go inside to clone the repository. Standard location to do it is: ```$HOME/Repositories/apiFISH```

```bash
mkdir $HOME/Repositories
cd $HOME/Repositories
```

Choose your clone method between HTTPS or SSH key:
- HTTPS
    ```bash
    git clone https://github.com/apiFISH/apiFISH.git
    ```
- SSH
    ```bash
    git clone git@github.com:apiFISH/apiFISH.git
    ```

### 2. Switch on the documentation branch

For apiFISH version 0.6.0, the online documentation is based on `development` branch:

```shell
git checkout development
```

Don't forget to update your local `development` branch with remote `development`:

```shell
git pull
```

### 3. Create a new branch for your modification

Create and switch on this new branch:
```shell
git checkout -b doc/name_of_my_branch
```

### 4. Fix what you want

You're reading the [online documentation](https://apiFISH.readthedocs.io/en/latest/index.html) and you find something to fix:

- Check your web link like https://apiFISH.readthedocs.io/en/latest/**user_guide/apiFISH_presentation**.html
- With your file editor, go to `apiFISH` > `docs` > `source` > **user_guide > apiFISH_presentation**.md
- Fix what you want

### 5. Share your modifications

- `git add -A`
- `git commit -m "write your message here"`
- `git push`
- Create a pull request [on github](https://github.com/apiFISH/apiFISH/pulls)
- wait for a developer to validate the PR
