from thread.save_excel_thread import SaveThread

def action_save_excel_click(self):
    self.save_tread =  SaveThread(self.state.excel_path[0], self.state.data)
    self.save_tread.start()

def action_save_bd_click():
    print('action_save_bd_click')
