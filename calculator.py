import tkinter as tk
import ttkbootstrap as ttk

previous_entry = ''
operator = ''
calculator_finished = False

# single function for all number buttons
def on_button_pressed(button):
    global previous_entry
    global operator
    global calculator_finished
    if calculator_finished:
        calculator_finished = False
        output_text.set('')
    current_text = output_field.get()
    if button in ['1','2','3','4','5','6','7','8','9','0','.']:
        if '.' in current_text and button == '.':
            return
        current_text += button
        output_text.set(current_text)
    elif button in ['/','*','-','+']:
        # save previous entry for calculating, save operator, and clear for next entry
        previous_entry = output_field.get()
        output_text.set('')
        operator = button
    elif button == '=':
        if previous_entry:
            result = ''
            if operator == '+':
                result = float(previous_entry) + float(current_text)
            elif operator == '-':
                result = float(previous_entry) - float(current_text)
            elif operator == '*':
                result = float(previous_entry) * float(current_text)
            elif operator == '/':
                if current_text == '0':
                    output_text.set("Error: division by 0")
                    return
                result = float(previous_entry) / float(current_text)
            output_text.set(str(result))
            calculator_finished = True
    elif button == 'clear entry':
        output_text.set('')
    elif button == 'clear':
        output_text.set('')
        previous_entry = ''
        operator = ''
    elif button == 'delete':
        current_text = current_text[:-1]
        output_text.set(current_text)
    elif button == 'inverse':
        if current_text:
            current_text = str(int(current_text) * -1)
            output_text.set(current_text)


app = ttk.Window(themename= 'darkly')
app.title("Calculator")
app.geometry("420x540")



output_text = ttk.StringVar()
output_field = ttk.Entry(app, font = 'Calibri 24', justify = 'right', textvariable= output_text)
ttk.Style().configure('light.Outline.TButton', font=('Calibri', 30))
ttk.Style().configure('darkly.TButton', font=('Calibri', 30))

b_clear_entry = ttk.Button(app, text = 'CE', style='light.Outline.TButton', width= 3, command= lambda: on_button_pressed('clear entry'))

b_clear_all = ttk.Button(app, text= 'C', style= 'light.Outline.TButton', width= 3, command= lambda: on_button_pressed('clear'))

b_delete = ttk.Button(app, text= '<-', style= 'light.Outline.TButton', width= 3, command= lambda: on_button_pressed('delete'))

b_division = ttk.Button(app, text= '/', style= 'light.Outline.TButton', width= 3, command= lambda: on_button_pressed('/'))

b_7 = ttk.Button(app, text= '7', style= 'light.Outline.TButton', width= 3, command= lambda: on_button_pressed('7'))

b_8 = ttk.Button(app, text= '8', style= 'light.Outline.TButton', width= 3, command= lambda: on_button_pressed('8'))

b_9 = ttk.Button(app, text= '9', style= 'light.Outline.TButton', width= 3, command= lambda: on_button_pressed('9'))

b_multiply = ttk.Button(app, text= 'x', style= 'light.Outline.TButton', width= 3, command= lambda: on_button_pressed('*'))

b_4 = ttk.Button(app, text= '4', style= 'light.Outline.TButton', width= 3, command= lambda: on_button_pressed('4'))

b_5 = ttk.Button(app, text= '5', style= 'light.Outline.TButton', width= 3, command= lambda: on_button_pressed('5'))

b_6 = ttk.Button(app, text= '6', style= 'light.Outline.TButton', width= 3, command= lambda: on_button_pressed('6'))

b_subtract = ttk.Button(app, text= '-', style= 'light.Outline.TButton', width= 3, command= lambda: on_button_pressed('-'))

b_1 = ttk.Button(app, text= '1', style= 'light.Outline.TButton', width= 3, command= lambda: on_button_pressed('1'))

b_2 = ttk.Button(app, text= '2', style= 'light.Outline.TButton', width= 3, command= lambda: on_button_pressed('2'))

b_3 = ttk.Button(app, text= '3', style= 'light.Outline.TButton', width= 3, command= lambda: on_button_pressed('3'))

b_addition = ttk.Button(app, text= '+', style= 'light.Outline.TButton', width= 3, command= lambda: on_button_pressed('+'))

b_inverse = ttk.Button(app, text= '+-', style= 'light.Outline.TButton', width= 3, command= lambda: on_button_pressed('inverse'))

b_0 = ttk.Button(app, text= '0', style= 'light.Outline.TButton', width= 3, command= lambda: on_button_pressed('0'))

b_decimal = ttk.Button(app, text= '.', style= 'light.Outline.TButton', width= 3, command= lambda: on_button_pressed('.'))

b_calculate = ttk.Button(app, text= '=', style= 'light.Outline.TButton', width= 3, command= lambda: on_button_pressed('='))

output_field.grid(row = 0, column = 0, columnspan= 4)
b_clear_entry.grid(row=1, column= 0)
b_clear_all.grid(row= 1, column= 1)
b_delete.grid(row= 1, column= 2)
b_division.grid(row=1, column= 3)
b_7.grid(row=2, column= 0)
b_8.grid(row=2, column = 1)
b_9.grid(row=2, column= 2)
b_multiply.grid(row=2, column = 3)
b_4.grid(row=3, column = 0)
b_5.grid(row=3,column=1)
b_6.grid(row=3,column=2)
b_subtract.grid(row=3,column=3)
b_1.grid(row=4,column=0)
b_2.grid(row=4,column=1)
b_3.grid(row=4,column=2)
b_addition.grid(row=4,column=3)
b_inverse.grid(row=5,column=0)
b_0.grid(row=5,column=1)
b_decimal.grid(row=5,column=2)
b_calculate.grid(row=5,column=3)


col_count, row_count = app.grid_size()
for col in range(col_count):
    app.grid_columnconfigure(col, minsize=80)

for row in range(row_count):
    app.grid_rowconfigure(row, minsize=80)


app.mainloop()
