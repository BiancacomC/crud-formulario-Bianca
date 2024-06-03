(function(win, doc){
        'use strict';
       
        //Veririca se o usuário quer realmente apagar o dado.
        if(doc.querySelector('.btnDel')){
            let btnDel = doc.querySelectorAll('.btnDel');//pega todos os botões de deletar que existirem na página
            for(let i = 0; i < btnDel.length; i++){
                btnDel[i].addEventListener('click', function(event){
                    if(confirm('Você quer realmente apagar este dado?')){
                        return true;
                    } else{
                        event.preventDefault();
                    }
                })
            }
        }
    })(window, document);