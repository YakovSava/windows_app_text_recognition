import customtkinter

from tkinter.messagebox import showwarning, showerror, showinfo

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("blue")

app = customtkinter.CTk()
app.geometry("600x600")
app.title('Text recognition')

def check_internet():
	data = entry_downoload_language.get()
	if (data == 'rus'):
		showerror(
			title='Stop war!',
			message='Stop war in Ukraine!'
		)
	elif (data not in ['eng']):
		showwarning(
			title='Not supported!',
			message=f'This lang ({data}) not supported in this app!'
		)
	else:
		showinfo(
			title='Supported!',
			message=f'This lang ({data}) supported in this app!'
		)

customtkinter.CTkLabel(master=app, justify=customtkinter.LEFT, text='This is a photo text recognition app.\n\
The text can be either copied or saved to a file.', compound='right').place(x=0, y=0)

customtkinter.CTkLabel(master=app, justify=customtkinter.LEFT, text='In the window below, you can enter your language\n\
(in the form of a three-letter ISO-639-3 style designation)', compound='left').place(x=0, y=50)

customtkinter.CTkButton(master=app, command=check_internet, text='Downoload lang', compound='left').place(x=0, y=80)
entry_downoload_language = customtkinter.CTkEntry(master=app, placeholder_text="Entry your lang")
entry_downoload_language.place(x=0, y=110)

customtkinter.CTkLabel(master=app, justify=customtkinter.LEFT, text='(Downloading a language model requires internet)', compound='left').place(x=300, y=0)

change_lang = customtkinter.CTkOptionMenu(app, values=["eng", "rus", "fra", "deu"])
change_lang.place(x=300, y=30)
change_lang.set("Change language")

