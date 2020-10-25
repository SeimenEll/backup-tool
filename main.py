import mainWindow
import sys
import csv
import os.path
from PyQt5 import QtCore, QtGui, QtWidgets


def append_backup_entry(backup_entry):
    # Open file in append mode
    with open('./backup.csv', 'a+', newline='') as backup_csv:
        csv_writer = csv.writer(backup_csv)
        csv_writer.writerow(backup_entry)


def load_backup_file_entry():
    # Open file in read mode
    with open('./backup.csv', 'r') as backup_csv:
        csv_reader = csv.reader(backup_csv, delimiter=',')
        line_count = 0
        for row in csv_reader:
            # first row contains no data
            if line_count > 0:
                # write source path into list widget
                ui.listDir.addItem(str(row[0]))
                # write destination path into label
                ui.labelBackupPath.setText(str(row[1]))
            line_count += 1


def add_directory():
    # Ask user for backup source directory
    backup_source = QtWidgets.QFileDialog.getExistingDirectory()
    # Add item to list
    ui.listDir.addItem(str(backup_source))
    # Ask user for backup destination directory
    backup_dest = QtWidgets.QFileDialog.getExistingDirectory()
    # Add item to backup path label
    ui.labelBackupPath.setText(str(backup_dest))
    ui.labelBackupPath.adjustSize()

    # Save backup tuple into backup file
    backup_entry = [str(backup_source), str(backup_dest)]
    append_backup_entry(backup_entry)


def change_backup_path():
    # Save old label text
    backup_dest_old = str(ui.labelBackupPath.text())
    # Ask user for backup destination directory
    backup_dest = str(QtWidgets.QFileDialog.getExistingDirectory())
    # Add item to backup path label
    ui.labelBackupPath.setText(backup_dest)
    ui.labelBackupPath.adjustSize()
    change_backup_entry(backup_dest_old, backup_dest)


# TODO: Search in backup file for old backup path and set it to new backup path.
def change_backup_entry(old, new):
    # Open file in read mode
    with open('./backup.csv', 'r') as backup_csv:
        csv_reader = csv.reader(backup_csv, delimiter=',')
        backup_lines = list(csv_reader)
        #print(backup_lines)
        #for row in backup_lines:

        #index_show = backup_lines.index(str(old))


def check_backup_file():
    if not os.path.exists('./backup.csv'):
        with open('backup.csv', 'w', newline='') as f:
            heading_entry = ['source', 'destination']
            csv_writer = csv.writer(f)
            csv_writer.writerow(heading_entry)


check_backup_file()
app = QtWidgets.QApplication(sys.argv)
mWin = QtWidgets.QMainWindow()
ui = mainWindow.Ui_MainWindow()
ui.setupUi(mWin)
# mWin = uic.loadUi("mainwindow.ui")
ui.btnAddDir.clicked.connect(add_directory)
ui.tbtnChangeBackup.clicked.connect(change_backup_path)

# Load all saved backup tuple entries
load_backup_file_entry()

mWin.show()
sys.exit(app.exec_())
