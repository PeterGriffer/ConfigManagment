from vfs_manager import VFSManager

class VFS:
    def __init__(self, name='defaultVFS'):
        self.name = name
        self.console = None
        self.vfs_manager = VFSManager()
        self.vfs_loaded = False
    
    def get_prompt(self):
        if self.vfs_loaded:
            return self.vfs_manager.get_prompt()
        else:
            return f"[{self.name}]$ "
    
    def set_prompt(self, newprompt):
        # Для совместимости со старым кодом
        pass
    
    def load_vfs(self, json_file_path):
        """Загрузка VFS из JSON файла"""
        try:
            success = self.vfs_manager.load_vfs(json_file_path)
            if success:
                self.vfs_loaded = True
                self.name = self.vfs_manager.loaded_vfs_name
            return success
        except Exception as e:
            print(f"Ошибка загрузки VFS: {e}")
            return False
    
    def list_directory(self, path=None):
        """Список содержимого директории"""
        if not self.vfs_loaded:
            return "VFS не загружена. Используйте команду 'load-vfs' сначала."
        return self.vfs_manager.list_directory(path)
    
    def change_directory(self, path):
        """Смена текущей директории"""
        if not self.vfs_loaded:
            return "VFS не загружена. Используйте команду 'load-vfs' сначала."
        return self.vfs_manager.change_directory(path)
    
    def read_file(self, file_path):
        """Чтение файла"""
        if not self.vfs_loaded:
            return "VFS не загружена. Используйте команду 'load-vfs' сначала."
        return self.vfs_manager.read_file(file_path)
    
    def get_current_path(self):
        """Получить текущий путь"""
        if not self.vfs_loaded:
            return "/"
        return self.vfs_manager.current_path