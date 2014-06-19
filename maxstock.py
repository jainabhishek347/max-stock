#!/usr/bin/python
import csv
import sys

class CompanyStock():
  """
  Basicn function this class is :
  Load csv file fetch iformation for companies.
  """
  def __init__(self,csv_file):
    self.read_file_content(csv_file)
    self.results = {}

  def read_file_content(self,csv_file):
    """  
    Read csv file if its not readable raise I/O exception.
    """
    try:
      self.csv_content = csv.reader(open(csv_file,'r'))
      self.heading_column = self.csv_content.next()
      self.companies_data = list(self.csv_content)
    except IOError:
      print "Unable to open file."

  def set_max_stock(self):
    """
    Set max stocks corrosponding to the company.
    """
    try:
      for row in self.companies_data:
        for index, column in enumerate(self.heading_column):
          if index >1:
            if not self.results.get(column):
              self.results[column] = [tuple([row[index], row[0], row[1]])]
            else:
              if float(row[index]) > float(self.results[column][0][0]):
                self.results[column] = [tuple([row[index], row[0], row[1]])]
              elif float(row[index]) == float(self.results[column][0][0]):
                self.results[column].append(tuple([row[index], row[0], row[1]]))

    except Exception:
      self.results = None
      print "csv doesn't have valid data...."
      return False

    return True

  def get_max_stock(self):
    """  
    Return result fo all companies with maximum stock.
    """
    return self.results

  def print_stocks(self):
    """
    print results as an end user readable format
    """
    if self.results:
      print "="*50
      print '{: ^20} {: ^4} {: ^4} {: ^10}'.format("COMPANY", "YEAR", "MONTH", "PRICE") 
      print "="*50
      for company, items in self.results.iteritems():
        for item in items:
          print '{: ^20} {: ^4} {: ^4} {: ^10}'.format(company, item[1], item[2], item[0] ) 
      print "="*50
   
if __name__ == '__main__':
  """  
  Take csv file as input and validate it.
  """
  try:
    if len(sys.argv) >= 2:
      csv_file = sys.argv[1]
      if not csv_file.endswith('.csv'):    
        print "Not a vaid csv file..."
      else:
        csv_stock = CompanyStock(csv_file)
        csv_stock.set_max_stock()
        csv_stock.print_stocks()
    else:
      print "No Input file..."
  except Exception, e:
    print e
    print "Please Input valid csv file...."

