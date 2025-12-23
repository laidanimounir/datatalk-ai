import pandas as pd
from pathlib import Path
from typing import List

class ExcelProcessor:
    """معالج ملفات Excel لتحويلها إلى نصوص"""
    
    def __init__(self, excel_folder: str = "data/exel"):
        self.excel_folder = Path(excel_folder)
    
    def load_excel_as_text(self, file_path: Path) -> List[str]:
        """تحويل ملف Excel إلى قائمة من النصوص"""
        
        # قراءة الملف
        if file_path.suffix == '.csv':
            df = pd.read_csv(file_path)
        else:
            df = pd.read_excel(file_path)
        
        documents = []
        
        # تحويل كل صف إلى نص
        for idx, row in df.iterrows():
            text_parts = [f"from file {file_path.name}:"]
            
            for col in df.columns:
                value = row[col]
                if pd.notna(value):  # تجاهل القيم الفارغة
                    text_parts.append(f"{col}: {value}")
            
            document = " | ".join(text_parts)
            documents.append(document)
        
        return documents
    
    def process_all_files(self) -> List[dict]:
        """معالجة جميع ملفات Excel"""
        
        all_documents = []
        excel_files = list(self.excel_folder.glob("*.xlsx")) + \
                      list(self.excel_folder.glob("*.csv"))
        
        print(f"processing {len(excel_files)} file...")
        
        for file in excel_files:
            print(f"  - processing {file.name}")
            texts = self.load_excel_as_text(file)
            
            # إضافة metadata لكل document
            for text in texts:
                all_documents.append({
                    "content": text,
                    "source": file.name,
                    "type": "excel"
                })
        
        print(f"created = oky {len(all_documents)} document")
        return all_documents


# اختبار
if __name__ == "__main__":
    processor = ExcelProcessor()
    docs = processor.process_all_files()
    
    # عرض أول 3 documents
    print("\n ferst 3 documment")
    for i, doc in enumerate(docs[:3]):
        print(f"\n{i+1}. {doc['content'][:150]}...")
