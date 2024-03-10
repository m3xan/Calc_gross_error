from window.second_windows.about_window.about_window import AboutDialog

def action_info_click(self):
    self.dialog = AboutDialog(self.state.user_id)
    return self.dialog.exec()
