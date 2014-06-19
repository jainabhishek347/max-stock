import csv
import sys
import unittest

from maxstock import CompanyStock
class TestCSVStock(unittest.TestCase):
  """  
  Company Max Stock unit test cases.
  """
  def setUp(self):
    """  
    this will load csv valid and invalid
    """
    self.rightfile = 'rightfile.csv'
    self.wrongfile = 'wrongfile.csv'

  def tearDown(self):
    """  
    no need to reset or do anything here as its input as a file that we didnt change in it during test.
    """
    try:
      pass
    except:
      pass

  def test_success(self):
    """  
    positive test : just test if there is no exception is raised and when set max stock it return True.
    """
    x = CompanyStock(self.rightfile)    
    self.assertTrue(x.set_max_stock())

  def test_compare_exact_value(self):
    """  
    positive test : just test if there is no exception is raised and when set max stock it return True
    and compare results : match expacted values for 'company A'
    """
    x = CompanyStock(self.rightfile)    
    x.set_max_stock()
    data = x.get_max_stock()

    self.assertEqual(data['Company A'][0][0],'799','This is not write csv.')
    self.assertEqual(data['Company A'][0][1],'1996','This is not write csv.')
    self.assertEqual(data['Company A'][0][2],'Apr','This is not write csv.')
    

  def test_invalid_data(self): 
    """  
    Negative test : just test if is raised with invalid csv of not valid format csv
    """
    x = CompanyStock(self.wrongfile)  
    self.assertFalse(x.set_max_stock())

if __name__ == '__main__':
    """  
    Run unit test cases for company max stock during year and month. 
    """
    suite = unittest.TestLoader().loadTestsFromTestCase(TestCSVStock)
    unittest.TextTestRunner(verbosity=2).run(suite)            
    sys.exit()
