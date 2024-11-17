// 1. Histórico escolar de qualquer aluno
// Trocar o ID para o aluno desejado:
MATCH (a:Aluno {id: "22122000"})-[r:MATRICULADO]->(d:Disciplina)
RETURN d.id AS disciplina_codigo, 
       d.nome AS disciplina_nome, 
       r.ano AS ano, 
       r.semestre AS semestre, 
       r.nota_final AS nota
ORDER BY r.ano, r.semestre;

// 2. Histórico de disciplinas ministradas por qualquer professor
// Trocar o ID para o professor desejado:
MATCH (p:Professor {id: "P002"})-[r:MINISTRA]->(d:Disciplina)
RETURN d.id AS disciplina_codigo, 
       d.nome AS disciplina_nome, 
       r.ano AS ano, 
       r.semestre AS semestre;

// 3. Listar alunos que já se formaram (foram aprovados em todos os cursos de uma matriz curricular)
// No exemplo, a query utiliza o ano 2023 e o primeiro semestre, alterar caso seja necessário:
MATCH (a:Aluno)-[r:MATRICULADO]->(d:Disciplina)
WHERE r.nota_final >= 5.0
AND r.ano = 2023 AND r.semestre = 1
WITH DISTINCT a.id AS RA, a.nome AS aluno_nome
RETURN RA, aluno_nome;

// 4. Listar todos os professores que são chefes de departamento, junto com o nome do departamento
MATCH (p:Professor)-[:CHEFE]->(d:Departamento)
RETURN p.id AS RA, 
       p.nome AS professor_nome, 
       d.nome AS departamento_nome;

// 5. Saber quais alunos formaram um grupo de TCC e qual professor foi o orientador
MATCH (a:Aluno)-[:PERTENCE_AO_GRUPO]->(t:TCC)<-[:ORIENTA]-(p:Professor)
RETURN a.id AS aluno_id, 
       a.nome AS aluno_nome, 
       p.id AS professor_id, 
       p.nome AS orientador, 
       t.titulo AS titulo;
