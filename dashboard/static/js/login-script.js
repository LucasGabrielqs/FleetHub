const view_password = document.getElementById('view-password');
const id_pass = document.getElementById('id_password');

view_password.addEventListener('click', () =>{
    const span_hidden = view_password.getElementsByTagName('span')[0];
    
    if (span_hidden.getAttribute('class') == 'fa fa-eye fa-fw'){//quando está com o olho cortado, a senha estará visível
        span_hidden.setAttribute('class', 'fa fa-eye-slash fa-fw');//define o icone para o olho cortado
        view_password.setAttribute('tittle', 'Ocultar Senha');
        id_pass.setAttribute('type', 'text');
    }
    else{
        span_hidden.setAttribute('class', 'fa fa-eye fa-fw')//define o icone para o olho normal
        view_password.setAttribute('tittle', 'Exibir Senha');
        id_pass.setAttribute('type', 'password');
    }
})