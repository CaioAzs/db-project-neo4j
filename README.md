# Banco de Dados - NEO4J

---
Caio de Souza Conceição - RA: 22.122.033-8 <br>
Lucas Dias Batista - RA: 22.122.065-0

---

Este projeto utiliza o **Neo4j**, para modelar um modelo básico de faculdade. As coleções principais usadas para armazenar os dados são:

1. **Departamento**: Armazena informações sobre os departamentos da universidade.
   - Atributos: `id`, `nome`

2. **Curso**: Armazena os cursos oferecidos pela universidade.
   - Atributos: `id`, `nome`
   - Relacionamento com `Departamento`: Um curso pertence a um departamento.

3. **Disciplina**: Armazena as disciplinas oferecidas nos cursos.
   - Atributos: `id`, `nome`
   - Relacionamento com `Curso`: Uma disciplina pertence a um curso.

4. **Professor**: Armazena informações sobre os professores.
   - Atributos: `id`, `nome`
   - Relacionamento com `Departamento`: Um professor pode ser chefe de um departamento.
   - Relacionamento com `Disciplina`: Um professor ministra uma disciplina em determinado semestre e ano.

5. **Aluno**: Armazena informações sobre os alunos da universidade.
   - Atributos: `id`, `nome`
   - Relacionamento com `Disciplina`: Um aluno pode ser matriculado em várias disciplinas, com suas notas e semestres.

6. **TCC**:  Armazena grupos de TCC.
   - Atributos: `id`, `titulo`
   - Relacionamento com `Aluno`: Um aluno pode pertencer a um grupo de TCC.
   - Relacionamento com `Professor`: Um professor pode orientar um TCC.


### Queries utilizadas

1. **Professores Chefes de Departamento**:

```cypher
MATCH (p:Professor)-[:CHEFE]->(d:Departamento)
RETURN p.id AS RA, p.nome AS professor_nome, d.nome AS departamento_nome;
```

2. **Alunos Formados em 2023 - 1º Semestre**:

```cypher
MATCH (a:Aluno)-[r:MATRICULADO]->(d:Disciplina)
WHERE r.nota_final >= 5.0 AND r.ano = 2023 AND r.semestre = 1
WITH DISTINCT a.id AS RA, a.nome AS aluno_nome
RETURN RA, aluno_nome;
```

3. **Histórico de Disciplinas de um Professor (P002)**:

```cypher
MATCH (p:Professor {id: "P002"})-[r:MINISTRA]->(d:Disciplina)
RETURN d.id AS disciplina_codigo, d.nome AS disciplina_nome, r.ano AS ano, r.semestre AS semestre;
```

4. **Histórico do Aluno 22122000**:

```cypher
MATCH (a:Aluno {id: "22122000"})-[r:MATRICULADO]->(d:Disciplina)
RETURN d.id AS disciplina_codigo, d.nome AS disciplina_nome, r.ano AS ano, r.semestre AS semestre, r.nota_final AS nota
ORDER BY r.ano, r.semestre;
```

5. **Grupos de TCC**:

```cypher
MATCH (a:Aluno)-[:PERTENCE_AO_GRUPO]->(t:TCC)<-[:ORIENTA]-(p:Professor)
RETURN a.id AS aluno_id, a.nome AS aluno_nome, p.id AS professor_id, p.nome AS orientador, t.titulo as titulo;
```


### Como Executar o Código e Validar as Queries

1. **Executar o docker compose**:
     ```
     docker-compose up -d
     ```

2. **Instalar a Biblioteca Python**:
     ```
     pip install neo4j
     ```

3. **Executar o Código**:
     ```
     python main.py
     ```

4. **Validação das Queries**:
   - As queries podem ser executadas diretamente na interface do Neo4j (Neo4j Browser) ou direto pelo código Python.
