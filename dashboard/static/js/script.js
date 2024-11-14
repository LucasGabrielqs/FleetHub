const menu = document.getElementById('sidebar-expansive');
const element_icon = document.getElementsByClassName('element-icon');
const sidebar_exp = document.getElementById('sidebar-expansive');
const img_expand = document.getElementById('img_sidebar-expansive');
const expand_button = document.getElementById('div-img_sidebar-expansive');
const icon_expand = document.getElementsByClassName('icon');
const sidebar = document.getElementById('sidebar');
const user_icon = document.getElementById('user_icon');//icone do menu de usuário
const user_menu = document.getElementById('user_menu');
const gestor_name = document.getElementById('gestor_name');
const texto1 = document.getElementById('text-init');
const texto2 = document.getElementById('text-veicles');
const texto3 = document.getElementById('text-users');
const texto4 = document.getElementById('text-reservations');
const texto5 = document.getElementById('text-routes');
const texto6 = document.getElementById('text-maintenance');
const texto7 = document.getElementById('text-supply');


user_menu.addEventListener('click', () => {//lógica para o menu de usuário
    if (user_icon.style.transform === 'rotate(0deg)') {//menu aberto
        user_icon.style.transform = 'rotate(180deg)';
    } else {//menu fechado
        user_icon.style.transform = 'rotate(0deg)';
    }
});


expand_button.addEventListener('click', () =>{//lógica para a barra lateral
    if (texto1.innerText){
        menu.style.width = '44px';
        sidebar.style.width = '44px';
        user_menu.style.width = '30px';
        user_menu.style.height = '30px';
        user_menu.style.justifyContent = 'center';
        img_expand.style.rotate = '180deg';
        gestor_name.innerText = '';
        user_icon.style.display = 'none';
        texto1.innerText = '';
        texto2.innerText = '';
        texto3.innerText = '';
        texto4.innerText = '';
        texto5.innerText = '';
        texto6.innerText = '';
        texto7.innerText = '';

        for (let icon of icon_expand) {
            icon.style.width = '24px'; // Ajuste de largura dos ícones
            icon.style.height = '24px';
        }
        for (let element of element_icon){
            element.style.marginLeft = '0';
        }
    }
    else{
        menu.style.transition = '800ms';
        sidebar.style.transition = '800ms';
        img_expand.style.rotate = '0deg';
        menu.style.width = '260px';
        sidebar.style.width = '260px';
        user_menu.style.width = '120px';
        user_menu.style.height = '40px';
        user_icon.style.display = 'block';
        user_menu.style.justifyContent = 'space-evenly';
        gestor_name.innerText = 'Thiago';
        texto1.innerText = 'Início';
        texto2.innerText = 'Veículos';
        texto3.innerText = 'Usuários';
        texto4.innerText = 'Reservas';
        texto5.innerText = 'Rotas';
        texto6.innerText = 'Manutenção';
        texto7.innerText = 'Abastecimento';
        for (let icon of icon_expand) {
            icon.style.width = '12px'; // Ajuste de largura dos ícones
            icon.style.height = '12px';
        }
        for (let element of element_icon){
            element.style.marginLeft = '15px';
        }
    }
})