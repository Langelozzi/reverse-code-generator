import re
from .abstract_reverse_code_generator import AbstractReverseCodeGenerator


class CSharpReverseCodeGenerator(AbstractReverseCodeGenerator):
    def generate(code: str, starting_indent_level=0) -> str:
        return '\n'.join(CSharpReverseCodeGenerator.generate_lines(code, starting_indent_level))

    def generate_lines(code: str, starting_indent_level=0) -> list[str]:
        sb_calls = []

        lines = code.split('\n')
        for line in lines:
            indent_level = starting_indent_level

            # if line is empty or only contains whitespace
            if not line.strip():
                sb_calls.append("sb.AppendLine();")

            # determine how much to pad the line by
            padding_increment_amount = CSharpReverseCodeGenerator._count_indentation(
                line)
            indent_level += padding_increment_amount

            # fix any string issues with the line
            cleansed_line = CSharpReverseCodeGenerator._cleanse_code_line_for_sb(
                line)

            if cleansed_line:
                sb_calls.append(CSharpReverseCodeGenerator._generate_sb_call(
                    cleansed_line, indent_level))

        return sb_calls

    # Private helper methods
    def _generate_sb_call(code_line: str, indent_level: int) -> str:
        return 'sb.AppendLine($"{"".PadBy(' + f'{indent_level}' + ')}' + f'{code_line}' + '");'

    def _cleanse_code_line_for_sb(code_line: str) -> str:
        cleaned_code_line = re.sub(
            '[{}]', lambda x: '{{' if x.group() == '{' else '}}', code_line.strip())
        cleaned_code_line = re.sub('"', r'\\"', cleaned_code_line)
        return cleaned_code_line

    def _count_indentation(s):
        count = 0
        index = 0

        while index < len(s) and (s[index] == ' ' or s[index] == '\t'):
            if s[index] == ' ':
                # Count consecutive spaces
                consecutive_spaces = 0
                while index < len(s) and s[index] == ' ':
                    consecutive_spaces += 1
                    index += 1

                # Check if consecutive spaces are a multiple of 4
                count += consecutive_spaces // 4
            elif s[index] == '\t':
                # Count single tabs
                count += 1
                index += 1

        return count
