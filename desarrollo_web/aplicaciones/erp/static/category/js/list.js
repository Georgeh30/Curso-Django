// Para cuando de carge la pagina list.html se ejecute esta funcion donde interara para cargar todos los
// registros dentro de la tabla html de una manera mas rapida con ajax
$(function() {
    $('#nombre_tabla_list').DataTable({
        responsive: true,  // Se adapte a movil o web
        autoWidth: false,  // Respeta los anchos de la columnas que especifique manualmente
        destroy: true,  // Reinicializar la tabla con otro proceso
        deferRender: true,  // Agiliza la carga de muchos datos con datatables
        ajax: {  // PETICION AJAX PARA PODER OBTENER LOS DATOS DE LA TABLA QUE ESTA EN EL template/list.js
            url: window.location.pathname,  // obtiene la ruta actual donde se encuentra la pagina web
            type: 'POST',  // tipo de peticion
            data: {
                'action': 'searchdata'
            },  // parametros, en este caso para ser enviado a la clase list dentro de views.py y recibida dentro.
            // Para cuando no se manda en formato diccionario, si no que dentro de una variable dentro de otro diccionario
            // pero se deja vacio porque no es asi.
            dataSrc: ""
        },
        // Para poner los nombres de cada atributo del diccionario que convertimos dentro de la clase listview en views.py
        // que son los nombres de cada columna de la tabla o modelo Category
        columns: [
            {"data": "id"},  // data es el nombre del diccionario y name el nombre de la columna en este caso la del id
            {"data": "name"},  // data es el nombre del diccionario y name el nombre de la columna
            {"data": "desc"},  // este es para indicar el nombre de la segunda columna de la tabla
            {"data": "desc"},  // para indicar la tercer columna del html que es donde estan los botones no importa el nombre
        ],
        // Nos sirve para personalizar cada columna de la tabla html
        columnDefs: [
            {
                targets: [-1],  // indicamos que de la columna con posicion 2 es la que vamos a modificar
                class: 'text-center',  // atributo html para que este centrado
                orderable: false,  // para decir que no se ordene esa columna ya que son solo botones
                // Para enviarles otros datos como una etiqueta html para que muestre un saludo o algo.
                render: function (data, type, row) {  // [data] ES PARA DE LA COLUMNA QUE ESTAMOS ESPECIFICANDO Y PARA EL OBJETO COMPLETO Y PODER LLAMAR row.name U OTRO DATO ESPECIFICO
                    // return data;  // Enviamos la info que querramos
                    var buttons = '<a href="/erp/category/update/'+ row.id +'/" class="btn btn-warning btn-sm"><i class="fas fa-edit"></i></a> ';
                    buttons += '<a href="/erp/category/delete/'+ row.id +'/" class="btn btn-danger btn-sm"><i class="fas fa-trash-alt"></i></a>';
                    return buttons;
                }
            }
        ],
        initComplete: function (settings, json) {  // Se ejecuta una vez se cargue la tabla con los datos
//            alert('Tabla Cargada');
        }
    });
});