class TestsWithList:

    def test_list_1(self, create_list_7):
        for number in create_list_7:
            assert number % 7 == 0

    def test_add_value(self, create_list_7):
        create_list_7.append('test value')
        assert create_list_7[-1] == 'test value'

    def test_edit_value(self, create_list_7):
        create_list_7[5] = 'new value'
        assert create_list_7[5] == 'new value'


class TestWithVar:

    def test_multiple_number_1(self, create_sum):
        new_sum = create_sum + 1
        assert new_sum % 2 != 0

    def test_multiple_number_2(self, create_sum):
        new_sum = create_sum + 2
        assert new_sum % 2 == 0


class TestWithTuple:

    def test_transform_list_in_tuple(self, create_list_7):
        transform_tuple = tuple(create_list_7)
        assert type(transform_tuple) is tuple


class TestWithSet:

    def test_transform_list_in_set(self, create_list_7):
        transform_set = set(create_list_7)
        assert type(transform_set) is set


class TestWithDict:

    def test_key_dict_list_value(self, create_dict, create_list_7):
        assert create_dict['key_2'] == create_list_7

    def test_key_dict_list_len(self, create_dict, create_list_7):
        assert len(create_dict['key_2']) == len(create_list_7)
