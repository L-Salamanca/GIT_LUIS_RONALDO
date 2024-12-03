
# **NARUTOMANIA**  

Un proyecto inspirado en el universo de *Naruto*, enfocado en la gestión de información sobre ninjas y sus misiones. Esta aplicación ofrece un sistema robusto para administrar datos de manera eficiente y ordenada, utilizando Python y almacenamiento en archivos JSON.

---

## 📌 **Objetivos del Proyecto**  

- Crear un sistema CRUD para la gestión de ninjas y misiones.  
- Almacenar y recuperar datos de manera persistente.  
- Ofrecer una interfaz clara y fácil de usar.  
- Demostrar habilidades en desarrollo de aplicaciones con Python.  

---

## 🛠️ **Funcionalidades Principales**  

- **Registrar Ninjas:**  
  Agrega nuevos ninjas con detalles específicos:  
  - Nombre del ninja.  
  - Aldea de origen.  
  - Número de misiones completadas.  
  - Rango dentro de la jerarquía ninja.  

- **Gestionar Información:**  
  - **Actualizar Datos:** Modifica la información de los ninjas.  
  - **Eliminar Ninjas:** Borra registros antiguos o incorrectos.  
  - **Listar Ninjas:** Muestra una lista detallada y organizada de todos los ninjas registrados.  

- **Administrar Misiones:**  
  - Asigna nuevas misiones a los ninjas.  
  - Realiza un seguimiento detallado de cada misión.  

---

## 📂 **Estructura del Proyecto**  

```plaintext
NARUTOMANIA/
│
├── README.md          # Documentación del proyecto  
├── menu.py            # Archivo principal del programa  
├── ninjas.json        # Almacenamiento de datos de ninjas  
└── src/  
    ├── ninja_crud.py  # Lógica CRUD para ninjas  
    └── mission_crud.py # Gestión de misiones  
```

---

## 🚀 **Instalación**  

1. **Clonar el Repositorio:**  
   ```bash  
   git clone https://github.com/usuario/narutomania.git  
   ```  

2. **Navegar al Directorio del Proyecto:**  
   ```bash  
   cd narutomania  
   ```  

3. **Ejecutar el Proyecto:**  
   ```bash  
   python menu.py  
   ```  

---

## 💡 **Ejemplo de Uso**  

| Acción                    | Comando                   | Descripción                                      |  
|---------------------------|---------------------------|--------------------------------------------------|  
| **Agregar Ninja**         | `add_ninja()`             | Registra un nuevo ninja en la base de datos.     |  
| **Actualizar Información**| `update_ninja(id)`        | Edita los detalles de un ninja existente.        |  
| **Eliminar Ninja**        | `delete_ninja(id)`        | Elimina un ninja específico del registro.        |  
| **Ver Todos los Ninjas**  | `list_ninjas()`           | Muestra la lista completa de ninjas registrados. |  

---

## 👥 **Colaboradores**  

- **Luis Fernando Pérez Salamanca**  
- **Ronaldo Antonio Oviedo**  

---
