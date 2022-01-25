import sys

import pandas as pd
from PyQt5 import QtWidgets

import option_widget
from Model__Options import OptionsModel


class OptionWidget(QtWidgets.QWidget):
    def __init__(self, strategy: str, data_df: pd.DataFrame, instr_df: pd.DataFrame):
        super(OptionWidget, self).__init__()

        # ---------- basic data modifications ---------------
        max_min_size = 300
        self.strategy = strategy
        self.opt_df: 'pd.DataFrame' = data_df
        self.instr_df: 'pd.DataFrame' = instr_df

        # ------------- widget customizations and initialization -----------
        self.ui = option_widget.Ui_Form()
        self.ui.setupUi(self)
        self.setMinimumHeight(max_min_size)
        self.setMaximumHeight(max_min_size)

        # ------------ create model ------------
        name_exp_df = self.instr_df[self.instr_df['name'].isin(self.opt_df['name'].values)].loc[:, ["name", "expiry"]]
        self.options_model = OptionsModel(name_exp_df)

        # ------------ process data -------------
        _unique_symb_names = self.opt_df['name'].values.tolist()
        self.options_model.update_model(_unique_symb_names[0])  # explicitly update model with current selection

        # ------------ data mapping ---------------
        self.ui.label_strategy_name.setText(f"<h2>{strategy}</h2>")

        self.ui.comboBox_symb_name.addItems(_unique_symb_names)
        # add selection change signal to filter other combobox
        self.ui.comboBox_symb_name.currentIndexChanged[str].connect(lambda x: self.options_model.update_model(x))
        self.ui.comboBox_expiry_date.setModel(self.options_model)
        self.ui.comboBox_atm_option.addItems(("ATM-1", "ATM", "ATM+1"))

        self.ui.comboBox_symb_name.setCurrentIndex(0)  # show the name, that is used to set filter initially


class Window(QtWidgets.QMainWindow):
    def __init__(self):
        super(Window, self).__init__()

        self.vboxLayout = QtWidgets.QVBoxLayout()
        self.central_widget = QtWidgets.QWidget()
        self.central_widget.setLayout(self.vboxLayout)
        self.setCentralWidget(self.central_widget)

        # ----------- load files from user's local directory -----------
        self.instr_df = pd.read_csv("name_exp.csv")
        self.opt_df = pd.read_csv("another_file.csv")

        # ----------- add a widget frame --------
        self.add_strategy_option()

    def add_strategy_option(self):
        _widget = OptionWidget(strategy="Title", data_df=self.opt_df, instr_df=self.instr_df)
        self.vboxLayout.addWidget(_widget)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    w = Window()
    w.show()
    sys.exit(app.exec_())
