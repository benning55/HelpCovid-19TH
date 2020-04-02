from abc import ABC

from django.core.management import BaseCommand, CommandError
from core.models import User, Categorie
from django.contrib.auth.models import Group


class Command(BaseCommand):
    """Django command to add db"""

    def handle(self, *args, **options):
        users = User.objects.all()
        if users.count() < 1:
            self.stdout.write("Create Super User")
            User.objects.create_superuser(
                username='admin',
                email='test@gmail.com',
                password='admin@kmitl'
            ).save()
        else:
            self.stdout.write("Already have super user")

        category = Categorie.objects.all()
        if category.count() < 1:
            names = ['สิ่งก่อสร้าง', 'ปรับปรุงโครงสร้าง', 'เครื่องมือแพทย์', 'วัสดุการแพทย์']
            descriptions = ['สิ่งปลูกสร้าง / งานโครงสร้าง ที่เป็นการสร้างขึ้นใหม่ เช่น Modular ARI Clinic', 'การปรับปรุงโครงสร้าง หรือ กายภาพใด ๆ ในห้องที่มีอยู่เดิม ไม่ใช่การสร้าง โครงสร้างหลักใหม่', 'เครื่องมือแพทย์ ที่เป็นของกึ่งถาวร ใช้แล้วนำกลับมาใช้ใหม่ได้อีก', 'วัสดุต่าง ๆ ที่ใช้แล้วทิ้ง เช่น หน้ากาก เสื้อกาวน์ ถุงมือ']
            for i in range(4):
                Categorie.objects.create(
                    name=names[i],
                    description=descriptions[i]
                )
            self.stdout.write("Create Category")
        else:
            self.stdout.write("Already Create Category")

