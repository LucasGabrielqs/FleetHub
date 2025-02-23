const campos_input = document.getElementsByClassName('input_container');
const alterar_input_data_inicio = document.getElementById('data_inicio');
const alterar_input_data_fim = document.getElementById('data_fim');
const alterar_input_tipo_carga = document.getElementById('tipo_carga');
const alterar_input_cidade_inicio = document.getElementById('cidade_rota');
const alterar_input_cidade_fim = document.getElementById('cidade_fim');
const rodape = document.getElementById('rodape');

for (let i = 0; i < campos_input.length; i++) {
    campos_input[i].addEventListener('dblclick', () => {
        mostrarCustomConfirm()
    });
}

function fazer_alteracoes() {
    alterar_input_data_inicio.style.pointerEvents = 'visible';
    alterar_input_data_fim.style.pointerEvents = 'visible';
    alterar_input_tipo_carga.style.pointerEvents = 'visible';
    alterar_input_cidade_inicio.style.pointerEvents = 'visible';
    alterar_input_cidade_fim.style.pointerEvents = 'visible';
    rodape.style.display = 'flex'; // Exibe o rodapé
}

function cancelar_alteracoes(){
    if(confirm('As Informações não Salvas serão Perdidas!')){
        alterar_input_data_inicio.style.pointerEvents = 'none';
        alterar_input_data_fim.style.pointerEvents = 'none';
        alterar_input_tipo_carga.style.pointerEvents = 'none';
        alterar_input_cidade_inicio.style.pointerEvents = 'none';
        alterar_input_cidade_fim.style.pointerEvents = 'none';
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