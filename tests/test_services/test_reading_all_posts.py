from app.services import list_all

def test_reading_all_posts_from_file():
    result = len(list_all())
    expected = 1 
    assert result > expected

