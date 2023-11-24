# From Policy to Plate

## Overview

A web-based Flask prediction tool to predict the level of food insecurity in a given country based on the quality of its governance. Created for SUTD's 2023 Term 3 2D Project.

## Installation

To install and run the app, follow these steps:

1. Clone the repository:

    ```shell
    git clone https://github.com/rappleit/term3-2d-webapp.git
    cd project
    ```

2. First make sure that the `pipenv` package is installed.

    ```shell
    python -m pip install --user pipenv
    ```


3. Install dependencies:

    ```shell
    pip install -r requirements.txt
    ```

4. Activate the virtualenv
    ```shell
    python -m pipenv shell
    ```

## Usage

To start the app, run the following command:

```shell
flask run
```

To exit the app, run the following command:
```shell
exit
```

Folder Structure
The project structure is as follows:

```
/project
    ├── app
    │   ├── static
    │   ├── templates
    │   ├── __init__.py
    │   ├── middleware.py
    │   └── routes.py
    ├── predMod.pkl
    ├── config.py
    ├── requirements.txt
    └── application.py
```