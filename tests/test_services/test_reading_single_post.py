from app.services import find_one

def test_reading_specific_post_from_file():
    result = find_one(1)
    expected = {'id': '1', 'author': 'autor test', 'date_post': '2020-12-11', 'email': 'test@mail.com', 'title': 'titulo test', 'text': 'test test'}
    assert result == expected