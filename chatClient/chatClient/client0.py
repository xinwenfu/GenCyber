#!/usr/bin/python3

######################
# based on https://www.geeksforgeeks.org/gui-chat-application-using-tkinter-in-python/

# run a python script in terminal without the python command
# Use a shebang line at the "start" of your script:
# #!/usr/bin/python3

# make the file executable:
# chmod +x arbitraryname

# if necessary, put it in a directory on your PATH (can be a symlink):
# cd ~/bin/
##################################

# import all the required modules
import socket
import threading
from tkinter import *
from tkinter import font
from tkinter import ttk
from tkinter import messagebox
import os

# import all functions /
# everthing from chat.py file?
# from chat import *

PORT = 9999
SERVER = "10.0.2.7"
ADDRESS = (SERVER, PORT)
FORMAT = "utf-8"

# Create a new client socket
# and connect to the server
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)




# GUI class for the chat
class GUI:
	# constructor method
	def __init__(self):
		
		# chat window which is currently hidden
		self.Window = Tk()
		self.Window.withdraw()
		#Position the window
		self.Window.geometry("+100+50")              

		
		# login window
		self.login = Toplevel()
		# set the title
		self.login.title("Login")
		self.login.resizable(width = True, height = True)
		self.login.configure(width = 400, height = 300)
                
		# Position the login window
		self.login.geometry("+50+25")

		# create a Label
		self.pls = Label(self.login,
					text = "Please login to continue",
					justify = CENTER,
					font = "Helvetica 14 bold")
		self.pls.place(relheight = 0.15,
					relx = 0.1,
					rely = 0.02)
		# create a Label
		self.labelName = Label(self.login,
				       text = "Your Name: ",
				       font = "Helvetica 12")		
		self.labelName.place(relheight = 0.2,
				     relx = 0.1,
				     rely = 0.2)
		# create a entry box for typing the message
		self.entryName = Entry(self.login, font = "Helvetica 14")
		self.entryName.place(relwidth = 0.4,
				     relheight = 0.12,
				     relx = 0.35,
				     rely = 0.2)
		# set the focus of the curser
		self.entryName.focus()

		# create a IP label
		self.labelIP = Label(self.login,
				       text = "IP: ",
				       font = "Helvetica 12")		
		self.labelIP.place(relheight = 0.2,
				     relx = 0.1,
				     rely = 0.35)
		# create a entry box for typing IP
		self.entryIP = Entry(self.login, font = "Helvetica 14")
		self.entryIP.place(relwidth = 0.4,
				     relheight = 0.12,
				     relx = 0.35,
				     rely = 0.35)
		self.entryIP.insert(END, SERVER)

		# create a port label
		self.labelPort = Label(self.login,
				       text = "Port: ",
				       font = "Helvetica 12")		
		self.labelPort.place(relheight = 0.2,
				     relx = 0.1,
				     rely = 0.5)
		# create a entry box for typing port
		self.entryPort = Entry(self.login, font = "Helvetica 14")
		self.entryPort.place(relwidth = 0.4,
				     relheight = 0.12,
				     relx = 0.35,
				     rely = 0.5)
		self.entryPort.insert(END, PORT)
                
                
		# create a Continue Button along with action
		self.go = Button(self.login,
				 text = "CONTINUE",
				 font = "Helvetica 14 bold",
				 command = lambda: self.goAhead(self.entryName.get()))	
		self.go.place(relx = 0.6,
			      rely = 0.85)

		self.Window.protocol("WM_DELETE_WINDOW", self.on_close_window)
		self.login.protocol("WM_DELETE_WINDOW", self.on_close_login)
		self.Window.mainloop()
                
	def on_close_login(self):
#                if messagebox.askokcancel("Quit", "Do you want to quit?"):
                        self.login.destroy()
                        #message="EXIT"
                        #client.send(message.encode(FORMAT))
                        client.close()
                        #exit(0) # this exit will hang over there because of the receiving thread
                        os._exit(0) # this exit will exit everything including threas; 

	def on_close_window(self):
 #               if messagebox.askokcancel("Quit", "Do you want to quit?"):
                        self.Window.destroy()
                        message="EXIT"
                        client.send(message.encode(FORMAT))
                        client.close()
                        #exit(0)
                        os._exit(1)

                        
	def goAhead(self, name):
		SERVER=self.entryIP.get()
		PORT=int(self.entryPort.get())

		self.login.destroy()
		self.layout(name)

		client.connect(ADDRESS)

		# the thread to receive messages
		rcv = threading.Thread(target=self.receive)
		rcv.start()

	# The main layout of the chat
	def layout(self,name):
		
		self.name = name
		# to show chat window
		self.Window.deiconify()
		self.Window.title("GenCyber Chat Room")
		self.Window.resizable(width = True,
				      height = True)
		self.Window.configure(width = 470,
				      height = 350,
				      bg = "#17202A")
                
               
		self.labelHead = Label(self.Window,
				       bg = "#17202A",
				       fg = "#EAECEE",
				       text = self.name ,
				       font = "Helvetica 12 bold",
				       pady = 5)
		
		self.labelHead.place(relwidth = 1)
		self.line = Label(self.Window,
				  width = 450,
				  bg = "#ABB2B9")
		
		self.line.place(relwidth = 1,
				rely = 0.07,
				relheight = 0.012)
		
		self.textCons = Text(self.Window,
				     width = 20,
				     height = 2,
				     bg = "#17202A",
				     fg = "#EAECEE",
				     font = "Helvetica 12",
				     padx = 5,
				     pady = 5)
		
		self.textCons.place(relheight = 0.745,
				    relwidth = 1,
				    rely = 0.08)

		self.the_menu = Menu(self.textCons, tearoff=0)
		self.the_menu.add_command(label="Cut")
		self.the_menu.add_command(label="Copy")
		self.the_menu.add_command(label="Paste")

                # Enable copy and paste of text in the Text class
		self.textCons.bind_class("Text", "<Button-3><ButtonRelease-3>", self.show_menu)
 		
		self.labelBottom = Label(self.Window,
					 bg = "#ABB2B9",
					 height = 80)
		
		self.labelBottom.place(relwidth = 1,
				       rely = 0.825)
		
		self.entryMsg = Entry(self.labelBottom,
				      bg = "#2C3E50",
				      fg = "#EAECEE",
				      font = "Helvetica 12")
		
		# place the given widget
		# into the gui window
		self.entryMsg.place(relwidth = 0.74,
				    relheight = 0.03,
				    rely = 0.008,
				    relx = 0.011)
		
		self.entryMsg.focus()
		
		# create a Send Button
		self.buttonMsg = Button(self.labelBottom,
					text = "Send",
					font = "Helvetica 10 bold",
					width = 20,
					bg = "#ABB2B9",
					command = lambda : self.sendButton(self.entryMsg.get()))
		
		self.buttonMsg.place(relx = 0.77,
				     rely = 0.008,
				     relheight = 0.03,
				     relwidth = 0.22)
		
		self.textCons.config(cursor = "arrow")
		
		# create a scroll bar
		scrollbar = Scrollbar(self.textCons)
		
		# place the scroll bar
		# into the gui window
		scrollbar.place(relheight = 1, relx = 0.974)
		
		scrollbar.config(command = self.textCons.yview)
		
		self.textCons.config(state = DISABLED)

	def show_menu(self, e):
                w = e.widget
                self.the_menu.entryconfigure("Cut", command=lambda: w.event_generate("<<Cut>>"))
                self.the_menu.entryconfigure("Copy", command=lambda: w.event_generate("<<Copy>>"))
                self.the_menu.entryconfigure("Paste", command=lambda: w.event_generate("<<Paste>>"))
                self.the_menu.tk.call("tk_popup", self.the_menu, e.x_root, e.y_root)
        
	# function to basically start the thread for sending messages
	def sendButton(self, msg):
		self.textCons.config(state = DISABLED)
		self.msg=msg
		self.entryMsg.delete(0, END)
		snd= threading.Thread(target = self.sendMessage)
		snd.start()

	# function to receive messages
	def receive(self):
		while True:
			try:
				message = client.recv(1024).decode(FORMAT)
				
				# if the messages from the server is NAME send the client's name
				if message == 'NAME':
					client.send(self.name.encode(FORMAT))
				else:
					# insert messages to text box
					self.textCons.config(state = NORMAL)
					self.textCons.insert(END, message+"\n")
					
					self.textCons.config(state = DISABLED)
					self.textCons.see(END)
			except:
				# an error will be printed on the command line or console if there's an error
				print("An error occured!")
				client.close()
				break
		
	# function to send messages
	def sendMessage(self):
		self.textCons.config(state=DISABLED)
		while True:
			message = (f"<Me>: {self.msg}")

 			# insert messages to text box
			self.textCons.config(state = NORMAL)
			self.textCons.insert(END, message+"\n")
					
			self.textCons.config(state = DISABLED)
			self.textCons.see(END)

			message = (f"KNOCK {self.name}: {self.msg}")

			client.send(message.encode(FORMAT))	
                        
			break	
                
# create a GUI class object
g = GUI()
