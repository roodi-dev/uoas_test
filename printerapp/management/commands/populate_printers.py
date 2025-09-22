from django.core.management.base import BaseCommand
from printerapp.models import Printer

class Command(BaseCommand):
    help = 'Populate the database with initial printer data'

    def handle(self, *args, **kwargs):
        printers_data = [
            {
                'name': 'Kyocera Ecosys M3540dn',
                'image_url': 'https://uoas.co.za/wp-content/uploads/2021/05/Kyocera-Ecosys-M3540dn.jpg',
                'description': 'The Kyocera Ecosys M3540dn is a compact, efficient printer ideal for small businesses. It offers high-quality printing, low running costs, and reliable performance.',
                'features': [
                    'Print speed: Up to 40 pages per minute',
                    'Resolution: 1200 x 1200 dpi',
                    'Connectivity: USB, Ethernet',
                    'Features: Duplex printing, toner save mode',
                ],
                'category': 'small',
            },
            {
                'name': 'Kyocera Ecosys M2040dn and Ecosys M2540dn Printers',
                'image_url': 'https://uoas.co.za/wp-content/uploads/2021/05/Kyocera-Ecosys-M2040dn-and-Ecosys-M2540dn.png',
                'description': 'These wireless printers provide versatile printing options for small to medium businesses, with excellent connectivity and energy efficiency.',
                'features': [
                    'Print speed: Up to 42 pages per minute',
                    'Resolution: 1200 x 1200 dpi',
                    'Connectivity: USB, Ethernet, Wi-Fi',
                    'Features: Wireless printing, duplex, mobile printing support',
                ],
                'category': 'small',
            },
            {
                'name': 'Kyocera Ecosys M3660idn Printer',
                'image_url': 'https://uoas.co.za/wp-content/uploads/2021/05/Kyocera-Ecosys-M3660idn.png',
                'description': 'The Kyocera Ecosys M3660idn is a high-performance wireless printer designed for busy offices requiring fast and reliable printing.',
                'features': [
                    'Print speed: Up to 50 pages per minute',
                    'Resolution: 1200 x 1200 dpi',
                    'Connectivity: USB, Ethernet, Wi-Fi',
                    'Features: Duplex, mobile printing, large paper capacity',
                ],
                'category': 'small',
            },
            {
                'name': 'Kyocera Ecosys M6230cidn and Ecosys M6630cidn Printer',
                'image_url': 'https://uoas.co.za/wp-content/uploads/2021/05/Kyocera-Ecosys-M6230cidn-and-Ecosys-M6630cidn.png',
                'description': 'These printers offer advanced features for medium to large businesses, including color printing and high capacity.',
                'features': [
                    'Print speed: Up to 60 pages per minute',
                    'Resolution: 1200 x 1200 dpi',
                    'Connectivity: USB, Ethernet, Wi-Fi',
                    'Features: Color printing, duplex, large paper trays',
                ],
                'category': 'small',
            },
            {
                'name': 'Canon Imagerunner 1643 series',
                'image_url': 'https://uoas.co.za/wp-content/uploads/2021/05/Canon-Image-Runner-1643-series.jpg',
                'description': 'The Canon Imagerunner 1643 series is a reliable printer series suitable for various office environments with excellent print quality.',
                'features': [
                    'Print speed: Up to 43 pages per minute',
                    'Resolution: 1200 x 1200 dpi',
                    'Connectivity: USB, Ethernet',
                    'Features: Duplex printing, energy saving mode',
                ],
                'category': 'small',
            },
            {
                'name': 'Canon Image Runner C1325iF',
                'image_url': 'https://uoas.co.za/wp-content/uploads/2021/05/Canon-Image-Runner-C1325iF.jpg',
                'description': 'High-capacity printer designed for large enterprises with reliable performance and advanced features.',
                'features': [
                    'Print speed: Up to 35 pages per minute',
                    'Resolution: 1200 x 1200 dpi',
                    'Connectivity: USB, Ethernet, Wi-Fi',
                    'Features: High capacity, duplex printing, network ready',
                ],
                'category': 'large',
            },
            {
                'name': 'Canon Image Runner Advance DX 8705i',
                'image_url': 'https://uoas.co.za/wp-content/uploads/2021/05/imageRUNNER-ADVANCE-DX-8705i.jpg',
                'description': 'Networked printer with advanced scanning and printing capabilities for large business environments.',
                'features': [
                    'Print speed: Up to 50 pages per minute',
                    'Resolution: 1200 x 1200 dpi',
                    'Connectivity: USB, Ethernet, Wi-Fi',
                    'Features: Duplex, mobile printing, advanced scanning',
                ],
                'category': 'large',
            },
            {
                'name': 'Risograph Printers',
                'image_url': 'https://uoas.co.za/wp-content/uploads/2021/05/Risograph.jpg',
                'description': 'Specialized printers for unique business needs and labeling solutions.',
                'features': [
                    'Print speed: Variable',
                    'Resolution: High quality',
                    'Connectivity: USB, Ethernet',
                    'Features: Label printing, high speed, cost effective',
                ],
                'category': 'other',
            },
        ]

        for printer_data in printers_data:
            printer, created = Printer.objects.get_or_create(
                name=printer_data['name'],
                defaults={
                    'image_url': printer_data['image_url'],
                    'description': printer_data['description'],
                    'features': printer_data['features'],
                }
            )
            if created:
                self.stdout.write(self.style.SUCCESS(f"Created printer: {printer.name}"))
            else:
                self.stdout.write(f"Printer already exists: {printer.name}")
