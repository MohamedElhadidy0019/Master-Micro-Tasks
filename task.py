import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from matplotlib.figure import Figure
#from Plot import PlotFunction
import numpy as np

from Plot import PlotClass
import matplotlib.pyplot as plt
import string


class MplCanvas(FigureCanvasQTAgg):

    def __init__(self, parent=None, width=5, height=4, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)
        super(MplCanvas, self).__init__(fig)


def is_integer(txt):
    '''
    check if the string is an integer

    Parameters
    ----------
    txt: string

    Returns
    -------
    boolean
        true if the string is an integer
    
    '''
    is_positive_integer = txt.isdigit()
    is_negative_integer =  txt.startswith("-") and txt[1:].isdigit()
    is_integer = is_positive_integer or is_negative_integer
    return is_integer
def is_valid_eq(equation):
    '''
    check if the string is a valid equation

    Parameters
    ----------
    equation: string
    
    Returns
    -------
    boolean
        true if the string is a valid equation
    '''
    allowed = set('.'+'('+')'+' '+'X'+'x'+string.digits + '-' + '+' + '*'+ '/' + '^' )
    return (set(equation) <= allowed)

class Window(QWidget):


    def plot_clicked(self):

        #clear canvas
        self.canvas.axes.clear()
        self.canvas.draw()

        #clear error message
        self.error_message.setText("")
        
        #read fom text boxe
        equation=str(self.equation_text.text())
        lower_x=str(self.lower_x.text())
        upper_x=str(self.upper_x.text())


        #check if the input is valid
        flag_valid_eq=is_valid_eq(equation)
        flag_valid_x=is_integer(lower_x) and is_integer(upper_x)

        if (not(flag_valid_eq)) and(not(flag_valid_x)):
            self.error_message.setText("please enter a valid equation and range")
            return
        elif not(flag_valid_eq):
            self.error_message.setText("please enter a valid equation")
            return
        elif not(flag_valid_x):
            self.error_message.setText("please enter a valid range")
            return
        
        
        upper_x=int(upper_x)
        lower_x=int(lower_x)

        range=(np.abs(upper_x-lower_x))*10 +1
        x=np.linspace(lower_x,upper_x,range)
        try:
            y=PlotClass.plotFunction(x,equation)
            if np.nan in y:
                self.error_message.setText("division by zero error, please enter a valid equation")
                return
            self.canvas.axes.plot(x,y)
            self.canvas.draw()
        except:
            self.error_message.setText("please enter a valid equation")
            return

        



    def __init__(self):
        super().__init__()
        self.setWindowTitle("PYPY Plotter")
        # Create an outer layout
        outerLayout = QVBoxLayout()
       


        #fisrt horizontal layout for entering equation
        layout_function_input = QHBoxLayout() # Create a layout for the equation input
        # Add widgets to the layout
        lbl_eqn=QLabel("Function=")
        lbl_eqn.setAlignment(Qt.AlignCenter)
        self.lbl_eqn=lbl_eqn
        layout_function_input.addWidget(self.lbl_eqn)
        equation_text=QLineEdit()
        self.equation_text=equation_text   #text box for equation
        layout_function_input.addWidget(self.equation_text) #add text box to layout




        #second horizontal layout for entering range
        layout_function_bound=QHBoxLayout()
        lbl_lower_bound=QLabel("minmum x=")
        lbl_lower_bound.setAlignment(Qt.AlignCenter)
        layout_function_bound.addWidget(lbl_lower_bound)
        lower_x=QLineEdit()
        self.lower_x=lower_x
        layout_function_bound.addWidget(self.lower_x)
        layout_function_bound.setContentsMargins(10,0,10,0)

        lbl_upper_bound=QLabel("maximum x=")
        lbl_upper_bound.setAlignment(Qt.AlignCenter)
        layout_function_bound.addWidget(lbl_upper_bound)
        upper_x=QLineEdit()
        self.upper_x=upper_x
        layout_function_bound.addWidget(self.upper_x)
        layout_function_bound.setContentsMargins(10,20,10,0)



        #third horizontal layout for plot button
        layout_plot_button=QHBoxLayout()
        plot_button=QPushButton("Plot")
        plot_button.clicked.connect(self.plot_clicked)
        layout_plot_button.addWidget(plot_button)
        layout_plot_button.setContentsMargins(100,20,100,20)


        #fourth horizontal layout for error message
        layout_error_message=QHBoxLayout()
        error_message=QLabel("")
        error_message.setAlignment(Qt.AlignCenter)
        self.error_message=error_message
        layout_error_message.addWidget(self.error_message)
        layout_error_message.setContentsMargins(0,0,0,20)



        #fifth horizontal layout for canvas
        layout_mpl=QHBoxLayout()
        sc = MplCanvas(self, width=5, height=4, dpi=100)
        self.canvas=sc
        layout_mpl.addWidget(self.canvas,stretch=1,alignment=Qt.AlignCenter)
        self.show()

       


        #here we stack the horizontal layouts in the outer layout
        outerLayout.addLayout(layout_function_input)
        outerLayout.addLayout(layout_function_bound)
        outerLayout.addLayout(layout_plot_button)
        outerLayout.addLayout(layout_error_message)
        outerLayout.addLayout(layout_mpl)

        self.setLayout(outerLayout)

        #set the mimum width and height ow window
        min_width=670
        min_height=715
        self.setMinimumSize(QSize(min_width, min_height))

    

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())