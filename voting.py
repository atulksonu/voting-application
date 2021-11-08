from pywebio.input import *
from pywebio.io_ctrl import input_control
from pywebio.output import *
from uuid import uuid4
from tkinter import*
import requests


def voting():
    print(' Welcome to E-voting process\n enter to join the network')

    name = input ('enter your name',type="text")
    unique_id = str(uuid4())
    print('{} : {}' .format(name,unique_id))

    New_user = radio('Requesting for joinng the network')
# import requests module , Making a get request
    requests.get('http://api.github.com')
    response = requests.get('https://api.github.com')

    if response:
        print('Success!')
    else:
        print('An error has occurred.')

# P2P already connected users 
    users = radio('approve the request',['Yes'])      
    check = checkbox(['all the details are correct'])
    if users == 'Yes':
        voting('new_user join the network')
    else:
        print('An error has occurred')
        
    if check:
        selction = radio("select your voters",['A','B',])
        put_text('Thnaks, your response has been recorded in our database')
        return style(put_text('voitng has been recorded, we will announce the result soon... '),'color: green ')    

    

voting()

