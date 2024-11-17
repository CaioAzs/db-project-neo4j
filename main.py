from neo4j import GraphDatabase
import random

URI = "neo4j://localhost"
AUTH = ("neo4j", "adminadmin")

try:
    driver = GraphDatabase.driver(URI, auth=(AUTH))
    print("Conexão com o Neo4j estabelecida.")
except Exception as e:
    print("Erro ao conectar ao Neo4j:", e)
    exit()

disciplinas = [
    {"id": "DS1000", "nome": "Cálculo Diferencial e Integral"},
    {"id": "DS1002", "nome": "Física"},
    {"id": "DS1003", "nome": "Álgebra Linear"},
    {"id": "DS1004", "nome": "Mecânica dos Sólidos"},
    {"id": "DS1005", "nome": "Banco de Dados"},
    {"id": "DS1006", "nome": "Termodinâmica"},
    {"id": "DS1007", "nome": "Cálculo Numérico"},
    {"id": "DS1008", "nome": "Resistência dos Materiais"},
    {"id": "DS1009", "nome": "Fundamentos de Programação"}
]

alunos = [
    {"id": "22122000", "nome": "Caio"},
    {"id": "22122001", "nome": "Lucas Dias"},
    {"id": "22122002", "nome": "Lucas Rebouças"},
    {"id": "22122003", "nome": "Pedro Algodão"},
    {"id": "22122004", "nome": "Samir Costa"}
]

professores = [
    {"id": "P001", "nome": "Luciano"},
    {"id": "P002", "nome": "Anjoletto"},
    {"id": "P003", "nome": "Isaac"},
    {"id": "P004", "nome": "Charles"},
    {"id": "P005", "nome": "Destro"}
]

cursos = [
    {"id": "CO001", "nome": "Ciência da Computação"},
    {"id": "CO002", "nome": "Administração"},
    {"id": "CO003", "nome": "Engenharia Elétrica"}
]

departamentos = [
    {"id": "DP001", "nome": "Ciência da Computação"},
    {"id": "DP002", "nome": "Administração"},
    {"id": "DP003", "nome": "Engenharias"}
]

# Criar relação "MINISTRA" entre Professores e Disciplinas
professor_disciplina_relations = [
    {"professor_id": "P001", "disciplina_id": "DS1000", "ano": 2023, "semestre": 1},
    {"professor_id": "P002", "disciplina_id": "DS1002", "ano": 2023, "semestre": 1},
    {"professor_id": "P003", "disciplina_id": "DS1003", "ano": 2023, "semestre": 2},
    {"professor_id": "P004", "disciplina_id": "DS1004", "ano": 2024, "semestre": 1},
    {"professor_id": "P002", "disciplina_id": "DS1005", "ano": 2024, "semestre": 1},
    {"professor_id": "P005", "disciplina_id": "DS1006", "ano": 2024, "semestre": 1},
    {"professor_id": "P001", "disciplina_id": "DS1007", "ano": 2024, "semestre": 1},
    {"professor_id": "P002", "disciplina_id": "DS1008", "ano": 2024, "semestre": 1},
    {"professor_id": "P003", "disciplina_id": "DS1009", "ano": 2024, "semestre": 1}
]

# Criar relação CHEFE entre Professor e Departamento
professor_departamento_relations = [
    {"professor_id": "P001", "departamento_id": "DP001"},  # Luciano -> Ciência da Computação
    {"professor_id": "P002", "departamento_id": "DP002"},  # Anjoletto -> Administração
    {"professor_id": "P003", "departamento_id": "DP003"}   # Isaac -> Engenharias
]

# Criar relação MATRICULADO entre Alunos e Disciplinas
matriculas = [
    {"aluno_id": "22122000", "disciplina_id": "DS1000", "ano": 2023, "semestre": 1, "nota_final": (10.0)}, #Aluno formado no 1 semestre de 2023
    {"aluno_id": "22122000", "disciplina_id": "DS1006", "ano": 2023, "semestre": 1, "nota_final": (9.0)},
    {"aluno_id": "22122000", "disciplina_id": "DS1008", "ano": 2023, "semestre": 1, "nota_final": (10.0)},
    {"aluno_id": "22122000", "disciplina_id": "DS1009", "ano": 2023, "semestre": 1, "nota_final": (10.0)},
    {"aluno_id": "22122001", "disciplina_id": "DS1000", "ano": 2023, "semestre": 1, "nota_final": random.uniform(3.0, 10.0)},
    {"aluno_id": "22122002", "disciplina_id": "DS1001", "ano": 2023, "semestre": 2, "nota_final": random.uniform(3.0, 10.0)},
    {"aluno_id": "22122003", "disciplina_id": "DS1001", "ano": 2024, "semestre": 1, "nota_final": random.uniform(3.0, 10.0)},
    {"aluno_id": "22122001", "disciplina_id": "DS1002", "ano": 2024, "semestre": 1, "nota_final": random.uniform(3.0, 10.0)},
    {"aluno_id": "22122002", "disciplina_id": "DS1002", "ano": 2024, "semestre": 2, "nota_final": random.uniform(3.0, 10.0)},
    {"aluno_id": "22122003", "disciplina_id": "DS1003", "ano": 2024, "semestre": 2, "nota_final": random.uniform(3.0, 10.0)},
    {"aluno_id": "22122004", "disciplina_id": "DS1003", "ano": 2024, "semestre": 1, "nota_final": random.uniform(3.0, 10.0)},
    {"aluno_id": "22122004", "disciplina_id": "DS1004", "ano": 2024, "semestre": 2, "nota_final": random.uniform(3.0, 10.0)},
    {"aluno_id": "22122002", "disciplina_id": "DS1004", "ano": 2023, "semestre": 1, "nota_final": random.uniform(3.0, 10.0)},
    {"aluno_id": "22122001", "disciplina_id": "DS1005", "ano": 2023, "semestre": 2, "nota_final": random.uniform(3.0, 10.0)},
    {"aluno_id": "22122003", "disciplina_id": "DS1005", "ano": 2024, "semestre": 1, "nota_final": random.uniform(3.0, 10.0)},
    {"aluno_id": "22122002", "disciplina_id": "DS1006", "ano": 2023, "semestre": 1, "nota_final": random.uniform(3.0, 10.0)},
    {"aluno_id": "22122004", "disciplina_id": "DS1007", "ano": 2024, "semestre": 2, "nota_final": random.uniform(3.0, 10.0)},
    {"aluno_id": "22122003", "disciplina_id": "DS1007", "ano": 2023, "semestre": 1, "nota_final": random.uniform(3.0, 10.0)},
    {"aluno_id": "22122001", "disciplina_id": "DS1008", "ano": 2024, "semestre": 1, "nota_final": random.uniform(3.0, 10.0)},
    {"aluno_id": "22122001", "disciplina_id": "DS1009", "ano": 2023, "semestre": 1, "nota_final": random.uniform(3.0, 10.0)}
]



def create_nodes_and_relationships():
    with driver.session() as session:
        # Criar Departamentos
        for departamento in departamentos:
            session.run("""
            CREATE (d:Departamento {id: $id, nome: $nome})
            """, id=departamento["id"], nome=departamento["nome"])
            
        #Cria cursos e associa a um departamento
        for curso, departamento in zip(cursos, departamentos):
            session.run("""
            CREATE (c:Curso {id: $id, nome: $nome})
            """, id=curso["id"], nome=curso["nome"])
            
            session.run("""
            MATCH (c:Curso {id: $curso_id}), (d:Departamento {id: $dep_id})
            CREATE (c)-[:PERTENCE]->(d)
            """, curso_id=curso["id"], dep_id=departamento["id"])

        # Criar Disciplinas e Relacioná-las aos Cursos
        for disciplina in disciplinas:
            session.run("""
            CREATE (disc:Disciplina {id: $id, nome: $nome})
            """, id=disciplina["id"], nome=disciplina["nome"])
            session.run("""
            MATCH (disc:Disciplina {id: $id}), (c:Curso {id: $curso_id})
            CREATE (disc)-[:PERTENCE]->(c)
            """, id=disciplina["id"], curso_id=cursos[random.randint(0,2)]["id"])

        # Criar Professores e Alunos
        for professor in professores:
            session.run("""
            CREATE (p:Professor {id: $id, nome: $nome})
            """, id=professor["id"], nome=professor["nome"])
        for aluno in alunos:
            session.run("""
            CREATE (a:Aluno {id: $id, nome: $nome})
            """, id=aluno["id"], nome=aluno["nome"])
            
            
        
        #CRIAÇÃO DAS RELAÇÕES
        for relation in professor_disciplina_relations:
            session.run("""
            MATCH (p:Professor {id: $professor_id}), (d:Disciplina {id: $disciplina_id})
            CREATE (p)-[:MINISTRA {ano: $ano, semestre: $semestre}]->(d)
            """, 
            professor_id=relation["professor_id"], 
            disciplina_id=relation["disciplina_id"], 
            ano=relation["ano"], 
            semestre=relation["semestre"])
            
        for relation in professor_departamento_relations:
            session.run("""
            MATCH (p:Professor {id: $professor_id}), (d:Departamento {id: $departamento_id})
            CREATE (p)-[:CHEFE]->(d)
            """, 
            professor_id=relation["professor_id"], 
            departamento_id=relation["departamento_id"])
            
        for matricula in matriculas:
            session.run("""
            MATCH (a:Aluno {id: $aluno_id}), (d:Disciplina {id: $disciplina_id})
            CREATE (a)-[:MATRICULADO {ano: $ano, semestre: $semestre, nota_final: $nota_final}]->(d)
            """, 
            aluno_id=matricula["aluno_id"], 
            disciplina_id=matricula["disciplina_id"], 
            ano=matricula["ano"], 
            semestre=matricula["semestre"], 
            nota_final=matricula["nota_final"])

        # Criar Relações de TCC
        session.run("""
        CREATE (t:TCC {id: "TCC001", titulo: "Estudo de Grafo"})
        """)
        session.run("""
        MATCH (a:Aluno {id: "22122000"}), (p:Professor {id: "P001"}), (t:TCC {id: "TCC001"})
        CREATE (a)-[:PERTENCE_AO_GRUPO]->(t)
        CREATE (p)-[:ORIENTA]->(t)
        """)
        session.run("""
        MATCH (a:Aluno {id: "22122001"}), (t:TCC {id: "TCC001"})
        CREATE (a)-[:PERTENCE_AO_GRUPO]->(t)
        """)
        session.run("""
        MATCH (a:Aluno {id: "22122002"}), (t:TCC {id: "TCC001"})
        CREATE (a)-[:PERTENCE_AO_GRUPO]->(t)
        """)

try:
    create_nodes_and_relationships()
    print("Nós e relações criados.")
except Exception as e:
    print("Erro ao criar nós ou relações:", e)
    
def run_queries():
    with driver.session() as session:
        query1 = """
        MATCH (p:Professor)-[:CHEFE]->(d:Departamento)
        RETURN p.id AS RA, p.nome AS professor_nome, d.nome AS departamento_nome;
        """
        result1 = session.run(query1)
        print("\nProfessores Chefes de Departamento:")
        for record in result1:
            print(f"RA: {record['RA']} | Professor: {record['professor_nome']} | Departamento: {record['departamento_nome']}")
        
        query2 = """
        MATCH (a:Aluno)-[r:MATRICULADO]->(d:Disciplina)
        WHERE r.nota_final >= 5.0 AND r.ano = 2023 AND r.semestre = 1
        WITH DISTINCT a.id AS RA, a.nome AS aluno_nome
        RETURN RA, aluno_nome;
        """
        result2 = session.run(query2)
        print("\nAlunos Formados em 2023 - 1º Semestre:")
        for record in result2:
            print(f"RA: {record['RA']} | Aluno: {record['aluno_nome']}")
        
        query3 = """
        MATCH (p:Professor {id: "P002"})-[r:MINISTRA]->(d:Disciplina)
        RETURN d.id AS disciplina_codigo, d.nome AS disciplina_nome, r.ano AS ano, r.semestre AS semestre;
        """
        result3 = session.run(query3)
        print("\nHistórico de Disciplinas de um Professor (P002):")
        for record in result3:
            print(f"Disciplina: {record['disciplina_nome']} ({record['disciplina_codigo']}) | Ano: {record['ano']} | Semestre: {record['semestre']}")
        
        query4 = """
        MATCH (a:Aluno {id: "22122000"})-[r:MATRICULADO]->(d:Disciplina)
        RETURN d.id AS disciplina_codigo, d.nome AS disciplina_nome, r.ano AS ano, r.semestre AS semestre, r.nota_final AS nota
        ORDER BY r.ano, r.semestre;
        """
        result4 = session.run(query4)
        print("\nHistórico do Aluno 22122000:")
        for record in result4:
            print(f"Disciplina: {record['disciplina_nome']} ({record['disciplina_codigo']}) | Ano: {record['ano']} | Semestre: {record['semestre']} | Nota: {record['nota']}")
        
        query5 = """
        MATCH (a:Aluno)-[:PERTENCE_AO_GRUPO]->(t:TCC)<-[:ORIENTA]-(p:Professor)
        RETURN a.id AS aluno_id, a.nome AS aluno_nome, p.id AS professor_id, p.nome AS orientador, t.titulo as titulo;
        """
        result5 = session.run(query5)
        print("\nGrupos de TCC:")
        for record in result5:
            print(f"Aluno: {record['aluno_nome']} ({record['aluno_id']}) | Orientador: {record['orientador']} ({record['professor_id']}) | TCC: {record['titulo']}")
            
try:
    run_queries()
except Exception as e:
    print("Erro ao executar as consultas:", e)
finally:
    driver.close()
    print("Conexão com o Neo4j encerrada.")