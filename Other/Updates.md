# AI Powered Ducument Management for Smart Governance.

#### Pain Points:

- 30-40% time lost in manual tasks.
- High error rate (10-15%).
- Weak search & privacy issues.
- Document volume +30%/year.
- LLM limitations.

#### Objectives:

- Build a protoype solution that leverages AI and OCR to digitize, claaify, extract, and summarize government documents, enabling:
  - Faster response time.
  - Easier tracking.
  - Greater transparency in local governance.

#### Smart City Enablers

- Transform legacy paper systems into digital knowledge.
- Speeds up service delivery for public services e.g., permits, licenses, citizen requests, etc.
- Enables croe-agency collaboration through centralized document intelligence.
- Increases transparency with AI-powered search & tracebility.

#### Tech Focus:

- AI OCR Engines.
- AI Agents for Document Type Classifiaction.
- Container-Based Architecture Deployment e.g., Docker, Kubernates, etc.

#### Deliverables:

- Classify 5 Doc Types:
  - invoice, receipt, resume, report, contract.
- OCR (English).
- Structured Data Extraction.

#### Judging Criteria:

- Core functionality 40%: Accuracy, perfomance, doc classification, OCR (English), structured data extraction.
- Bounus features & integration 15% (e.g., Multi-language, Summarization, search/index, PII masking, additional or enhanced features beyond core scope, etc).
- Performance & Usability 10%: precessing speed (doc/min), resource eficiency, (CPU, RAM, usage of the Docker containers, UI UX).
- Innovation & technical approach 10%: creative use of open-source models, how well hard problems are solved, creativity in technical design, problem-solving, aproach, use AI/ML methods (e.g., LLM, RAG, Vision-Language Models)., and scalability.
- Presentation & pitching 15%: clarity, well is the solution explanation and it's potential business impact.

#### Proposed Hackathon Process Guidline:

- Input: provide resources.
- Dataset:
  - Pre-labled document sets(invoices, receipts, forms, reports).
- OutputL Single script -> output (classification.json, ocr.text, summary.txt).
- Rules & Expectations:
  - Timebox: 48 hours.
  - Teams: up to 5.
  - Must use open-source AI/ML tools.

#### The Dataset:

- Two parts:
  - training_set: contains docs and a label.csv file with the correct answers.
  - testing_set: contains only docs. the labels are secret!
- How to use it:
  - use the training_set to build the and the train your models.
  - your final solution will be judged on its performance on the unseen testing_set.
- Goal:
  - build a model that learns and generalizes, not one that just memorizes the training data.

#### Dataset Folder Layout:

```
Dataset/
|
|___training_set/
|    |
|    |___docs/
|    |    |
|    |    |___doc1 {pdf, png, jpeg, ...etc}
|    |    |___...docn
|    |___labels.csv <--- The "answers" for the training docs
|___testing_set/
     |
     |___docs/
          |
          |___test_doc1 {pdf, png, jpeg, ...etc}
          |___...test_docn (no labels provided)
```

#### Output Format:

```
{
    "filename": "inv_123.pdf",
    "classification": {
        "doc_type": "invoice",
        "confidence": 0.98
    },
    "full_text_ocr": "The entire OCR'd text contnt goes here...",
    "extracted_data": {
        "vendor": "CDG Group",
        "invoice_date": "2025-08-19",
        "total_amount": 7500.00,
        "currency": "THB"
    },
    "summary": "This is the summary of the doc...",
    "pii_detection": [
        {"type": "PERSON_NAME", "text": "John Doe"},
        {"type": "THAI_ID", "text": "1-1020-30405-60-7"}
    ]
}
```

#### What should be delivered:

- Core Tasks (Must-Have):
  - Document Classification:
    - Accurately classify documents into 5 document types (e.g., invoice, receipt, resume, report, contract).
    - The system should automatically identify the document type based on layout, text content, and visual cues.
  - OCR Extraction: Perform OCR primarily in English including handwriting. This task is a major challenge and already a highly valuable solution on its own.
  - Structured Data Extraction: For one or two document types (e.g., invoices and receipts), extract key information into a structured format like JSON. This is more valuable than a generic text summary.
  - Example for an invoice:
    {"vendor" : "Company A",
    "invoice date" : "2025-08-19",
    "total amount" : 1500.75,
    "Currency" : "THB"}
- Bonus Goals (Nice-to-Have):
  -Expanded Language Support:Additional support for more Languages e.g.. Thai Japanese, Korean, or Chinese.
  - Advanced Summarization: For complex or lengthy documents (e.g, reports, contracts, legal agreements), generate a concise and coherent summary highlighting key points or sections.
  - Search & Indexing:
    - O 1 Output the extracted data in a format ready for indexing in a search engine like Elasticsearch or OpenSearch.
    - Support metadata tagging for efficient filtering and retrieval.
  - Compliance Feature:
    - Automatically detect and flag/mask Personally Identifiable Information (PII) like names, addresses, or ID numbers.
    - Ensure extracted and stored data adheres to privacy and compliance standards (e.g, PDPA, GDPR).
