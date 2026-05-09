# Documentación del Proyecto: Preprocesamiento en Ciencia de Datos

## Introducción
Este proyecto tiene como objetivo practicar y documentar técnicas de **preprocesamiento de datos** en proyectos de Ciencia de Datos.  
Las funcionalidades implementadas incluyen:
- Crear un repositorio en GitHub.
- Configurar el archivo `.gitignore` para excluir archivos innecesarios.
- Realizar un commit inicial con un archivo README.md
- Clonación y Configuración
- Creación y Gestión de Ramas
- Pull Request y Fusión
- Implementación de funciones en Python para cargar, limpiar y normalizar datasets.

---

## Comandos Git usados
- `git clone <url>` → Clonar el repositorio desde GitHub.
<img width="728" height="240" alt="clonado" src="https://github.com/user-attachments/assets/43f76f56-33ac-4d3e-b3d2-a01c3c777d25" />


- `git config --global user.name "TuNombre"` → Configurar nombre de usuario.
- `git config --global user.email "tuemail@example.com"` → Configurar correo electrónico.
<img width="726" height="83" alt="user and email" src="https://github.com/user-attachments/assets/6e1fb7bc-9086-4c8f-86ab-5190a8738100" />


- `git checkout -b feature-preprocesamiento` → Crear y cambiar a una nueva rama.
<img width="582" height="111" alt="rama-feature" src="https://github.com/user-attachments/assets/777393c1-2185-4063-8f2e-02efaafb8734" />


- `git add <archivo>` → Añadir archivos al área de preparación.
- `git commit -m "mensaje"` → Guardar cambios en el historial.
- `git push origin <rama>` → Subir cambios a GitHub.
<img width="597" height="337" alt="commit de rama" src="https://github.com/user-attachments/assets/e3c5b77b-6794-45e4-8ee1-8d69283ceacc" />


- `git branch -d <rama>` → Eliminar una rama local.
- `git push origin --delete <rama>` → Eliminar una rama en GitHub.
<img width="803" height="103" alt="delete_branch" src="https://github.com/user-attachments/assets/56440ced-7367-4599-a50b-b0c468595ba0" />

--

## Automatización: Explicación del workflow de GitHub Actions creado

Se configuró un workflow en `.github/workflows/python-app.yml` que:
- Instala dependencias desde `requirements.txt`.
- Ejecuta pruebas con `pytest`.
- Se activa en cada push o pull request hacia la rama `main`.

📸 Evidencia: Captura de pantalla de la ejecución exitosa en la pestaña Actions.

---

##  Capturas de pantalla

- `Archivo .gitignore`.
<img width="638" height="412" alt="Captura de pantalla 2026-05-09 123120" src="https://github.com/user-attachments/assets/8967fc2a-51ce-4170-8187-056b28d56071" />
<img width="431" height="489" alt="Captura de pantalla 2026-05-09 123313" src="https://github.com/user-attachments/assets/ca87e3f3-2c25-492e-be4f-440e4c5ec638" />


- `Clonar repositorio`.
<img width="369" height="329" alt="Captura de pantalla 2026-05-09 125104" src="https://github.com/user-attachments/assets/0e4a7e2a-8c07-4891-ab72-d51f4b4caa10" />


- `Rama - feature-preprocesamiento`.
<img width="836" height="408" alt="Captura de pantalla 2026-05-09 134801" src="https://github.com/user-attachments/assets/e0882ab4-0b90-4d56-ac84-9da3cc444036" />
<img width="803" height="103" alt="delete_branch" src="https://github.com/user-attachments/assets/a42398ef-3f4a-41a1-8214-f27c891d4411" />

- `Commit desde VSCode`.
<img width="597" height="505" alt="commit de código" src="https://github.com/user-attachments/assets/e8d2d57b-204a-40ef-8fdd-0f1ee498819c" />


- `Pull request y fusión en GitHub`. 
<img width="807" height="452" alt="pull request" src="https://github.com/user-attachments/assets/01efc58c-2b95-4a95-88f9-4a3e39fc8d25" />
<img width="793" height="185" alt="merge" src="https://github.com/user-attachments/assets/90ec90dc-c632-4273-95c5-949e20e1673f" />
<img width="792" height="407" alt="merge2" src="https://github.com/user-attachments/assets/4a97b6d3-bef3-400c-b69c-9ab6658a7bd0" />


- `Delete branch`.
<img width="803" height="103" alt="delete_branch" src="https://github.com/user-attachments/assets/c42e37bf-59c6-4f02-8ef2-fc896a2e1b24" />
