# Code Playground
This repository is a collection of coding experiments
It uses Git submodules to organize the contents. Each folder have its own Github repository.

## Working with Submodules

Follow the instructions below to properly clone, update, and contribute to this repository.

### Cloning the Repository with Submodules

When cloning this repository for the first time, it's important to include the `--recursive` flag to initialize and clone the submodules:

```bash
git clone --recursive <repository-url>
```

### Initializing and Updating Submodules

If you've already cloned the repository and want to ensure that submodules are initialized and up-to-date, run the following command:

```bash
git submodule update --init --recursive
```

### Contributing to Submodules

If you're contributing to a submodule, navigate to the submodule directory, make your changes, and commit them as you would in a regular Git repository:

```bash
cd submodule-directory
# Make changes
git add .
git commit -m "Your commit message"
git push origin master  # or your branch name
``` 

### Updating Submodules in the Main Repository

To update the submodules recorded in the main repository to their latest commits, run:

``` bash
git submodule update --recursive --remote
```

### Committing Submodule Changes in the Main Repository
If you've made changes to submodules and want to include these changes in the main repository, commit the changes in the main repository:

```bash
git add .
git commit -m "Update submodule changes"
git push origin master  # or your branch name
```

### Cloning and Updating Submodules for Contributors
When contributors clone the repository, they should also initialize and update the submodules:

```bash
git clone --recursive <repository-url>
# or if already cloned
git submodule update --init --recursive
```

> **Important Notes:**
> Always ensure submodules are initialized and updated before working on the project.
> Be aware of the submodules and their status when contributing changes to the main repository.
> For more detailed information on Git submodules, refer to the [Git Submodules documentation](https://git-scm.com/docs/git-submodule).

