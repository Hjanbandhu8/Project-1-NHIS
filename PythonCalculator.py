from tkinter import *
from customtkinter import *
import re

root = Tk()
root.geometry('400x500')
root.title('Harshal Calculator')
#this action will display the input given by the user in input box
def display_input(_input):
    
    input_box.insert(index=INSERT, string=_input)
    display_result()
 #this function will do the calculation of the input and show the result in result label the if else statement is used to show the result only after mathematical calculation   
def display_result():
    try:
        calculation = input_box.get()
        
        if re.search(pattern=r'[\+\-\*\%/]', string = calculation):
          result=eval(calculation)
          result_lb.config(text=f'= {result}')
        else:
            result_lb.config(text='')  
    except  Exception as error:
        print(error)
#This function will delete the recent input
def delete_input():
    index = input_box.index(INSERT)-1
    input_box.delete(index)
    display_result()
#This function will clear the entire mathematical operation
def clear_input():
    input_box.delete(0, END)
    result_lb.config(text='')
    
    input_box.config(font=('Bold',20))
    result_lb.config(font=('Bold',15))    
#This function is used to mainstream the result after complete calculation
def highlight_result():
    input_box.config(font=('Bold',15))
    result_lb.config(font=('Bold',25))
#This function is used to change the theme of the calculator
def theme_changing():
    if root.cget('bg') == 'SystemButtonFace':
        
        root.tk_setPalette('Black')
        input_box.config(bg='black')
        result_lb.config(bg='black')
        theme_btn.config(text='🌞')
    else:
        root.tk_setPalette('SystemButtonFace')
        theme_btn.config(text='🌙')

# Function to handle deleting the number after a special character
def delete_after_special():
    current = input_box.get()
    special_characters = ['+', '-', '*', '/']
    
    # Find the index of the first special character
    for char in special_characters:
        if char in current:
            # Find the position of the special character and keep everything before it
            index = current.index(char)
            input_box.delete(0, END)
            input_box.insert(END, current[:index+1])  # Keep the special character too
            display_result()
            return
    
    # If no special character is found, do nothing
    return


input_box = Entry(root, font=('Bold',20), justify = RIGHT , bd = 0, bg = 'LAVENDER')
input_box.place(x=15, y=10, width=360, height =50)

result_lb=Label(root, font=('Bold',15), anchor=E , bg='LAVENDER')
result_lb.place(x=15, y=60, width=360, height = 40)

clear_btn = CTkButton(master= root, text='C', width=40, height =40, font=('Bold',30), fg_color='PURPLE', command=clear_input)
clear_btn.place(x=15, y=135)

delete_btn = CTkButton(master= root, text='D', width=40, height =40, font=('Bold',30), fg_color='PURPLE', command=delete_input)
delete_btn.place(x=70, y=135)

percent_btn = CTkButton(master= root, text='%', width=40, height =40, font=('Bold',30), command= lambda: display_input(_input='%'), fg_color='PURPLE')
percent_btn.place(x=125, y=135)

divide_btn = CTkButton(master= root, text='÷', width=40, height =40, font=('Bold',30), command= lambda: display_input(_input='/'), fg_color='PURPLE')
divide_btn.place(x=180, y=135)

btn7_btn = CTkButton(master= root, text='7', width=40, height =40, font=('Bold',30), command= lambda: display_input(_input='7'))
btn7_btn.place(x=15, y=210)

btn8_btn = CTkButton(master= root, text='8', width=40, height =40, font=('Bold',30), command= lambda: display_input(_input='8'))
btn8_btn.place(x=70, y=210)

btn9_btn = CTkButton(master= root, text='9', width=40, height =40, font=('Bold',30), command= lambda: display_input(_input='9'))
btn9_btn.place(x=125, y=210)

multiply_btn = CTkButton(master= root, text='x', width=40, height =40, font=('Bold',30), command= lambda: display_input(_input='*'), fg_color='PURPLE')
multiply_btn.place(x=180, y=210)

btn6_btn = CTkButton(master= root, text='6', width=40, height =40, font=('Bold',30), command= lambda: display_input(_input='6'))
btn6_btn.place(x=15, y=285)

btn5_btn = CTkButton(master= root, text='5', width=40, height =40, font=('Bold',30), command= lambda: display_input(_input='5'))
btn5_btn.place(x=70, y=285)

btn4_btn = CTkButton(master= root, text='4', width=40, height =40, font=('Bold',30), command= lambda: display_input(_input='4'))
btn4_btn.place(x=125, y=285)

Subs_btn = CTkButton(master= root, text='-', width=40, height =40, font=('Bold',30), command= lambda: display_input(_input='-'), fg_color='PURPLE')
Subs_btn.place(x=180, y=285)

btn3_btn = CTkButton(master= root, text='3', width=40, height =40, font=('Bold',30), command= lambda: display_input(_input='3'))
btn3_btn.place(x=15, y=360)

btn2_btn = CTkButton(master= root, text='2', width=40, height =40, font=('Bold',30), command= lambda: display_input(_input='2'))
btn2_btn.place(x=70, y=360)

btn1_btn = CTkButton(master= root, text='1', width=40, height =40, font=('Bold',30), command= lambda: display_input(_input='1'))
btn1_btn.place(x=125, y=360)

Add_btn = CTkButton(master= root, text='+', width=40, height =40, font=('Bold',30), command= lambda: display_input(_input='+') ,fg_color='PURPLE')
Add_btn.place(x=180, y=360)

theme_btn = Button(root, text='🌙', font=('Bold',30), command=theme_changing)
theme_btn.place(x=15, y= 435,width=40, height = 50)

btn0_btn = CTkButton(master= root, text='0', width=40, height =40, font=('Bold',30), command= lambda: display_input(_input='0'))
btn0_btn.place(x=70, y=435)

btndec_btn = CTkButton(master= root, text='.', width=40, height =40, font=('Bold',30), command= lambda: display_input(_input='.'))
btndec_btn.place(x=125, y=435)

equal_btn = CTkButton(master= root, text='=', width=40, height =40, font=('Bold',30), fg_color='PURPLE', command=highlight_result)
equal_btn.place(x=180, y=435)

NumC_btn = CTkButton(master= root, text='NumC', width=40, height =40, font=('Bold',30), fg_color='PURPLE', command=delete_after_special)
NumC_btn.place(x=235, y=135)


root.mainloop()