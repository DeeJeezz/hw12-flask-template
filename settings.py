from os.path import isfile
import json

SETTINGS_FILE_PATH = 'project_settings.json'

# Установили значение по умолчанию, если файла не оказалось.
CONFIG = {
    'DEBUG': True,
    'SOME_VARIABLE': '',
}

# Если файл есть - перезаписали настройки.
if isfile(SETTINGS_FILE_PATH):
    with open(SETTINGS_FILE_PATH) as f:
        CONFIG = json.load(f)
