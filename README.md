# DevOps Docker CI Project

Projeto prático para demonstrar fundamentos de DevOps com Docker, GitHub Actions, testes automatizados e scan de segurança.

## Arquitetura

```text
Developer
   ↓
GitHub
   ↓
GitHub Actions
   ├── Tests
   ├── Lint
   ├── Docker Build
   └── Trivy Security Scan

## Security

A pipeline executa Trivy para análise de vulnerabilidades da imagem.

Atualmente algumas vulnerabilidades críticas são herdadas da imagem base Debian e são reportadas pelo scanner para acompanhamento.
