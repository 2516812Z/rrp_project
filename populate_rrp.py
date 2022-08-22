
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'rrp_project.settings')

import django
django.setup()

from rrp.models import *

def populate():

    Users = [
        {'user': {'username': "admin", 'password': 1234, 'email': "admin@test.com"}, 'picture': '/users_images/admin.png', 'position': 'admin', 'superior': 'iso', 'cirt': True, 'reporter': True},
        {'user': {'username': "sadmin", 'password': 1234, 'email': "sadmin@test.com"}, 'picture': '/users_images/sadmin.png', 'position': 'sadmin', 'superior': None, 'cirt': True, 'reporter': True},
        {'user': {'username': "iso", 'password': 1234, 'email': "iso@test.com"}, 'picture': '/users_images/iso.png', 'position': 'iso', 'superior': 'sadmin', 'cirt': True, 'reporter': True},
        {'user': {'username': "user", 'password': 1234, 'email': "user@test.com"}, 'picture': '/users_images/user.png', 'position': 'user', 'superior': 'bm', 'cirt': False, 'reporter': True},
        {'user': {'username': "bm", 'password': 1234, 'email': "bm@test.com"}, 'picture': '/users_images/bm.png', 'position': 'bm', 'superior': 'sadmin', 'cirt': False, 'reporter': True},
        {'user': {'username': "fin", 'password': 1234, 'email': "fin@test.com"}, 'picture': '/users_images/fin.png', 'position': 'fin', 'superior': 'sadmin', 'cirt': True, 'reporter': True},
        {'user': {'username': "legal", 'password': 1234, 'email': "legal@test.com"}, 'picture': '/users_images/legal.png', 'position': 'legal', 'superior': 'sadmin', 'cirt': True, 'reporter': True},
    ]

    Assets = [
        {'assetName': 'PC001', 'assetType': 'Personal', 'dataLevel': 'L'},
        {'assetName': 'LT001', 'assetType': 'Laptop', 'dataLevel': 'M'},
        {'assetName': 'SE001', 'assetType': 'Server', 'dataLevel': 'H'}
    ]

    Ransomwares = [
        {'ransomwareName': 'Petya', 'ransomwareType': 'Locker', 'description': "Cannot recovery"},
        {'ransomwareName': 'WannaCry', 'ransomwareType': 'Crypto', 'description': "Partial recovery"},
        {'ransomwareName': 'AD', 'ransomwareType': 'Scareware', 'description': "Full recovery"}
    ]

    RiskLevelAssessment = [
        {'dataLevel': 'H', 'ransomwareType': 'Crypto', 'riskLevel': 'H3'},
        {'dataLevel': 'H', 'ransomwareType': 'Locker', 'riskLevel': 'H1'},
        {'dataLevel': 'H', 'ransomwareType': 'Scareware', 'riskLevel': 'L2'},
        {'dataLevel': 'M', 'ransomwareType': 'Crypto', 'riskLevel': 'M2'},
        {'dataLevel': 'M', 'ransomwareType': 'Locker', 'riskLevel': 'M1'},
        {'dataLevel': 'M', 'ransomwareType': 'Scareware', 'riskLevel': 'L1'},
        {'dataLevel': 'L', 'ransomwareType': 'Crypto', 'riskLevel': 'H2'},
        {'dataLevel': 'L', 'ransomwareType': 'Locker', 'riskLevel': 'H1'},
        {'dataLevel': 'L', 'ransomwareType': 'Scareware', 'riskLevel': 'L1'}
    ]

    Events = {

    }

    Informations = [
        {'title': 'Asset classification', 'info': '3 classification: Personal, Laptop, Server; 3 data leve: H(High), M(Medium), L(Low)'},
        {'title': 'Ransomware classification', 'info': '3 classification: Crypto, Locker, Scareware'},
        {'title': 'Risk Level', 'info': '3 High level: H3,H2,H1; 2 Medium level: M2,M1; 2 Low Level: L2,L1'}
    ]

    Evidence = [
    ]






if __name__ == "__main__":
    print("Starting rrp's populating script...")
    populate()
