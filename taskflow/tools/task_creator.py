import sys
import odoorpc

def create_task(db, user, password, host, port, title, description, state):

    odoo = odoorpc.ODOO(host, port=port)
    odoo.login(db, user, password)

    Task = odoo.env['taskflow.task']
    if state not in ['draft', 'progress', 'completed', 'cancel']:
        print("Estado inválido. Use un estado válido: 'draft', 'progress', 'completed' o 'cancel'.")
        return
    try:
        task_id = Task.create({
            'name': title,
            'description': description,
            'start_date': odoo.env['ir.fields'].today(),
            'end_date': odoo.env['ir.fields'].today() + odoo.env['ir.fields'].relativedelta(days=1),
            'state': state
        })
        print(f"Tarea creada exitosamente con ID: {task_id}")
    except Exception as e:
        print(f"Error al crear la tarea: {e}")





if __name__ == "__main__":
    if len(sys.argv) != 8:
        print("""
              Uso: python create_task.py <db> <user> <password> <host> <port> <titulo> <descripcion> <estado>
              Ejemplo: python create_task.py mydb admin admin localhost 8069 "Tarea de prueba" "Esta es una tarea de prueba" "progress"
              Por favor, proporcione los argumentos correctos.
              """)
    else:
        db = sys.argv[1]
        user = sys.argv[2]
        password = sys.argv[3]
        host = sys.argv[4]
        port = int(sys.argv[5])
        title = sys.argv[6]
        description = sys.argv[7]
        state = sys.argv[8]
        create_task(db, user, password, host, port, title, description, state)