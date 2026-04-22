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
    for noticia in noticias:
        cursor.execute(
            f"""IF NOT EXISTS (SELECT TOP 1 * FROM [dbo].[tbl_NEWS] WHERE TITULO = '{noticia["titulo"]}')
                INSERT INTO [dbo].[tbl_NEWS] (TITULO,SUBTITULO,DESCRICAO,LINK)
                VALUES('{noticia['titulo']}',
                '{noticia['subtitulo']}',
                '{noticia['descricao']}',
                '{noticia['link']}')
                """
        )
    conn.commit()
    conn.close()
