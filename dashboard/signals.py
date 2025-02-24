from django.db.models.signals import post_migrate
from django.dispatch import receiver
from django.apps import apps

@receiver(post_migrate)
def criar_registros_padrao(sender, **kwargs):
    if sender.name == "dashboard":  # Apenas para o app "dashboard"
        Estado = apps.get_model('dashboard', 'Estado')
        Forma_Pagamento = apps.get_model('dashboard', 'Forma_Pagamento')
        TipoUsuario = apps.get_model('usuarios', 'TipoUsuario')
        StatusUsuario = apps.get_model('usuarios', 'StatusUsuario')
        Status_Veiculo = apps.get_model('veiculos', 'Status_Veiculo')
        Tipos_Veiculo = apps.get_model('veiculos', 'Tipo_Veiculo')
        Status_Reserva = apps.get_model('dashboard', 'Status_Reserva')
        Tipo_Manutencao = apps.get_model('dashboard', 'Tipo_Manutencao')
        Prioridade_Atendimento = apps.get_model('dashboard', 'Prioridade_Atendimento')
        Tipo_Combustivel = apps.get_model('dashboard', 'Tipo_Combustivel')

        

        estados_padrao = [
            "AC", "AL", "AP", "AM", "BA", "CE", "DF", "ES", "GO", "MA", 
            "MT", "MS", "MG", "PA", "PB", "PR", "PE", "PI", "RJ", "RN",
            "RS", "RO", "RR", "SC", "SP", "SE", "TO"
        ]
        
        for sigla in estados_padrao:
            estado, created = Estado.objects.get_or_create(sigla=sigla)
            if created:
                print(f"Estado {sigla} criado.")

        tipos_usuario = ["ADMIN", "Cliente"]
        for tipo in tipos_usuario:
            tipo_usuario, created = TipoUsuario.objects.get_or_create(nome=tipo)
            if created:
                print(f"Tipo de Usuário {tipo} criado.")

        tipo_veiculo = ["Comum","Carga"]
        for tipo in tipo_veiculo:
            tipo_veiculo, created = Tipos_Veiculo.objects.get_or_create(tipo=tipo)
            if created:
                print(f"Tipo de Veiculo {tipo} criado.")

        status_usuario = ["Ativo", "Inativo"]
        for status in status_usuario:
            status_user, created = StatusUsuario.objects.get_or_create(status=status)
            if created:
                print(f"Status de Usuário {status} criado.")

        status_list = [
            {"status": "Disponível", "status_cor": "34C759"},
            {"status": "Reservado", "status_cor": "007AFF"},
            {"status": "Em Uso", "status_cor": "FFCC00"},
            {"status": "Atrasado", "status_cor": "FF3B30"},
            {"status": "Manutenção", "status_cor": "625E5E"},
        ]
        for status_ in status_list:
            status_veiculo, created = Status_Veiculo.objects.get_or_create(
                status=status_["status"], status_cor=status_["status_cor"]
            )
            if created:
                print(f"Status do Veículo {status_['status']} criado.")

        pagamentos_list = [
            "Cartão de Crédito", "Cartão de Débito", "PIX",
            "Boleto Bancário", "Transferência Bancária"
        ]
        for forma in pagamentos_list:
            pagamento, created = Forma_Pagamento.objects.get_or_create(forma_pagamento=forma)
            if created:
                print(f"Forma de Pagamento {forma} criada.")

        status_reserva = [
            {"status": "Concluída", "status_cor": "34C759"},
            {"status": "Pendente", "status_cor": "FFCC00"},
            {"status": "Cancelada", "status_cor": "FF3B30"},
            {"status": "Em Andamento", "status_cor": "625E5E"},    
        ]
        for status_ in status_reserva:
            status_reserva, created = Status_Reserva.objects.get_or_create(
                status=status_["status"], status_cor=status_["status_cor"]
            )
            if created:
                print(f"Status de Reserva {status_['status']} criado.")


        tipo_manutencao = [
            {"nome_manutencao": "Realizada"}, #"status_cor": "34C759" , "status_cor": "FFCC00"  , "status_cor": "FF3B30"
            {"nome_manutencao": "Pendente"},
            {"nome_manutencao": "Não foi Possível Realizar"}   
        ]
        for status_ in tipo_manutencao:
            tipo_manutencao, created = Tipo_Manutencao.objects.get_or_create(
                nome_manutencao=status_["nome_manutencao"] #status_cor=status_["status_cor"]
            )
            if created:
                print(f"Tipo de Manutenção {status_['nome_manutencao']} criado.")


        tipo_combustivel = [
            {"nome_combustivel": "Díesel"},
            {"nome_combustivel": "Díesel S10"},
            {"nome_combustivel": "Gasolina Comum"},  
            {"nome_combustivel": "Gasolina Aditivada"},
            {"nome_combustivel": "Etanol"}  
        ]
        for status_ in tipo_combustivel:
            tipo_combustivel, created = Tipo_Combustivel.objects.get_or_create(
                nome_combustivel=status_["nome_combustivel"]
            )
            if created:
                print(f"Tipo de Combutível {status_['nome_combustivel']} criado.")

        prioridade_atendimento = [
            {"prioridade": "Muito Urgente"},
            {"prioridade": "Urgente"},
            {"prioridade": "Pouco Urgente"},
        ]
        for status_ in prioridade_atendimento:
            prioridade_atendimento, created = Prioridade_Atendimento.objects.get_or_create(
                nome_prioridade=status_["prioridade"]
            )
            if created:
                print(f"Prioridade de Atendimento {status_['prioridade']} criado.")