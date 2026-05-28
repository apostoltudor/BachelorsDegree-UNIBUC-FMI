# Assembly Runner

A seamless assembly runner that simplifies running `.s` and `.asm` x86 assembly files within a Docker container. With this tool, you can quickly execute x86 assembly code without needing to manually handle dependencies or setups.

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Dependencies](#dependencies)
- [Examples](#examples)
- [Contributors](#contributors)
- [License](#license)

## Introduction

This project provides a simple interface to run x86 assembly code using Docker containers. By executing a single command, you can compile and run `.s` or `.asm` files. The tool automatically selects the latest assembly file in the current directory if no file is specified.

## Features

- Run `.s` and `.asm` assembly files within a Docker container.
- Auto-select the latest assembly file if no file is specified.
- Easy-to-use command structure for running code.
- Supports running any valid assembly code without manual setup.

## Installation

1. Ensure you have Docker installed on your system.
2. Clone this repository to your local machine:  
   git clone <repository-url>
3. Make sure the `run` script has executable permissions:  
   chmod +x run

## Usage

To run an assembly file, use the following command:
```bash
./run [program_name]
```

The `program_name` argument is optional and specifies which `.s` or `.asm` file to run.  
If `program_name` is not provided, the script will automatically select the latest `.s` or `.asm` file in the current directory.

## Dependencies

Docker is required to run the assembly code in a containerized environment. Ensure Docker is installed and running on your system.

To install all dependencies you can to run
```bash
./run init
```

## Examples

### Running a Specific File

If you have a file named `hello.s` in your directory, you can run it with the following command: 
```bash 
./run hello.s
```

### Running the Latest Assembly File

If you have multiple `.s` and `.asm` files in your directory, you can let the script choose the most recent one by running:
```bash
./run
```

### Debugging with run command and VSCode
If you have a file named `hello.asm` in your directory, you can run it with the following command: 
```bash 
./run gdb hello.asm
```

Then run the **docker-debug** configuration in order to debug from VSCode. Make sure you either use this project in VSCode or add the **.vscode** directory in your project.


### Debugging with VSCode only
Start the **vscode-debug** configuration from VSCode. Once the debugger is connected, run the task **docker-attach**.

### Debugging remotely via gdb
If you have a file named `hello.asm` in your directory, you can run it with the following command: 
```bash 
./run gdb hello.asm
```

Run from a different console 
```bash
gdb executable
```

Inside gdb execute
```
target remote 0.0.0.0:4444
```

## Contributors

- **Radu Buzas** - Initial work
- **Florin Dinu** - VSCode and remote debug support

## License

This project is licensed under the MIT License. See the LICENSE file for details.
