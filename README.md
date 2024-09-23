# Chatbot com FastAPI e Padrões de Design

Este projeto é uma API de chatbot construída com **FastAPI**, utilizando **padrões de design** como **Strategy**, **Factory** e **princípios SOLID**. O chatbot realiza interações por meio de texto ou voz, integrando-se com APIs de **STT (Speech-to-Text)** e **TTS (Text-to-Speech)**. O código é organizado utilizando **interfaces**, **serviços**, **controladores** e **utilitários** para garantir modularidade e flexibilidade.

## Tabela de Conteúdos
- [Visão Geral](#visão-geral)
- [Arquitetura](#arquitetura)
- [Tecnologias Utilizadas](#tecnologias-utilizadas)
- [Funcionalidades](#funcionalidades)
- [Estrutura do Projeto](#estrutura-do-projeto)
- [Configuração e Instalação](#configuração-e-instalação)
- [Rotas Principais](#rotas-principais)
- [Exemplo de Uso](#exemplo-de-uso)
- [Testes](#testes)
- [Contribuições](#contribuições)
- [Licença](#licença)

## Visão Geral
Este chatbot utiliza FastAPI para criar uma API backend que fornece endpoints para comunicação com o usuário, seja via texto ou voz, integrando-se com APIs de STT e TTS para converter fala em texto e vice-versa.

## Arquitetura
A arquitetura do chatbot foi projetada seguindo os princípios SOLID e organizando o código de maneira modular com os seguintes componentes principais:
- **Controller**: Responsável por gerenciar as requisições HTTP e orquestrar as interações entre serviços.
- **Services**: Lógica central do chatbot, incluindo comunicação com APIs de STT e TTS.
- **Strategy Pattern**: Gerencia as estratégias de intenções e processamento de entrada e resposta. Aplicado em outras camadas também.
- **Factory Pattern**: Cria instâncias de serviços e componentes conforme necessário.
- **Utils**: Funções utilitárias que ajudam no processamento e validação de dados.

## Tecnologias Utilizadas
- **FastAPI**: Framework web para criar APIs rápidas e performáticas.
- **Python Tipado**: Uso de tipagem estática para maior segurança e clareza no código.
- **APIs de STT e TTS**: Integração com serviços de voz para facilitar interações por áudio.

## Funcionalidades
- **Interações via Texto e Voz**: O chatbot pode receber e responder tanto em texto quanto em áudio.
- **Modularidade**: Fácil adição de novas funcionalidades, como novas estratégias de resposta.
- **Boas Práticas de Design**: Implementação dos princípios SOLID e padrões de design para garantir código limpo e de fácil manutenção.

## Estrutura do Projeto
O projeto está dividido em diversos componentes para garantir uma separação de responsabilidades clara:
- **Interfaces**: Contratos para os serviços e estratégias, garantindo flexibilidade nas implementações.
- **Serviços (Services)**: Implementações que contêm a lógica central do chatbot.
- **Controladores (Controllers)**: Responsáveis por receber e processar as requisições HTTP e chamar os serviços adequados.
- **Utilitários (Utils)**: Funções auxiliares que facilitam operações comuns como formatação e validação.

## Configuração e Instalação

1. Clone o repositório:
   ```bash
   https://github.com/Alexandrelimax/backend_dialogflowcx.git
   ```
### Instale as dependências:

```bash
    pip install -r requirements.txt
```
