import unittest
import inspect
from random import choice

from inst_to_dict_meta import InstToDict, DictToolsMix




TEST_OUTPUT_FILENAME = None
FILENAME = 'excomunication.thm'


class Test_InstToDict(unittest.TestCase):
    def get_obj_to_test(self, value):
        return InstToDict(value), {c: ord(c) for c in value}
    
    def test_instance_returns_dict_type(self):
        instance, _ = self.get_obj_to_test(FILENAME)
        self.assertTrue(isinstance(instance, dict))

    def test_instance_returns_expected_dict(self):
        instance, test_dict = self.get_obj_to_test(FILENAME)
        self.assertEqual(instance, test_dict)

    def test_instance_retains_standart_dict_methods(self):
        instance, test_dict = self.get_obj_to_test(FILENAME)

        for o in (instance, test_dict):
            o.update({1:22, 's': 'spam'})
            
        self.assertEqual(instance, test_dict)
        self.assertFalse(set(dir(test_dict)) - set(dir(instance)))

    def test_InstToDict_retains_mixin_methods(self):
        keys_to_pop = set(choice(FILENAME) for t in range(len(FILENAME)//2))
        instance, test_dict = self.get_obj_to_test(FILENAME)

        instance.pops(*keys_to_pop)
        {test_dict.pop(k) for k in keys_to_pop}
        
        self.assertEqual(instance, test_dict)
        self.assertFalse(set(DictToolsMix.__dict__) - set(dir(instance)))

    def test_InstToDict_retains_init_values(self):
        instance, test_dict = self.get_obj_to_test(FILENAME)
        
        self.assertEqual(instance.filename, FILENAME)

        with self.assertRaises(AttributeError):
            test_dict.filename

    def test_proper_methods_are_classmethods(self):
        for attr in InstToDict.__dict__:
            val = getattr(InstToDict, attr)
            if not attr.startswith('__') and callable(val):
                self.assertTrue(inspect.ismethod(val), f'not a classmethod\n\t{attr}: {val}')




if __name__ == '__main__':
    unittest.main(verbosity=2)
