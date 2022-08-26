#!/usr/bin/env python
# coding: utf-8

# In[2]:


from tkinter import *
from tkinter import scrolledtext

import matplotlib
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

import matplotlib.pyplot as plt
import PVTBackEnd
    
window = Tk()
window.title("PVT CALCULATOR")

#Create Plot Functions
def Rs_plot():
    plot1 = Toplevel(window)
    P = float(e1.get())
    T = float(e2.get())
    Yo = float(e3.get())
    Yg = float(e4.get())
    z = float(e5.get())
    API = PVTBackEnd.api_gravity(Yo)

    x = range(int(e1.get()), 0, -100)
    y = [PVTBackEnd.gasoil_ratio(P, T, Yg, API) for P in x]
    
    fig = plt.Figure(figsize = (7, 4), dpi = 100)
    fig.add_subplot(111).plot(x, y)
    fig.add_subplot(111).set_title('Pressure vs GOR')
    fig.add_subplot(111).set_xlabel('Pressure (psia)')
    fig.add_subplot(111).set_ylabel('GOR (scf/stb)')

    chart = FigureCanvasTkAgg(fig, plot1)
    chart.get_tk_widget().pack()

def Bo_plot():
    plot2 = Toplevel(window)
    P = float(e1.get())
    T = float(e2.get())
    Yo = float(e3.get())
    Yg = float(e4.get())
    z = float(e5.get())
    API = PVTBackEnd.api_gravity(Yo)
    pg = PVTBackEnd.gas_density(P, T, z, Yg)

    x = range(int(e1.get()), 0, -100)
    x2 = [PVTBackEnd.gasoil_ratio(P, T, Yg, API) for P in x]
    y = [PVTBackEnd.oil_fvf(T, Yo, Yg, Rs) for Rs in x2]

    fig = plt.Figure(figsize = (7, 4), dpi = 100)
    fig.add_subplot(111).plot(x, y)
    fig.add_subplot(111).set_title('Pressure vs Oil FVF')
    fig.add_subplot(111).set_xlabel('Pressure (psia)')
    fig.add_subplot(111).set_ylabel('Oil FVF (rb/stb)')
    
    chart = FigureCanvasTkAgg(fig, plot2)
    chart.get_tk_widget().pack()

def Bg_plot():
    plot3 = Toplevel(window)
    P = float(e1.get())
    T = float(e2.get())
    Yo = float(e3.get())
    Yg = float(e4.get())
    z = float(e5.get())
    API = PVTBackEnd.api_gravity(Yo)
    Bg = PVTBackEnd.gas_fvf(P, T, z)
    pg = PVTBackEnd.gas_density(P, T, z, Yg)
    
    x = range(int(e1.get()), 0, -100)
    y = [PVTBackEnd.gas_fvf(P, T, z) for P in x]

    fig = plt.Figure(figsize = (7, 4), dpi = 100)
    fig.add_subplot(111).plot(x, y)
    fig.add_subplot(111).set_title('Pressure vs Gas FVF')
    fig.add_subplot(111).set_xlabel('Pressure (psia)')
    fig.add_subplot(111).set_ylabel('Gas FVF (scf/stb)')
    
    chart = FigureCanvasTkAgg(fig, plot3)
    chart.get_tk_widget().pack()

#Create Command Functions
def calculation():
    P = float(e1.get())
    T = float(e2.get())
    Yo = float(e3.get())
    Yg = float(e4.get())
    z = float(e5.get())
    
    API = PVTBackEnd.api_gravity(Yo)
    Rs = PVTBackEnd.gasoil_ratio(P, T, Yg, API)
    Pb = PVTBackEnd.bubble_pressure(T, Yg, Rs, API)
    Bo = PVTBackEnd.oil_fvf(T, Yo, Yg, Rs)
    Bg = PVTBackEnd.gas_fvf(P, T, z)
    pg = PVTBackEnd.gas_density(P, T, z, Yg)

    e6.delete(0, END)
    e6.insert(END, "{:.2f}".format(Rs))
    e7.delete(0, END)
    e7.insert(END, "{:.2f}".format(Pb))
    e8.delete(0, END)
    e8.insert(END, "{:.2f}".format(Bo))
    e9.delete(0, END)
    e9.insert(END, "{:.5f}".format(Bg))
    e10.delete(0, END)
    e10.insert(END, "{:.2f}".format(pg))

def simulation():
    table1.delete(1.0, END)
    Num = 1
    
    for P in range(int(e1.get()), 0, -100 ):
        T = float(e2.get())
        Yo = float(e3.get())
        Yg = float(e4.get())
        z = float(e5.get())
        
        API = PVTBackEnd.api_gravity(Yo)
        Rs = PVTBackEnd.gasoil_ratio(P, T, Yg, API)
        Pb = PVTBackEnd.bubble_pressure(T, Yg, Rs, API)
        Bo = PVTBackEnd.oil_fvf(T, Yo, Yg, Rs)
        Bg = PVTBackEnd.gas_fvf(P, T, z)
        pg = PVTBackEnd.gas_density(P, T, z, Yg)
        
        table1.insert(END, "{:8d}\t{:11.2f}\t{:9.2f}\t{:7.2f}\t{:11.5f}\t{:10.2f}\n"
                      .format(int(Num), P, Rs, Bo, Bg, pg))
        Num = Num + 1

#Create Menu Bar Options
menubar = Menu(window)

filemenu = Menu(menubar, tearoff = 0)
filemenu.add_command(label = "New")
filemenu.add_command(label = "Open")
filemenu.add_command(label = "Save")
filemenu.add_command(label = "Exit")
menubar.add_cascade(label = "File", menu = filemenu)

plotmenu = Menu(menubar, tearoff = 0)
plotmenu.add_command(label = "Pressure vs GOR", command = Rs_plot)
plotmenu.add_command(label = "Pressure vs Oil FVF", command = Bo_plot)
plotmenu.add_command(label = "Pressure vs Gas FVF", command = Bg_plot)
menubar.add_cascade(label = "Plot", menu = plotmenu)

# Create Input Property Labels
l1 = Label(window, text = "Pressure").grid(row = 0, column = 0)
l2 = Label(window, text = "Temperature").grid(row = 1, column = 0)
l3 = Label(window, text = "Oil Gravity").grid(row = 2, column = 0)
l4 = Label(window, text = "Gas Gravity").grid(row = 3, column = 0)
l5 = Label(window, text = "z-Factor").grid(row = 4, column = 0)

# Create Input Property Units
u1 = Label(window, text = "psia").grid(row = 0, column = 2)
u2 = Label(window, text = "deg R").grid(row = 1, column = 2)
u3 = Label(window, text = "fraction").grid(row = 2, column = 2)
u4 = Label(window, text = "fraction").grid(row = 3, column = 2)
u5 = Label(window, text = "fraction").grid(row = 4, column = 2)

# Create Output Property Labels
l6 = Label(window, text = "Gas Oil Ratio").grid(row = 0, column = 3)
l7 = Label(window, text = "Bubble Pressure").grid(row = 1, column = 3)
l8 = Label(window, text = "Oil FVF").grid(row = 2, column = 3)
l9 = Label(window, text = "Gas FVF").grid(row = 3, column = 3)
l10 = Label(window, text = "Gas Density").grid(row = 4, column = 3)

# Create Output Property Units
u6 = Label(window, text = "scf/stb").grid(row = 0, column = 5)
u7 = Label(window, text = "psia").grid(row = 1, column = 5)
u8 = Label(window, text = "rb/stb").grid(row = 2, column = 5)
u9 = Label(window, text = "rb/scf").grid(row = 3, column = 5)
u10 = Label(window, text = "lbm/scf").grid(row = 4, column = 5)

#Create Scrolled Text Box
table1 = scrolledtext.ScrolledText(window, width=65, height=30)
table1.grid(column = 0, row = 9, columnspan = 8, rowspan = 8)
l11 = Label(window, text="---------------------------------------   Simulation Results   ---------------------------------------")
l11.grid(row = 7, column = 0, columnspan = 8)
l12 = Label(window, text="Num               Pressure               GOR               Oil FVF               Gas FVF               Gas Density")
l12.grid(row = 8, column = 0, columnspan = 8)

# Create Property Entries
press_text = StringVar()
e1 = Entry(window, textvariable = press_text)
e1.grid(row = 0, column = 1)
temp_text = StringVar()
e2 = Entry(window, textvariable = temp_text)
e2.grid(row = 1, column = 1)
oilsg_text = StringVar()
e3 = Entry(window, textvariable = oilsg_text)
e3.grid(row = 2, column = 1)
gassg_text = StringVar()
e4 = Entry(window, textvariable = gassg_text)
e4.grid(row = 3, column = 1)
zfac_text = StringVar()
e5 = Entry(window, textvariable = zfac_text)
e5.grid(row = 4, column = 1)

# Create Property Results
gor_text = StringVar()
e6 = Entry(window, textvariable = gor_text)
e6.grid(row = 0, column = 4)
pbub_text = StringVar()
e7 = Entry(window, textvariable = pbub_text)
e7.grid(row = 1, column = 4)
oilfvf_text = StringVar()
e8 = Entry(window, textvariable = oilfvf_text)
e8.grid(row = 2, column = 4)
gasfvf_text = StringVar()
e9 = Entry(window, textvariable = gasfvf_text)
e9.grid(row = 3, column = 4)
gasden_text = StringVar()
e10 = Entry(window, textvariable = gasden_text)
e10.grid(row = 4, column = 4)

# Create Command Buttons
b1 = Button(window, text = "Run\nCalculation", width = 10, command = calculation)
b1.grid(row = 0, column = 6, rowspan = 2)
b2 = Button(window, text = "Run\nSimulation", width = 10, command = simulation)
b2.grid(row = 2, column = 6, rowspan = 2)
b3 = Button(window, text = "Close", width = 10, command = window.destroy)
b3.grid(row = 4, column = 6, columnspan = 2)

#Display the Window from tkinter
window.config(menu = menubar)
window.mainloop()


# In[ ]:




