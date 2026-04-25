programa {
  funcao inicio() {
    cadeia nome
    escreva("Digite seu nome: ")
    leia(nome)
    escreva("Olá ", nome, "! Seja bem vindo")
    // declarando as variáveis
    real peso, altura, imc
  escreva("\nDigite seu peso (kg): ")
  leia(peso)
  escreva("Digite sua altura: ")
  leia(altura)
  
  // não esquecer de colocar a multiplicação
  // entre perênteses (altura * altura)
  imc = peso / (altura * altura)
  escreva("O resultado do imc é: ",imc)
    
  }
}
