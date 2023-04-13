
let apellido = document.getElementByid('apellido')
let nombre = document.getElementByid('nombre')
let edad = document.getElementBy('edad')
let sexo = document.getElementBy('sexo')
let direccion = document.getElementBy('direccion')
let obrasocial = document.getElementBy('obrasocial')
let ingresodatos


class Documentos {

    constructor (apellido, npmbre, edad, sexo, direccion, obrasocial) {

        this.apellido = apellido
        this.nombre = nombre
        this.edad = edad
        this.direccion = direccion
        this.sexo = sexo
        this.obrasocial = obrasocial

    }
    


}
let apellido = new Documentos(`apellido`)