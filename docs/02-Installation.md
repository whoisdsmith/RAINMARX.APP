# Installation

## Prerequisites

Before you begin, ensure you have the following software installed on your system:

- **Python 3.6 or higher**: Python is the programming language used to develop RAINMARX. You can download and install the latest version of Python from the [official Python website](https://www.python.org/downloads/). Make sure to add Python to your system's PATH during installation.
- **Git**: Git is a version control system that allows you to clone the RAINMARX repository. You can download and install Git from the [official Git website](https://git-scm.com/downloads).

To verify that Python and Git are installed, open a terminal (or command prompt) and run the following commands:

```bash
python --version
git --version
```

You should see output indicating the versions of Python and Git installed on your system.

## Steps

Follow these steps to install RAINMARX:

### 1\. Clone the Repository

First, you need to clone the RAINMARX repository from GitHub to your local machine. Open a terminal (or command prompt) and navigate to the directory where you want to clone the repository. Then, run the following command:

```bash
git clone https://github.com/yourusername/RAINMARX.git
```

Replace `yourusername` with the actual GitHub username where the RAINMARX repository is hosted. This command will create a new directory named `RAINMARX` and download all the project files into it.

Next, navigate into the newly created directory:

```bash
cd RAINMARX
```

### 2\. Create a Virtual Environment (Optional but Recommended)

It is a good practice to create a virtual environment for your Python projects. A virtual environment allows you to manage dependencies separately from the system-wide Python installation, preventing potential conflicts between packages.

To create a virtual environment, run the following commands:

```bash
python -m venv env
```

This command creates a virtual environment named `env` in the current directory. To activate the virtual environment, use the appropriate command for your operating system:

- **Windows**:

  ```bash
  .\env\Scripts\activate
  ```

- **macOS and Linux**:

  ```bash
  source env/bin/activate
  ```

After activating the virtual environment, you should see `(env)` prefixed to your command prompt, indicating that the virtual environment is active.

### 3\. Install Dependencies

RAINMARX relies on several external Python packages, which are listed in the `requirements.txt` file. To install these dependencies, run the following command:

```bash
pip install -r requirements.txt
```

This command will read the `requirements.txt` file and install all the packages listed in it. Ensure you have an active internet connection as the packages will be downloaded from the Python Package Index (PyPI).

### 4\. Verify the Installation

To verify that RAINMARX is installed correctly, you can run the main script and check if the CLI application starts without errors:

```bash
python RAINMARX.py
```

You should see the ASCII art title "RAINMARX" and the main menu with various options to interact with your Raindrop.io account.

### 5\. Deactivate the Virtual Environment

Once you have verified the installation, you can deactivate the virtual environment by running:

```bash
deactivate
```

This will return your terminal to the system-wide Python environment. You can reactivate the virtual environment anytime you want to use RAINMARX by following the activation steps mentioned earlier.

### Additional Tips

- **Updating Dependencies**: If there are updates to the dependencies, you can update your local environment by running `pip install --upgrade -r requirements.txt`.
- **Removing the Virtual Environment**: If you no longer need the virtual environment, you can remove it by deleting the `env` directory.


---

[<- Previous](01-Introduction.md) | [Next ->](03-Configuration.md)
