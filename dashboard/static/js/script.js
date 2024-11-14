const menu = document.getElementById('sidebar-expansive');
const div = document.getElementById('div-img_sidebar-expansive');
const img_expand = document.getElementById('img_sidebar-expansive');
const icon_expand = document.getElementsByClassName('icon');
const texto1 = document.getElementById('text-init');
const texto2 = document.getElementById('text-veicles');
const texto3 = document.getElementById('text-users');
const texto4 = document.getElementById('text-reservations');
const texto5 = document.getElementById('text-routes');
const texto6 = document.getElementById('text-maintenance');
const texto7 = document.getElementById('text-supply');

div.addEventListener('click', () =>{
    if (texto1.innerText){
        menu.style.width = '40px';
        img_expand.style.rotate = '180deg';
        
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
    }
    else{
        menu.style.transition = '500ms';
        img_expand.style.rotate = '0deg';
        menu.style.width = '260px';
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
    }
})