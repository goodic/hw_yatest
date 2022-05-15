import pytest
from main import YaDisc

# Укажите свой токен
token = ''
ya_disc = YaDisc(token)
# Укажите имя папки которой НЕТ на диске. Тест в процессе удаляет папку!
test_folder = 'tester'


def test_create_folder():
    assert ya_disc.create_folder(test_folder).status_code == 201


def test_create_folder_fail():
    assert ya_disc.create_folder(test_folder).status_code != 201


def test_check_folder():
    assert ya_disc.check_folder(test_folder).status_code == 200


def test_delete_folder():
    assert ya_disc.delete_folder(test_folder).status_code == 204


def test_check_folder_fail():
    assert ya_disc.check_folder(test_folder).status_code != 200


def test_delete_folder_fail():
    assert ya_disc.delete_folder(test_folder).status_code != 204



