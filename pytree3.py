# THE PYTHON TREE !!
# Python Helper, show best libraries per subject and give documentation

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
                         'Web Applcation': {'Django': 'https://docs.djangoproject.com/en/4.0/', 
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
                                        'Beautifulsoup': 'https://beautiful-soup-4.readthedocs.io/en/latest/', 
                                        'Scrapy': 'https://docs.scrapy.org/en/latest/',  
                                        'Selenium': 'https://selenium-python.readthedocs.io/',
                                        }
                        }

    # Prompt user for a subject
    def get_subject(self):
        sub = 's'
        while sub not in self.subjects:
            sub = input('Choose a subject of Python: Data Science/Web Application/Mobile App/Games/Automation:   ').title()
            if sub in self.subjects:
                return sub

    # Gets the subject and return a choosen library
    def get_lib(self, sub):
        lib = 's'
        while lib not in self.subjects:
            if sub == 'Data Science':
                lib = input('Choose a library for Data Science: Pandas/Scikitlearn/Matplotlib/Seaborn/Pytorch/Keras/Tensorflow:  ').title()
                if lib in self.subjects['Data Science']:
                    return lib

            elif sub == 'Web Application':
                lib = input('Choose a library for Web Development: Djando/Flask/Cherrypy:  ').title()
                if lib in self.subjects['Web Application']:
                    return lib

            elif sub == 'Mobile Application':
                lib = input('Choose a library for Mobile Development: Kivy/Tkinter:  ').title()
                if lib in self.subjects['Mobile App']:
                    return lib

            elif sub == 'Games':
                lib = input('Choose a library for Game Development: Pygame/Pykyra/Pyglet:  ').title()
                if lib in self.subjects['Games']:
                    return lib

            elif sub == 'Automation':
                lib = input('Choose a library for Automation: Urllib/Requests/Webbot/Beatifulsoup/Scrapy/Selenium:  ').title()
                if lib in self.subjects['Automation']:
                    return lib

def main():
    try:
        pyhelper = PythonHelper()
        sub = pyhelper.get_subject()
        lib = pyhelper.get_lib(sub)
        print(pyhelper.subjects[sub][lib])
    except ValueError:
        main()

if __name__ == '__main__':
    main()
