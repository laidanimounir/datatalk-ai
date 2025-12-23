# RAG Search Engine "datatalk"

##  التقنيات المستخدمة
- **LangChain**: إطار عمل لبناء تطبيقات LLM
- **ChromaDB**: قاعدة بيانات Vector للبحث الذكي
- **Pandas**: معالجة بيانات Excel
- **Streamlit**: واجهة المستخدم
- **Python 3.10+**

## هيكل المشروع 
rag-search-engine/
├── data/
│ ├── exel/ # ملفات Excel
│ └── pdf/ # ملفات PDF
├── src/
│ └── document_processor.py # معالج المستندات
├── app.py # التطبيق الرئيسي
└── requirements.txt # المكتبات


## How DataTalk understands the data
DataTalk uses a Retrieval-Augmented Generation (RAG) approach.

1. Each row from the Excel files is converted into a short text description.
2. These texts are turned into numerical vectors using a multilingual embeddings model from Hugging Face.
3. All vectors are stored in a vector database (Chroma).
4. When the user asks a question, the question is also converted into a vector.
5. The system finds the most similar vectors (closest meanings) and returns the most relevant rows.

This allows the app to search by meaning (semantics), not only by exact keywords.


##  ما تم إنجازه حتى الآن
- [x] إعداد البيئة البرمجية
- [x] قراءة ملفات Excel
- [x] تحويل البيانات إلى نصوص قابلة للبحث (5000+ document)
- [ ] فهرسة البيانات في ChromaDB
- [ ] بناء Agent للبحث الذكي
- [ ] واجهة Streamlit تفاعلية

إنشاء بيئة افتراضية
python -m venv venv
venv\Scripts\activate

تثبيت المكتبات
pip install -r requirements.txt

اختبار معالج المستندات
python src/document_processor.py

