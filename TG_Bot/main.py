
import asyncio
from database import dp
from database import bot

from database import DatabaseManager

# Запуск процесса поллинга новых апдейтов
async def main():
    db_manager = DatabaseManager()
    await db_manager.create_table()

    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())