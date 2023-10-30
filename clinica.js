



class Documento {

    constructor(dni, apellido, nombre, edad, sexo, direccion, obrasocial) {
        this.dni = dni
        this.apellido = apellido
        this.nombre = nombre
        this.edad = edad
        this.direccion = direccion
        this.sexo = sexo
        this.obrasocial = obrasocial

    }

}
// DOM Events
//document.getElementById('ingreso')

//.addEventListener('submit', function (e) {
function captura() {
    const dni = document.getElementById('dni').value;
    const apellido = document.getElementById('apellido').value;

    const nombre = document.getElementById('nombre').value;

    const edad = document.
        getElementById('edad').value;

    const sexo = document.getElementById('sexo').value;

    const direccion = document.getElementById('direccion').value;

    const obrasocial = document.getElementById('obrasocial').value;

   // console.log(dni,apellido, nombre, edad, sexo)
}


const Docu = new Documento(dni, apellido, nombre, sexo, edad, direccion, obrasocial)

console.log(Docu(dni,apellido, ))
captura(dni, apellido, nombre, sexo, direccion, obrasocial)
{
    if (dni == Docu(dni)) {
        alert("cargar turno")
    }
    else { 
    // e.preventDefault();
    alert("dar turno")}

}




class UI {
    addDocumentos(Docu) {
        const listado = document.getElementById('listado');
        const element = document.createElement('div');
        element.innerHTML = `
            <div class ="tarjeta">
                <div class="tarjeta formato">
                    <strong> Documentos Apellido</strong> : ${Docu.apellido}

                    <strong> Documentos Nombre</strong> : ${Docu.nombre};                    

                </div>




            </div> `;

        listado.appendChild(element);

        const UIT = new UI();
        UIT.addproduct(Docu);





    }

    deleteDocumentos() {

    }

    showMessage() {

    }
}


