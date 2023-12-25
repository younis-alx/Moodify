import pytest
from backend.extract.URL_validator import id_extractor, url_validator


class TestURLValidator:
    @pytest.fixture(autouse=True)
    def setup(self):
        self.url = 'https://twitter.com/realDonaldTrump/status/1346234777005284352'
        self.url1 = 'https://twitter.com/realDonaldTrump/status/1346234777005284352?s=20'
        self.url3 = 'https://google.com'

    def test_id_extractor(self):
        assert id_extractor(self.url) == '1346234777005284352'
        assert id_extractor(self.url1) == '1346234777005284352'
        assert id_extractor(self.url3) == None

    def test_url_validator(self):
        assert url_validator(self.url)
        assert not url_validator(self.url3)
