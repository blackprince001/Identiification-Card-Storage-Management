# Identification Card Storage Manager

## Quick Start

- Clone the repository

    ```bash
    git clone https://github.com/blackprince001/Identification-Card-Storage-Management
    ```

- Move into the directory

    ```bash
    cd Identification-Card-Storage-Management
    ```

- Set up a virtual environment with Venv on Vscode or any python environment manager you have installed, and it will automatically install the dependencies. This project uses pipenv to handle dependency installs and virtual environments.

- To simply install project dependencies, run the command below.

  ```bash
  pipenv sync
  ```

- Set up a dev environment by running the command to install dependencies to work on the project. Do note that the make command is already dependent on the one above. So if you use this command, there will be no need for you to run the prev one.
  
  ```bash
  pipenv sync --dev
  ```

  while you're in `/Identification-Card-Storage-Management`

## Testing

To run the tests in the project:

- You need to install the dev packages:

  ```bash
  pipenv install --dev
  ```
  
- Run pytest make commands highlighted above
