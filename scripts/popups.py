import tkinter as tk
from tkinter import ttk


class SelectDialog():
    """
        Creates a temporary popup box and returns the user
        input to the calling function

        Parameters:
        text (string) - Message to be displayed
        options (list) - Options for the user to choose from
        result (empty list) - output is returned through this list
        op_type (str) - should be either 'radiobutton' or 'checkbox'
        root (tk.tk()) - tk() object which would be set as master
    """
    def __init__(self, text, options, result, op_type, root=None):

        assert len(options) != 0, "Empty choice list!"
        assert (
                op_type == 'checkbox' or
                op_type == 'radiobutton'), "Invalid choice type!"

        self.root = root
        self.top = tk.Toplevel(self.root)
        choices = []
        # Create frame for message
        msg_frame = tk.Frame(self.top, borderwidth=5, relief='ridge')
        msg_frame.pack(fill='both', expand=True)
        # Create label for the message
        label = tk.Label(msg_frame, text=text)
        label.grid(row=0, column=0, columnspan=3, padx=4, pady=4)
        # Create button to submit
        ok_btn = tk.Button(msg_frame, text="Ok", width=5, height=1)
        ok_btn.grid(row=len(options)+1, column=1, pady=2)
        # Create the widgets for user choices
        if op_type == 'checkbox':
            self.check_var = []
            for i, value in enumerate(options, 1):
                self.check_var.append(tk.IntVar())
                choices.append(tk.Checkbutton(
                                              msg_frame, text=value,
                                              variable=self.check_var[i]))
                choices[-1].deselect()
                choices[-1].grid(row=i, column=1, pady=2, sticky=(tk.W))
            ok_btn['command'] = lambda: self._cb_submit(result)
        else:
            self.var = tk.StringVar()
            for i, value in enumerate(options, 1):
                choices.append(tk.Radiobutton(
                                              msg_frame, text=value,
                                              variable=self.var,
                                              value=value, indicatoron=True))
                choices[-1].grid(row=i, column=1, pady=2, sticky=(tk.W))
            self.var.set(options[0])
            ok_btn['command'] = lambda: self._rb_submit(result)
        # Put window on top
        self.top.transient(self.root)
        self.top.grab_set()

    def _cb_submit(self, result):
        """Call back for Ok button for checkbox input"""
        for var in self.check_var:
            result.append(var.get() == 1)
        self.top.destroy()

    def _rb_submit(self, result):
        """Call back for Ok button for radiobutton input"""
        result.append(self.var.get())
        self.top.destroy()


class GetNumInput():
    """
        Creates a temporary popup box to request the user
        to input a number
    """
    def __init__(self, text, range_, result, root):
        assert len(range_) != 0, "Empty choice list!"
        self.root = root
        self.top = tk.Toplevel(self.root)
        # Create frame for message
        msg_frame = tk.Frame(self.top, borderwidth=5, relief='ridge')
        msg_frame.pack(fill='both', expand=True)
        # Create label for the message
        label = tk.Label(msg_frame, text=text)
        label.pack(padx=4, pady=4)
        # Create combobox for user choices
        self.usr_input = tk.StringVar()
        choices = ttk.Combobox(
                               msg_frame, textvariable=self.usr_input,
                               values=range_, state="readonly")
        choices.current(0)
        choices.pack()
        # Create button to submit
        ok_btn = tk.Button(msg_frame, text="Ok", width=5, height=1)
        ok_btn['command'] = lambda: self._choice_submit(result)
        ok_btn.pack(side=tk.BOTTOM, padx=4, pady=4)
        # Put window on top
        self.top.transient(self.root)
        self.top.grab_set()

    def _choice_submit(self, result):
        """Call back for Ok button"""
        try:
            result.append(int(self.usr_input.get()))
        except ValueError:
            result.append(self.usr_input.get())
        self.top.destroy()
