---
_db_id:
content_type: topic
ready: true
title: Ensuring Access to Accurate Data
---


#### Electronically Identifying and Classifying Documents

- **What is Electronic Identity Verification**? Electronic identity verification matches data like name, date of birth, address, and SSN against databases to confirm identity. Electronic IDs (eID) serve as digital proofs for identity verification, enabling access to government benefits, bank services, and mobile payments.
  EIV helps in combating financial crimes like money laundering and fraud by verifying customer identity, enhancing the Know Your Customer (KYC) process. This includes both basic information (name, ID, address, etc.) and more complex data (social media, financial information) that enriches customer risk profiles.

- **Real-time Identity Verification**: Real-time identity verification builds upon EIV and provides updated, immediate information across platforms. It enhances financial institutions' abilities to detect suspicious activities and comply with regulatory requirements.

#### Capturing Data from Documents

- **What is Data Capturing**? Data capture involves extracting relevant information from documents (e.g., scanned images, PDFs, or handwritten notes) to streamline processes such as inventory management in hospitals.

- **Document Data Capture**: Automated data capture systems like OCR (Optical Character Recognition) and ICR (Intelligent Character Recognition) allow businesses to extract data efficiently from various documents (e.g., invoices, contracts) by digitizing the information and organizing it into structured formats.

- **Technologies Used in Document Data Capture**:

  - OCR: Extracts data from printed or scanned images.
  - ICR: Works similarly to OCR but is designed for recognizing handwritten text.
  - OMR: Used for capturing marked data like surveys or test answers.
  - Barcodes: Used to capture vast amounts of information encoded in barcodes.

- **Solutions for Capturing Data**: Tools like Brainware and Athento utilize these technologies to automate data extraction, validation, and categorization, reducing manual errors and increasing efficiency.

#### Ensuring Users Only See the Information They Need

- **The Six Steps to Optimal Data Capture**:

  1. **File Identification**: Assessing existing content to determine scope, type, and location.
  2. **OCR and Rendering**: Standardizing documents and converting them into searchable formats.
  3. **Classification**: Organizing documents into groups to make retrieval easier.
  4. **Data Extraction**: Extracting relevant data (e.g., invoice number) and appending metadata.
  5. **QA and Reconciliation**: Verifying the accuracy of the captured data through manual checks.
  6. **Upload and Output**: Uploading data into relevant systems or repositories for further use.

#### Indexing Data for Ease of Search and Retrieval

- **What is Indexing Data**? Indexing is a method used to optimize database performance by reducing disk accesses needed for querying data. It creates a sorted structure (index) to quickly locate and retrieve information in a database.

- **Types of Indexing**:

  - **Dense Index**: Every search key value in the data file has an index record.
  - **Sparse Index**: Index records are created only for a subset of items, pointing to blocks of records for efficient searching.

- **Performance Considerations**:

  - **Access Time**: Time taken to retrieve data.
  - **Insertion and Deletion Time**: Time required for adding or removing records.
  - **Space Overhead**: Additional storage space required by the index.
