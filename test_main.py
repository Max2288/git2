from functions import opredelitel_1_poryadka
from functions import opredelitel_2_poryadka
from functions import opredelitel_3_poryadka
from functions import fib
import pytest

test_for_opr_1 = []
with open('testforopredelitel1.txt','r') as file_opr_1:
    new_lst = file_opr_1.readlines()
    for item in new_lst:
        list_int_from_strings = [i for i in item.split(':')]
        list_int_from_strings[0] = list_int_from_strings[0].replace(',','').replace('[','').replace(']','').split()
        list_int_from_strings[0] = [int(i) for i in list_int_from_strings[0]]
        item = ([[list_int_from_strings[0][i]]for i in range(0,len(list_int_from_strings[0]))],\
                int(list_int_from_strings[1].replace('\n','')))
        test_for_opr_1.append(item)

@pytest.mark.parametrize('test_inp, expect',test_for_opr_1)
def test_determinant_1(test_inp,expect):
    assert opredelitel_1_poryadka(test_inp) == expect

test_for_opr_2 = []
with open('testforopredelitel2.txt','r') as file_opr_2:
    new_lst = file_opr_2.readlines()
    for item in new_lst:
        list_int_from_strings = [i for i in item.split(':')]
        list_int_from_strings[0] = list_int_from_strings[0].replace(',','').replace('[','').replace(']','').split()
        list_int_from_strings[0] = [int(i) for i in list_int_from_strings[0]]
        item = ([[list_int_from_strings[0][i],list_int_from_strings[0][i+1]]\
            for i in range(0,len(list_int_from_strings[0]),2)],\
                int(list_int_from_strings[1].replace('\n','')))
        test_for_opr_2.append(item)
    

@pytest.mark.parametrize('test_inp, expect',test_for_opr_2)
def test_determinant_2(test_inp,expect):
    assert opredelitel_2_poryadka(test_inp) == expect

test_for_opr_3 =[]
with open('testforopredelitel3.txt','r') as file_opr_3:
    new_lst = file_opr_3.readlines()
    for item in new_lst:
        list_int_from_strings = [i for i in item.split(':')]
        list_int_from_strings[0] = list_int_from_strings[0].replace(',','').replace('[','').replace(']','').split()
        list_int_from_strings[0] = [int(i) for i in list_int_from_strings[0]]
        item = ([[list_int_from_strings[0][i],list_int_from_strings[0][i+1],list_int_from_strings[0][i+2]]\
            for i in range(0,len(list_int_from_strings[0]),3)],\
                int(list_int_from_strings[1].replace('\n','')))
        test_for_opr_3.append(item)
       

@pytest.mark.parametrize('test_inp, expect',test_for_opr_3)
def test_determinant_3(test_inp,expect):
    assert opredelitel_3_poryadka(test_inp) == expect

test_for_fib = []
with open('testfib.txt','r') as file_fib:
    test_for_fib = file_fib.readlines()
    for index in range(len(test_for_fib)):
        test_for_fib[index] = test_for_fib[index].replace('\n','')
        list_int_from_strings = [int(i) for i in test_for_fib[index].split(':')]
        test_for_fib[index] = (list_int_from_strings[0],list_int_from_strings[1])

    
@pytest.mark.parametrize('test_inp, expect',test_for_fib)
def test_fib(test_inp, expect):
    assert fib(test_inp) == expect
    