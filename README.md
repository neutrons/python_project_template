# python_project_template

This repository is a template repository for Python projects under neutrons.
After you create a new repository using this repo as template, please follow the following steps to adjust it for the new project.

## Codebase Adjustments

1. Adjust the branch protection rules for the new repo. By default, we should protect the `main` (stable), `qa` (release candidate), and `next` (development) branches.

    1.1 Go to the `Settings` tab of the new repo.

    1.2 Click on `Branches` on the left side.

    1.3 Click on `Add rule` button.

    1.4 Follow the instructions from Github.

1. Change the License if MIT license is not suitable for you project. For more information about licenses, please
refer to [Choose an open source license](https://choosealicense.com/).

1. Update the environment dependency file `environment.yml`, which contain both runtime and development dependencies.
For more information about conda environment file, please refer to [Conda environment file](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html#creating-an-environment-file-manually).

    3.1 Specify environment 'name' field to match package name

    3.2 We strongly recommended using a single `environment.yml` file to manage all the dependencies, including the runtime and development dependencies.

    3.3 Please add comments to the `environment.yml` file to explain the dependencies.

    3.4 Please prune the dependencies to the minimum when possible, we would like the solver to figure out the dependency tree for us.

1. Adjust pre-commit configuration file, `.pre-commit-config.yaml` to enable/disable the hooks you need. For more information about pre-commit, please refer to [pre-commit](https://pre-commit.com/).

1. Having code coverage, `codecov.yaml` is **strongly recommended**, please refer to [Code coverage](https://coverage.readthedocs.io/en/coverage-5.5/) for more information.

1. Adjust the demo Github action yaml files for CI/CD. For more information about Github action, please refer to [Github action](https://docs.github.com/en/actions).

    6.1 Specify package name at: .github/workflows/package.yml#L34

    6.2 Specify package name at: .github/workflows/package.yml#L46

1. Adjust the conda recipe, `conda-recipe/meta.yaml` to provide the meta information for the conda package. For more information about conda recipe, please refer to [Conda build](https://docs.conda.io/projects/conda-build/en/latest/).

    7.1 Specify package name at: conda.recipe/meta.yaml#L15

    7.2 Update license family, if necessary: conda.recipe/meta.yaml#L42

1. Adjust `pyproject.toml` to match your project. For more information about `pyproject.toml`,
please refer to [pyproject.toml](https://www.python.org/dev/peps/pep-0518/).

    8.1 Specify package name at: pyproject.toml#L2

    8.2 Specify package description at: pyproject.toml#L3

    8.3 Specify package name at: pyproject.toml#L58

    8.4 Specify any terminal entry points (terminal commands) at: pyproject.toml#68.

1. Adjust files for pixi

    9.1 After updating your environment file, make sure to run `pixi install` and commit the updated lock file.

    9.2 Specify package name at: pyproject.toml#L116

    9.3 Specify package name at: unittest.yml#74

In the example, invoking `packagename-cli` in a terminal is equivalent to running the python script `from packagenamepy.packagename.import main; main()`

    8.5 Projects will use a  single `pyproject.toml` file to manage all the project metadata, including the project name, version, author, license, etc.

    8.6 Python has moved away from `setup.cfg`/`setup.py`, and we would like to follow the trend for our new projects.

1. Specify package name at  src/packagenamepy

1. Specify package name at: src/packagenamepy/packagename.py

1. If a GUI isn't used, delete the MVP structure at src/packagenamepy:
    11.1: mainwindow.py
    11.2: home/
    11.3: help/

1. Clear the content of this file and add your own README.md as the project README file.
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

## Packaging building instructions

The default package publishing service is anaconda.
However, we also support PyPI publishing as well.

### Instruction for publish to PyPI

1. Make sure you have the correct access to the project on PyPI.
1. Make sure `git status` returns a clean state.
1. At the root of the repo, use `python -m build` to generate the wheel.
1. Check the wheel with `twine check dist/*`, everything should pass before we move to next step.
1. When doing manual upload test, make sure to use testpypi instead of pypi.
1. Use `twine upload --repository testpypi dist/*` to upload to testpypi, you will need to specify the testpipy url in your `~/.pypirc`, i.e.

``````
[distutils]
index-servers = pypi, testpypi

[testpypi]
    repository = https://test.pypi.org/legacy/
    username = __token__
    password = YOUR_TESTPYPI_TOKEN

``````

1. Test the package on testpypi with `pip install --index-url https://test.pypi.org/simple/ mypackagename`.
1. If everything is good, use the Github workflow, `package.yml` to trigger the publishing to PyPI.

### Instruction for publish to Anaconda

Publishing to Anaconda is handled via workflow, `package.yml`.
If your target channel is not `neutrons`, make sure change it in the `package_pixi.yml` file.

## Development environment setup

### Build development environment

1. By default, we recommend providing a single `environment.yml` that covers all necessary packages for development.
2. The runtime dependency should be in `meta.yaml` for anaconda packaging, and `pyproject.toml` for PyPI publishing.
3. When performing editable install for your feature branch, make sure to use `pip install --no-deps -e .` to ensure that `pip` does not install additional packages from `pyproject.toml` into development environment by accident.

## Pixi

Pixi is a tool that helps to manage the project's dependencies and environment.
Currently this template repo have both conventional `conda` based environment (`environment.yml` and `conda.recipe/meta.yaml`) and `pixi` based environment (`pyproject.toml`).

### How to use Pixi

1. Install `pixi` by running `curl -fsSL https://pixi.sh/install.sh | bash` (or following the instruction on the [official website](https://pixi.sh/))
1. If planning to build the conda package locally, you need to configure the `pixi` to use the `detached-environments` as `conda build` will fail if the environment is in the source tree (which `pixi` does by default).
    2.1. Run `pixi config set detached-environments true`
    2.2. Make sure to commit the config file `.pixi/config.toml` to the repository (it is ignored by default).
1. Run `pixi install` to install the dependencies.
1. Adjust the tasks in `pyproject.toml` to match your project's needs.
   3.1. Detailed instructions on adding tasks can be found in the [official documentation](https://pixi.sh/latest/features/tasks/).
   3.2. You can use `pixi run` to see available tasks, and use `pixi run <task-name>` to run a specific task (note: if the selected task has dependencies, they will be run first).

    ```bash
    ❯ pixi run

    Available tasks:
            build-conda
            build-docs
            build-pypi
            clean-all
            clean-conda
            clean-docs
            clean-pypi
            publish-conda
            publish-pypi
            test
            verify-conda
    ```

1. Remember to remove the GitHub actions that still use `conda` actions.

### Pixi environment location

By default, `pixi` will create a virtual environment in the `.pixi` directory at the root of the repository.
However, when setting `detached-environments` to `true`, `pixi` will create the virtual environment in the cache directory (see [official documentation](https://pixi.sh/latest/features/environment/#caching-packages) for more information).
If you want to keep your environment between sessions, you should add the following lines to your `.bashrc` or `.bash_profile`:

```bash
export PIXI_CACHE_DIR="$HOME/.pixi/cache"
```

### Known issues

On SNS Analysis systems, the `pixi run build-conda` task will fail due to `sqlite3` file locking issue.
This is most likely due to the user directory being a shared mount, which interfering with `pixi` and `conda` environment locking.
