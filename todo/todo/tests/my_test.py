from notes.views import data

class TestMyFunction:
    def setup_method(self):
        self.request

    def test_my_function(self):
        assert data(self.request) ==
