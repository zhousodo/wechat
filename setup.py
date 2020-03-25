from cx_Freeze import  setup,Executable

setup(name='test to exe',
      version='1.0',
      description='test from py file to exe file',
      executables=[Executable("client.py")]

      )