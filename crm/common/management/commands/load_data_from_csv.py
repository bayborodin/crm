import ftplib
import csv
from django.core.management.base import BaseCommand

from accounts.models import Account, LegalEntity
from accounts.models import AccountType
from common.models import CommunicationType, Country, State, City
from logistics.models import DeliveryPrice
from offerings.models import OfferingGroup, Offering
from orders.models import Order, OrderOffering
from shipments.models import Shipment, ShipmentOffering


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
            if str_resp == '550 No files found':
                print('No files in this directory')
            else:
                raise
        ftp.close()

        return max(file_list)

    def handle(self, *args, **kvargs):
        file_name = self.get_filename()
        ftp = self.get_ftp_connection()
        ftp.retrbinary('RETR ' + file_name,
                       open(f'/tmp/{file_name}', 'wb').write)
        ftp.close()

        # oбъявим словарь, ключи которого - тип объекта(object_type),
        # а значения - класс, объект которого будем создавать
        create_strategy = {
            'accounts': Account,
            'account_types': AccountType,
            'communication_types': CommunicationType,
            'delivery_prices': DeliveryPrice,
            'legal_entities': LegalEntity,
            'offering_groups': OfferingGroup,
            'offerings': Offering,
            'orders': Order,
            'order_details': OrderOffering,
            'shipments': Shipment,
            'shipment_offerings': ShipmentOffering,
            'countries': Country,
            'states': State,
            'cities': City,
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
                except (ValueError, IndexError) as e:
                    # если данные не корректны - игнорируем их
                    print(
                        f'Ошибка создания объекта {object_class} из строки: '
                        f'{row} ({str(e)})',
                    )
                    # continue
                except (NotImplementedError):
                    print(
                        f'Создание объекта {object_class} из CSV не реализовано!')
