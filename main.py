import config
from modules.csharp_reverse_code_generator import CSharpReverseCodeGenerator


def main():
    starting_indent_level = config.starting_indent_level
    input_file = config.input_file
    output_file = config.output_file

    reverse_generator = CSharpReverseCodeGenerator

    code: str = reverse_generator.read_code_from_file(input_file)
    generator_code: list[str] = reverse_generator.generate(
        code, starting_indent_level)
    reverse_generator.output_to_file(generator_code, output_file)


if __name__ == "__main__":
    main()
