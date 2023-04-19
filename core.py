# ==============================================================================#
#                                                                               #
#                                  Fraunhofer FOKUS                             #
#                                                                               #
#                                                                               #
#    All rights reserved. Distribution or duplication without previous          #
#    written agreement of the owner prohibited.                                 #
#                                                                               #
# ===============================================================================
# ===============================================================================
# -*-coding:utf-8-*-
# : $  wang_library
# : $  Ya Wang
# : $  19.04.2023
# ===============================================================================
import matplotlib.pyplot as plt

def create_bar_chart(data, labels, title='', xlabel='', ylabel='', color='blue'):
    fig, ax = plt.subplots()
    ax.bar(labels, data, color=color)
    ax.set_title(title)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)

    plt.show()

def create_line_chart(data, labels, title='', xlabel='', ylabel='', color='blue'):
    fig, ax = plt.subplots()
    ax.plot(labels, data, color=color)
    ax.set_title(title)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)

    plt.show()

def create_pie_chart(data, labels, title=''):
    fig, ax = plt.subplots()
    ax.pie(data, labels=labels, autopct='%1.1f%%')
    ax.set_title(title)

    plt.show()
