from django.test import TestCase
from django.contrib.auth.models import User
import time
from rrp.models import *

# Create your tests here.
class UsersTest(TestCase):
    def test_default(self):
        User.objects.create(username="default", password="password", email="email")
        user = User.objects.get(username="default")
        users = Users.objects.create(user=user)
        self.assertEqual(user.username, "default")
        self.assertEqual(user.password, "password")
        self.assertEqual(user.email, "email")
        self.assertIsNone(users.position)
        self.assertIsNone(users.superior)
        self.assertTrue(users.cirt is False)
        self.assertTrue(users.reporter is False)

    def test_attributes(self):
        User.objects.create(username="user", password="password", email="email")
        user = User.objects.get(username="user")
        users = Users.objects.create(user=user, position="user", superior="bm", cirt=False, reporter=True)
        self.assertEqual(users.position, "user")
        self.assertEqual(users.superior, "bm")
        self.assertTrue(users.cirt is False)
        self.assertTrue(users.reporter is True)

class AssetTest(TestCase):
    def test_asset(self):
        Asset.objects.create(assetName="TEST001", assetType="TEST", dataLevel="L")
        asset = Asset.objects.get(assetName="TEST001")
        self.assertEqual(asset.assetName, "TEST001")
        self.assertEqual(asset.assetType, "TEST")
        self.assertEqual(asset.dataLevel, "L")

class RansomwareTest(TestCase):
    def test_ransomware(self):
        Ransomware.objects.create(ransomwareName="RN", ransomwareType="RT", description="test")
        ransomware = Ransomware.objects.get(ransomwareName="RN")
        self.assertEqual(ransomware.ransomwareName, "RN")
        self.assertEqual(ransomware.ransomwareType, "RT")
        self.assertEqual(ransomware.description, "test")

class RiskLevelAssessmentTest(TestCase):
    def test_riskLevelAssessment(self):
        RiskLevelAssessment.objects.create(dataLevel="H", ransomwareType="RT", riskLevel="H3")
        risklevelassessment = RiskLevelAssessment.objects.get(dataLevel="H")
        self.assertEqual(risklevelassessment.dataLevel, "H")
        self.assertEqual(risklevelassessment.ransomwareType, "RT")
        self.assertEqual(risklevelassessment.riskLevel, "H3")

class EventTest(TestCase):
    def test_event(self):
        User.objects.create(username="default", password="password", email="email")
        user = User.objects.get(username="default")
        users = Users.objects.create(user=user)
        Asset.objects.create(assetName="TEST001", assetType="TEST", dataLevel="L")
        asset = Asset.objects.get(assetName="TEST001")
        Ransomware.objects.create(ransomwareName="RN", ransomwareType="RT", description="test")
        ransomware = Ransomware.objects.get(ransomwareName="RN")
        Event.objects.create(requestTime="2022-08-28 17:21:00",
                             requestUser=users,
                             userAsset=asset,
                             ransomware=ransomware,
                             ransomwareType="RT",
                             ransomAmount=10,
                             duration=72,
                             description="des")
        event = Event.objects.get(requestUser=users)
        self.assertEqual(event.userAsset, asset)
        self.assertEqual(event.ransomware, ransomware)
        self.assertEqual(event.ransomwareType, "RT")
        self.assertEqual(event.ransomAmount, 10)
        self.assertEqual(event.duration, 72)
        self.assertEqual(event.description, "des")

class InformationTest(TestCase):
    def test_information(self):
        Information.objects.create(title="info", info="info details")
        information = Information.objects.get(title="info")
        self.assertEqual(information.title, "info")
        self.assertEqual(information.info, "info details")




