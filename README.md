# datafun-03-analytics
No idea what is happening with this project but make sure to activate the .venv and deactivate when done

The brief instructions:
1. Create Github repo on Github browser
2. Use VS code GUI top clone repo to machine
3. Create .venv (Instructions below)
4. Update requests and pip install
5. create requirements.txt and whatever else
6. commit with changes to Github


Using venv in Visual Studio Code
1
2
A virtual environment (venv) in Python is a tool that helps to keep dependencies required by different projects in separate places, by creating isolated Python environments for them. This is particularly useful when working with multiple projects that require different versions of the same package.

Creating a Virtual Environment

To create a virtual environment in Visual Studio Code (VS Code), you can use the built-in venv module. Open the terminal in VS Code and run the following command:

# macOS/Linux
python3 -m venv .venv

# Windows
python -m venv .venv
This command creates a virtual environment named .venv in your project directory
1
.

Activating the Virtual Environment

After creating the virtual environment, you need to activate it. The activation command varies depending on your operating system:

Windows (cmd.exe): .venv\Scripts\activate.bat

Windows (PowerShell): .venv\Scripts\Activate.ps1

macOS/Linux: source .venv/bin/activate

Once activated, your terminal prompt will change to indicate that you are now working within the virtual environment
2
.

Selecting the Interpreter in VS Code

To ensure that VS Code uses the virtual environment's Python interpreter, you need to select it. Open the Command Palette (Ctrl+Shift+P) and run the Python: Select Interpreter command. Choose the interpreter located in the .venv directory
1
.

Installing Packages

With the virtual environment activated, you can now install packages using pip. For example, to install the requests package, run:

pip install requests
The installed packages will be isolated within the virtual environment and will not affect other projects or the global Python installation
2
.

Deactivating the Virtual Environment

When you are done working on your project, you can deactivate the virtual environment by running:

deactivate
This will revert your terminal to the global Python environment
2
.