import os
import tempfile
import re
import pytest
import shutil
import file_service as fs


@pytest.fixture(scope='function')
def setup_and_cleanup():
    tmp_dir = tempfile.mkdtemp()
    yield tmp_dir
    shutil.rmtree(tmp_dir)


def test_create_file_new_name(setup_and_cleanup):
    file_name = "test_file.txt"
    expected_content = "test_content"

    file_path = os.path.join(setup_and_cleanup, file_name)
    fs.create(file_path, expected_content)

    with open(file_path, 'r') as f:
        content = f.read()

    assert expected_content == content


def test_create_file_with_existing_name(setup_and_cleanup):
    file_name = "test_file.txt"
    expected_content = "test_content"

    file_path = os.path.join(setup_and_cleanup, file_name)
    with pytest.raises(fs.CreateFileException) as cfe:
        fs.create(file_path, expected_content)
        fs.create(file_path, expected_content)

    assert 'Can not create {} cause it exists'\
        .format(file_path) == str(cfe.value)


def test_read_existing_file(setup_and_cleanup):
    file_name = "test_file.txt"
    expected_content = "test_content"
    file_path = os.path.join(setup_and_cleanup, file_name)

    with open(file_path, "w") as f:
        f.write(expected_content)

    content = fs.read(file_path)

    assert expected_content == content


def test_read_not_existing_file(setup_and_cleanup):
    file_name = "test_file.txt"

    file_path = os.path.join(setup_and_cleanup, file_name)
    with pytest.raises(fs.ReadFileException) as rfe:
        fs.read(file_path)

    assert 'Can not read {} cause No such file or directory'\
        .format(file_path) == str(rfe.value)


def test_remove_existing_file(setup_and_cleanup):
    file_name = "test_file.txt"
    expected_content = "test_content"

    file_path = os.path.join(setup_and_cleanup, file_name)

    with open(file_path, 'w') as f:
        f.write(expected_content)

    fs.remove(file_path)

    assert not os.path.exists(file_path)


def test_remove_not_existing_file(setup_and_cleanup):
    file_name = "test_file.txt"

    file_path = os.path.join(setup_and_cleanup, file_name)
    with pytest.raises(fs.RemoveFileException,
                       match=r'Can not remove .* cause .*'):
        fs.remove(file_path)


def test_get_meta_data_existing_file(setup_and_cleanup):
    file_name = "test_file.txt"
    expected_content = "test_content"

    file_path = os.path.join(setup_and_cleanup, file_name)
    with open(file_path, "w") as f:
        f.write(expected_content)

    meta_data = fs.get_meta(file_path)
    assert re.match('size: .* bytes atime: .* ctime: .* mtime: .*',
                    meta_data)


def test_get_meta_data_not_existing_file(setup_and_cleanup):
    file_name = "test_file.txt"

    file_path = os.path.join(setup_and_cleanup, file_name)
    with pytest.raises(fs.GetMetaDataException,
                       match=r'Can not get metadata .* cause .*'):
        fs.get_meta(file_path)
