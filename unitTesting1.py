import unittest #Demonstrating a working of unittest

#This is where the the Unit Test goes for testing the function
class TestStringMethods(unittest.TestCase):

    #Function to test for Upper case
    def test_upper(self):
        #Given an example of upper case 
        self.assertEqual('foo'.upper(), 'FOO')

    
    def test_isupper(self):
        #Return True if the string is upper case 
        self.assertTrue('FOO'.isupper())
        #Return False if the string is lower case
        self.assertFalse('Foo'.isupper())

#Check if all characters passed in the function 
def test_split(self):

    s = 'hello world' #<- Given an example test string 
    self.assertEqual(s.split(), ['hello', 'world'])
    #Check that s.split fails when the separator is not a string

    #This would raise any Type Error
    with self.assertRaises(TypeError):
        #Return a list of string after separated by 2 
        s.split(2) 

#Python program use to call main function
if __name__ == '__main__':
    unittest.main() #Provide a command line in the test script 