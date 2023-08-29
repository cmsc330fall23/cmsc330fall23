# Project 0: Setup

Due: September 2, 2023 at 11:59 PM

This project is simply to get your system ready. Although you will "submit" this project on Gradescope, it is not counted towards your final grade.  The good-faith attempt (GFA) rule **does not apply** to this project.

**Start with the [Instructions](#instructions)!**

## Table of Contents

- [Languages and Packages](#languages-and-packages)
- [Visual Studio Code](#visual-studio-code)
  - [Extensions](#extensions)
  - [Windows VSCode Setup](#windows-vscode-setup)
- [Instructions](#instructions)
  - [Linux (NOT WSL)](#linux-not-wsl)
  - [Windows](#windows)
  - [macOS](#macos)
- [Verifying Setup](#verifying-setup)
- [Troubleshooting `gradescope-submit`](#troubleshooting-gradescope-submit)
  - [Incorrect Passwords](#incorrect-passwords)
  - [HTTP Errors](#http-errors)
  - [Failed Gradescope Compilation](#failed-gradescope-compilation)
- [Special macOS Instructions](#special-macos-instructions)
  - [Do you have a Mac running an older version of macOS?](#do-you-have-a-mac-running-an-older-version-of-macos)


## Languages and Packages

In this course, we will be programming in Python, OCaml, Rust, and Racket.  Below is a summary of the packages that need to be installed.  You do not need to use these links, they are just for reference or learning more about the languages and/or packages.  You can skip below to the instructions.

- [Git](https://git-scm.com/)
- [Python](https://www.python.org)
    - [pytest](https://docs.pytest.org/en/7.3.x)
- [OCaml](http://ocaml.org)
    - [OPAM](https://opam.ocaml.org)
    - [OUnit](https://opam.ocaml.org/packages/ounit)
    - [dune](https://opam.ocaml.org/packages/dune)
    - [utop](https://opam.ocaml.org/packages/utop)
- [Rust](https://www.rust-lang.org)
- [Racket](https://download.racket-lang.org/)

## Visual Studio Code

There is no required text editor/IDE for this course, however, instructors are familiar with [VS Code](https://code.visualstudio.com/download) so we recommend it.

### Extensions

Here is a short list of some useful extensions, feel free to explore the marketplace for more
- General Use
  - Remote - SSH
  - Remote Explorer
  - Git History
  - WSL (for windows users)
- Python
  - Python
  - Pylance
  - isort
- Ocaml
  - OCaml Platform (Make sure you read the setup instructions to install ocamllsp)
- Rust
  - rust-analyzer
- Racket
  - Magic Racket
 
### Windows VSCode setup

(Do this step after WSL is installed.)
It is recommended to use Vscode on Windows because of its integration with WSL. With the WSL extension, you can open a WSL terminal within VSCode.
1. Install the WSL extension in VSCode
2. Click the >< icon labeled `Open a remote window` located in the very bottom left corner of the screen.
3. Select "Connect to WSL" - Now VSCode will be loaded within wsl, it will now be using the linux filesystem and terminal.
4. Use `` ctrl + ` `` to open a terminal.
5. Create a directory for your 330 projects
6. Clone project 0 into that directory

For future projects you will select `open folder` to open the linux folder containing the project and edit the files, while using the wsl terminal for compilation, testing, and submitting.
  
## Instructions

First, [create your project repository](https://classroom.github.com/a/1Plgv8Fw) - you will have to do this for every project

Next, you will need to clone this repository to your local filesystem. To do this, you will first need to make a SSH key to authenticate with github. 
**If you are on windows, do the key setup and clone in WSL. NOT in Powershell**
1. Open Terminal
2. Paste `ssh-keygen -t ed25519 -C "your_email@example.com"`, substituting your github email address
3. When you're prompted to "Enter a file in which to save the key", you can **press Enter to accept the default file location**. Please note that if you created SSH keys previously, ssh-keygen may ask you to rewrite another key. If this is the case, press `ctrl + c` to cancel the generation, you already have a key.
4. At the prompt, type a secure passphrase. I prefer something short - you will be typing this a lot. A weak password is a hell of a lot better than no password.

You have now created a public/private key pair located at `~/.ssh/id_ed25519` and `~/.ssh/id_ed25519.pub`
Next we will add your public key to your github account

5. Run `cat ~/.ssh/id_ed25519.pub` and copy the public key that is displayed.
6. Go to [https://github.com/settings/keys](https://github.com/settings/keys)
7. Click "Add a new SSH key"
8. Paste in your copied public key, it should look similar to `ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIO891GqdwqFqYA3UF3JbMQeOqn6hQGa2nJERrONqvi9h aspr@umd.edu`
9. Add the key. You can now authenticate this computer to GitHub using SSH. 
 
Optional: If you dont want to type the password every time you push/pull [Use `ssh-add` to add the key to the ssh agent](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent?#adding-your-ssh-key-to-the-ssh-agent) If you are on windows, use the Linux instructions in WSL. Do not continue to the hardware security key section.


Then (after modifying the command with your username) run:
```
git clone git@github.com:cmsc330fall23/project-0-YOUR_GITHUB_USERNAME
```

The files in the `project-0` folder will be used for the [Verifying Setup](#verifying-setup) section at the bottom.

The following sections will help you install the necessary packages and programs on your operating system.  Some steps may take a long time. Please be patient.  **Read all instructions very carefully.**

The output of each command is important, so please pay careful attention to what each one prints. **Do not ignore error messages**.  We will be available in office hours to help you get set up if you run into problems.  As a general rule, no output means the command executed successfully.

**Please skip to the section below that corresponds with your operating system.**

### Windows

*This will only work on Windows 10 and newer.  If you are on an older version, you will probably need to set up a Linux VM.*
**All instructions must be executed within WSL, NOT in powershell**

1. Follow the directions [here](https://docs.microsoft.com/en-us/windows/wsl/install-win10) to install the Windows Subsystem for Linux
2. Make sure you are on WSL 2 with [this test](https://learn.microsoft.com/en-us/windows/wsl/install#check-which-version-of-wsl-you-are-running)
3. Install the basic dependencies:
    - Run `sudo apt update && sudo apt upgrade` to update your local package listing
    - Run `sudo apt install python3 python3-dev python3-pip ocaml ocaml-native-compilers camlp4 make m4 curl libssl-dev pkg-config`
4. Install some Pip packages for testing
    - Run `python3 -m pip install pytest`
5. Install and initialize the OCaml package manager
    - Run `sh <(curl -sL https://raw.githubusercontent.com/ocaml/opam/master/shell/install.sh)` (when prompted for the installation location, just hit enter to select the default)
        - Run `opam --version`.  You should be on version 2 (followed by some versions; just make sure the major version is 2).  Check out [the manual](https://opam.ocaml.org/doc/Install.html) if this is not the case. You may have to follow special directions for your particular operating system and version.
        - If you encounter any issues, or are running a different flavor of linux, check out [the manual](https://opam.ocaml.org/doc/Install.html)
    - Run `opam init --disable-sandboxing`
    - If it hangs at "Fetching repository information", press Enter. This may take a while. Please be patient
    - When prompted to modify `~/.profile` (or another file), type "n", but remember the filename
    - Open `~/.profile` (or the file mentioned above) in your text editor
    - Add the line `` eval `opam config env` `` (these are backticks, not single quotes)
    - Save the file
    - Run `source ~/.profile` (or the file you just edited)
6. Initialize OCaml
    - Run `opam update`
    - We will be using OCaml version 4.13.X. Run `ocaml -version` to check which version is currently installed
    - If you are already on 4.13.X, you can skip to #7
    - If you are on another version, run `opam switch 4.13.0`
    - If you get an error saying that switch is not currently installed, run `opam switch create 4.13.0`. (This may take a while. Please be patient)
      - While installing the new switch, if you get an error for `bwrap`, first remove the `.opam` directory using `rm -r ~/.opam` and then reinitialize opam by **disabling sanboxing** using `opam init --disable-sandboxing`. Type "n" when prompted to modify `~/.profile`. Once opam has been initialized, rerun `opam switch create 4.13.0`
    - Run `eval $(opam env)`
    - Ensure you are now on the correct version by running `ocaml -version`
7. Install OCaml packages
    - Run `opam install gradescope_submit ocamlfind ounit utop dune qcheck`
8. Install Rust
    - Go to [https://www.rust-lang.org/tools/install](https://www.rust-lang.org/tools/install) and run the installation command provided
    - If prompted, just select the defaults
    - Append `~/.cargo/bin` to the `PATH` environment variable. First, do `echo $SHELL`.
      - If `echo $SHELL` gives `/bin/zsh`, do `echo "export PATH=\"$HOME/.cargo/bin:$PATH\"" >> ~/.zshrc`
      - If `echo $SHELL` gives `/bin/bash`, do `echo "export PATH=\"$HOME/.cargo/bin:$PATH\"" >> ~/.bashrc`
9. You do not need WSL to run racket code, so you can just install Racket directly onto your windows machine
    - Go to https://download.racket-lang.org/ and download the Windows (x64, 64-bit) installer
    - Run the installer
    - Racket comes with its own IDE: DrRacket. This is the recommended way to edit Racket files, but you also may use VS Code with Racket extension(s)
  

### macOS

Check the [Special macOS Instructions](#special-macos-instructions) to check if you need to follow any special steps. Then, come back here.

1. Install the Homebrew package manager (Updated in Fall 2021)
    - Run `/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"`
2. Install python
    - Run `brew install python3`
    - Restart your terminal after the installation has completed and type `python3 --version`. Confirm it is 3.8 or higher
3. Install the basic dependencies
    - Run `brew install ocaml opam openssl`
4. Install some Pip packages for testing
    - Run `python3 -m pip install pytest`
5. Initialize the OCaml package manager
    - Run `opam init`
    - When prompted to modify `~/.zshrc` or `~/.bash_profile` (or similar file), type "y"
    - Run  `source ~/.zshrc` or `source ~/.bash_profile` (or the file mentioned above)
6. Initialize OCaml
    - Run `opam update`
    - We will be using OCaml version 4.13.X.  Run `ocaml -version` to check
      which version is currently installed
    - If you are already on 4.13.X, you can skip to #7
    - If you are on another version, run `opam switch 4.13.0`.  If you get an
      error saying that switch is not currently installed, run `opam switch
      create 4.13.0`. (This may take a while. Please be patient)
    - Run `eval $(opam env)`
    - Ensure you are now on the correct version by running `ocaml -version`
7. Install OCaml packages
    - Run `opam install gradescope_submit ocamlfind ounit utop dune qcheck`
8. Install Rust
    - Go to [https://www.rust-lang.org/tools/install](https://www.rust-lang.org/tools/install) and run the installation command provided
    - If prompted, just select the defaults
    - Append `~/.cargo/bin` to the `PATH` environment variable. First, do `echo $SHELL`.
      - If `echo $SHELL` gives `/bin/zsh`, do `echo "export PATH=\"$HOME/.cargo/bin:$PATH\"" >> ~/.zshrc`
      - If `echo $SHELL` gives `/bin/bash`, do `echo "export PATH=\"$HOME/.cargo/bin:$PATH\"" >> ~/.bashrc`
9. Install Racket
    - Go to https://download.racket-lang.org/ and download your respective installer for Racket depending on your machine. (If you have a M1/M2 chip select Apple Silicon. If you have an Intel chip select Mac OS 64-bit)
    - Run the installer
    - Racket comes with its own IDE: DrRacket. This is the recommended way to edit Racket files, but you also may use VS Code with Racket extension(s)
     
### Linux (NOT WSL)

These instructions assume you have a Debian-based system (e.g. Ubuntu).  If you have a different distribution, you will have to find and download the corresponding packages in your native package manager.  Note that the packages there may have slightly different names.

1. Firstly, install the basic dependencies:
    - Run `sudo apt update` to update your local package listing
    - Run `sudo apt install python3 python3-dev python3-pip ocaml ocaml-native-compilers camlp4 make m4 curl libssl-dev pkg-config`
2. Install some Pip packages for testing
    - Run `python3 -m pip install pytest`
3. Install and initialize the OCaml package manager
    - Run `sh <(curl -sL https://raw.githubusercontent.com/ocaml/opam/master/shell/install.sh)` (when prompted for the installation location, just hit enter to select the default)
        - Run `opam --version`.  You should be on version 2 (followed by some versions, just make sure the major version is 2).  Check out [the manual](https://opam.ocaml.org/doc/Install.html) if this is not the case, you may have to follow special directions for your particular operating system and version.
        - If you encounter any issues, or are running a different flavor of linux, check out [the manual](https://opam.ocaml.org/doc/Install.html)
    - Run `opam init`
    - If it hangs at "Fetching repository information" press Enter. (This may take a while. Please be patient)
    - When prompted to modify `~/.profile` (or another file), type "n", but remember the filename
    - Open `~/.profile` (or the file mentioned above) in your text editor
    - Add the line `` eval `opam config env` `` (these are backticks, not single quotes)
    - Save the file
    - Run `source ~/.profile` (or the file you just edited)
4. Initialize OCaml
    - Run `opam update`
    - We will be using OCaml version 4.13.X. Run `ocaml -version` to check which version is currently installed
    - If you are already on version 4.13.X, you can skip to #5
    - If you are on another version, run `opam switch 4.13.0`.  If you get an error saying that switch is not currently installed, run `opam switch create 4.13.0`. (This may take a while. Please be patient)
    - Run `eval $(opam env)`
    - Ensure you are now on the correct version by running `ocaml -version`
5. Install OCaml packages
    - Run `opam install gradescope_submit ocamlfind ounit utop dune qcheck`
6. Install Rust
    - Go to [https://www.rust-lang.org/tools/install](https://www.rust-lang.org/tools/install) and run the installation command provided
    - If prompted, just select the defaults
    - Append `~/.cargo/bin` to the `PATH` environment variable. First, do `echo $SHELL`.
      - If `echo $SHELL` gives `/bin/zsh`, do `echo "export PATH=\"$HOME/.cargo/bin:$PATH\"" >> ~/.zshrc`
      - If `echo $SHELL` gives `/bin/bash`, do `echo "export PATH=\"$HOME/.cargo/bin:$PATH\"" >> ~/.bashrc`
9. Install Racket
    - Go to https://download.racket-lang.org/ and download the Linux_x86_64 installer
    - Run the installer
    - Racket comes with its own IDE: DrRacket. This is the recommended way to edit Racket files, but you also may use VS Code with Racket extension(s)

## Link GitHub to Gradescope

**IMPORTANT**
Log into your Gradescope account and go to your account settings. Scroll down to the `Linked Accounts` section. If you do not already
have your GitHub account linked here, click the `Link a GitHub account` button and log into your GitHub account.
  
## How to Submit

Whenever you want to submit your project to Gradescope, you will need to push your latest version to your repo. Follow these steps to do so:

First, make sure all your changes are pushed to GitHub using the `git add`, `git commit`, and `git push` commands. We will teach you basic git usage in the first few days of the course, but you can refer to [these notes](https://bakalian.cs.umd.edu/assets/notes/git.pdf) for assistance. Additionally you can refer to a [testing repo](https://github.com/CliffBakalian/git-basics) Cliff made, but it's recommended you make your own.

Next, to submit your project, you can run `submit` from your project directory.

The `submit` command will pull your code from GitHub, not your local files. If you do not push your changes to GitHub, they will not be uploaded to Gradescope.

## Verifying Setup

To verify that you have the correct versions installed, run 
`pytest test/public/public.py` in this directory.  You should not get any errors.  
This will create a file called p0.report.  **Push your changes onto GitHub.** Then, submit this file by running `submit` in 
the project folder.  You will have to enter your credentials.  Alternatively, you can manually submit 
the file to Gradescope by uploading the p0.report file to the appropriate assignment.

## Troubleshooting `submit`

### Incorrect Passwords 

Make sure that the email address and password you entered is of the account
where your CMSC 330 course enrollment shows up. (If you login through "school
credentials" option and don't remember your **Gradescope** password, please
reset it.) Many people have multiple Gradescope accounts, and
we suggest you to merge them before trying to submit.

### Submission failed. Did you connect GitHub to Gradescope?

You didnt connect GitHub to Gradescope. 
Go to [Gradescope account settings](https://www.gradescope.com/account/edit), and "Link a GitHub account"


### HTTP Errors

Remove the `submit` config file by doing
`rm -r ~/.gradescope-submit`. Then, refer to the troubleshooting for incorrect
passwords and try it again.

### Failed Gradescope Compilation

You didnt push your changes to GitHub...


## Special macOS Instructions

Check to see if you're running an older version of macOS. Either click the Apple button in the menubar in the top-left and click "About This Mac", or else run `sw_vers` from the terminal. You should only need the special section if your macOS version is less than 10.15

If your macOS version is less than 10.15, follow [the directions for macOS](#macos), but with the changes listed below. Otherwise, ignore the following section.

- If you have run the special instructions in previous classes or semesters, undo by uninstalling homebrew:
  - `/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/uninstall.sh)"`
  - You will probably have leftover files in `/opt/homebrew` or `/usr/local`. We will *try* to help you delete them in OH.
- Afterwards, run `brew install` INDIVIDUALLY on each of ocaml, opam, openssl.
  - so `brew install ocaml`, `brew install opam`, etc.
