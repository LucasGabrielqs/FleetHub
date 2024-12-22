buttonhoje = document.getElementById('button-hoje');
buttonproximosdias = document.getElementById('button-proximosdias');

buttonhoje.addEventListener('click', () =>{
    alternar_botoes()
})
buttonproximosdias.addEventListener('click', () =>{
    alternar_botoes()
})

function alternar_botoes(){
    if (buttonhoje.getAttribute('class') == 'button-hoje-selecionado'){
        buttonhoje.setAttribute('class', 'button-hoje')
        buttonproximosdias.setAttribute('class', 'button-proximosdias-selecionado')
    }
    else if (buttonproximosdias.getAttribute('class') == 'button-proximosdias-selecionado'){
        buttonhoje.setAttribute('class', 'button-hoje-selecionado')
        buttonproximosdias.setAttribute('class', 'button-proximosdias')
    }
}
