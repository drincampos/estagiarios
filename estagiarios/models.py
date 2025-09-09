from django.db import models

MESA_DIRETORA = {
    "PR": "Presidência",
    "VC": "Vice-Presidência",
    "1S": "Primeira Secretaria",
    "2S": "Segunda Secretaria",
    "3S": "Terceira Secretaria",
}

NIVEL_ACADEMICO = {
    "2G": "Segundo Grau",
    "SP": "Superior",
}


class UnidadesCLDF(models.Model):

    nome_unidade = models.CharField('Unidade', max_length=100, null=False, blank=False)
    sigla = models.CharField('Sigla', max_length=15, null=False, blank=False)
    subordinacao = models.CharField(
        'Unidade da mesa',
        max_length=2, 
        null=False, 
        blank=False, 
        choices=MESA_DIRETORA.items(), 
        default="1S"
    )

    class Meta:
        verbose_name = "Unidade da CLDF"
        verbose_name_plural = "Unidades da CLDF"

    def __str__(self):
        return f"{self.nome_unidade} - {MESA_DIRETORA[self.subordinacao]}"


class Estagiario(models.Model):

    nome_estagiario = models.CharField('Nome', max_length=200, null=False, blank=False)
    fone = models.CharField('Fone(s)', max_length=40, null=False, blank=False)
    email = models.EmailField('E-mail', max_length=100, null=False, blank=False)
    nivel = models.CharField('Nível', choices=NIVEL_ACADEMICO.items(), max_length=2, null=False, blank=False)
    unidade_cldf = models.ForeignKey(UnidadesCLDF, on_delete=models.SET_NULL, null=True)
    matricula = models.IntegerField('Matrícula', null=False, blank=False)
    data_inicio = models.DateField('Data início', )
    

    class Meta:
        verbose_name = "Estagiário"
        verbose_name_plural = "Estagiários"

    def __str__(self):
        return self.nome_estagiario
    




