{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "f58b1d4e",
   "metadata": {},
   "outputs": [],
   "source": [
    "import tkinter as tk\n",
    "\n",
    "# Function to update the display when a button is pressed\n",
    "def button_click(value):\n",
    "    current = display.get()\n",
    "    display.delete(0, tk.END)\n",
    "    display.insert(0, current + str(value))\n",
    "\n",
    "# Function to clear the display\n",
    "def button_clear():\n",
    "    display.delete(0, tk.END)\n",
    "\n",
    "# Function to calculate the result\n",
    "def button_equal():\n",
    "    try:\n",
    "        result = eval(display.get())\n",
    "        display.delete(0, tk.END)\n",
    "        display.insert(0, result)\n",
    "    except Exception as e:\n",
    "        display.delete(0, tk.END)\n",
    "        display.insert(0, \"Error\")\n",
    "\n",
    "# Creating the main window (root)\n",
    "root = tk.Tk()\n",
    "root.title(\"Calculator\")\n",
    "\n",
    "# Creating the display field (input box)\n",
    "display = tk.Entry(root, width=20, font=(\"Arial\", 24), borderwidth=2, relief=\"solid\", justify=\"right\")\n",
    "display.grid(row=0, column=0, columnspan=4)\n",
    "\n",
    "# Creating the buttons for the calculator\n",
    "buttons = [\n",
    "    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),\n",
    "    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),\n",
    "    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),\n",
    "    ('0', 4, 0), ('.', 4, 1), ('+', 4, 2), ('=', 4, 3),\n",
    "]\n",
    "\n",
    "# Adding the buttons to the window\n",
    "for (text, row, col) in buttons:\n",
    "    if text == \"=\":\n",
    "        button = tk.Button(root, text=text, width=5, height=2, font=(\"Arial\", 18), command=button_equal)\n",
    "    else:\n",
    "        button = tk.Button(root, text=text, width=5, height=2, font=(\"Arial\", 18), command=lambda t=text: button_click(t))\n",
    "    button.grid(row=row, column=col, padx=5, pady=5)\n",
    "\n",
    "# Creating the Clear button\n",
    "clear_button = tk.Button(root, text=\"C\", width=5, height=2, font=(\"Arial\", 18), command=button_clear)\n",
    "clear_button.grid(row=5, column=0, columnspan=4, pady=10)\n",
    "\n",
    "# Run the GUI\n",
    "root.mainloop()\n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "8c157956",
   "metadata": {},
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "base",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
