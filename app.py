import funciones
from datetime import datetime

while True:
  selection = funciones.print_menu_and_ask_for_selection()
  if (selection == '1'):
    status = funciones.ask_for_status()
    records = funciones.read_records(status)
    funciones.print_records(records)
  elif (selection == '2'):
    funciones.add_record({
      'Id': int(input('Id: ')),
      'Tarea': input('Tarea: '),
      'Descripcion': input('Descripcion: '),
      'Estado': input('Estado: '),
      'Fecha inicio': input('Fecha inicio [DD/MM/YYYY]: '),
      'Fecha finalizacion': input('Fecha finalizacion [DD/MM/YYYY]: '),
    })
  elif (selection == '3'):
    funciones.update_record(
      int(input('Ingrese id de la tarea a modificar: ')),
      {
      'Tarea': input('Tarea: '),
      'Descripcion': input('Descripcion: '),
      'Estado': input('Estado: '),
      'Fecha inicio': input('Fecha inicio [DD/MM/YYYY]: '),
      'Fecha finalizacion': input('Fecha finalizacion [DD/MM/YYYY]: '),
      }
    )
  elif (selection == '4'):
    funciones.delete_record(int(input('Ingrese el id de la tarea a eliminar: ')))
