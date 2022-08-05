import sys
from PyQt5.QtWidgets import QApplication, QFileDialog, QMainWindow
from PyQt5 import uic
from Encoder import encoder
from Decoder import decoder

NoneEncAuth = 'Nan'
NoneDecAuth = 'Nan'



class Example(QMainWindow):

    def __init__(self):
        # FileIn = True
        # TextIn = False
        # FileOut = True
        super().__init__()
        uic.loadUi('InterFace.ui', self)  # Загружаем дизайн
        # TextOut = False
        self.CBEnc.activated.connect(self.ComboBoxEnc)
        self.CBDec.activated.connect(self.ComboBoxDec)
        self.EncFileBut.clicked.connect(self.Encode)
        self.DecFileBut.clicked.connect(self.Decode)
        self.EncTransf.clicked.connect(self.EncText)
        self.DecTransf.clicked.connect(self.DecText)
        self.FileRadioButtonEnc.status = 'File'
        self.TextRadioButtonEnc.status = 'Text'
        self.FileRadioButtonDec.status = 'File'
        self.TextRadioButtonDec.status = 'Text'
        self.ClearEncText.clicked.connect(self.ClearEnc)
        self.ClearDecText.clicked.connect(self.ClearDec)
        self.FileRadioButtonEnc.toggled.connect(lambda: self.FileClickedEnc())
        self.TextRadioButtonEnc.toggled.connect(lambda: self.TextClickedEnc())
        self.FileRadioButtonDec.toggled.connect(lambda: self.FileClickedDec())
        self.TextRadioButtonDec.toggled.connect(lambda: self.TextClickedDec())
        self.SaveFileEnc.clicked.connect(self.SaveFileEncF)
        self.SaveFileDec.clicked.connect(self.SaveFileDecF)
        self.SaveFileEnc.hide()
        self.SaveFileDec.hide()
        self.TextEncIn.hide()
        self.TextEncOut.hide()
        self.TextDecIn.hide()
        self.TextDecOut.hide()
        self.EncTransf.hide()
        self.DecTransf.hide()
        self.ClearEncText.hide()
        self.ClearDecText.hide()

        # self.initUI()

    def Decode(self):
        try:
            file_in = QFileDialog.getOpenFileName(self)[0]
            file_out = QFileDialog.getSaveFileName(self)[0]
            decoder(file_in, file_out, True, '')
            self.StatusLabel2.setText('Status: Success')
        except BaseException:
            self.StatusLabel2.setText('Status: Error')

    def Encode(self):
        try:
            file_in = QFileDialog.getOpenFileName(self)[0]
            file_out = QFileDialog.getSaveFileName(self)[0]
            encoder(file_in, file_out, True, '')
            print('end')
            self.StatusLabel1.setText('Status: Success')
        except BaseException:
            self.StatusLabel1.setText('Status: Error')

    def FileClickedEnc(self):
        if self.FileRadioButtonEnc.isChecked():
            self.EncFileBut.show()
            self.TextEncIn.hide()
            self.TextEncOut.hide()
            self.EncTransf.hide()
            self.SaveFileEnc.hide()
            self.ClearEncText.hide()

    def TextClickedEnc(self):
        if self.TextRadioButtonEnc.isChecked():
            self.EncFileBut.hide()
            self.TextEncIn.show()
            self.TextEncOut.show()
            self.EncTransf.show()
            self.ClearEncText.show()

    def FileClickedDec(self):
        if self.FileRadioButtonDec.isChecked():
            self.DecFileBut.show()
            self.TextDecIn.hide()
            self.TextDecOut.hide()
            self.DecTransf.hide()
            self.SaveFileDec.hide()
            self.ClearDecText.hide()

    def TextClickedDec(self):
        if self.TextRadioButtonDec.isChecked():
            self.DecFileBut.hide()
            self.TextDecIn.show()
            self.TextDecOut.show()
            self.DecTransf.show()
            self.ClearDecText.show()

    def EncText(self):
        self.TextEncOut.setText('')
        if NoneEncAuth == 'Nan':
            try:
                textenc = self.TextEncIn.toPlainText()
                listencout, textencout = encoder('', '', False, textenc)
                self.TextEncOut.setText(''.join(listencout) + '\n' + textencout)
                if self.TextEncOut.toPlainText() == '\n':
                    self.SaveFileEnc.hide()
                else:
                    self.SaveFileEnc.show()
                self.StatusLabel1.setText('Status: Success')
            except BaseException:
                self.StatusLabel1.setText('Status: Error')
        elif NoneEncAuth == 'Tol':
            try:
                textenc = self.TextEncIn.toPlainText()
                File = open('Tolstoy.txt', 'r', encoding='utf-8')
                dict_symb = {}
                txt = File.read().split('\n')
                File.close()
                for i in txt:
                    if i[0:2] == 'Li':
                        dict_symb['Line Break'] = i.split(' ')[3]
                    elif i[0] == ' ':
                        dict_symb[' '] = i[4::]
                    else:
                        dict_symb[i.split(' ')[0]] = i.split(' ')[2]
                textencoutlist = []
                textencoutlist2 = []
                for i in textenc:
                    if i == '\n':
                        textencoutlist.append(dict_symb['Line Break'])
                        textencoutlist2.append(f'Line Break : {dict_symb["Line Break"]}')
                    elif i == ' ':
                        textencoutlist.append(dict_symb[' '])
                        textencoutlist2.append(f'  : {dict_symb[" "]}')
                    else:
                        textencoutlist.append(dict_symb[i])
                        textencoutlist2.append(f'{i} : {dict_symb[i]}')
                textencout2 = '\n'.join(textencoutlist2)
                textencout = ''.join(textencoutlist)
                self.TextEncOut.setText(textencout2 + '\n\n' + textencout)
                if self.TextEncOut.toPlainText() == '':
                    self.SaveFileEnc.hide()
                else:
                    self.SaveFileEnc.show()
                self.StatusLabel1.setText('Status: Success')
            except BaseException:
                self.StatusLabel1.setText('Status: Error')
        elif NoneEncAuth == 'Dos':
            try:
                textenc = self.TextEncIn.toPlainText()
                File = open('Dostoevskiy.txt', 'r', encoding = 'utf-8')
                dict_symb = {}
                txt = File.read().split('\n')
                File.close()
                for i in txt:
                    if i[0:2] == 'Li':
                        dict_symb['Line Break'] = i.split(' ')[3]
                    elif i[0] == ' ':
                        dict_symb[' '] = i[4::]
                    else:
                        dict_symb[i.split(' ')[0]] = i.split(' ')[2]
                textencoutlist = []
                textencoutlist2 = []
                for i in textenc:
                    if i == '\n':
                        textencoutlist.append(dict_symb['Line Break'])
                        textencoutlist2.append(f'Line Break : {dict_symb["Line Break"]}')
                    elif i == ' ':
                        textencoutlist.append(dict_symb[' '])
                        textencoutlist2.append(f'  : {dict_symb[" "]}')
                    else:
                        textencoutlist.append(dict_symb[i])
                        textencoutlist2.append(f'{i} : {dict_symb[i]}')
                textencout2 = '\n'.join(textencoutlist2)
                textencout = ''.join(textencoutlist)
                self.TextEncOut.setText(textencout2 + '\n\n' + textencout)
                if self.TextEncOut.toPlainText() == '':
                    self.SaveFileEnc.hide()
                else:
                    self.SaveFileEnc.show()
                self.StatusLabel1.setText('Status: Success')
            except BaseException:
                self.StatusLabel1.setText('Status: Error')
        elif NoneEncAuth == 'Push':
            try:
                textenc = self.TextEncIn.toPlainText()
                File = open('Pushkin.txt', 'r', encoding = 'utf-8')
                dict_symb = {}
                txt = File.read().split('\n')
                File.close()
                for i in txt:
                    if i[0:2] == 'Li':
                        dict_symb['Line Break'] = i.split(' ')[3]
                    elif i[0] == ' ':
                        dict_symb[' '] = i[4::]
                    else:
                        dict_symb[i.split(' ')[0]] = i.split(' ')[2]
                textencoutlist = []
                textencoutlist2 = []
                for i in textenc:
                    if i == '\n':
                        textencoutlist.append(dict_symb['Line Break'])
                        textencoutlist2.append(f'Line Break : {dict_symb["Line Break"]}')
                    elif i == ' ':
                        textencoutlist.append(dict_symb[' '])
                        textencoutlist2.append(f'  : {dict_symb[" "]}')
                    else:
                        textencoutlist.append(dict_symb[i])
                        textencoutlist2.append(f'{i} : {dict_symb[i]}')
                textencout2 = '\n'.join(textencoutlist2)
                textencout = ''.join(textencoutlist)
                self.TextEncOut.setText(textencout2 + '\n\n' + textencout)
                if self.TextEncOut.toPlainText() == '':
                    self.SaveFileEnc.hide()
                else:
                    self.SaveFileEnc.show()
                self.StatusLabel1.setText('Status: Success')
            except BaseException:
                self.StatusLabel1.setText('Status: Error')


    def DecText(self):
        self.TextDecOut.setText('')
        if NoneDecAuth == 'Nan':
            try:
                textdec = self.TextDecIn.toPlainText()
                textdecout = decoder('', '', False, textdec)
                self.TextDecOut.setText(textdecout)
                if self.TextDecOut.toPlainText() == '':
                    self.SaveFileDec.hide()
                else:
                    self.SaveFileDec.show()
                self.StatusLabel2.setText('Status: Success')
            except BaseException:
                self.StatusLabel2.setText('Status: Error')
        elif NoneDecAuth == 'Tol':
            try:
                textdec = self.TextDecIn.toPlainText()
                File = open('Tolstoy.txt', 'r', encoding='utf-8')
                txt = File.read().split('\n')
                File.close()
                dict_symb = {}
                for i in txt:
                    if i[0:2] == 'Li':
                        dict_symb[i.split(' ')[3]] = 'Line Break'
                    elif i[0] == ' ':
                        dict_symb[i[4::]] = ' '
                    else:
                        dict_symb[i.split(' ')[2]] = i.split(' ')[0]
                list_out = []
                itr = ''
                for i in textdec:
                    itr += i
                    if itr in dict_symb:
                        if dict_symb[itr] == 'Line Break':
                            list_out.append('\n')
                        else:
                            list_out.append(dict_symb[itr])
                        itr = ''
                        continue
                textdecout = ''.join(list_out)
                self.TextDecOut.setText(textdecout)
                if self.TextDecOut.toPlainText() == '':
                    self.SaveFileDec.hide()
                else:
                    self.SaveFileDec.show()
                self.StatusLabel2.setText('Status: Success')
            except BaseException:
                self.StatusLabel2.setText('Status: Error')
        elif NoneDecAuth == 'Dos':
            try:
                textdec = self.TextDecIn.toPlainText()
                File = open('Dostoevskiy.txt', 'r', encoding='utf-8')
                txt = File.read().split('\n')
                File.close()
                dict_symb = {}
                for i in txt:
                    if i[0:2] == 'Li':
                        dict_symb[i.split(' ')[3]] = 'Line Break'
                    elif i[0] == ' ':
                        dict_symb[i[4::]] = ' '
                    else:
                        dict_symb[i.split(' ')[2]] = i.split(' ')[0]
                list_out = []
                itr = ''
                for i in textdec:
                    itr += i
                    if itr in dict_symb:
                        if dict_symb[itr] == 'Line Break':
                            list_out.append('\n')
                        else:
                            list_out.append(dict_symb[itr])
                        itr = ''
                        continue
                textdecout = ''.join(list_out)
                self.TextDecOut.setText(textdecout)
                if self.TextDecOut.toPlainText() == '':
                    self.SaveFileDec.hide()
                else:
                    self.SaveFileDec.show()
                self.StatusLabel2.setText('Status: Success')
            except BaseException:
                self.StatusLabel2.setText('Status: Error')
        elif NoneDecAuth == 'Push':
            try:
                textdec = self.TextDecIn.toPlainText()
                File = open('Pushkin.txt', 'r', encoding='utf-8')
                txt = File.read().split('\n')
                File.close()
                dict_symb = {}
                for i in txt:
                    if i[0:2] == 'Li':
                        dict_symb[i.split(' ')[3]] = 'Line Break'
                    elif i[0] == ' ':
                        dict_symb[i[4::]] = ' '
                    else:
                        dict_symb[i.split(' ')[2]] = i.split(' ')[0]
                list_out = []
                itr = ''
                for i in textdec:
                    itr += i
                    if itr in dict_symb:
                        if dict_symb[itr] == 'Line Break':
                            list_out.append('\n')
                        else:
                            list_out.append(dict_symb[itr])
                        itr = ''
                        continue
                textdecout = ''.join(list_out)
                self.TextDecOut.setText(textdecout)
                if self.TextDecOut.toPlainText() == '':
                    self.SaveFileDec.hide()
                else:
                    self.SaveFileDec.show()
                self.StatusLabel2.setText('Status: Success')
            except BaseException:
                self.StatusLabel2.setText('Status: Error')


    def SaveFileEncF(self):
        try:
            file_out = QFileDialog.getSaveFileName(self)[0]
            File = open(file_out, 'w', encoding = 'utf-8')
            File.write('CODE\n')
            File.write(self.TextEncOut.toPlainText())
            File.close()
            self.StatusLabel1.setText('Status: Success')
        except BaseException:
            self.StatusLabel1.setText('Status: Error')

    def SaveFileDecF(self):
        try:
            file_out = QFileDialog.getSaveFileName(self)[0]
            File = open(file_out, 'w', encoding = 'utf-8')
            File.write('TEXT\n')
            File.write(self.TextDecOut.toPlainText())
            File.close()
            self.StatusLabel2.setText('Status: Success')
        except BaseException:
            self.StatusLabel2.setText('Status: Error')




    def ComboBoxEnc(self, index):
        global NoneEncAuth
        if self.CBEnc.itemText(index) == 'W/O':
            NoneEncAuth = 'Nan'
        elif self.CBEnc.itemText(index) == 'Tolstoy L. N.':
            NoneEncAuth = 'Tol'
        elif self.CBEnc.itemText(index) == 'Dostoevskiy F. M.':
            NoneEncAuth = 'Dos'
        elif self.CBEnc.itemText(index) == 'Pushkin A. S.':
            NoneEncAuth = 'Push'

    def ComboBoxDec(self, index):
        global NoneDecAuth
        if self.CBDec.itemText(index) == 'W/O':
            NoneDecAuth = 'Nan'
        elif self.CBDec.itemText(index) == 'Tolstoy L. N.':
            NoneDecAuth = 'Tol'
        elif self.CBDec.itemText(index) == 'Dostoevskiy F. M.':
            NoneDecAuth = 'Dos'
        elif self.CBDec.itemText(index) == 'Pushkin A. S.':
            NoneDecAuth = 'Push'





    def ClearEnc(self):
        self.TextEncIn.setText('')
        self.TextEncOut.setText('')

    def ClearDec(self):
        self.TextDecIn.setText('')
        self.TextDecOut.setText('')




if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())