import tkinter as tk
from tkinter.filedialog import askopenfilename, asksaveasfilename
import platform,socket,re,uuid,psutil,configparser

config = configparser.ConfigParser()

# Class for the about page
class about():
  def __init__(self) -> None:
      self = tk.Toplevel()
      label = tk.Label(self, text='Version: 0.1')
      platformlabel = tk.Label(self, text=f'Platform: {platform.system()}')
      releaselabel = tk.Label(self, text=f'Release: {platform.release()}')
      versionlabel = tk.Label(self, text=f'Version: {platform.version()}')
      architlabel = tk.Label(self, text=f'Proccessor Architecture: {platform.machine()}')
      hostnamelabel = tk.Label(self, text=f'Hostname: {socket.gethostname()}')
      nodelabel = tk.Label(self, text=f'Node Name: {platform.node()}')
      ipaddlabel = tk.Label(self, text=f'IP Address: {socket.gethostbyname(socket.gethostname())}')
      macaddlabel = tk.Label(self, text="Mac Address: "+':'.join(re.findall('..', '%012x' % uuid.getnode())))
      processorlabel = tk.Label(self, text=f'Processor: {platform.processor()}')
      ramlabel = tk.Label(self, text=str(round(psutil.virtual_memory().total / (1024.0 **3)))+" GB")
      self.title('About')
      label.pack()
      platformlabel.pack()
      releaselabel.pack()
      versionlabel.pack()
      architlabel.pack()
      hostnamelabel.pack()
      nodelabel.pack()
      ipaddlabel.pack()
      macaddlabel.pack()
      processorlabel.pack()
      ramlabel.pack()
      self.mainloop()

class configeditor():
  def __init__(self) -> None:
      editor = tk.Toplevel()
      editor.title("Simple Text Editor")

      editor.rowconfigure(0, minsize=800, weight=1)
      editor.columnconfigure(1, minsize=800, weight=1)

      txt_edit = tk.Text(editor)
      fr_buttons = tk.Frame(editor)
      btn_open = tk.Button(fr_buttons, text="Open", command=self.open_file(txt_edit))
      btn_save = tk.Button(fr_buttons, text="Save As...", command=self.save_file(txt_edit))
      btn_open.grid(row=0, column=0, sticky="ew", padx=5, pady=5)
      btn_save.grid(row=1, column=0, sticky="ew", padx=5)

      fr_buttons.grid(row=0, column=0, sticky="ns")
      txt_edit.grid(row=0, column=1, sticky="nsew")
  
  def open_file(wtf,txt_edit):
    """Open a file for editing."""
    '''filepath = askopenfilename(
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
    )
    print(filepath)
    print(type(filepath))'''
    filepath = 'config.ini'
    if not filepath:
        return
    txt_edit.delete("1.0", tk.END)
    with open(filepath, "r") as input_file:
        text = input_file.read()
        txt_edit.insert(tk.END, text)
    window.title(f"Simple Text Editor - {filepath}")
  
  def save_file(wtf,txt_edit):
    """Save the current file as a new file."""
    '''filepath = asksaveasfilename(
        defaultextension="txt",
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")],
    )'''
    filepath = 'config.ini'
    if not filepath:
        return
    with open(filepath, "w") as output_file:
        text = txt_edit.get("1.0", tk.END)
        output_file.write(text)
    window.title(f"Simple Text Editor - {filepath}")

def CreateConfig():
    config['Steam'] = {'WebAPIkey': '',
                        'SteamID': '',
                        'UseAuthToken': 'False'}
    config['MongoDBinfo'] = {'UseMongo': 'True',
                        'ClientAddress': '',
                        'ClientPort': '27017',
                        'DBName': ''}
    config['MySQLDBinfo'] = {'UseMySQL': 'False',
                        'ClientAddress': '',
                        'ClientPort': '',
                        'DBName': ''}
    config['AWSDBinfo'] = {'UseAWS': 'False',
                        'ClientAddress': '',
                        'ClientPort': '',
                        'DBName': ''}
    config['OracleDBinfo'] = {'UseOracle': 'False',
                        'ClientAddress': '',
                        'ClientPort': '',
                        'DBName': ''}
    config['PostgreDBinfo'] = {'UsePostgre': 'False',
                        'ClientAddress': '',
                        'ClientPort': '',
                        'DBName': ''}
    with open('config.ini', 'w') as configfile:
        config.write(configfile)

window = tk.Tk()
buttonconfigedit = tk.Button(text='Config Editor', command=lambda: configeditor())
buttoncreatconfig = tk.Button(text='Make Config', command=lambda: CreateConfig())
buttonabout = tk.Button(text='About', command=lambda: about())
buttonexit = tk.Button(text='Exit', command=lambda: exit(1))
buttonconfigedit.pack()
buttoncreatconfig.pack()
buttonabout.pack()
buttonexit.pack()
window.title('GUI Testing')
window.mainloop()
