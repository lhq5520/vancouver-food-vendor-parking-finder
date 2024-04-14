from views.input_view import *
from views.output_view import *
from utils.model_helper import *
from views.data_frame import *
from views.map import *

def run_view_gui_all_parking_info():
    all_parking_info = get_all_parking_info()
    view_gui_all_parking_info(all_parking_info)

def main():
    gui_main_menu(run_view_gui_all_parking_info())

if __name__ == '__main__':
    main()