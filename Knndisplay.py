import Tkinter as tk
import csv
class Knndisplay(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
	t = SimpleTable(self,9,7)
	t.pack(side="top", fill="x")
	t.set(0,0,"k-value")
class SimpleTable(tk.Frame):
   def __init__(self, parent, rows=7, columns=6):
        # use black background so it "peeks through" to 
        # form grid lines
		
        tk.Frame.__init__(self, parent, background="black")
        self._widgets = []
	with open("metrics.csv",'rb') as csvfile:
		lines=csv.reader(csvfile)
		dataset=list(lines)
	dataset.insert(0,["accuracy","error rate","sensitivity","specificity","precision","F-value"])
	for row in range(rows):
		current_row = []
		dataset[row].insert(0,'-1')
		for column in range(columns):
			if row is 0 and column is 0:
				label = tk.Label(self, text="%s" % ("k value"), borderwidth=0, width=10)
			if column is 0 and row>0:
				label = tk.Label(self, text="%s" % ("k="+str(2*row-1)), borderwidth=0, width=10)
			elif row is 0:
				label = tk.Label(self, text="%s" %(dataset[row][column]), borderwidth=0, width=10)
			elif column >0:
				j="%0.3f" %float(dataset[row][column])
				label = tk.Label(self, text="%s" %(str(j)), borderwidth=0, width=10)
			label.grid(row=row, column=column, sticky="nsew", padx=1, pady=1)
			current_row.append(label)
		self._widgets.append(current_row)
	for column in range(columns):
		self.grid_columnconfigure(column, weight=1)
   def set(self, row, column, value):
		widget = self._widgets[row][column]
		widget.configure(text=value)
		
def display_knn():
    app = Knndisplay()
    app.mainloop()
			
			
			
			