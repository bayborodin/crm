import ftplib
import csv
from django.core.management.base import BaseCommand

from accounts.models import Account
from accounts.models import AccountType


class Command(BaseCommand):
    help = 'Display current time'

    def get_ftp_connection(self):
        server = '212.19.5.226'
        username = 'User3'
        password = 'DhtvtYy0'
        remote_path = 'connect'

        ftp_connection = ftplib.FTP(server, username, password)
        ftp_connection.cwd(remote_path)

        return ftp_connection

    def get_filename(self):
        ftp = self.get_ftp_connection()

        file_list = []

        try:
            file_list = ftp.nlst()
        except ftplib.error_perm as resp:
            str_resp = str(resp)
            if str_resp == "550 No files found":
                print("No files in this directory")
            else:
                raise
        ftp.close()

        return max(file_list)

    def handle(self, *args, **kvargs):
        file_name = self.get_filename()
        ftp = self.get_ftp_connection()
        ftp.retrbinary("RETR " + file_name, open(f'/tmp/{file_name}', 'wb').write)
        ftp.close()

        # oбъявим словарь, ключи которого - тип объекта(object_type),
        # а значения - класс, объект которого будем создавать
        create_strategy = {
            'accounts': Account,
            'account_types': AccountType
        }

        # parse csv file
        with open(f'/tmp/{file_name}', 'r') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=';')
            # обрабатываем csv-файл
            for row in csv_reader:
                try:
                    object_type = row[0]
                except IndexError:
                    # игнорируем пустую строку
                    print('Пустая строка - игнорируем!')
                    continue

                try:
                    # получаем класс, объект которого нужно создать
                    object_class = create_strategy[object_type]
                except KeyError:
                    # если тип данных не известен, игнорируем строку
                    print(f'Неизвестный тип данных: {object_type}')
                    continue

                try:
                    # создаем объект
                    res = object_class.from_tuple(row)
                    print(res)
                except (ValueError, IndexError):
                    # если данные не корректны - игнорируем их
                    print(f'Ошибка создания объекта {object_class} из строки: {row}')
                    continue
                except (NotImplementedError):
                    print(f'Создание объекта {object_class} из CSV не реализовано!')
