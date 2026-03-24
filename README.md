# Global Supply Chain Risk Analysis 2026

## Overview
This project analyzes global supply chain risks using real-world shipment data to identify patterns, disruptions, and key risk factors affecting logistics operations worldwide. The analysis leverages big data processing on Databricks to process and visualize supply chain metrics across multiple dimensions.

## Dataset
The analysis uses the `supplychain.sc.riskdata2026` dataset containing comprehensive shipment information:

**Key Attributes:**
- **Shipment Details**: Origin/Destination ports, Transport modes, Product categories
- **Operational Metrics**: Distance (km), Weight (MT), Lead time (days)
- **Risk Factors**: Weather conditions, Geopolitical risk scores, Carrier reliability scores, Fuel price index
- **Outcomes**: Disruption occurrence indicators

**Data Processing:**
- Implemented data cleaning pipeline filtering null shipment IDs
- Created silver layer table with ingestion timestamps for data lineage
- Stored processed data in Delta Lake format for ACID transactions and time travel capabilities

## Key Analyses

### 1. Data Quality & Exploration
- Schema validation and data profiling
- Identification of high-risk shipments (Lead Time > 100 days)
- Data cleaning and transformation pipeline

### 2. Transport Mode Analysis
- Average lead time by transport mode
- Performance comparison across Air, Sea, Rail, and Road transport
- Insights for optimal transport selection

### 3. Weather Impact Assessment
- Distribution of shipments by weather conditions
- Count of unique weather scenarios affecting operations
- Weather-related risk patterns

### 4. Geographic Analysis
- Top destination ports by total shipment weight
- Weight distribution across global logistics hubs
- Created `Largest_Destination` view for ongoing monitoring

### 5. Product Category Performance
- Total weight shipped by product category
- Category-wise logistics metrics
- Created `Category_winner` view and persistent Delta table

## Technologies & Tools

- **Platform**: Databricks (AWS)
- **Processing Engine**: Apache Spark (PySpark)
- **Storage Format**: Delta Lake
- **Languages**: Python, SQL
- **Data Architecture**: Medallion Architecture (Bronze → Silver)
- **Key Libraries**: PySpark SQL Functions

## Project Structure
```
GlobalSupplyChainRiskAnalysis2026/
├── SupplyChainRiskAnalysis.ipynb  # Main analysis notebook
└── README.md                       # Project documentation
```

## Setup & Execution

### Prerequisites
- Databricks workspace (Community Edition or higher)
- Access to Unity Catalog
- SQL Warehouse or Cluster with DBR 14.3+

### Running the Analysis
1. Import the `SupplyChainRiskAnalysis` notebook into your Databricks workspace
2. Ensure access to the `supplychain.sc.riskdata2026` table
3. Attach to a SQL warehouse or cluster
4. Run all cells sequentially (Cells 1-10)

### Output Tables & Views
- `supplychain.sc.riskdata2026_silver` - Cleaned and processed data
- `Largest_Destination` - View of top destinations by weight
- `Category_winner` - View of product categories by weight
- `supplychain.sc.Category_winner` - Persistent Delta table

## Key Insights

- Identified critical supply chain bottlenecks through transport mode analysis
- Quantified weather impact on shipment operations
- Mapped high-volume logistics corridors for strategic planning
- Established data quality baselines with automated validation

## Skills Demonstrated

✓ Big Data Processing with Apache Spark  
✓ Data Engineering (ETL pipelines, data quality)  
✓ SQL & PySpark proficiency  
✓ Delta Lake implementation  
✓ Data Modeling (Medallion Architecture)  
✓ Analytical View creation for Business Intelligence  
✓ Cloud Data Platform expertise (Databricks)  

## Future Enhancements
- Predictive modeling for disruption risk scoring
- Real-time streaming analytics integration
- Interactive dashboard development
- ML-based route optimization
- Geospatial visualization of shipment routes

## Author
Developed as part of a data analytics portfolio project demonstrating end-to-end data engineering and analytics capabilities.

## License
This project is available for educational and portfolio purposes.

---

**Note**: This analysis uses synthetic/sample data for demonstration purposes.