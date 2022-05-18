
import numexpr
import matplotlib.pyplot as plt
import numpy as np

class PlotClass:



    def stringPreprocess(functionString):
        '''
        function to replace all '^' to '**' in order to make it suitable for python
        and 'x' to '(x)'
        
        Parameters
        ----------
        fucntionString: string like
            the function needed to be evaluated
        
        returns
        functionString: string like
            the function with '^' replaced by '**' and 'x' replaced by '(x)'
        '''
        newString=functionString
        newString=newString.replace('^','**')
        newString=newString.replace('x','(x)')
        return  newString

    def toLiteral(x,functionString):
        '''
        function to substitute each x with a value

        Parameters
        ----------
        x: int list 
            values to put in the string
        functionString: String
            the function entered bu user

        returns : list of strings with variable x substituted
        '''
        literalStrings=[]
        for i in x:
            literalStrings.append(functionString.replace('x',str(i)))

        return literalStrings
        

    def evaluateFunction(literalString,x):
        '''
        eavaluating a mathematical string

        Parameters
        ----------
        literalString: list of strings
            the strings with different values of x

        returns
        y: float numpy array
            the evaluation of each string
        '''
        y=[]
        i=0
        for equation in literalString:
            try:
                y.append(numexpr.evaluate(equation).item())
            except:
                y.append(np.nan)
                x[i]=np.nan
            i+=1
        
        return np.array(y)

    def plotFunction(x,mathFunction):
        '''
        calculating the y values of a mathematical function for all x values

        Parameters
        ----------
        x: int list
            values to put in the string
        mathFunction: String
            the function entered by user

        returns
        y: float numpy array
        
        '''
        y=PlotClass.evaluateFunction(PlotClass.toLiteral(x,PlotClass.stringPreprocess(mathFunction)),x)
        return(y)
        


