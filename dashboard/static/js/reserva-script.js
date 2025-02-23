const campos_input = document.getElementsByClassName('input_container');
const alterar_input_veiculo = document.getElementById('veiculo');
const alterar_input_data_reserva = document.getElementById('date_reserva');
const alterar_input_data_entrega = document.getElementById('data_entrega');
const alterar_input_motorista = document.getElementById('motorista');
const alterar_input_status = document.getElementById('status');
const alterar_input_idade_condutor = document.getElementById('idade-condutor');
const alterar_input_forma_pagamento = document.getElementById('forma_pagamento_teste');
const rodape = document.getElementById('rodape');

for (let i = 0; i < campos_input.length; i++) {
    campos_input[i].addEventListener('dblclick', () => {
        mostrarCustomConfirm()
    });
}

function fazer_alteracoes() {
    alterar_input_veiculo.style.pointerEvents = 'visible';
    alterar_input_data_reserva.style.pointerEvents = 'visible';
    alterar_input_data_entrega.style.pointerEvents = 'visible';
    alterar_input_motorista.style.pointerEvents = 'visible';
    alterar_input_idade_condutor.style.pointerEvents = 'visible';
    alterar_input_forma_pagamento.style.pointerEvents = 'visible';
    alterar_input_status.style.pointerEvents = 'visible'
    rodape.style.display = 'flex'; // Exibe o rodapé
}

function cancelar_alteracoes(){
    if(confirm('As Informações não Salvas serão Perdidas!')){
        alterar_input_veiculo.style.pointerEvents = 'visible';
        alterar_input_data_reserva.style.pointerEvents = 'none';
        alterar_input_data_entrega.style.pointerEvents = 'none';
        alterar_input_motorista.style.pointerEvents = 'none';
        alterar_input_idade_condutor.style.pointerEvents = 'none';
        alterar_input_status.style.pointerEvents = 'none';
        alterar_input_forma_pagamento.style.pointerEvents = 'none';
        rodape.style.display = 'none';
        //adicionar lógica para recarregar as informações salvas
    }
}


//lógica para caixa de diálogo personalizada
const custom_confirm = document.getElementById('custom-confirm');
// Mostra o modal personalizado
function mostrarCustomConfirm() {
    if (rodape.style.display == 'flex'){
        return
    }else{
        document.getElementById('custom-confirm').style.display = 'block'
    }
    
}

// Fecha o modal sem executar nenhuma ação
function fecharCustomConfirm() {
    document.getElementById('custom-confirm').style.display = 'none';
}

// Executa a ação ao clicar em "Sim"
function confirmarAcao() {
    fecharCustomConfirm(); // Fecha o modal
    fazer_alteracoes()
}


function calcularValor() {
    const veiculoSelect = document.getElementById('veiculo');
    const dataReserva = document.getElementById('date_reserva').value;
    const dataEntrega = document.getElementById('data_entrega').value;
    const idadeCondutor = document.getElementById('idade-condutor').value;
    const valorInput = document.getElementById('valor');

    console.log(valorInput)

    if (!veiculoSelect.value || !dataReserva || !dataEntrega || !idadeCondutor) {
        valorInput.value = '';
        return;
    }

    const valorTotalVeiculo = parseFloat(veiculoSelect.options[veiculoSelect.selectedIndex].getAttribute('data-valor')) || 0;
    const reservaDate = new Date(dataReserva);
    const entregaDate = new Date(dataEntrega);

    const dias = Math.max(1, Math.ceil((entregaDate - reservaDate) / (1000 * 60 * 60 * 24))); 

    const porcentagemDiaria = 0.003;  
    const diaria = valorTotalVeiculo * porcentagemDiaria; 

    let valorTotal = dias * diaria; 

    if (parseInt(idadeCondutor) < 25) {
        valorTotal *= 1.1; 
    }

    valorInput.value = valorTotal.toFixed(2); 
}
