import sys

from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog
from PyQt5.QtWidgets import QTableWidgetItem

from MainWindowDesign import Ui_MainWindow
from InsertWindowDesign import Ui_InsertDialogWindow
from ParentTableDialogWindowDesign import Ui_ParentTableWindow
from NoDeletableWindowDesign import Ui_NoDeletableDialogWindow
from InsertParentWindowDesign import Ui_InsertParentDialogWindow
from NoUniqueDialogWindow import Ui_NoUniqueDialogWindow
from SearchWindowDesign import Ui_SearchDialogWindow
from UpdateWindow import Ui_UpdateWindow
from UpdateParentWindowDesign import Ui_UpdateParentDialogWindow
from Connection import DataBase


class PhoneBook(QMainWindow):
    def __init__(self):
        super(PhoneBook, self).__init__()

        # Подключаем и создаем главное окно
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Подключаем и создаем диалоговое окно добавления элемента
        self.insert_window = QDialog()
        self.ui_insert_dialog = Ui_InsertDialogWindow()
        self.ui_insert_dialog.setupUi(self.insert_window)

        # Подключаем и создаем диалоговое окно поиска
        self.search_window = QDialog()
        self.ui_search_dialog = Ui_SearchDialogWindow()
        self.ui_search_dialog.setupUi(self.search_window)

        # Подключаем и создаем диалоговое окно изменения
        self.update_window = QDialog()
        self.ui_update_dialog = Ui_UpdateWindow()
        self.ui_update_dialog.setupUi(self.update_window)

        # Подключаем и создаем окно родительских таблиц
        self.parent_window = QDialog()
        self.ui_parent_dialog = Ui_ParentTableWindow()
        self.ui_parent_dialog.setupUi(self.parent_window)

        # Подключаем и создаем окно предупреждения о невозможности удаления элемента из родительской таблицы
        self.nodeletable_window = QDialog()
        self.ui_nodeletable_dialog = Ui_NoDeletableDialogWindow()
        self.ui_nodeletable_dialog.setupUi(self.nodeletable_window)

        # Подключаем и создаем окно добавления элемента родительской таблицы
        self.insert_parent_window = QDialog()
        self.ui_insert_parent_dialog = Ui_InsertParentDialogWindow()
        self.ui_insert_parent_dialog.setupUi(self.insert_parent_window)

        # Подключаем и создаем окно изменения элемента родительской таблицы
        self.update_parent_window = QDialog()
        self.ui_update_parent_dialog = Ui_UpdateParentDialogWindow()
        self.ui_update_parent_dialog.setupUi(self.update_parent_window)

        # Подключаем и создаем окно предупреждения о невозможности добавления элемента в родительскую таблицу
        self.nounique_window = QDialog()
        self.ui_nounique_dialog = Ui_NoUniqueDialogWindow()
        self.ui_nounique_dialog.setupUi(self.nounique_window)

        # Подключаемся к БД
        self.database = DataBase()

        # Показываем данные из БД
        self.view_main_data()

        # Проверяем нажатие кнопки Добавить главного окна
        self.ui.InsertButton.clicked.connect(self.insert_button_clicked)

        # Проверяем нажатие кнопки Удалить текущую строку главного окна
        self.ui.DeleteButton.clicked.connect(self.delete_button_clicked)

        # Проверяем нажатие кнопки Изменить текущую строку главного окна
        self.ui.UpdateButton.clicked.connect(self.update_button_clicked)

        # Проверяем нажатие кнопки Поиск главного окна
        self.ui.SearchButton.clicked.connect(self.search_button_clicked)

        # Проверяем нажатие кнопки Остановить поиск главного окна
        self.ui.StopSeacrhButton.clicked.connect(self.stop_search_button_clicked)

        # Проверяем нажатие кнопки Показать родительскую таблицу
        self.ui.ShowParentTableButton.clicked.connect(self.show_parent_table_window_button_clicked)

        # Проверяем нажатие кнопки Сохранить в окне добавления контакта
        self.ui_insert_dialog.InsertSaveButton.clicked.connect(self.insert_window_save_button_clicked)

        # Проверяем нажатие кнопки Удалить в окне родительской таблицы
        self.ui_parent_dialog.ParentTableDeleteButton.clicked.connect(self.parent_window_delete_button_clicked)

        # Проверяем нажатие кнопки Добавить в окне родительской таблицы
        self.ui_parent_dialog.ParentTableInsertButton.clicked.connect(self.parent_window_insert_button_clicked)

        # Проверяем нажатие кнопки Изменить в окне родительской таблицы
        self.ui_parent_dialog.ParentTableUpdateButton.clicked.connect(self.parent_window_update_button_clicked)

        # Проверяем нажатие кнопки Cохранить в окне добавления родительской таблицы
        self.ui_insert_parent_dialog.SaveParentButton.clicked.connect(self.insert_parent_window_save_button_clicked)

        # Проверяем нажатие кнопки Cохранить в окне изменения родительской таблицы
        self.ui_update_parent_dialog.SaveParentButton.clicked.connect(self.update_parent_window_save_button_clicked)

        # Проверяем нажатие кнопки Искать в окне поиска
        self.ui_search_dialog.SearchBeginButton.clicked.connect(self.search_begin_button_clicked)

        # Проверяем нажатие кнопки Сохранить в окне изменения элемента главной таблицы
        self.ui_update_dialog.SaveButton.clicked.connect(self.update_window_save_button_clicked)

        # Переменная для хранения id
        self.current_id = 0

        # Переменная для хранения изменяемой строки
        self.updating_row = -1

        # Переменная для хранения выбранной родительской таблицы
        self.selected_parent = "Фамилии"

        # Переменная для хранения id родительской таблицы
        self.current_parent_id = 0

        # Переменная для хранения изменяемой строки родительской таблицы
        self.updating_parent_row = -1

    def view_main_data(self):
        data = self.database.get_full_table()

        rows_number = 0
        for row in data:
            self.ui.DataTable.setRowCount(rows_number + 1)
            for i in range(len(row)):
                item = QTableWidgetItem()
                item.setText(str(row[i]))
                self.ui.DataTable.setItem(rows_number, i, item)
            rows_number += 1

    def open_insert_window(self):
        self.clear_insert_window()
        self.fill_insert_window_comboboxes()
        self.insert_window.show()

    def insert_window_save_button_clicked(self):
        new_element = [self.ui_insert_dialog.FamilyComboBox.currentText(),
                       self.ui_insert_dialog.NameComboBox.currentText(),
                       self.ui_insert_dialog.OtcComboBox.currentText(),
                       self.ui_insert_dialog.StreetComboBox.currentText(),
                       self.ui_insert_dialog.BldnInput.text(),
                       self.ui_insert_dialog.Bldn_hInput.text(),
                       self.ui_insert_dialog.ApprInput.text(),
                       self.ui_insert_dialog.PhoneInput.text()]
        self.database.insert_element_to_main(new_element)
        self.ui.DataTable.clearContents()
        self.view_main_data()
        self.insert_window.close()

    def insert_button_clicked(self):
        self.open_insert_window()

    def delete_button_clicked(self):
        row = self.ui.DataTable.currentRow()
        if row != -1:
            item = self.ui.DataTable.item(row, 0)
            self.database.delete_element_from_main(item.text())
            self.ui.DataTable.removeRow(row)

    def show_parent_table_window_button_clicked(self):
        self.selected_parent = self.ui.ShowParentComboBox.currentText()
        parent = self.ui.ShowParentComboBox.currentText()
        self.ui_parent_dialog.ParentTableWindowName.setText(parent)
        self.view_parent_data(parent)
        self.parent_window.show()

    def view_parent_data(self, parent):
        item = QTableWidgetItem()
        item.setText("ID")
        self.ui_parent_dialog.ParentTable.setHorizontalHeaderItem(0, item)
        item = QTableWidgetItem()
        if parent == 'Фамилии':
            data = self.database.get_families_table()
            item.setText("Фамилия")
            self.ui_parent_dialog.ParentTable.setHorizontalHeaderItem(1, item)
        elif parent == 'Имена':
            data = self.database.get_names_table()
            item.setText("Имя")
            self.ui_parent_dialog.ParentTable.setHorizontalHeaderItem(1, item)
        elif parent == 'Отчества':
            data = self.database.get_otchestvo_table()
            item.setText("Отчество")
            self.ui_parent_dialog.ParentTable.setHorizontalHeaderItem(1, item)
        else:
            data = self.database.get_streets_table()
            item.setText("Улица")
            self.ui_parent_dialog.ParentTable.setHorizontalHeaderItem(1, item)

        rows_number = 0
        for row in data:
            self.ui_parent_dialog.ParentTable.setRowCount(rows_number + 1)
            for i in range(len(row)):
                item = QTableWidgetItem()
                item.setText(str(row[i]))
                self.ui_parent_dialog.ParentTable.setItem(rows_number, i, item)
            rows_number += 1

    def parent_window_delete_button_clicked(self):
        parent = self.ui_parent_dialog.ParentTableWindowName.text()
        row = self.ui_parent_dialog.ParentTable.currentRow()
        if row != -1:
            item = self.ui_parent_dialog.ParentTable.item(row, 1)
            deletable = self.database.element_deletable(item.text())
            if deletable:
                item = self.ui_parent_dialog.ParentTable.item(row, 0)
                self.database.delete_element_from_parent_table(parent, item.text())

                self.ui_parent_dialog.ParentTable.clearContents()
                self.view_parent_data(parent)
            else:
                self.nodeletable_window.show()

    def parent_window_insert_button_clicked(self):
        self.open_insert_parent_window()

    def fill_update_parent_window(self):
        if self.selected_parent == "Фамилии":
            self.ui_update_parent_dialog.UpdateWindowName.setText("Изменение фамилии")
        elif self.selected_parent == "Имена":
            self.ui_update_parent_dialog.UpdateWindowName.setText("Изменение имени")
        elif self.selected_parent == "Отчества":
            self.ui_update_parent_dialog.UpdateWindowName.setText("Изменение отчества")
        else:
            self.ui_update_parent_dialog.UpdateWindowName.setText("Изменение улицы")

        item = self.ui_parent_dialog.ParentTable.item(self.updating_parent_row, 1)
        self.ui_update_parent_dialog.ParentInput.setText(item.text())

    def parent_window_update_button_clicked(self):
        self.updating_parent_row = self.ui_parent_dialog.ParentTable.currentRow()
        if self.updating_parent_row != -1:
            item = self.ui_parent_dialog.ParentTable.item(self.updating_parent_row, 0)
            self.current_parent_id = int(item.text())

            self.fill_update_parent_window()
            self.update_parent_window.open()

    def update_parent_window_save_button_clicked(self):
        element = self.ui_update_parent_dialog.ParentInput.text()
        if self.database.element_unique(self.selected_parent, element):
            self.database.update_element_in_parent(self.selected_parent, element, self.current_parent_id)
            self.ui_parent_dialog.ParentTable.clearContents()
            self.view_parent_data(self.selected_parent)
            self.update_parent_window.close()
            self.ui.DataTable.clearContents()
            self.view_main_data()
        else:
            self.nounique_window.show()

    def open_insert_parent_window(self):
        self.clear_insert_parent_window()
        if self.selected_parent == "Фамилии":
            self.ui_insert_parent_dialog.InsertWindowName.setText("Добавление фамилии")
        elif self.selected_parent == "Имена":
            self.ui_insert_parent_dialog.InsertWindowName.setText("Добавление имени")
        elif self.selected_parent == "Отчества":
            self.ui_insert_parent_dialog.InsertWindowName.setText("Добавление отчества")
        else:
            self.ui_insert_parent_dialog.InsertWindowName.setText("Добавление улицы")

        self.insert_parent_window.show()

    def insert_parent_window_save_button_clicked(self):
        element = self.ui_insert_parent_dialog.ParentInput.text()
        if self.database.element_unique(self.selected_parent, element):
            self.database.insert_element_to_parent_table(self.selected_parent, element)
            self.ui_parent_dialog.ParentTable.clearContents()
            self.view_parent_data(self.selected_parent)
            self.insert_parent_window.close()
        else:
            self.nounique_window.show()

    def fill_insert_window_comboboxes(self):
        data = self.database.get_families()
        for i in range(len(data)):
            self.ui_insert_dialog.FamilyComboBox.addItem(data[i][0], userData=None)

        data = self.database.get_names()
        for i in range(len(data)):
            self.ui_insert_dialog.NameComboBox.addItem(data[i][0], userData=None)

        data = self.database.get_otchestvo()
        for i in range(len(data)):
            self.ui_insert_dialog.OtcComboBox.addItem(data[i][0], userData=None)

        data = self.database.get_streets()
        for i in range(len(data)):
            self.ui_insert_dialog.StreetComboBox.addItem(data[i][0], userData=None)

    def clear_insert_window(self):
        self.ui_insert_dialog.FamilyComboBox.clear()
        self.ui_insert_dialog.NameComboBox.clear()
        self.ui_insert_dialog.OtcComboBox.clear()
        self.ui_insert_dialog.StreetComboBox.clear()
        self.ui_insert_dialog.BldnInput.clear()
        self.ui_insert_dialog.Bldn_hInput.clear()
        self.ui_insert_dialog.ApprInput.clear()
        self.ui_insert_dialog.PhoneInput.clear()

    def clear_insert_parent_window(self):
        self.ui_insert_parent_dialog.ParentInput.clear()

    def search_button_clicked(self):
        self.open_search_window()

    def open_search_window(self):
        self.search_window.open()

    def clear_search_window(self):
        self.ui_search_dialog.FamiyInput.clear()
        self.ui_search_dialog.NameInput.clear()
        self.ui_search_dialog.OtcInput.clear()
        self.ui_search_dialog.StreetInput.clear()
        self.ui_search_dialog.BldnInput.clear()
        self.ui_search_dialog.Bldn_hInput.clear()
        self.ui_search_dialog.ApprInput.clear()
        self.ui_search_dialog.PhoneInput.clear()

    def view_search_data(self, data):
        rows_number = 0
        for row in data:
            self.ui.DataTable.setRowCount(rows_number + 1)
            for i in range(len(row)):
                item = QTableWidgetItem()
                item.setText(str(row[i]))
                self.ui.DataTable.setItem(rows_number, i, item)
            rows_number += 1

    def search_begin_button_clicked(self):
        data = [self.ui_search_dialog.FamiyInput.text(),
                self.ui_search_dialog.NameInput.text(),
                self.ui_search_dialog.OtcInput.text(),
                self.ui_search_dialog.StreetInput.text(),
                self.ui_search_dialog.BldnInput.text(),
                self.ui_search_dialog.Bldn_hInput.text(),
                self.ui_search_dialog.ApprInput.text(),
                self.ui_search_dialog.PhoneInput.text()]
        results = self.database.search_elements_in_main(data)
        self.ui.DataTable.clearContents()
        self.view_search_data(results)
        self.search_window.close()

    def stop_search_button_clicked(self):
        self.ui.DataTable.clearContents()
        self.view_main_data()

    def update_button_clicked(self):
        self.updating_row = self.ui.DataTable.currentRow()
        if self.updating_row != -1:
            item = self.ui.DataTable.item(self.updating_row, 0)
            self.current_id = int(item.text())
            self.set_elements_to_update(self.updating_row)
            self.update_window.open()

    def set_elements_to_update(self, row):
        item = self.ui.DataTable.item(row, 5)
        self.ui_update_dialog.BldnInput.setText(item.text())
        item = self.ui.DataTable.item(row, 6)
        self.ui_update_dialog.Bldn_hInput.setText(item.text())
        item = self.ui.DataTable.item(row, 7)
        self.ui_update_dialog.ApprInput.setText(item.text())
        item = self.ui.DataTable.item(row, 8)
        self.ui_update_dialog.PhoneInput.setText(item.text())

    def update_window_save_button_clicked(self):
        elements = [self.ui_update_dialog.BldnInput.text(),
                    self.ui_update_dialog.Bldn_hInput.text(),
                    self.ui_update_dialog.ApprInput.text(),
                    self.ui_update_dialog.PhoneInput.text()]
        self.database.update_element_in_main(self.current_id, elements)
        item = self.ui.DataTable.item(self.updating_row, 5)
        item.setText(elements[0])
        item = self.ui.DataTable.item(self.updating_row, 6)
        item.setText(elements[1])
        item = self.ui.DataTable.item(self.updating_row, 7)
        item.setText(elements[2])
        item = self.ui.DataTable.item(self.updating_row, 8)
        item.setText(elements[3])
        self.update_window.close()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = PhoneBook()
    window.show()

    sys.exit(app.exec())
