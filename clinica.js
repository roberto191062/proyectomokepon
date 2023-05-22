



class Documentos {

    constructor(numerodocumento, apellido, nombre, edad, sexo, direccion, obrasocial) {
        this.numerodocumento = numerodocumento
        this.apellido = apellido
        this.nombre = nombre
        this.edad = edad
        this.direccion = direccion
        this.sexo = sexo
        this.obrasocial = obrasocial

    }

}
// DOM Events
document.getElementById('ingreso')

    .addEventListener('submit', function (e) {
     alert(ingreso)
        const apellido = document.getElementById('apellido').value;

        const nombre = document.getElementById('nombre').value;
        const edad = document.getElementById('edad').value;
        const sexo = document.getElementById('edad').value;
        const direccion = document.getElementById('direccion').value;
        const obrasocial = document.getElementById('obrasocial').value;

        

        const Documentos = new Documentos(apellido, nombre, sexo, edad, direccion, obrasocial)

        console.log(Documentos.apellido);

        const ui = new ui();
        ui.addproduct(Documentos);

        e.preventDefault();



      }
    )

class UI {
    addDocumentos(Documentos) {
        const element = document.createElement('div');
        element.innerHTML =`
            <div class ="tarjeta">
                <div class="tarjeta body">
                    <strong> Documentos Apellido</strong> : ${Documentos.apellido}

                    <strong> Documentos Nombre</strong> : ${Documentos.nombre};                    

                </div>




            </div>;

            listado.appendChild(element);`

    }

    deleteDocumentos() {

    }

    showMessage() {

    }
}


