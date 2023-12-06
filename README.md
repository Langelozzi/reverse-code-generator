# Reverse Code Generator

## Table of Contents

- [Description](#description)
- [Installation](#installation)
- [Usage](#usage)
- [License](#license)

## Description

The next generation of programmers are starting to leverage code generation systems. This project aims to speed up the development of the code generators by converting the end product code into a set of strings that can be used in a code generator.


## Installation

To install the project:

- Clone this repository: `git clone https://github.com/Langelozzi/reverse-code-generator.git`
- Install the required dependencies: `pip install -r requirements.txt`

## Usage

To use the generator, follow these steps:

1. Open the `config.py` file and set the config variables accordingly
    - `starting_indent_level`: Allows you to choose how many indentations the furthest left code should have. (Default `0`)
    - `input_file`: The file path of the input file, containing the end product code. (Default: `input.txt`)
    - `output_file`: The file path of the output file, where the generator code will be written to. (Default: `output.txt`)
2. Copy your end product code into the input file. Ensure that it is formatted how you want the end product to be formatted
3. Run the main script: `python main.py`
4. Open the output file and the generator code will have been written to the file

## License

- This project is licensed under the MIT License - see the [LICENSE] file for details