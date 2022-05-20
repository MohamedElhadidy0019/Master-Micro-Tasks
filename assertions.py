from Plot import PlotClass
import task
import numexpr
import matplotlib.pyplot as plt
import numpy as np



def test_string_Preprocess():
    functionString='x^2'
    newString=PlotClass.stringPreprocess(functionString)
    assert newString=='(x)**2'

def test_toLiteral():
    x=[1,2,3]
    functionString='x^2'
    literalStrings=PlotClass.toLiteral(x,PlotClass.stringPreprocess(functionString))
    assert literalStrings==['(1)**2','(2)**2','(3)**2']


def test_is_integer():
    assert task.is_integer('1')
    assert task.is_integer('99')
    assert not(task.is_integer('1.0'))
    assert not(task.is_integer('1.1'))
    assert not(task.is_integer('1.1.1'))
    assert not(task.is_integer('f'))


def test_is_valid_eq():
    assert task.is_valid_eq('x^2')
    assert task.is_valid_eq('x^2+x')
    assert not(task.is_valid_eq('print(x)'))






if __name__ == '__main__':
    test_string_Preprocess()
    test_toLiteral()
    test_is_integer()
    test_is_valid_eq()
    print("all passed")