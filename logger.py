"""
Logging va Analytics Modulasi
"""
import json
import os
from datetime import datetime

class BotLogger:
    def __init__(self, log_file='bot_activity.json'):
        self.log_file = log_file
        self.logs = self.load_logs()
    
    def load_logs(self):
        """Mavjud logsni yuklash"""
        if os.path.exists(self.log_file):
            try:
                with open(self.log_file, 'r', encoding='utf-8') as f:
                    return json.load(f)
            except:
                return []
        return []
    
    def save_logs(self):
        """Logsni saqlash"""
        with open(self.log_file, 'w', encoding='utf-8') as f:
            json.dump(self.logs, f, ensure_ascii=False, indent=2)
    
    def log_user_action(self, user_id, action, topic=None, level=None, pages=None):
        """Foydalanuvchi harakatini qaydi qilish"""
        log_entry = {
            'timestamp': datetime.now().isoformat(),
            'user_id': user_id,
            'action': action,
            'topic': topic,
            'level': level,
            'pages': pages
        }
        self.logs.append(log_entry)
        self.save_logs()
    
    def log_error(self, user_id, error_message, error_type=None):
        """Xatolarni qaydi qilish"""
        error_entry = {
            'timestamp': datetime.now().isoformat(),
            'user_id': user_id,
            'error': error_message,
            'error_type': error_type
        }
        self.logs.append(error_entry)
        self.save_logs()
    
    def get_stats(self):
        """Statistika olish"""
        stats = {
            'total_users': len(set(log.get('user_id') for log in self.logs)),
            'total_referats': len([log for log in self.logs if log.get('action') == 'referat_created']),
            'total_errors': len([log for log in self.logs if 'error' in log]),
            'most_used_level': self.get_most_used_level(),
            'average_pages': self.get_average_pages(),
            'most_used_format': self.get_most_used_format()
        }
        return stats
    
    def get_most_used_level(self):
        """Eng ko'p ishlatilgan ta'lim darajasi"""
        levels = {}
        for log in self.logs:
            if log.get('level'):
                levels[log['level']] = levels.get(log['level'], 0) + 1
        return max(levels, key=levels.get) if levels else None
    
    def get_average_pages(self):
        """O'rtacha betlar soni"""
        pages = [log.get('pages') for log in self.logs if log.get('pages')]
        return sum(pages) / len(pages) if pages else 0
    
    def get_most_used_format(self):
        """Eng ko'p ishlatilgan format"""
        formats = {}
        for log in self.logs:
            if log.get('format'):
                formats[log['format']] = formats.get(log['format'], 0) + 1
        return max(formats, key=formats.get) if formats else None
    
    def print_stats(self):
        """Statistikani chop qilish"""
        stats = self.get_stats()
        print("\n" + "="*50)
        print("📊 BOT STATISTIKASI")
        print("="*50)
        print(f"Jami foydalanuvchilar: {stats['total_users']}")
        print(f"Jami yaratilgan referatlar: {stats['total_referats']}")
        print(f"Xatolar soni: {stats['total_errors']}")
        print(f"Eng ko'p ishlatilgan ta'lim darajasi: {stats['most_used_level']}")
        print(f"O'rtacha betlar soni: {stats['average_pages']:.1f}")
        print(f"Eng ko'p ishlatilgan format: {stats['most_used_format']}")
        print("="*50 + "\n")


# Foydalanish misoli:
if __name__ == '__main__':
    logger = BotLogger()
    
    # Misoliy logsni qo'shish
    logger.log_user_action(
        user_id=12345,
        action='referat_created',
        topic='O\'zbekiston tarixiga',
        level='university',
        pages=10
    )
    
    logger.log_user_action(
        user_id=12345,
        action='referat_created',
        topic='Biologiya',
        level='school',
        pages=5
    )
    
    logger.print_stats()
