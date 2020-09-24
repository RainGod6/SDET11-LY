import pytest
import yaml


class TestYaml:

    def test_yaml(self):
        print(yaml.load("""
            - Hesperiidae
            - Papilionidae
            - Apatelodidae
            - Epiplemidae
           """))

    @pytest.mark.parametrize("a,b", yaml.safe_load(open("testyaml.yaml", encoding='utf-8')))
    def test_yaml_read(self, a, b):
        assert a + b == 10




