# THE PYTHON TREE !!
# Python Helper, show best libraries per subject and give documentation
from tkinter import *
import tkinter
import tkinter.ttk as ttk
import webbrowser
from colorama import Style
from setuptools import Command

# Object Python Helper
class PythonHelper:
    def __init__(self):
        self.subjects = {'Data Science': {'Pandas': 'https://pandas.pydata.org/docs/#',
                                          'Scikitlearn': 'https://scikit-learn.org/stable/',
                                          'Matplotlib': 'https://matplotlib.org/',
                                          'Seaborn': 'https://seaborn.pydata.org/tutorial.html',
                                          'Pytorch': 'https://pytorch.org/',
                                          'Keras': 'https://keras.io/',
                                          'Tensorflow': 'https://www.tensorflow.org/',
                                          },
                         'Web Application': {'Django': 'https://docs.djangoproject.com/en/4.0/',
                                             'Flask': 'https://flask.palletsprojects.com/en/2.1.x/',
                                             'Cherrypy': 'https://docs.cherrypy.dev/en/latest/',
                                            },
                         'Mobile App': {'Kivy': 'https://kivy.org/doc/stable/',
                                        'Tkinter': 'https://docs.python.org/3/library/tk.html',
                                        },
                         'Games': {'Pygame': 'https://www.pygame.org/news',
                                   'Pykyra': 'https://pypi.org/project/pykira/',
                                   'Pyglet': 'https://pyglet.readthedocs.io/en/latest/',
                                   },
                         'Automation': {'Urllib': 'https://docs.python.org/3/library/urllib.html',
                                        'Requests': 'https://requests.readthedocs.io/en/latest/',
                                        'Webbot': 'https://webbot.readthedocs.io/en/latest/',
                                        'Beautifulsoup': 'https://beautiful-soup-4.readthedocs.io/en/  latest/',
                                        'Scrapy': 'https://docs.scrapy.org/en/latest/',
                                        'Selenium': 'https://selenium-python.readthedocs.io/',
                                        }
                        }

# Create Screen
class Screen:
    def __init__(self):
        #Create Screen
        self.screen = Tk()
        self.screen.geometry('800x500')
        self.screen.title('Python Helper')

        # Create Tree
        self.tree = ttk.Treeview(self.screen)
        self.tree.heading('#0', text= 'Subjects', anchor=tkinter.W)

        # Add Style
        self.style = ttk.Style()
        self.style.theme_use('clam')

        # Create Parent Rows
        self.tree.column('#0', width=50, minwidth=25)
        self.tree.insert(parent='', index='end', iid=0, text='Data Science')
        self.tree.insert(parent='', index='end', iid=1, text='Web Application')
        self.tree.insert(parent='', index='end', iid=2, text='Mobile App')
        self.tree.insert(parent='', index='end', iid=3, text='Games')
        self.tree.insert(parent='', index='end', iid=4, text='Automation')

        # Create Data Science Childs
        self.tree.insert(parent='0', index='end', iid=pyhelper.subjects['Data Science']['Pandas'], text='Pandas')
        self.tree.insert(parent='0', index='end', iid=pyhelper.subjects['Data Science']['Scikitlearn'], text='Scikitlearn')
        self.tree.insert(parent='0', index='end', iid=pyhelper.subjects['Data Science']['Matplotlib'], text='Matplotlib')
        self.tree.insert(parent='0', index='end', iid=pyhelper.subjects['Data Science']['Seaborn'], text='Seaborn')
        self.tree.insert(parent='0', index='end', iid=pyhelper.subjects['Data Science']['Pytorch'], text='Pytorch')
        self.tree.insert(parent='0', index='end', iid=pyhelper.subjects['Data Science']['Keras'], text='Keras')
        self.tree.insert(parent='0', index='end', iid=pyhelper.subjects['Data Science']['Tensorflow'], text='Tensorflow')

        # Create Web Application Childs
        self.tree.insert(parent='1', index='end', iid=pyhelper.subjects['Web Application']['Django'], text='Django')
        self.tree.insert(parent='1', index='end', iid=pyhelper.subjects['Web Application']['Flask'], text='Flask')
        self.tree.insert(parent='1', index='end', iid=pyhelper.subjects['Web Application']['Cherrypy'], text='Cherrypy')

        # Create Mobile App Childs
        self.tree.insert(parent='2', index='end', iid=pyhelper.subjects['Mobile App']['Kivy'], text='Kivy')
        self.tree.insert(parent='2', index='end', iid=pyhelper.subjects['Mobile App']['Tkinter'], text='Tkinter')

        # Create Games Childs
        self.tree.insert(parent='3', index='end', iid=pyhelper.subjects['Games']['Pygame'], text='Pygame')
        self.tree.insert(parent='3', index='end', iid=pyhelper.subjects['Games']['Pykyra'], text='Pykyra')
        self.tree.insert(parent='3', index='end', iid=pyhelper.subjects['Games']['Pyglet'], text='Pyglet')

        # Create Automation Childs
        self.tree.insert(parent='4', index='end', iid=pyhelper.subjects['Automation']['Urllib'], text='Urllib')
        self.tree.insert(parent='4', index='end', iid=pyhelper.subjects['Automation']['Requests'], text='Requests')
        self.tree.insert(parent='4', index='end', iid=pyhelper.subjects['Automation']['Webbot'], text='Webbot')
        self.tree.insert(parent='4', index='end', iid=pyhelper.subjects['Automation']['Beautifulsoup'], text='Beatifulsoup')
        self.tree.insert(parent='4', index='end', iid=pyhelper.subjects['Automation']['Scrapy'], text='Scrapy')
        self.tree.insert(parent='4', index='end', iid=pyhelper.subjects['Automation']['Selenium'], text='Selenium')

        # Bind Tree
        self.tree.bind('<Double-Button>', self.openurl)

        # Pack TreeView
        self.tree.pack(side=tkinter.TOP, fill='both', expand=True)

    # Function to open selected row
    def openurl(self, e):
        selected = self.tree.focus()
        webbrowser.open(selected)


# Run App
pyhelper = PythonHelper()
def main():
    app = Screen()
    app.screen.mainloop()

if __name__ == '__main__':
    main()