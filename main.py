from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.button import MDRectangleFlatButton
from kivymd.uix.filechooser import MDFileChooserIconView
from plyer import share
import img2pdf
import os

class RootWidget(MDBoxLayout):
    def convert_and_share(self):
        app = MDApp.get_running_app()
        user_data_dir = app.user_data_dir
        temp_pdf_path = os.path.join(user_data_dir, "temp.pdf")
        
        # Get selected files from FileChooser
        filechooser = self.ids.filechooser
        selected_files = [os.path.join(filechooser.path, f) for f in filechooser.selection]
        
        if not selected_files:
            return
        
        # Convert images to PDF
        with open(temp_pdf_path, "wb") as f:
            f.write(img2pdf.convert(selected_files))
        
        # Share the PDF
        share.share(file_path=temp_pdf_path, subject="Converted PDF", content="Here's your PDF")

class MyApp(MDApp):
    def build(self):
        self.load_kv('main.kv')
        return RootWidget()

if __name__ == "__main__":
    MyApp().run()
