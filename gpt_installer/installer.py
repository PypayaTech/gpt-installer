import os
import subprocess
from gpt_installer.utils import load_text_file, check_operating_system, get_openai_api_reply


class Installer:
    def __init__(self):
        self._extract_installation_instructions_prompt = load_text_file("prompts/extract_installation_instructions.txt")
        self._generate_installation_script_prompt = load_text_file("prompts/generate_installation_script.txt")
        self._operating_system = check_operating_system()
        self._language = "batch" if self._operating_system == "Windows" else "bash"

    def extract_installation_instructions(self, readme_content_or_path):
        if os.path.isfile(readme_content_or_path):
            readme_content = load_text_file(readme_content_or_path)
        else:
            readme_content = readme_content_or_path
        self._extract_installation_instructions_prompt = self._extract_installation_instructions_prompt.replace(
            "{MANUAL}", readme_content)
        return get_openai_api_reply(
            [{"role": "system", "content": self._extract_installation_instructions_prompt}])

    def generate_installation_script(self, installation_instructions):
        self._generate_installation_script_prompt = self._generate_installation_script_prompt.replace("{BASH_OR_BATCH}",
                                                                                                      self._language)
        self._generate_installation_script_prompt = self._generate_installation_script_prompt.replace(
            "{INSTALLATION_INSTRUCTIONS}", installation_instructions)
        return get_openai_api_reply(
            [{"role": "system", "content": self._generate_installation_script_prompt}])

    @staticmethod
    def run_installation_script(installation_script):
        subprocess.run(installation_script, shell=True)
