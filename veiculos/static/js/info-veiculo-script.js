const campos_input = document.getElementsByClassName('input_container');
const alterar_input_modelo = document.getElementById('modelo');
const alterar_input_marca = document.getElementById('marca');
const alterar_input_valor = document.getElementById('valor-carro');
const alterar_cor = document.getElementById('cor-carro');
const alterar_input_ano = document.getElementById('ano-carro');
const alterar_input_km = document.getElementById('km-carro');
const alterar_input_motor = document.getElementById('motor-carro');
const alterar_input_status = document.getElementById('select-status-carro');
const alterar_input_placa = document.getElementById('placa-carro');
const alterar_input_chassi = document.getElementById('chassi-carro');
const alterar_input_tipo = document.getElementById('tipo')
const alterar_img_carro = document.getElementById('img');
const rodape = document.getElementById('rodape');

for (let i = 0; i < campos_input.length; i++) {
    campos_input[i].addEventListener('dblclick', () => {
        mostrarCustomConfirm()
    });
}

function fazer_alteracoes() {
    alterar_input_modelo.style.pointerEvents = 'visible';
    alterar_input_marca.style.pointerEvents = 'visible';
    alterar_input_ano.style.pointerEvents = 'visible';
    alterar_input_chassi.style.pointerEvents = 'visible';
    alterar_input_km.style.pointerEvents = 'visible';
    alterar_input_motor.style.pointerEvents = 'visible';
    alterar_input_placa.style.pointerEvents = 'visible';
    alterar_input_status.style.pointerEvents = 'visible';
    alterar_input_valor.style.pointerEvents = 'visible';
    alterar_cor.style.pointerEvents = 'visible';
    alterar_input_tipo.style.pointerEvents = 'visible';
    alterar_img_carro.style.display = 'block';
    rodape.style.display = 'flex'; // Exibe o rodapé
}

function cancelar_alteracoes(){
    if(confirm('As Informações não Salvas serão Perdidas!')){
        alterar_input_modelo.style.pointerEvents = 'none';
        alterar_input_marca.style.pointerEvents = 'none';
        alterar_input_ano.style.pointerEvents = 'none';
        alterar_input_chassi.style.pointerEvents = 'none';
        alterar_input_km.style.pointerEvents = 'none';
        alterar_input_motor.style.pointerEvents = 'none';
        alterar_input_placa.style.pointerEvents = 'none';
        alterar_input_status.style.pointerEvents = 'none';
        alterar_input_valor.style.pointerEvents = 'none';
        alterar_cor.style.pointerEvents = 'none';
        alterar_input_tipo.style.pointerEvents = 'none';
        alterar_img_carro.style.display = 'none';
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