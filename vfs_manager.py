import json
import base64
import os
from datetime import datetime

class VFSNode:
    """Узел виртуальной файловой системы (файл или папка)"""
    def __init__(self, name, node_type, content=None, size=0, created=None, modified=None):
        self.name = name
        self.type = node_type  # 'file' или 'directory'
        self.content = content
        self.size = size
        self.created = created or datetime.now()
        self.modified = modified or datetime.now()
        self.children = {} if node_type == 'directory' else None

class VFSManager:
    """Менеджер виртуальной файловой системы"""
    
    def __init__(self):
        self.root = VFSNode('', 'directory')
        self.current_path = '/'
        self.loaded_vfs_name = None
    
    def load_vfs(self, json_file_path):
        """Загрузка VFS из JSON файла"""
        try:
            if not os.path.exists(json_file_path):
                raise FileNotFoundError(f"VFS файл не найден: {json_file_path}")
            
            with open(json_file_path, 'r', encoding='utf-8') as f:
                vfs_data = json.load(f)
            
            # Валидация структуры
            if 'name' not in vfs_data or 'structure' not in vfs_data:
                raise ValueError("Неверный формат VFS: отсутствует 'name' или 'structure'")
            
            self.root = VFSNode('', 'directory')
            self._build_tree(self.root, vfs_data['structure'])
            self.loaded_vfs_name = vfs_data['name']
            self.current_path = '/'
            
            print(f"VFS '{self.loaded_vfs_name}' успешно загружена")
            return True
            
        except json.JSONDecodeError as e:
            raise ValueError(f"Неверный формат JSON: {e}")
        except Exception as e:
            raise Exception(f"Ошибка загрузки VFS: {e}")
    
    def _build_tree(self, parent_node, structure):
        """Рекурсивное построение дерева файловой системы"""
        for item in structure:
            if 'name' not in item or 'type' not in item:
                continue
                
            if item['type'] == 'directory':
                new_node = VFSNode(item['name'], 'directory')
                if 'children' in item:
                    self._build_tree(new_node, item['children'])
                parent_node.children[item['name']] = new_node
                
            elif item['type'] == 'file':
                content = None
                size = item.get('size', 0)
                
                if 'content' in item:
                    if item.get('encoding') == 'base64':
                        # Декодируем base64
                        content = base64.b64decode(item['content']).decode('utf-8')
                    else:
                        content = item['content']
                
                new_node = VFSNode(item['name'], 'file', content, size)
                parent_node.children[item['name']] = new_node
    
    def get_current_directory(self):
        """Получить текущую директорию"""
        return self._resolve_path(self.current_path)
    
    def _resolve_path(self, path):
        """Разрешить путь к узлу"""
        if path == '/':
            return self.root
        
        path_parts = [p for p in path.split('/') if p]
        current_node = self.root
        
        for part in path_parts:
            if part not in current_node.children:
                return None
            current_node = current_node.children[part]
        
        return current_node
    
    def list_directory(self, path=None):
        """Список содержимого директории"""
        target_path = path or self.current_path
        node = self._resolve_path(target_path)
        
        if not node:
            return f"Директория не найдена: {target_path}"
        
        if node.type != 'directory':
            return f"Не директория: {target_path}"
        
        if not node.children:
            return "Директория пуста"
        
        result = []
        for name, child in node.children.items():
            if child.type == 'directory':
                result.append(f"{name}/")
            else:
                result.append(f"{name} ({child.size} байт)")
        
        return "\n".join(result)
    
    def change_directory(self, path):
        """Смена текущей директории"""
        if path == '/':
            self.current_path = '/'
            return True
        
        if path.startswith('/'):
            # Абсолютный путь
            target_path = path
        else:
            # Относительный путь
            if self.current_path == '/':
                target_path = f'/{path}'
            else:
                target_path = f'{self.current_path}/{path}'
        
        # Нормализация пути
        target_path = target_path.rstrip('/')
        if not target_path:
            target_path = '/'
        
        node = self._resolve_path(target_path)
        if not node:
            return f"Директория не найдена: {path}"
        
        if node.type != 'directory':
            return f"Не директория: {path}"
        
        self.current_path = target_path
        return True
    
    def read_file(self, file_path):
        """Чтение файла"""
        if not file_path.startswith('/'):
            # Относительный путь
            if self.current_path == '/':
                file_path = f'/{file_path}'
            else:
                file_path = f'{self.current_path}/{file_path}'
        
        node = self._resolve_path(file_path)
        if not node:
            return f"Файл не найден: {file_path}"
        
        if node.type != 'file':
            return f"Не файл: {file_path}"
        
        return node.content or "[Пустой файл]"
    
    def get_prompt(self):
        """Получить приглашение с текущим путем"""
        if self.current_path == '/':
            return f"[VFS:{self.loaded_vfs_name} /]$ "
        else:
            return f"[VFS:{self.loaded_vfs_name} {self.current_path}]$ "