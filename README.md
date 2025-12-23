# RAG Search Engine

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

##  ما تم إنجازه حتى الآن
- [x] إعداد البيئة البرمجية
- [x] قراءة ملفات Excel
- [x] تحويل البيانات إلى نصوص قابلة للبحث (5000+ document)
- [ ] فهرسة البيانات في ChromaDB
- [ ] بناء Agent للبحث الذكي
- [ ] واجهة Streamlit تفاعلية