from app.services import create, list_all


def test_writing_on_file():
    create('test_author', 'test_date_post', 'test_email', 'test_title', 'test_text')

    get_last_post_test = list_all()[-1]

    expected = 'test_email'

    assert expected == get_last_post_test['email']



