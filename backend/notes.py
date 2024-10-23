Extract first 10 pages of a document into a single file
Load this file into S3 bucket
Preprocess into chunks and then embed and then load into a ChromaDB database







rag-app/
│
├── backend/
│   ├── database/
│   │   ├── chromadb.py         # Interactions with ChromaDB
│   │   └── config.py           # Configuration for database settings
│   │
│   ├── storage/
│   │   ├── s3_service.py       # Interactions with S3
│   │   ├── raw/
│   │   │   ├── document1.py   #
│   │   ├── chunks/
│   │   │   ├── text1.py   #
│   │   │   ├── image1.py   #
│   │   └── embeddings/
│   │   │   ├── embedding1.py   #
│   │   └── config.py           # Configuration for S3 settings
│   │
│   ├── retrieval/
│   │   ├── retriever.py        # Logic for retrieving relevant documents
│   │   └── retrieval_utils.py   # Helper functions for the retrieval process
│   │
│   ├── generation/
│   │   ├── llm_service.py      # Interactions with the LLM API
│   │   └── config.py           # Configuration for LLM settings
│   │
│   ├── api/
│   │   ├── app.py              # Main API application file
│   │   └── routes.py           # API route definitions
│   │
│   ├── utils/
│   │   ├── data_loader.py      # Utility functions for data loading
│   │   ├── preprocessing.py     # Preprocessing functions, if needed
│   │   └── helpers.py          # General helper functions
│   │
│   ├── tests/
│   │   ├── test_retriever.py    # Unit tests for the retriever
│   │   ├── test_llm_service.py   # Unit tests for the LLM service
│   │   ├── test_chromadb.py      # Unit tests for ChromaDB interactions
│   │   ├── test_s3_service.py     # Unit tests for S3 interactions
│   │   └── test_api.py          # API tests
│   │
│   ├── requirements.txt          # Python package dependencies
│   ├── config.yaml               # Configuration file for parameters
│   └── main.py                   # Entry point for running the backend
│
├── frontend/
│   ├── public/                   # Public assets (e.g., images, favicon)
│   ├── src/
│   │   ├── components/           # React components
│   │   ├── pages/                # Pages of the app
│   │   ├── services/             # API service calls
│   │   ├── utils/                # Utility functions (e.g., formatting)
│   │   └── App.js                # Main React application file
│   │
│   ├── package.json              # Node.js dependencies
│   ├── .env                      # Environment variables (e.g., API endpoint)
│   └── README.md                 # Frontend documentation
│
├── docker-compose.yml             # Docker compose file for services
└── README.md                     # Overall project documentation
