from PyQt5.QtWidgets import QTabWidget,QWidget,QApplication,QHBoxLayout,QMainWindow,QAction,QFormLayout,QDateEdit,QDateTimeEdit
from PyQt5.QtWidgets import QLabel,QLineEdit,QRadioButton,QPushButton,QMessageBox,QSpinBox,QVBoxLayout,QComboBox,QSpinBox
import sqlite3
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.create_menu()
        self.setMinimumSize(900,500)
        self.open=Window()
        self.setCentralWidget(self.open)
        self.show()

    def create_menu(self):
        menubar=self.menuBar()

        register=menubar.addMenu("Ekleme ve Kayıt")

        add_book=QAction("Kitap Ekle",self)
        add_member=QAction("Üye Ekle",self)

        operation=menubar.addMenu("Ödünç Verme Ve Teslim")

        barrow_book=QAction("Ödünç Verme",self)
        delivery_book=QAction("Teslim",self)



        settings=menubar.addMenu("Ayarlar") #Seçenekler de olabilir

        create_database=settings.addAction("Veritabanı Oluştur")
        #o dizinde olup olmadığını kontrol etmeli


        register.addAction(add_book)
        register.addAction(add_member)
        operation.addAction(barrow_book)
        operation.addAction(delivery_book)

        register.triggered.connect(self.response)
        operation.triggered.connect(self.response)


    def response(self,action):
        if action.text() == "Kitap Ekle":
            yazi=action.text()
            self.open.new_tab(add_book(),yazi)

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.tabwidget=QTabWidget()
        self.tabwidget.addTab(add_book(),"Kitap Ekle")
        self.tabwidget.setTabsClosable(True)
        h_box=QHBoxLayout()
        h_box.addWidget(self.tabwidget)
        self.setLayout(h_box)
        self.tabwidget.tabCloseRequested.connect(self.close_function)
        self.show()

    def close_function(self,index):
        self.tabwidget.removeTab(index)
    def new_tab(self,w_name,yazi):
        self.tabwidget.addTab(w_name,yazi)

class add_book(QWidget):
    def __init__(self):
        super().__init__()

        self.book_name=QLabel("Kitap İsmi")
        self.book_name_t=QLineEdit()

        self.book_author=QLabel("Yazar")
        self.book_author_t=QLineEdit()

        self.publishing_house=QLabel("Yayın Evi")
        self.publishing_house_t=QLineEdit()

        self.book_type=QLabel("Kitap Türü") #Combobox olmalı
        self.book_type_t=QLineEdit()

        self.isbn=QLabel("ISBN Numarası")
        self.isbn_t=QLineEdit()

        self.about_book=QLabel("Kitap Notu")
        self.about_book_t=QLineEdit()

        
        self.save_button=QPushButton("Kayıt Et")
        self.save_button.clicked.connect(self.save)

        f_box=QFormLayout()

        f_box.addWidget(self.book_name)
        f_box.addWidget(self.book_name_t)
        f_box.addWidget(self.book_author)
        f_box.addWidget(self.book_author_t)
        f_box.addWidget(self.publishing_house)
        f_box.addWidget(self.publishing_house_t)
        f_box.addWidget(self.book_type)
        f_box.addWidget(self.book_type_t)
        f_box.addWidget(self.isbn)
        f_box.addWidget(self.isbn_t)
        f_box.addWidget(self.save_button)

        self.setLayout(f_box)
        self.show()
    
    def save(self):pass

class add_member(QWidget):
    def __init__(self):
        super().__init__()

        self.name_surname=QLabel("Ad Soyad")
        self.name_surname_t=QLineEdit()

        self.phone_number=QLabel("Telefon Numarası")
        self.phone_number_t=QLineEdit()

        self.tc_number=QLabel("T.C. Kimlik Numarası")
        self.tc_number_t=QLineEdit()

        self.save_button=QPushButton("Kayıt Et")
        self.save_button.clicked.connect(self.save)

    def save(self):
        pass
        

class barrow_book(QWidget):
    def __init__(self):
        super().__init__()

        self.book_isbn=QLabel("Kitap ISBN")
        self.book_isbn_t=QLineEdit()






app = QApplication(sys.argv)
pencere = MainWindow()
sys.exit(app.exec_())








