import subprocess
from PySide6.QtWidgets import QApplication, QWidget, QFileDialog, QMessageBox
from PySide6.QtCore import QThread, QObject, Signal
from PySide6.QtGui import QPixmap
from UI_Pyside6 import UI, sub
from download import *


class Subwindow(QWidget):
    user = Signal(dict)

    def __init__(self):
        super().__init__()

        self.saveuser = SaveUser()
        self.user_thread = QThread()
        self.user.connect(self.saveuser.save_user)
        self.saveuser.completed.connect(self.complete_user)
        self.saveuser.moveToThread(self.user_thread)
        self.user_thread.start()

        self.ui = sub.Ui_Form()
        self.ui.setupUi(self)

        self.refresh()

        self.ui.label.setPixmap(QPixmap('user_cookie/re.png'))

        self.ui.pushButton.clicked.connect(self.refresh)

    def refresh(self):
        cook_data = ger_qrcode_url()
        make_qrcode(cook_data)
        self.ui.label.setPixmap(QPixmap('user_cookie/re.png'))
        self.user.emit(cook_data)

    def complete_user(self):
        self.user_thread.quit()
        self.user_thread.wait()


class SaveUser(QObject):
    completed = Signal(bool)

    def __init__(self):
        super().__init__()

    def save_user(self, cook_data):
        get_cookie(cook_data)
        self.completed.emit(True)


class Worker(QObject):
    progress = Signal(int)
    completed = Signal(bool)
    video_progress = Signal(int)

    def __init__(self):
        super().__init__()

    def audio_download(self, url, dire):
        html = (get_html(url))
        title = find_title(html)
        filename = replace_error_character(title)
        audio_url = get_audiodata(html)
        audio_content = requests.get(url=audio_url, headers=header, stream=True)
        content_size = float(audio_content.headers['Content-Length']) / 1024
        count = 0
        with open(dire + filename + '.mp3', 'wb') as audio:
            for chunk in audio_content.iter_content(chunk_size=1024):
                if chunk:
                    audio.write(chunk)
                    count += len(chunk)
                    v = count / content_size / 1024 * 100
                    self.progress.emit(v)

    def video_download(self, url, index, dire):
        html = (get_html(url))
        title = find_title(html)
        filename = replace_error_character(title)
        video_url = get_videodata(html, index)
        video_content = requests.get(url=video_url, headers=header, stream=True)
        content_size = float(video_content.headers['Content-Length']) / 1024
        count = 0
        with open(dire + filename + '.mp4', 'wb') as video:
            for chunk in video_content.iter_content(chunk_size=1024):
                if chunk:
                    video.write(chunk)
                    count += len(chunk)
                    v = count / content_size / 1024 * 100
                    self.video_progress.emit(v)
        cmd = f"ffmpeg -y -i {dire}{filename}.mp3 -i {dire}{filename}.mp4 -c:v copy -c:a aac -strict experimental {dire}{filename}compound.mp4"
        subprocess.run(cmd)
        self.completed.emit(True)


class Worker_2(QObject):
    audio_progress_2 = Signal(int)
    completed_2 = Signal(bool)
    video_progress_2 = Signal(int)

    def __init__(self):
        super().__init__()

    def audio_download(self, url, dire):
        html = (get_html(url))
        title = find_title(html)
        filename = replace_error_character(title)
        audio_url = get_audiodata(html)
        audio_content = requests.get(url=audio_url, headers=header, stream=True)
        content_size = float(audio_content.headers['Content-Length']) / 1024
        count = 0
        with open(dire + filename + '.mp3', 'wb') as audio:
            for chunk in audio_content.iter_content(chunk_size=1024):
                if chunk:
                    audio.write(chunk)
                    count += len(chunk)
                    v = count / content_size / 1024 * 100
                    self.audio_progress_2.emit(v)

    def video_download(self, url, index, dire):
        html = (get_html(url))
        title = find_title(html)
        filename = replace_error_character(title)
        video_url = get_videodata(html, index)
        video_content = requests.get(url=video_url, headers=header, stream=True)
        content_size = float(video_content.headers['Content-Length']) / 1024
        count = 0
        with open(dire + filename + '.mp4', 'wb') as video:
            for chunk in video_content.iter_content(chunk_size=1024):
                if chunk:
                    video.write(chunk)
                    count += len(chunk)
                    v = count / content_size / 1024 * 100
                    self.video_progress_2.emit(v)
        cmd = f"ffmpeg -y -i {dire}{filename}.mp3 -i {dire}{filename}.mp4 -c:v copy -c:a aac -strict experimental {dire}{filename}compound.mp4"
        subprocess.run(cmd)
        self.completed_2.emit(True)


class MyWindow(QWidget, UI.Ui_Form):
    audio_info = Signal(str, str)
    video_info = Signal(str, int, str)
    audio_info_2 = Signal(str, str)
    video_info_2 = Signal(str, int, str)

    def __init__(self):
        super().__init__()

        self.worker = Worker()
        self.worker_2 = Worker_2()
        self.saveuser = SaveUser()
        self.worker_2_thread = QThread()
        self.worker_thread = QThread()

        self.worker.progress.connect(self.updateProgress)

        self.worker.completed.connect(self.complete)
        self.worker_2.completed_2.connect(self.complete_2)

        self.worker.video_progress.connect(self.update_video_Progress)

        self.worker_2.audio_progress_2.connect(self.updateProgress_2)
        self.worker_2.video_progress_2.connect(self.updateProgress_3)

        self.audio_info.connect(self.worker.audio_download)
        self.video_info.connect(self.worker.video_download)

        self.audio_info_2.connect(self.worker_2.audio_download)
        self.video_info_2.connect(self.worker_2.video_download)

        self.worker.moveToThread(self.worker_thread)

        self.worker_2.moveToThread(self.worker_2_thread)

        self.setupUi(self)

        self.subwindow = Subwindow()

        self.lineEdit.setText(f'{os.getcwd()}/video/')
        self.makedir()

        self.conbind()

        self.hide()

    def makedir(self):
        try:
            os.mkdir(f'{os.getcwd()}/video/')
        except FileExistsError:
            pass

    def hide(self):
        self.radioButton.hide()
        self.label_16.hide()
        self.radioButton_2.hide()
        self.label_17.hide()
        self.radioButton_3.hide()
        self.label_18.hide()
        self.radioButton_4.hide()
        self.label_37.hide()

    def add_task(self):
        url = self.lineEdit_2.text()
        try:
            html = (get_html(url))
            title = find_title(html)
            index_text = resolution(html)
            self.settext(index_text)
            if not bool(self.label_5.text()):
                self.label_5.setText(url)
                self.label_5.setWordWrap(True)
                self.label_3.setText(title)
                self.label_3.setWordWrap(True)
            else:
                self.label_6.setText(url)
                self.label_6.setWordWrap(True)
                self.label_4.setText(title)
                self.label_4.setWordWrap(True)
                self.pushButton_4.setEnabled(False)
        except ValueError:
            QMessageBox.information(self, "温馨提示", "错误！", QMessageBox.Yes | QMessageBox.No)
        except IndexError:
            self.label_5.clear()
            self.label_3.clear()

    def settext(self, te):
        value = []
        for key in te.keys():
            value.append(key)
        value_indexes = []
        for value_index in te.values():
            value_indexes.append(value_index)
        if len(value) == 1:
            self.radioButton.setText(str(value[0]))
            self.label_16.setText(str(value_indexes[0]))
            self.radioButton.show()
        elif len(value) == 2:
            self.radioButton.setText(str(value[0]))
            self.label_16.setText(str(value_indexes[0]))
            self.radioButton.show()
            self.radioButton_2.setText(str(value[1]))
            self.label_17.setText(str(value_indexes[1]))
            self.radioButton_2.show()
        elif len(value) == 3:
            self.radioButton.setText(str(value[0]))
            self.label_16.setText(str(value_indexes[0]))
            self.radioButton.show()
            self.radioButton_2.setText(str(value[1]))
            self.label_17.setText(str(value_indexes[1]))
            self.radioButton_2.show()
            self.radioButton_3.setText(str(value[2]))
            self.label_18.setText(str(value_indexes[2]))
            self.radioButton_3.show()
        elif len(value) == 4:
            self.radioButton.setText(str(value[0]))
            self.label_16.setText(str(value_indexes[0]))
            self.radioButton.show()
            self.radioButton_2.setText(str(value[1]))
            self.label_17.setText(str(value_indexes[1]))
            self.radioButton_2.show()
            self.radioButton_3.setText(str(value[2]))
            self.label_18.setText(str(value_indexes[2]))
            self.radioButton_3.show()
            self.radioButton_4.setText(str(value[3]))
            self.label_37.setText(str(value_indexes[3]))
            self.radioButton_4.show()
        self.check()

    def conbind(self):
        self.radioButton.clicked.connect(self.check)
        self.radioButton_2.clicked.connect(self.check)
        self.radioButton_3.clicked.connect(self.check)
        self.radioButton_4.clicked.connect(self.check)

        self.pushButton.clicked.connect(self.save_dir)

        self.pushButton_2.clicked.connect(self.start)

        self.pushButton_3.clicked.connect(self.getImg)

        self.pushButton_4.clicked.connect(self.add_task)

        self.pushButton_5.clicked.connect(self.start_2)

    def check(self):
        if self.radioButton.isChecked():
            return int(self.label_16.text())
        elif self.radioButton_2.isChecked():
            return int(self.label_17.text())
        elif self.radioButton_3.isChecked():
            return int(self.label_18.text())
        elif self.radioButton_4.isChecked():
            return int(self.label_37.text())

    def start(self):
        self.worker_thread.start()
        url = self.label_5.text()
        index = self.check()
        dire = self.lineEdit.text()
        self.audio_info.emit(url, dire)
        self.video_info.emit(url, index, dire)

    def start_2(self):
        self.worker_2_thread.start()
        url = self.label_6.text()
        index = self.check()
        dire = self.lineEdit.text()
        self.audio_info_2.emit(url, dire)
        self.video_info_2.emit(url, index, dire)

    def complete(self):
        self.label_5.clear()
        self.worker_thread.quit()
        self.worker_thread.wait()

    def complete_2(self):
        self.label_6.clear()
        self.worker_2_thread.quit()
        self.worker_2_thread.wait()
        self.pushButton_4.setEnabled(True)

    def getImg(self):
        self.subwindow.show()

    def save_dir(self):
        save_dire = QFileDialog.getExistingDirectory(self, '保存路径')
        self.lineEdit.setText(f'{save_dire}/')
        return save_dire

    def updateProgress(self, v):
        self.progressBar.setValue(v)

    def updateProgress_2(self, v):
        self.progressBar_4.setValue(v)

    def updateProgress_3(self, v):
        self.progressBar_3.setValue(v)

    def update_video_Progress(self, v):
        self.progressBar_2.setValue(v)


if __name__ == "__main__":
    app = QApplication([])
    window = MyWindow()
    window.setWindowTitle('视频下载器')
    window.show()
    app.exec()
