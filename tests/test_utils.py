import server.utils as u


def test_get_file_signed_path():
    file_with_sign = u.get_file_signed_path('/home/user/work/file.txt')
    assert file_with_sign == '/home/user/work/file.sig'
