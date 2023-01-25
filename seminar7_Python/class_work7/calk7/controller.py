# формируем кнопку. Связывает инициализатор *_model* и юзер-интерфейс ***_view***

import view, model
def init_data():
    a = view.input_data('A')
    b = view.input_data('B')
    model.init_a(a)
    model.init_b(b)

def print_values():
    a = model.get_a()
    b = model.get_b()
    view.print_consol(a)
    view.print_consol(b)


# def InitData() : 
#     a=View.inputData('A') 
#     b=View.inputData( ' B ' ) 
#     Mode1.InitA(a) 
#     Mode1.InitB(b)