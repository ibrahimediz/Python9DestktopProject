class Ui_Hastane(object):
    def setupUi(self, Hastane):
        Hastane.setObjectName("Hastane")
        Hastane.resize(438, 505)
        self.centralwidget = QtWidgets.QWidget(Hastane)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 10, 431, 451))
        self.tabWidget.setTabPosition(QtWidgets.QTabWidget.North)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.tab)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 411, 431))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.gridLayout_5 = QtWidgets.QGridLayout()
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.tableView = QtWidgets.QTableView(self.verticalLayoutWidget)
        self.tableView.setObjectName("tableView")
        self.gridLayout_5.addWidget(self.tableView, 0, 0, 1, 1)
        self.verticalLayout_2.addLayout(self.gridLayout_5)
        self.formLayout_5 = QtWidgets.QFormLayout()
        self.formLayout_5.setObjectName("formLayout_5")
        self.calendarWidget = QtWidgets.QCalendarWidget(self.verticalLayoutWidget)
        self.calendarWidget.setObjectName("calendarWidget")
        self.formLayout_5.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.calendarWidget)
        self.pushButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton.setObjectName("pushButton")
        self.formLayout_5.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.pushButton)
        self.verticalLayout_2.addLayout(self.formLayout_5)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.formLayoutWidget_2 = QtWidgets.QWidget(self.tab_2)
        self.formLayoutWidget_2.setGeometry(QtCore.QRect(10, 10, 411, 401))
        self.formLayoutWidget_2.setObjectName("formLayoutWidget_2")
        self.formLayout_6 = QtWidgets.QFormLayout(self.formLayoutWidget_2)
        self.formLayout_6.setContentsMargins(0, 0, 0, 0)
        self.formLayout_6.setObjectName("formLayout_6")
        self.label = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.label.setObjectName("label")
        self.formLayout_6.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.label_2 = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.label_2.setObjectName("label_2")
        self.formLayout_6.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.label_3 = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.label_3.setObjectName("label_3")
        self.formLayout_6.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.label_4 = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.label_4.setObjectName("label_4")
        self.formLayout_6.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.label_5 = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.label_5.setObjectName("label_5")
        self.formLayout_6.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_5)
        self.label_6 = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.label_6.setObjectName("label_6")
        self.formLayout_6.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.label_6)
        self.tableWidget = QtWidgets.QTableWidget(self.formLayoutWidget_2)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.formLayout_6.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.tableWidget)
        self.label_7 = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.label_7.setObjectName("label_7")
        self.formLayout_6.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.label_7)
        self.lineEdit = QtWidgets.QLineEdit(self.formLayoutWidget_2)
        self.lineEdit.setObjectName("lineEdit")
        self.formLayout_6.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.lineEdit)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.formLayoutWidget_2)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.formLayout_6.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.lineEdit_2)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.formLayoutWidget_2)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.formLayout_6.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.lineEdit_3)
        self.lineEdit_4 = QtWidgets.QLineEdit(self.formLayoutWidget_2)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.formLayout_6.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.lineEdit_4)
        self.comboBox = QtWidgets.QComboBox(self.formLayoutWidget_2)
        self.comboBox.setObjectName("comboBox")
        self.formLayout_6.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.comboBox)
        self.pushButton_2 = QtWidgets.QPushButton(self.formLayoutWidget_2)
        self.pushButton_2.setObjectName("pushButton_2")
        self.formLayout_6.setWidget(7, QtWidgets.QFormLayout.FieldRole, self.pushButton_2)
        self.pushButton_3 = QtWidgets.QPushButton(self.formLayoutWidget_2)
        self.pushButton_3.setObjectName("pushButton_3")
        self.formLayout_6.setWidget(8, QtWidgets.QFormLayout.FieldRole, self.pushButton_3)
        self.tabWidget.addTab(self.tab_2, "")
        Hastane.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Hastane)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 438, 18))
        self.menubar.setObjectName("menubar")
        self.menu_lemler = QtWidgets.QMenu(self.menubar)
        self.menu_lemler.setObjectName("menu_lemler")
        Hastane.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Hastane)
        self.statusbar.setObjectName("statusbar")
        Hastane.setStatusBar(self.statusbar)
        self.doktorislem = QtWidgets.QAction(Hastane)
        self.doktorislem.setObjectName("doktorislem")
        self.action_la_lemleri = QtWidgets.QAction(Hastane)
        self.action_la_lemleri.setObjectName("action_la_lemleri")
        self.actionRandevu_lemleri = QtWidgets.QAction(Hastane)
        self.actionRandevu_lemleri.setObjectName("actionRandevu_lemleri")
        self.menu_lemler.addAction(self.doktorislem)
        self.menu_lemler.addAction(self.action_la_lemleri)
        self.menu_lemler.addAction(self.actionRandevu_lemleri)
        self.menubar.addAction(self.menu_lemler.menuAction())

        self.retranslateUi(Hastane)
        self.tabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(Hastane)

    def retranslateUi(self, Hastane):
        _translate = QtCore.QCoreApplication.translate
        Hastane.setWindowTitle(_translate("Hastane", "MainWindow"))
        self.pushButton.setText(_translate("Hastane", "Randevu Al"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Hastane", "Randevular"))
        self.label.setText(_translate("Hastane", "HastaID"))
        self.label_2.setText(_translate("Hastane", "TC Kimlik"))
        self.label_3.setText(_translate("Hastane", "Adı"))
        self.label_4.setText(_translate("Hastane", "Soyadı"))
        self.label_5.setText(_translate("Hastane", "Tel"))
        self.label_6.setText(_translate("Hastane", "Poliklinik"))
        self.label_7.setText(_translate("Hastane", "0"))
        self.pushButton_2.setText(_translate("Hastane", "Kaydet"))
        self.pushButton_3.setText(_translate("Hastane", "Yeni"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("Hastane", "Hasta İşlemleri"))
        self.menu_lemler.setTitle(_translate("Hastane", "İşlemler"))
        self.doktorislem.setText(_translate("Hastane", "Doktor İşlemleri"))
        self.action_la_lemleri.setText(_translate("Hastane", "İlaç İşlemleri"))
        self.actionRandevu_lemleri.setText(_translate("Hastane", "Randevu İşlemleri"))