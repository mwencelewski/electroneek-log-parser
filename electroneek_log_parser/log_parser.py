import re
from abc import ABC, abstractmethod


class LogParsingStrategy(ABC):
    @abstractmethod
    def parse_log(self, log_text):
        pass


class ReplaceRegexStrategy(LogParsingStrategy):

    def __init__(self, regex_pattern, replacement):
        self.regex_pattern = regex_pattern
        self.replacement = replacement

    def parse_log(self, log_text):
        text = re.sub(self.regex_pattern, "", log_text, count=1)
        text = re.sub(self.regex_pattern, ",", text)
        return text

class LogParser:

    def __init__(self, strategy):
        self.strategy = strategy

    def set_strategy(self, strategy):
        self.strategy = strategy

    def parse_log_file(self, log_file_path):
        with open(log_file_path, 'r') as file:
            log_text = file.read()
            parsed_result = self.strategy.parse_log(log_text)
            return parsed_result

    def save_parsed_file(self, path="./"):
        pass

if __name__ == "__main__":

    log_parser = LogParser(ReplaceRegexStrategy(
        replacement="", regex_pattern=r"^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}.\d{3}Z,"))
    parsed_logs = log_parser.parse_log_file(
        r"/mnt/c/Bots/LogParser/autologs_ORCHTraining - Bot4_2023-06-22_11-02-01.txt")

    with open("./result.json", 'w') as result_file:
        result_file.writelines(parsed_logs)
