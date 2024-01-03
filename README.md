# python_project_template
This repository is a template repository for Python projects under neutrons.
After you create a new repository using this repo as template, please follow the following steps to adjust it for the new project.

1. Adjust the branch protection rules for the new repo. By default, we should protect the `main` (stable), `qa` (release candidate), and `next` (development) branches.

    1.1 Go to the `Settings` tab of the new repo.
    
    1.2 Click on `Branches` on the left side.
    
    1.3 Click on `Add rule` button.
    
    1.4 Follow the instructions from Github.

2. Change the License if MIT license is not suitable for you project. For more information about licenses, please refer to [Choose an open source license](https://choosealicense.com/).

3. Update the envrionment dependency files
    
    3.1 `environment.yml` is intended to provide the mimimum dependency for this project to run as it is.
    
    3.2 `environment_development.yml` should provide additional dependencies for development, such as testing, linting, etc.
    
    3.3 Developers should use `environment.yml` to create the development environment first, then use ``environment_development.yml` to update the environment to setup the development.

4. Adjust pre-commit configuration file, `.pre-commit-config.yaml` to enable/disable the hooks you need. For more information about pre-commit, please refer to [pre-commit](https://pre-commit.com/).

5. Having code coverage, `codecov.yaml` is **strongly recommended**, please refer to [Code coverage](https://coverage.readthedocs.io/en/coverage-5.5/) for more information.

