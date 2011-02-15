import unittest
from stomp_sender import process_params, process_brokers


class TestShellParams(unittest.TestCase):
    def test_empty_string_in_input_should_return_empty_dict(self):
        self.assertEqual(process_params(['']), {})


    def test_one_word_without_equal_sign_should_be_ignored(self):
        self.assertEqual(process_params(['testing']), {})
    

    def test_one_key_with_one_value(self):
        self.assertEqual(process_params(['key=value']), {'key': 'value'})


    def test_one_key_with_one_value_and_a_word_after_that_should_be_discarded(self):
        self.assertEqual(process_params(['key=value', 'testing']), {'key': 'value'})


    def test_one_key_with_one_value_and_a_word_before_that_should_be_discarded(self):
        self.assertEqual(process_params(['testing', 'key=value']), {'key': 'value'})


    def test_two_keys_and_values(self):
        self.assertEqual(process_params(['key1=value1', 'key2=value2']),
                         {'key1': 'value1', 'key2': 'value2'})


    def test_two_keys_and_values_with_a_word_in_the_middle_that_should_be_discarded(self):
        self.assertEqual(process_params(['key1=value1', 'spameggs', 'key2=value2']),
                         {'key1': 'value1', 'key2': 'value2'})


    def test_one_key_with_a_value_with_space(self):
        self.assertEqual(process_params(['key=v a l u e']),
                         {'key': 'v a l u e'})


    def test_two_keys_with_values_with_spaces(self):
        self.assertEqual(process_params(['key1=v a l u e 1', 'key2=v a l u e 2']),
                         {'key1': 'v a l u e 1', 'key2': 'v a l u e 2'})


    def test_two_keys_with_values_with_spaces_and_equal_sign(self):
        self.assertEqual(process_params(['key1=v a l = u e 1', 'key2=v a l u = e 2']),
                         {'key1': 'v a l = u e 1', 'key2': 'v a l u = e 2'})


    def test_two_keys_with_values_with_spaces_and_equal_sign_single_quote_and_double_quote_in_the_middle(self):
        self.assertEqual(process_params(['key1=v a l "= u e 1', 'key2=v a l" u" = e 2']),
                         {'key1': 'v a l "= u e 1', 'key2': 'v a l" u" = e 2'})


    def test_params_in_the_posix_way_should_be_treated_as_without_minus_signs(self):
        self.assertEqual(process_params(['--key1=v a l "= u e 1', 'eggsspam', '--key2=v a l" u" = e 2']),
                         {'key1': 'v a l "= u e 1', 'key2': 'v a l" u" = e 2'})


class TestProcessBrokers(unittest.TestCase):
    def test_process_just_one_broker(self):
        brokers = process_brokers('hostname:123')
        self.assertEqual(brokers, [('hostname', 123)])


    def test_process_two_brokers(self):
        brokers = process_brokers('hostname:123,otherhost:456')
        self.assertEqual(brokers, [('hostname', 123), ('otherhost', 456)])


    def test_process_two_brokers_with_space_between(self):
        brokers = process_brokers('hostname:123, otherhost:456')
        self.assertEqual(brokers, [('hostname', 123), ('otherhost', 456)])


unittest.main()
