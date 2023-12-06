from abc import ABC, abstractmethod


class AbstractReverseCodeGenerator(ABC):
    def read_code_from_file(input_file: str) -> str:
        with open(input_file, 'r') as f:
            return f.read()

    def output_to_file(code: str, output_file: str):
        with open(output_file, 'w') as f:
            f.write(code)

    @abstractmethod
    def generate(code: str, starting_indent_level=0) -> str:
        pass
