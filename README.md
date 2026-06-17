# DevOps Docker CI Pipeline

Projeto desenvolvido para demonstrar conhecimentos em DevOps, automação de CI/CD, containers, testes automatizados e segurança de imagens.

## Objetivos

Este projeto implementa uma pipeline completa utilizando GitHub Actions para:

* Executar testes automatizados
* Validar qualidade do código
* Realizar formatação automática
* Construir imagens Docker
* Executar análise de vulnerabilidades com Trivy
* Publicar imagens no GitHub Container Registry (GHCR)
* Utilizar versionamento semântico através de tags Git

---

## Arquitetura

```text
Developer
    │
    ▼
Git Push
    │
    ▼
GitHub Actions
    │
    ├── Pytest
    ├── Flake8
    ├── Black
    ├── Docker Build
    ├── Trivy Scan
    └── Push to GHCR
                │
                ▼
GitHub Container Registry
```

---

## Stack Utilizada

### Aplicação

* Python 3.12
* Flask
* Gunicorn

### DevOps

* Docker
* GitHub Actions
* GitHub Container Registry (GHCR)

### Qualidade

* Pytest
* Flake8
* Black

### Segurança

* Trivy

---

## Estrutura do Projeto

```text
.
├── app
│   ├── __init__.py
│   └── main.py
│
├── tests
│   └── test_app.py
│
├── .github
│   └── workflows
│       └── ci.yml
│
├── Dockerfile
├── requirements.txt
├── requirements-dev.txt
├── pytest.ini
├── .flake8
└── README.md
```

---

## Endpoints

### Health Check

```http
GET /health
```

Resposta:

```json
{
  "status": "healthy"
}
```

### Products

```http
GET /products
```

Resposta:

```json
[
  {
    "id": 1,
    "name": "Keyboard"
  },
  {
    "id": 2,
    "name": "Mouse"
  }
]
```

---

## Execução Local

### Clonar o repositório

```bash
git clone git@github.com:paulooj/devops-docker-ci.git

cd devops-docker-ci
```

### Criar ambiente virtual

```bash
python3 -m venv venv

source venv/bin/activate
```

### Instalar dependências

```bash
pip install -r requirements.txt
pip install -r requirements-dev.txt
```

### Executar aplicação

```bash
python app/main.py
```

---

## Executando Testes

```bash
pytest
```

---

## Verificando Qualidade

### Lint

```bash
flake8 app tests
```

### Formatação

```bash
black --check app tests
```

---

## Build Docker

```bash
docker build -t devops-docker-ci .
```

Executar container:

```bash
docker run -p 5000:5000 devops-docker-ci
```

---

## Pipeline CI/CD

A pipeline executa automaticamente:

```text
Push
 │
 ▼
Tests
 │
 ▼
Lint
 │
 ▼
Formatting
 │
 ▼
Docker Build
 │
 ▼
Trivy Scan
 │
 ▼
Push GHCR
```

---

## Versionamento Semântico

O projeto utiliza Semantic Versioning.

Exemplos:

```text
v1.0.0
v1.0.1
v1.1.0
v2.0.0
```

Criar nova versão:

```bash
git tag v1.0.0

git push origin v1.0.0
```

---

## Imagem Docker

Publicada automaticamente no GitHub Container Registry.

Exemplo:

```text
ghcr.io/paulooj/devops-docker-ci
```

Pull da imagem:

```bash
docker pull ghcr.io/paulooj/devops-docker-ci:latest
```

---

## Segurança

A pipeline executa análise de vulnerabilidades utilizando Trivy.

Itens analisados:

* Sistema Operacional da imagem
* Dependências Python
* Bibliotecas instaladas

---

## Problemas Resolvidos Durante o Projeto

Durante o desenvolvimento foram resolvidos problemas comuns encontrados em pipelines reais:

* Configuração de ambiente virtual Python
* Troubleshooting de imports no Pytest
* Conflito entre Black e Flake8
* Integração GitHub Actions
* Autenticação GitHub via SSH
* Integração com GitHub Container Registry (GHCR)
* Tratamento de vulnerabilidades identificadas pelo Trivy

---

## Próximas Evoluções

* [ ] Multi-stage Docker build otimizado
* [ ] Geração de SBOM com Syft
* [ ] Assinatura de imagens com Cosign
* [ ] Deploy em Kubernetes
* [ ] GitOps com Argo CD
* [ ] Observabilidade com Prometheus e Grafana
* [ ] Provisionamento de infraestrutura com Terraform

---

## Aprendizados

Este projeto foi desenvolvido como parte da preparação para atuar como Engenheiro DevOps, praticando conceitos de:

* CI/CD
* Containers
* Segurança
* Automação
* Testes
* Versionamento
* Troubleshooting
* Boas práticas de desenvolvimento

---

## Autor

Paulo Pereira

Projeto desenvolvido para evolução prática em DevOps, Cloud e Platform Engineering.
