from PyInstaller.utils.hooks import copy_metadata  # pylint:disable=import-error

datas = copy_metadata("flatten-dict")
