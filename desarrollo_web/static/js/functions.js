// SEGUNDA OPCION PARA MOSTRAR MENSAJE DE ERROR UTILIZANDO AJAX

// FUNCION PARA GUARDAR ALGUN MENSAJE DE ERROR Y DARLE FORMATO HTML PARA
// ENVIARLO DENTRO DEL METODO DE ABAJO PARA QUE SE MUESTRE DENTRO DEL MENSAJE DE ERROR
function message_error(obj) {
    var html = '';
    if (typeof (obj) == 'object') { // Si es un Objeto
        html = '<ul style="text-align: left;">';
        $.each(obj, function(key, value){
            html += '<li>' + key + ': ' + value + '</li>';
        });
        html += '</ul>';
    } else {
        html = '<p>' + obj + '</p>';
    }

    // Mensaje de Error
    Swal.fire({
        title: 'Error!',
        html: html,
        icon: 'error'
    });
}