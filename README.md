# Actividad 6 - Programación Orientada a Objetos 2026-2S

**Universidad:** Universidad Nacional de Colombia

**Actividad:** Actividad 6: Valor 20% - Interfaz gráfica y archivos de texto

**Estudiante:** Juan Diego Toro Zuluaga

**Docente:** Walter Hugo Arboleda Mazo

## Contenido

Aplicación en Python con interfaz gráfica de usuario en Tkinter que administra una agenda de contactos almacenada en un archivo de texto plano. El formulario cuenta con los cuatro botones de las operaciones CRUD:

- **Create:** agrega un contacto nuevo al archivo, validando que los campos no estén vacíos y que el nombre no exista ya.
- **Read:** carga los contactos del archivo en la tabla. Si se escribe un nombre, busca ese contacto y muestra su número.
- **Update:** modifica el número de un contacto existente y reescribe el archivo.
- **Delete:** elimina un contacto del archivo y reescribe el archivo.

Los datos se guardan en `contactos.txt`, un contacto por línea, con el formato `nombre,numero`.

## Ejecución

El programa abre una ventana de escritorio, por lo que debe ejecutarse localmente:

```
python actividad6_crud_contactos.py
```

En Google Colab no funciona, porque es un entorno sin interfaz gráfica.

El archivo `contactos.txt` se crea automáticamente al agregar el primer contacto. El repositorio incluye uno de ejemplo con dos registros.

## Archivos

- `actividad6_crud_contactos.py` - código fuente de la aplicación
- `contactos.txt` - archivo de texto con los contactos
- `Actividad6_POO_JuanDiegoToroZuluaga.pdf` - Actividad 6 POO
- `interfaz_a6_1_formulario.png` - formulario con los datos de un contacto nuevo
- `interfaz_a6_2_create.png` - resultado de la operación Create
- `interfaz_a6_3_read.png` - resultado de la operación Read
- `interfaz_a6_4_update.png` - resultado de la operación Update
- `interfaz_a6_5_delete.png` - resultado de la operación Delete
- `diagrama_clases_a6.png` - diagrama de clases
- `casos_uso_a6.png` - diagrama de casos de uso
