# my_project.spec

# Імпортуємо необхідні модулі
from PyInstaller.utils.hooks import collect_data_files


text_files = ['students', 'groups', 'rooms', 'dormitory']


png_files = ['background.png']


python_files = ['main.py', 'Student.py', 'Win_Student.py', 'Win_Search.py', 'Win_Group.py', 'Win_Dormitory.py', 'Subject.py', 'Room.py', 'Observer.py', 'Group.py', 'Dormitory.py']

a = Analysis(python_files,
             pathex=['.'],  # Шлях до директорії з Python-файлами
             binaries=None,
             datas=collect_data_files('.', text_files + png_files),  # Включаємо тексові та PNG файли
             hiddenimports=[],
             hookspath=None,
             runtime_hooks=None,
             excludes=None,
             cipher=None)

pyz = PYZ(a.pure, a.zipped_data,
          cipher=None)

exe = EXE(pyz,
          a.scripts,
          exclude_binaries=True,
          name='my_project.exe',  # Ім'я виконуваного файлу
          debug=False,
          strip=False,
          upx=True,
          console=True)