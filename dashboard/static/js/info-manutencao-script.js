const campos_input = document.getElementsByClassName('input_container');
const alterar_input_veiculo = document.getElementById('veiculo');
const alterar_input_km_atual = document.getElementById('km_atual');
const alterar_input_cpf = document.getElementById('tipo_manutencao');
const alterar_input_ddd = document.getElementById('atendimento');
const alterar_input_telefone = document.getElementById('data_entrega');
const alterar_input_status = document.getElementById('valor_manutencao');
const alterar_input_estado = document.getElementById("comentarios");
const alterar_input_status_manutencao = document.getElementById("status");
const rodape = document.getElementById('rodape');

for (let i = 0; i < campos_input.length; i++) {
    campos_input[i].addEventListener('dblclick', () => {
        mostrarCustomConfirm()
    });
}

function fazer_alteracoes() {
    alterar_input_veiculo.style.pointerEvents = 'visible';
    alterar_input_km_atual.style.pointerEvents = 'visible';
    alterar_input_cpf.style.pointerEvents = 'visible';
    alterar_input_ddd.style.pointerEvents = 'visible';
    alterar_input_telefone.style.pointerEvents = 'visible';
    alterar_input_status.style.pointerEvents = 'visible';
    alterar_input_estado.style.pointerEvents = 'visible';
    alterar_input_status_manutencao.style.pointerEvents = 'visible';
    rodape.style.display = 'flex'; // Exibe o rodapé
}

function cancelar_alteracoes(){
    if(confirm('As Informações não Salvas serão Perdidas!')){
        alterar_input_veiculo.style.pointerEvents = 'none';
        alterar_input_km_atual.style.pointerEvents = 'none';
        alterar_input_cpf.style.pointerEvents = 'none';
        alterar_input_ddd.style.pointerEvents = 'none';
        alterar_input_telefone.style.pointerEvents = 'none';
        alterar_input_status.style.pointerEvents = 'none';
        alterar_input_estado.style.pointerEvents = 'none';
        alterar_input_status_manutencao.style.pointerEvents = 'none';
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
        document.getElementById('custom-confirm').style.display = 'block';
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