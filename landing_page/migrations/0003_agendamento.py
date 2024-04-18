# Generated by Django 5.0.4 on 2024-04-18 11:33

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('landing_page', '0002_paciente_profissional_remove_servico_descricao_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Agendamento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_hora', models.DateTimeField(default=django.utils.timezone.now)),
                ('status', models.CharField(choices=[('AGENDADO', 'Agendado'), ('CANCELADO', 'Cancelado')], default='AGENDADO', max_length=10)),
                ('paciente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='landing_page.paciente')),
                ('profissional', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='landing_page.profissional')),
                ('servico', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='landing_page.servico')),
            ],
        ),
    ]
