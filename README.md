# python_project_template
This repository is a template repository for Python projects under neutrons.
After you create a new repository using this repo as template, please follow the following steps to adjust it for the new project.

1. Adjust the branch protection rules for the new repo. By default, we should protect the `main` (stable), `qa` (release candidate), and `next` (development) branches.

    1.1 Go to the `Settings` tab of the new repo.

    1.2 Click on `Branches` on the left side.

    1.3 Click on `Add rule` button.

    1.4 Follow the instructions from Github.

2. Change the License if MIT license is not suitable for you project. For more information about licenses, please refer to [Choose an open source license](https://choosealicense.com/).

3. Update the envrionment dependency file `environment.yml`, which contain both runtime and development dependencies. For more information about conda environment file, please refer to [Conda environment file](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html#creating-an-environment-file-manually).

    3.1 We strongly recommended using a single `environment.yml` file to manage all the dependencies, including the runtime and development dependencies.
    3.2 Please add comments to the `environment.yml` file to explain the dependencies.
    3.3 Please prune the dependencies to the minimum when possible, we would like the solver to figure out the dependency tree for us.


4. Adjust pre-commit configuration file, `.pre-commit-config.yaml` to enable/disable the hooks you need. For more information about pre-commit, please refer to [pre-commit](https://pre-commit.com/).

5. Having code coverage, `codecov.yaml` is **strongly recommended**, please refer to [Code coverage](https://coverage.readthedocs.io/en/coverage-5.5/) for more information.

6. Adjust the demo Github action yaml files for CI/CD. For more information about Github action, please refer to [Github action](https://docs.github.com/en/actions).

7. Adjust the conda recipe, `conda-recipe/meta.yaml` to provide the meta information for the conda package. For more information about conda recipe, please refer to [Conda build](https://docs.conda.io/projects/conda-build/en/latest/).

8. Adjust `pyproject.toml` to match your project. For more information about `pyproject.toml`, please refer to [pyproject.toml](https://www.python.org/dev/peps/pep-0518/).

    8.1 We strongly recommended using a single `pyproject.toml` file to manage all the project metadata, including the project name, version, author, license, etc.
    8.2 Python is moving away from `setup.cfg`/`setup.py`, and we would like to follow the trend for our new projects.

9. Adjust `__main__.py` if the software need to have a module level entrance. For pure Python library, please delete `__main__.py`.

10. Clear the content of this file and add your own README.md as the project README file. We recommend putting badges of the project status at the top of the README file. For more information about badges, please refer to [shields.io](https://shields.io/).
