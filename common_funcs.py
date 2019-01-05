import datetime
import toga
from toga.style.pack import *


def text_input(tag, readonly):
    box = toga.Box()
    label = toga.Label(tag, style=Pack(width=80))
    txt_input = toga.TextInput(readonly=readonly, style=Pack(width=100))

    box.add(label)
    box.add(txt_input)

    box.style.update(direction=ROW, alignment=LEFT, width=200, flex=1, padding=5, text_align=LEFT)

    return box, txt_input


def text_output(txt_box, info):
    try:
        txt_box.value = info
    except:
        txt_box.value = '???'


def slider(tag, range):
    box = toga.Box()
    label = toga.Label(tag)
    txt_input = toga.Slider()

    box.add(label)
    box.add(txt_input)

    box.style.update(direction=ROW, alignment=LEFT, width=300, flex=1, padding=5, text_align=LEFT)

    return box, txt_input


def selection(tag, items):
    box = toga.Box()
    label = toga.Label(tag, style=Pack(width=80))
    txt_input = toga.Selection(items=items, style=Pack(width=100))

    box.add(label)
    box.add(txt_input)

    box.style.update(direction=ROW, alignment=LEFT, width=300, flex=1, padding=5, text_align=LEFT)

    return box, txt_input


def heading(name):
    label = toga.Label(name)
    label.style.update(padding=10, color='grey')
    return label


def day_list():
    arr = []
    for i in range(1, 32):
        arr.append(i)
    return arr


def month_list():
    arr = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November',
           'December']
    return arr


def year_list():
    now = datetime.datetime.now()
    now_year = now.year
    arr = []

    for i in range(-now_year, -1900):
        arr.append(-i)

    return arr


def get_month(month):
    m_list = month_list()
    month_no = m_list.index(month) + 1
    return month_no
