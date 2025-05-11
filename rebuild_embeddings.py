from open_notebook.domain.notebook import Source, Note
from open_notebook.database.repository import repo_query

def rebuild_embeddings():
    # 清除现有的嵌入
    print("清除现有的嵌入...")
    repo_query("DELETE FROM source_embedding;")
    
    # 重新生成源文档的嵌入
    print("重新生成源文档的嵌入...")
    sources = Source.get_all()
    for source in sources:
        print(f"处理源文档: {source.title}")
        source.vectorize()
    
    print("完成！")

if __name__ == "__main__":
    rebuild_embeddings() 