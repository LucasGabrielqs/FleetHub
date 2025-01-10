const campos_input = document.getElementsByClassName('input_container');
const alterar_input_veiculo = document.getElementById('veiculo');
const alterar_input_data_inicio = document.getElementById('data_inicio');
const alterar_input_data_fim = document.getElementById('data_fim');
const alterar_input_km_viagem = document.getElementById('km_viagem');
const alterar_input_km_atual = document.getElementById('km_atual');
const alterar_input_km_final = document.getElementById('km_final');
const alterar_input_valor = document.getElementById('valor');
const alterar_input_tipo_carga = document.getElementById('tipo_carga');
const alterar_input_motorista = document.getElementById('motorista');
const alterar_input_cidade_inicio = document.getElementById('cidade_rota');
const alterar_input_cidade_fim = document.getElementById('cidade_fim');
// const alterar_input_ano = document.getElementById('codigo_reserva');
const alterar_input_estado_inicio = document.getElementById('estado_inicio');
const alterar_input_estado_fim = document.getElementById('estado_fim');
const alterar_input_forma_pagamento = document.getElementById('forma_pagamento');
const rodape = document.getElementById('rodape');

for (let i = 0; i < campos_input.length; i++) {
    campos_input[i].addEventListener('dblclick', () => {
        mostrarCustomConfirm()
    });
}

function fazer_alteracoes() {
    alterar_input_veiculo.style.pointerEvents = 'visible';
    alterar_input_data_inicio.style.pointerEvents = 'visible';
    alterar_input_data_fim.style.pointerEvents = 'visible';
    alterar_input_km_viagem.style.pointerEvents = 'visible';
    alterar_input_km_atual.style.pointerEvents = 'visible';
    alterar_input_km_final.style.pointerEvents = 'visible';
    alterar_input_tipo_carga.style.pointerEvents = 'visible';
    alterar_input_valor.style.pointerEvents = 'visible';
    alterar_input_motorista.style.pointerEvents = 'visible';
    alterar_input_cidade_inicio.style.pointerEvents = 'visible';
    alterar_input_estado_inicio.style.pointerEvents = 'visible';
    alterar_input_estado_fim.style.pointerEvents = 'visible';
    alterar_input_cidade_fim.style.pointerEvents = 'visible';
    alterar_input_valor.style.pointerEvents = 'visible';
    alterar_input_forma_pagamento.style.pointerEvents = 'visible';
    rodape.style.display = 'flex'; // Exibe o rodapé
}

function cancelar_alteracoes(){
    if(confirm('As Informações não Salvas serão Perdidas!')){
        alterar_input_veiculo.style.pointerEvents = 'visible';
        alterar_input_data_inicio.style.pointerEvents = 'none';
        alterar_input_data_fim.style.pointerEvents = 'none';
        alterar_input_km_viagem.style.pointerEvents = 'none';
        alterar_input_km_atual.style.pointerEvents = 'none';
        alterar_input_km_final.style.pointerEvents = 'none';
        alterar_input_tipo_carga.style.pointerEvents = 'none';
        alterar_input_valor.style.pointerEvents = 'none';
        alterar_input_motorista.style.pointerEvents = 'none';
        alterar_input_cidade_inicio.style.pointerEvents = 'none';
        alterar_input_estado_inicio.style.pointerEvents = 'none';
        alterar_input_estado_fim.style.pointerEvents = 'none';
        alterar_input_cidade_fim.style.pointerEvents = 'none';
        alterar_input_valor.style.pointerEvents = 'none';
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