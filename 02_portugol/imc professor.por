programa {
  funcao inicio() {
    cadeia nome 
     real peso, altura, imc
     escreva("Digite seu nome: ")
     leia(nome)
  escreva("\nDigite seu peso (kg): ")
  leia(peso)
  escreva("Digite sua altura: ")
  leia(altura)
  
  // não esquecer de colocar a multiplicação
  // entre perênteses (altura * altura)
  imc = peso / (altura * altura)
  escreva("---Bem vindo---", nome, " Seu imc é: ", imc)
    
  }
}
