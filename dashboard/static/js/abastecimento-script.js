const campos_input = document.getElementsByClassName('input_container');
const alterar_campos_input = document.getElementsByClassName('input_detect');
const alterar_imagem = document.getElementById('img');
const rodape = document.getElementById('rodape');

for (let i = 0; i < campos_input.length; i++) {
    campos_input[i].addEventListener('dblclick', () => {
        mostrarCustomConfirm()
    });
}

function fazer_alteracoes() {
    for (let i = 0; i < alterar_campos_input.length; i++) {
        alterar_campos_input[i].style.pointerEvents = 'visible'
    }
    alterar_imagem.style.display = 'flex';
    rodape.style.display = 'flex'; // Exibe o rodapé
}

function cancelar_alteracoes(){
    if(confirm('As Informações não Salvas serão Perdidas!')){
        for (let i = 0; i < alterar_campos_input.length; i++) {
            alterar_campos_input[i].style.pointerEvents = 'none'
        }
        alterar_imagem.style.display = 'none';
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
