(function(win,doc){
    'use strict';


    if(doc.querySelector('.btnDel')){
        let btnDel = doc.querySelectorAll('.btnDel');
        for(let i=0; i < btnDel.length; i++){
            btnDel[i].addEventListener('click', function(event){
                if(confirm('Tem certeza que deseja excluir ?')){
                    return true;
                }else{
                    event.preventDefault();
                }
            });
        }

    }
    if(doc.querySelector('#form')){
        let form = doc.querySelector('#form');
        function SendForm(event){
            event.preventDefault();
            let data = new FormData(form);
            const ajax = new XMLHttpRequest();
            let token = doc.querySelectorAll('input')[0].value;
            ajax.open('POST', form.action);
            ajax.setRequestHeader('X-CSRF-TOKEN', token)
            ajax.onreadystatechange = function(){
                if(ajax.status === 200 && ajax.readyState === 4){
                    let result = doc.querySelector('#result');
                    result.innerHTML = 'Cadastro Realizado com sucesso!'
                    result.classList.add('alert');
                    result.classList.add('alert-success');
                }
            }
            ajax.send(data);
            form.reset();
        }
        form.addEventListener('submit', SendForm, false);
    }
})(window,document);