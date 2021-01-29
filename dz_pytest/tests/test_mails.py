import pytest

from common.add_func import check_mail,check_bad_mail


class TestMail:

    @pytest.mark.parametrize('mail', ['test@test.ru', 'w@w.com', '123QWE@mmm.mmm'])
    def test_correct_mail(self, mail, log_file):
        assert check_mail(log_file, mail)

    @pytest.mark.parametrize('mail', ['test@test.', 'w@', '@tt'])
    def test_incorrect_mail(self, mail, log_file):
        assert check_bad_mail(log_file, mail)
