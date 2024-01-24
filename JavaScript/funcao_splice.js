
// A função splice altera um array
// Ela pode remover como também substituir elementos de um array

// remover 1 elemento a partir da posição do indice de memoria

let numeros = [1,2,3,4,5]

numeros.splice(2,1)

console.log("resultadoremoção",numeros)

let numeros2 = [1,2,3,4,5]

numeros2.splice(2,1,500)

console.log("Resultado substituição array",numeros2)

