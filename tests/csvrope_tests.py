from nose.tools import assert_equal, assert_true
from csv_plus.csv_plus import *

filename = 'temp_test.csv'
record1 = ['10/08/2016','1','test sim','q','np','r','122']
record2 = ['10/08/2016','1','test sim','q','wp','r','124']
record3 = ['10/08/2016','1','test sim','q','np','w','88']
record4 = ['10/08/2016','1','test sim','q','np','w','56']
record5 = ['10/08/2016','1','test sim','v','sc','r','127']
record6 = ['10/08/2016','1','test sim','v','rc','w','65']
record7 = ['12/08/2016','2','studying','v','sc','r','76']
record8 = ['12/08/2016','2','studying','v','rc','w','36']
record9 = ['13/08/2016','3','quant test sim','q','fdp','r','218']
record10 = ['13/08/2016','3','quant test sim','q','wp','w','58']
record11 = ['13/08/2016','3','quant test sim','q','geo','w','312']

def setup():
    print("SETUP!")
    # populate .csv file
    clear(filename)
    append_row(filename, record1)
    append_row(filename, record2)
    append_row(filename, record3)
    append_row(filename, record4)
    append_row(filename, record5)
    append_row(filename, record6)
    append_row(filename, record7)
    append_row(filename, record8)
    append_row(filename, record9)
    append_row(filename, record10)
    append_row(filename, record11)

def teardown():
    print("TEAR DOWN!")

def test_basic():
    print("I RAN!")
    
def test1():
    """Check count_rows() method."""    
    count = count_rows(filename)
    assert_equal(count, 11)
    
def test2():
    """Check get_row() method."""
    record6 = ['10/08/2016','1','test sim','v','rc','w','65']
    to_check = get_row(filename, 5)
    assert_equal(record6, to_check)

def test3():
    """Check append_row() and get_rows() methods."""     
    rows = get_rows(filename)
    assert_equal(len(rows),11)
    assert_equal(rows[0],record1)
    assert_equal(rows[10],record11)
    
def test4():
    """Check get_row_value() method."""
    value = get_row_value(filename, 5, 3)
    assert_equal('v', value)
    
def test5():
    """Check get_row_values() method."""
    values = get_row_values(filename, 5, [1, 4])
    assert_equal(['1', 'rc'], values)
    
def test6():
    """Check get_rows_value() method."""
    values = get_rows_value(filename, 2)
    assert_equal(len(values), 11)
    assert_true('studying' in values)
    
def test7():
    """Check get_row_with_value() method."""
    rows = get_rows_with_value(filename, 3, 'q')
    assert_equal(len(rows),7)
    
def test8():
    """Check get_rows_with_values() method."""
    target_values = [ [3,'q'],[3,'v'],[4,'np'] ]
    rows = get_rows_with_values(filename, target_values)
    assert_equal(len(rows),3)
    print(rows)
    assert_equal(len(rows[0]),7)
    assert_equal(len(rows[1]),4)
    assert_equal(len(rows[2]),3)
    assert_equal(rows[1][2][6],'76')
    
def test9():
    """Check write_row() method."""
    write_row(filename, ['This is a brand new row.'])
    count = count_rows(filename)
    assert_equal(count, 1)
    assert_true('brand' in str(get_rows(filename)))
    
def test10():
    """Check overwrite_row() method."""
    setup()
    overwrite_row(filename, 8, ['This is a new row.','A brand new one.'])
    count = count_rows(filename)
    assert_equal(count, 11)
    assert_true('This' in str(get_row(filename, 8)[0]))
    assert_true('brand' in str(get_row(filename, 8)[1]))
