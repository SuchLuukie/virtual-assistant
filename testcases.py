from setuptools import Command
from command_processing_module import CommandProcessingModule
import json

settings = json.load(open("settings/settings.json"))
cpm = CommandProcessingModule(None, settings)

testCases = [
    {
        "input": "Athena what's the weather",
        "expected_result": cpm.commands_module.weather_forecast()
    },
    {
        "input": "Athena what is 10 + 20",
        "expected_result": 30
    },
    {
        "input": "hello Athena",
        "expected_result": cpm.commands_module.greeting()
    }
]

index = 0
for testCase in testCases:
    index += 1

    result = cpm.process_command(testCase["input"].lower())
    if result == testCase["expected_result"]:
        print(f"[!] TestCase {index} Succesful")
    
    else:
        print(f"[!] TestCase {index} Unsuccesful, result: {result}")
