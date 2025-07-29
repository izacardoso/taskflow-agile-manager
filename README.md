# TaskFlow Agile Manager

## 🎯 Objetivo
Sistema para gerenciamento de tarefas baseado em metodologias ágeis, desenvolvido para uma startup de logística.

## 📌 Escopo
- CRUD de tarefas (Create, Read, Update, Delete)
- Planejamento com GitHub Projects (Kanban)
- Pipeline de testes com GitHub Actions
- Simulação de mudança de escopo

## 🔧 Metodologia Utilizada
SCRUM e Kanban com o uso do GitHub Projects para organização das tarefas.

## 🛠️ Tecnologias
- Python + Flask
- SQLite (opcional, usando lista em memória por simplicidade)
- PyTest
- GitHub Actions

## 🚀 Como Executar
```bash
git clone https://github.com/izacardoso/taskflow-agile-manager.git
cd taskflow-agile-manager
pip install -r requirements.txt
python src/app.py
```

## ✅ Testes
```bash
pytest
```

## 🔄 Mudança no Escopo
Durante o desenvolvimento, o cliente solicitou suporte a login de usuários. Essa mudança foi registrada no Kanban e documentada aqui como futura implementação.

## 👤 Desenvolvedora
Izabella Cardoso