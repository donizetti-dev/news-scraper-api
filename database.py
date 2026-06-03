from dotenv import load_dotenv
import os
load_dotenv()
import pyodbc


def get_connection():
    conn = pyodbc.connect(
        f'DRIVER={{{os.getenv("DB_DRIVER")}}};'
        f'SERVER={{{os.getenv("DB_SERVER")}}};'
        f'DATABASE={{{os.getenv("DB_NAME")}}};'
        "Trusted_Connection=yes;"
    )
    return conn

def insert_news(noticias):

    conn = get_connection()
    cursor = conn.cursor()
    #IF NOT EXISTS (SELECT TOP 1 * FROM [dbo].[tbl_NEWS] WHERE TITULO = '{noticia["titulo"]}')
    for noticia in noticias:
        cursor.execute(
            f"""
                INSERT INTO [dbo].[tbl_NEWS] (TITULO,SUBTITULO,DESCRICAO,LINK)
                VALUES('{noticia['titulo']}',
                '{noticia['subtitulo']}',
                '{noticia['descricao']}',
                '{noticia['link']}')
                """
        )
    conn.commit()
    conn.close()

def update_details(id,details):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        f"""UPDATE [dbo].[tbl_NEWS] 
        SET TITULO = '{details['titulo']}',
        SUBTITULO = '{details['subtitulo']}',
        DESCRICAO = '{details['descricao']}'
        WHERE ID = {id}
            """
    )
    conn.commit()
    conn.close()

def get_news():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""SELECT ID,
                   TITULO,
                    SUBTITULO,                           
                    DESCRICAO,
                    LINK,
                    CONCAT('',DATA_EXECUCAO) AS DATA_EXECUCAO 
                    FROM [NoticiasDB].[dbo].[tbl_NEWS]
                   """)
    
    rows = cursor.fetchall()
    data_news = []

    for row in rows:

        data_news.append({
            "id":row.ID,
            "title":row.TITULO,
            "caption":row.SUBTITULO,
            "description":row.DESCRICAO,
            "link":row.LINK,
            "execution_date":row.DATA_EXECUCAO
        })

    return data_news

def get_idrow(id):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(f"""SELECT ID,
                   TITULO,
                    SUBTITULO,                           
                    DESCRICAO,
                    LINK,
                    CONCAT('',DATA_EXECUCAO) AS DATA_EXECUCAO 
                    FROM [NoticiasDB].[dbo].[tbl_NEWS]
                   WHERE ID = {id}
                   """)
    
    rows = cursor.fetchall()
    data_news = []

    for row in rows:

        data_news.append({
            "id":row.ID,
            "title":row.TITULO,
            "caption":row.SUBTITULO,
            "description":row.DESCRICAO,
            "link":row.LINK,
            "execution_date":row.DATA_EXECUCAO
        })

    return data_news

def query_pending():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""SELECT ID,TITULO,LINK 
                    FROM [NoticiasDB].[dbo].[tbl_NEWS]
                    WHERE TITULO = 'PENDENTE'
                   """)
    
    rows = cursor.fetchall()
    details_pending = []

    for row in rows:

        details_pending.append({
            "id":row.ID,
            "title":row.TITULO,
            "link":row.LINK,
        })

    return details_pending

