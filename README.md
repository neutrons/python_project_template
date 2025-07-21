# Python Project Template (examplepyapp)

This repository contains a modern Python project managed entirely with [Pixi](https://pixi.sh/), a reproducible and declarative environment manager.
All build and packaging metadata is consolidated in a single `pyproject.toml` file, following modern Python packaging standards.

## Getting Started

This project uses [Pixi](https://pixi.sh/) as the single tool for managing environments, dependencies, packaging, and task execution.

### 1. Install Pixi

Follow the installation instructions from the [Pixi website](https://pixi.sh/), or use:

```bash
curl -fsSL https://pixi.sh/install.sh | bash
```

### 2. Set Up the Environment

Run the following command to create and activate the project environment with all dependencies:

```bash
pixi install
```

### 3. Explore Available Tasks

Use the following command to list all project-defined tasks:

```bash
pixi run
```

Example tasks:

- `build-pypi`: build the PyPI wheel
- `build-conda`: build the Conda package
- `test`: run the test suite
- `conda-publish`, `pypi-publish`: publish the built artifacts
- `clean-*`: clean build artifacts

### 4. Development Workflow

Activate the Pixi environment:

```bash
pixi shell
```

Then, for development:

- Run tests: `pixi run test`
- Run linting: `ruff check .`
- Perform editable install: `pip install --no-deps -e .`

This ensures your environment remains clean and all tasks are reproducible.

## Project Overview

- 📦 **Unified packaging** for both PyPI and Conda via [`pixi build`](https://prefix.dev/docs/pixi/pixi-build/)
- 🐍 **Python 3.11+** compatibility
- ⚙️ **Versioning** handled by [`versioningit`](https://github.com/jwodder/versioningit), derived from Git tags
- 🧪 **Testing** with `pytest` and code coverage reporting
- 🧼 **Linting & formatting** with [`ruff`](https://docs.astral.sh/ruff/)
- 🚀 **Task automation** via `pixi run`
- 🔁 Supports CLI and optional GUI through modular structure in `src/packagenamepy/`

## Codebase Adjustments

1.  Adjust the branch protection rules for the new repo. By default, we should protect the `main` (stable), `qa` (release candidate), and `next` (development) branches.

    1.1 Go to the `Settings` tab of the new repo.

    1.2 Click on `Branches` on the left side.

    1.3 Click on `Add rule` button.

    1.4 Follow the instructions from Github.

1.  Change the License if MIT license is not suitable for you project. For more information about licenses, please
    refer to [Choose an open source license](https://choosealicense.com/).

1.  Adjust pre-commit configuration file, `.pre-commit-config.yaml` to enable/disable the hooks you need. For more information about pre-commit, please refer to [pre-commit](https://pre-commit.com/).

1.  Having code coverage, `codecov.yaml` is **strongly recommended**, please refer to [Code coverage](https://coverage.readthedocs.io/en/coverage-5.5/) for more information.

1.  Adjust the GitHub Actions workflows for CI/CD to align with Pixi-only packaging. For more information about GitHub Actions, please refer to [GitHub Actions](https://docs.github.com/en/actions).

    - Ensure that `.github/workflows/package.yaml` uses only `pixi run` commands for all build and publish steps.

    - Validate that the following Pixi tasks are correctly invoked:

      - `pixi run pypi-build`
      - `pixi run pypi-publish`
      - `pixi run conda-build`
      - `pixi run conda-publish`

    - Remove or disable any steps using `conda-build`, `python setup.py`, or `pip install .`.

1.  The legacy `conda.recipe/meta.yaml` is no longer needed since Conda packaging is now handled via Pixi and `pyproject.toml`.

    - You may delete the `conda.recipe` folder entirely, unless it's still needed for backward compatibility with older workflows.

1.  Adjust `pyproject.toml` to match your project. For more information about `pyproject.toml`,
    please refer to [pyproject.toml](https://www.python.org/dev/peps/pep-0518/).

    - Specify package name at: pyproject.toml#L5

    - Specify package description at: pyproject.toml#L6

    - Specify any terminal entry points (terminal commands) at: pyproject.toml#30.

1.  Adjust files for pixi

    - After updating your environment file, make sure to run `pixi install` and commit the updated lock file.

    - Specify package name at: pyproject.toml#L65

      > In the example, invoking `packagename-cli` in a terminal is equivalent to running the python script `from packagenamepy.packagename import main; main()`

    - Projects will use a single `pyproject.toml` file to manage all the project metadata, including the project name, version, author, license, etc.

    - Python has moved away from `setup.cfg`/`setup.py`, and we would like to follow the trend for our new projects.

1.  Specify package name at src/packagenamepy

1.  Specify package name at: src/packagenamepy/packagename.py

1.  If a GUI isn't used, delete the MVP structure at src/packagenamepy:

    - mainwindow.py
    - home/
    - help/

1.  Clear the content of this file and add your own README.md as the project README file.
    We recommend putting badges of the project status at the top of the README file.
    For more information about badges, please refer to [shields.io](https://shields.io/).

## Repository Adjustments

### Add an access token to anaconda

Here we assume your intent is to upload the conda package to the [anaconda.org/neutrons](https://anaconda.org/neutrons) organization.
An administrator of `anaconda.org/neutrons` must create an access token for your repository in the [access settings](https://anaconda.org/neutrons/settings/access).

After created, the token must be stored in a `repository secret`:

1. Navigate to the main page of the repository on GitHub.com.
1. Click on the "Settings" tab.
1. In the left sidebar, navigate to the "Security" section and select "Secrets and variables" followed by "Actions".
1. Click on the "New repository secret" button.
1. Enter `ANACONDA_TOKEN` for the secret name
1. Paste the Anaconda access token
1. Click on the "Add secret" button
1. Test the setup by creating a release candidate tag,
   which will result in a package built and uploaded to `https://anaconda.org/neutrons/mypackagename`

### Add an access token to codecov

Follow the instructions in the [Confluence page](https://ornl-neutrons.atlassian.net/wiki/spaces/NDPD/pages/103546883/Coverage+reports)
to create the access token.

## Build & Publish Packages

Both PyPI and Conda packages are supported. All build and publishing steps are defined in Pixi tasks.

Note that if your project is not being built and published to PyPI, you can safely modify the `pyproject.toml`
to remove any pixi tasks related to PyPI, and the `hatch` dependency.

Similarly, if you are not publishing to conda, you can remove any related dependencies, configurations, and tasks.

### Publish to PyPI

1. Ensure you have access to the project on PyPI.
2. Clean working directory: `git status` should be clean.
3. Run the Pixi task to build the wheel:

   ```bash
   pixi run pypi-build
   ```

4. Check the wheel for issues manually:

   ```bash
   twine check dist/*
   ```

5. Upload to TestPyPI:

   ```bash
   pixi run pypi-publish-test
   ```

   Ensure your `~/.pypirc` contains the correct token:

   ```ini
   [distutils]
   index-servers = pypi testpypi

   [testpypi]
   repository = https://test.pypi.org/legacy/
   username = __token__
   password = YOUR_TESTPYPI_TOKEN
   ```

6. Install from TestPyPI to verify:

   ```bash
   pip install --index-url https://test.pypi.org/simple/ examplepyapp
   ```

7. When ready, trigger the GitHub Action (`package.yaml`) to upload to PyPI.

### Publish to Anaconda (Conda)

1. Ensure the target channel is correct in `.github/workflows/package.yaml`.
2. Run the Pixi build:

   ```bash
   pixi run conda-build
   ```

   This creates a `.conda` package in the project root.

3. Publish using:

   ```bash
   pixi run conda-publish
   ```

   Ensure the `ANACONDA_TOKEN` secret is configured in GitHub for CI/CD to work.

## Development environment setup

### Build development environment

1. By default, we recommend using `pixi install` to set up the development environment.
   This will create a virtual environment in the `.pixi` directory at the root of the repository.
1. If you prefer to use a detached environment, set the `detached-environments` option to `true` in `.pixi/config.toml`:

   ```bash
   pixi config set detached-environments true
   ```

1. If you want to keep your environment between sessions, add the following line to your `.bashrc` or `.bash_profile`:

   ```bash
   export PIXI_CACHE_DIR="$HOME/.pixi/cache"
   ```

1. After setting up the environment, you can activate it with:

   ```bash
   pixi shell
   ```

1. If you are using VSCode as your IDE, we recommend to start code with `pixi run code .` to ensure the correct environment is inherited by the IDE.
   Alternatively, you can specify the Python interpreter path using `Ctrl + Shift + P` and searching for "Python: Select Interpreter",
   or manually editing the `.vscode/settings.json` file to set the Python interpreter path:

   ```json
   {
     "python.pythonPath": ".pixi/venv/bin/python"
   }
   ```

### Auditing dependencies

The tool [`pip-audit`](https://github.com/pypa/pip-audit) allows for checking dependencies for versions with known weaknesses or vulnerabilities as registered in [open source vulnerabilities database (osv)](https://osv.dev/).
This is provided as the task `audit-deps` which will verify that there are no known python dependencies in the pixi environment.

**Finding source of issue:** This is an outdated example used to demonstrate how to suppress vulnerabilities.
Assume that `pixi run audit-deps` returns a message that there is a issue [PYSEC-2025-61](https://osv.dev/vulnerability/PYSEC-2025-61) that is associated with pillow v11.2.0.
Since this is an indirect dependency, one can use

```bash
$ pixi tree --invert pillow

  pillow 11.2.0
  └── anaconda-client 1.13.0
```

to find out that this is included by the anaconda-client package which is also not a runtime dependency.
This can be ignored.

**Ignoring a vulnerability:** Unfortunately, `pip-audit` does not have a configuration file that allows for ignoring issues.
This is done with a suppression in the `pyproject.toml` by modifying the task.

```
# ignore pillow error because it is only used by anaconda-client v1.13.0
audit-deps = { cmd = "pip-audit --local -s osv --ignore-vuln=PYSEC-2025-61" }
```

The comment is added to save future developers effort in confirming the issue.
At a later date, the team should periodically remove the suppression and confirm the issue persists or remove the suppression permanently.

## Pixi

Pixi is the single tool used to manage environments, dependencies, packaging, and task execution for this project.
All metadata is centralized in `pyproject.toml`, eliminating the need for `environment.yml` or `meta.yaml`.

### How to use Pixi

1. Install `pixi` by running `curl -fsSL https://pixi.sh/install.sh | bash`
   (or following the instruction on the [official website](https://pixi.sh/))
2. Run `pixi install` to create the virtual environments.
   By default, `pixi` creates a virtual environment in the `.pixi` directory at the root of the repository.
3. Run `pixi shell` to start a shell with an activate environment, and type `exit` to exit the shell.

Adjust the tasks in `pyproject.toml` to match your project's needs.
Detailed instructions on adding tasks can be found in the [official documentation](https://pixi.sh/latest/features/tasks/).

You can use `pixi task list` to see available tasks and their descriptions.

```bash
$> pixi task list
Tasks that can run on this machine:
-----------------------------------
Task                 Description
audit-deps           Audit the package dependencies for vulnerabilities
build-docs           Build documentation
conda-build          Build the conda package
pypi-build           Build the package for PyPI
test                 Run the test suite
```

Use `pixi run <task-name>` to run a specific task (note: if the selected task has dependencies, they will be run first).
You don't need to run `pixi shell` to run tasks, as `pixi run` will automatically activate the environment for you.

## Activating the Environment Automatically

Install [direnv](https://pixi.sh/latest/integration/third_party/direnv/)
and create a file `.envrc` in the project root directory with the following content:

```bash
watch_file pixi.lock
eval "$(pixi shell-hook)"
unset PS1
```

- The line watch_file pixi.lock directs direnv to re-evaluate the environment whenever the file `pixi.lock `changes.
- The line `unset PS1` prevents direnv from reporting on a nagging, albeit harmless, error message.

Then in the terminal, run `direnv allow`.
Now direnv activates the environment when you enter the project directory,
and deactivates it when you leave the directory.


### Known issues

On SNS Analysis systems, the `pixi run conda-build` task will fail due to `sqlite3` file locking issue.
This is most likely due to the user directory being a shared mount,
which interferes with `pixi` and `conda` environment locking.
