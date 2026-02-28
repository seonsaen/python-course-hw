from django.db import migrations
from django.contrib.auth.hashers import make_password

def add_mock_data(apps, schema_editor):
    User = apps.get_model('auth', 'User')
    Post = apps.get_model('core', 'Post')
    Comment = apps.get_model('core', 'Comment')

    user_ivan = User.objects.create(
        username='ivan',
        password=make_password('password123'),
        email='ivan@example.com',
        is_staff=True,
        is_superuser=True
    )
    user_daria = User.objects.create(
        username='daria',
        password=make_password('password123'),
        email='daria@example.com'
    )

    post_food = Post.objects.create(
        title='Отличный рецепт шарлотки',
        text='Сегодня испек пирог с яблоками. Получилось очень вкусно! Всем советую.',
        author=user_ivan
    )
    post_weekend = Post.objects.create(
        title='Планы на выходные',
        text='Кто знает, какая погода будет в субботу? Думаем поехать за город.',
        author=user_daria
    )

    Comment.objects.create(
        post=post_food,
        author=user_daria,
        text='Обязательно попробую приготовить на днях! Спасибо за идею.'
    )
    Comment.objects.create(
        post=post_weekend,
        author=user_ivan,
        text='Вроде бы обещают солнечную погоду без осадков, так что смело поезжайте!'
    )

def remove_mock_data(apps, schema_editor):
    User = apps.get_model('auth', 'User')
    User.objects.filter(username__in=['ivan', 'daria']).delete()

class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'), 
    ]

    operations = [
        migrations.RunPython(add_mock_data, remove_mock_data),
    ]