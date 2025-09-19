# Mermaid Diagram Templates for Enterprise Architecture

## Overview
This document provides standardized Mermaid diagram templates for enterprise architecture deliverables, ensuring consistency and clarity across all architectural visualizations.

## Business Architecture Diagrams

### Business Process Flow
```mermaid
flowchart TD
    A[Start Process] --> B{Decision Point}
    B -->|Condition 1| C[Process Step 1]
    B -->|Condition 2| D[Process Step 2]
    C --> E[Validation]
    D --> E
    E --> F{Validation Result}
    F -->|Pass| G[Complete Process]
    F -->|Fail| H[Exception Handling]
    H --> I[Corrective Action]
    I --> E
    G --> J[End Process]
    
    classDef startEnd fill:#90EE90
    classDef decision fill:#FFE4B5
    classDef process fill:#87CEEB
    classDef exception fill:#FFB6C1
    
    class A,J startEnd
    class B,F decision
    class C,D,E,I process
    class H exception
```

### Organizational Structure
```mermaid
graph TD
    CEO[Chief Executive Officer]
    CTO[Chief Technology Officer]
    CIO[Chief Information Officer]
    CFO[Chief Financial Officer]
    
    CEO --> CTO
    CEO --> CIO
    CEO --> CFO
    
    CTO --> DEV[Development Teams]
    CTO --> ARCH[Architecture Team]
    CTO --> INNOV[Innovation Team]
    
    CIO --> INFRA[Infrastructure Team]
    CIO --> APPS[Applications Team]
    CIO --> DATA[Data Team]
    
    CFO --> ACC[Accounting]
    CFO --> FPA[FP&A]
    CFO --> PROC[Procurement]
    
    classDef executive fill:#FFD700
    classDef manager fill:#87CEEB
    classDef team fill:#98FB98
    
    class CEO,CTO,CIO,CFO executive
    class DEV,ARCH,INNOV,INFRA,APPS,DATA manager
    class ACC,FPA,PROC team
```

### Business Capability Map
```mermaid
graph TB
    subgraph "Core Business Capabilities"
        SALES[Sales Management]
        MARKETING[Marketing & Brand]
        PRODUCT[Product Development]
        CUSTOMER[Customer Service]
    end
    
    subgraph "Supporting Capabilities"
        HR[Human Resources]
        FINANCE[Financial Management]
        LEGAL[Legal & Compliance]
        PROCUREMENT[Procurement]
    end
    
    subgraph "Enabling Capabilities"
        IT[Information Technology]
        DATA_CAP[Data & Analytics]
        SECURITY[Security & Risk]
        GOVERNANCE[Governance]
    end
    
    SALES --> CUSTOMER
    MARKETING --> SALES
    PRODUCT --> MARKETING
    
    HR --> SALES
    FINANCE --> PROCUREMENT
    LEGAL --> GOVERNANCE
    
    IT --> DATA_CAP
    SECURITY --> GOVERNANCE
    
    classDef core fill:#FFB6C1
    classDef supporting fill:#87CEEB
    classDef enabling fill:#98FB98
    
    class SALES,MARKETING,PRODUCT,CUSTOMER core
    class HR,FINANCE,LEGAL,PROCUREMENT supporting
    class IT,DATA_CAP,SECURITY,GOVERNANCE enabling
```

### Value Stream Map
```mermaid
flowchart LR
    CUSTOMER[Customer Request] --> INTAKE[Request Intake]
    INTAKE --> ANALYSIS[Requirement Analysis]
    ANALYSIS --> DESIGN[Solution Design]
    DESIGN --> DEVELOP[Development]
    DEVELOP --> TEST[Testing]
    TEST --> DEPLOY[Deployment]
    DEPLOY --> SUPPORT[Customer Support]
    
    INTAKE -.-> BACKLOG[(Product Backlog)]
    ANALYSIS -.-> SPECS[(Requirements Specs)]
    DESIGN -.-> ARCH[(Architecture Docs)]
    DEVELOP -.-> CODE[(Source Code)]
    TEST -.-> RESULTS[(Test Results)]
    DEPLOY -.-> PROD[(Production)]
    
    classDef activity fill:#87CEEB
    classDef artifact fill:#FFE4B5
    classDef customer fill:#90EE90
    
    class CUSTOMER customer
    class INTAKE,ANALYSIS,DESIGN,DEVELOP,TEST,DEPLOY,SUPPORT activity
    class BACKLOG,SPECS,ARCH,CODE,RESULTS,PROD artifact
```

## Application Architecture Diagrams

### Application Landscape
```mermaid
graph TB
    subgraph "Presentation Layer"
        WEB[Web Applications]
        MOBILE[Mobile Apps]
        API_GATEWAY[API Gateway]
    end
    
    subgraph "Business Logic Layer"
        ERP[ERP System]
        CRM[CRM System]
        BPM[Business Process Management]
        WORKFLOW[Workflow Engine]
    end
    
    subgraph "Data Layer"
        RDBMS[(Relational Database)]
        NOSQL[(NoSQL Database)]
        DWH[(Data Warehouse)]
        CACHE[(Cache)]
    end
    
    subgraph "Integration Layer"
        ESB[Enterprise Service Bus]
        MQ[Message Queue]
        ETL[ETL Processes]
    end
    
    WEB --> API_GATEWAY
    MOBILE --> API_GATEWAY
    API_GATEWAY --> ERP
    API_GATEWAY --> CRM
    
    ERP --> ESB
    CRM --> ESB
    BPM --> ESB
    WORKFLOW --> MQ
    
    ESB --> RDBMS
    ESB --> NOSQL
    ETL --> DWH
    
    classDef presentation fill:#FFB6C1
    classDef business fill:#87CEEB
    classDef data fill:#98FB98
    classDef integration fill:#FFE4B5
    
    class WEB,MOBILE,API_GATEWAY presentation
    class ERP,CRM,BPM,WORKFLOW business
    class RDBMS,NOSQL,DWH,CACHE data
    class ESB,MQ,ETL integration
```

### Application Integration Pattern
```mermaid
sequenceDiagram
    participant Client
    participant API_Gateway
    participant Auth_Service
    participant Business_Service
    participant Database
    
    Client->>API_Gateway: Request with credentials
    API_Gateway->>Auth_Service: Validate credentials
    Auth_Service-->>API_Gateway: Authentication token
    API_Gateway->>Business_Service: Authorized request
    Business_Service->>Database: Query data
    Database-->>Business_Service: Return data
    Business_Service-->>API_Gateway: Response
    API_Gateway-->>Client: Final response
```

### Microservices Architecture
```mermaid
graph TB
    subgraph "Client Applications"
        WEB_APP[Web Application]
        MOBILE_APP[Mobile Application]
        THIRD_PARTY[Third Party Apps]
    end
    
    subgraph "API Gateway & Load Balancer"
        LB[Load Balancer]
        API_GW[API Gateway]
    end
    
    subgraph "Microservices"
        USER_SVC[User Service]
        ORDER_SVC[Order Service]
        PAYMENT_SVC[Payment Service]
        INVENTORY_SVC[Inventory Service]
        NOTIFICATION_SVC[Notification Service]
    end
    
    subgraph "Data Stores"
        USER_DB[(User DB)]
        ORDER_DB[(Order DB)]
        PAYMENT_DB[(Payment DB)]
        INVENTORY_DB[(Inventory DB)]
    end
    
    subgraph "Infrastructure"
        MESSAGE_BROKER[Message Broker]
        CACHE_REDIS[Redis Cache]
        MONITORING[Monitoring]
    end
    
    WEB_APP --> LB
    MOBILE_APP --> LB
    THIRD_PARTY --> LB
    
    LB --> API_GW
    
    API_GW --> USER_SVC
    API_GW --> ORDER_SVC
    API_GW --> PAYMENT_SVC
    API_GW --> INVENTORY_SVC
    
    USER_SVC --> USER_DB
    ORDER_SVC --> ORDER_DB
    PAYMENT_SVC --> PAYMENT_DB
    INVENTORY_SVC --> INVENTORY_DB
    
    ORDER_SVC --> MESSAGE_BROKER
    PAYMENT_SVC --> MESSAGE_BROKER
    NOTIFICATION_SVC --> MESSAGE_BROKER
    
    USER_SVC --> CACHE_REDIS
    ORDER_SVC --> CACHE_REDIS
    
    classDef client fill:#FFB6C1
    classDef gateway fill:#87CEEB
    classDef service fill:#98FB98
    classDef database fill:#FFE4B5
    classDef infrastructure fill:#DDA0DD
    
    class WEB_APP,MOBILE_APP,THIRD_PARTY client
    class LB,API_GW gateway
    class USER_SVC,ORDER_SVC,PAYMENT_SVC,INVENTORY_SVC,NOTIFICATION_SVC service
    class USER_DB,ORDER_DB,PAYMENT_DB,INVENTORY_DB database
    class MESSAGE_BROKER,CACHE_REDIS,MONITORING infrastructure
```

## Technology Architecture Diagrams

### Infrastructure Architecture
```mermaid
graph TB
    subgraph "Internet"
        USERS[End Users]
        PARTNERS[Partners]
    end
    
    subgraph "DMZ"
        WAF[Web Application Firewall]
        LB[Load Balancer]
        PROXY[Reverse Proxy]
    end
    
    subgraph "Web Tier"
        WEB1[Web Server 1]
        WEB2[Web Server 2]
        WEB3[Web Server 3]
    end
    
    subgraph "Application Tier"
        APP1[App Server 1]
        APP2[App Server 2]
        APP3[App Server 3]
    end
    
    subgraph "Database Tier"
        DB_PRIMARY[(Primary Database)]
        DB_REPLICA[(Read Replica)]
        DB_BACKUP[(Backup)]
    end
    
    subgraph "Management & Monitoring"
        MONITOR[Monitoring System]
        BACKUP_SVC[Backup Service]
        LOG[Log Management]
    end
    
    USERS --> WAF
    PARTNERS --> WAF
    WAF --> LB
    LB --> PROXY
    PROXY --> WEB1
    PROXY --> WEB2
    PROXY --> WEB3
    
    WEB1 --> APP1
    WEB2 --> APP2
    WEB3 --> APP3
    
    APP1 --> DB_PRIMARY
    APP2 --> DB_PRIMARY
    APP3 --> DB_REPLICA
    
    DB_PRIMARY --> DB_REPLICA
    BACKUP_SVC --> DB_BACKUP
    
    MONITOR --> WEB1
    MONITOR --> APP1
    MONITOR --> DB_PRIMARY
    
    classDef external fill:#FFB6C1
    classDef dmz fill:#87CEEB
    classDef web fill:#98FB98
    classDef app fill:#FFE4B5
    classDef database fill:#DDA0DD
    classDef mgmt fill:#F0E68C
    
    class USERS,PARTNERS external
    class WAF,LB,PROXY dmz
    class WEB1,WEB2,WEB3 web
    class APP1,APP2,APP3 app
    class DB_PRIMARY,DB_REPLICA,DB_BACKUP database
    class MONITOR,BACKUP_SVC,LOG mgmt
```

### Cloud Architecture
```mermaid
graph TB
    subgraph "On-Premises"
        ON_PREM[Legacy Systems]
        USERS[Corporate Users]
    end
    
    subgraph "Azure Cloud"
        subgraph "Production Environment"
            PROD_VNET[Production VNet]
            PROD_AKS[AKS Cluster]
            PROD_DB[(Azure SQL Database)]
            PROD_STORAGE[Azure Storage]
        end
        
        subgraph "Development Environment"
            DEV_VNET[Development VNet]
            DEV_AKS[AKS Cluster]
            DEV_DB[(Development DB)]
        end
        
        subgraph "Shared Services"
            AAD[Azure Active Directory]
            KEY_VAULT[Azure Key Vault]
            MONITOR[Azure Monitor]
            BACKUP[Azure Backup]
        end
    end
    
    subgraph "AWS Cloud"
        AWS_S3[S3 Storage]
        AWS_LAMBDA[Lambda Functions]
        AWS_RDS[(RDS Database)]
    end
    
    USERS --> AAD
    ON_PREM --> PROD_VNET
    
    AAD --> PROD_AKS
    AAD --> DEV_AKS
    
    PROD_AKS --> PROD_DB
    PROD_AKS --> PROD_STORAGE
    PROD_AKS --> KEY_VAULT
    
    DEV_AKS --> DEV_DB
    
    MONITOR --> PROD_AKS
    MONITOR --> DEV_AKS
    BACKUP --> PROD_DB
    
    PROD_AKS --> AWS_S3
    AWS_LAMBDA --> AWS_RDS
    
    classDef onprem fill:#FFB6C1
    classDef azure fill:#87CEEB
    classDef aws fill:#FFE4B5
    classDef shared fill:#98FB98
    
    class ON_PREM,USERS onprem
    class PROD_VNET,PROD_AKS,PROD_DB,PROD_STORAGE,DEV_VNET,DEV_AKS,DEV_DB azure
    class AWS_S3,AWS_LAMBDA,AWS_RDS aws
    class AAD,KEY_VAULT,MONITOR,BACKUP shared
```

### Network Architecture
```mermaid
graph TB
    subgraph "Internet"
        INTERNET[Internet]
    end
    
    subgraph "Edge Network"
        EDGE_ROUTER[Edge Router]
        FIREWALL[Firewall]
        DDoS[DDoS Protection]
    end
    
    subgraph "DMZ - 192.168.1.0/24"
        DMZ_SWITCH[DMZ Switch]
        WEB_SERVERS[Web Servers]
        EMAIL_SERVER[Email Server]
        DNS_SERVER[DNS Server]
    end
    
    subgraph "Internal Network - 10.0.0.0/16"
        CORE_SWITCH[Core Switch]
        
        subgraph "Management - 10.0.1.0/24"
            MGMT_SERVERS[Management Servers]
            MONITORING[Monitoring Systems]
        end
        
        subgraph "Application - 10.0.10.0/24"
            APP_SERVERS[Application Servers]
            DB_SERVERS[Database Servers]
        end
        
        subgraph "User Network - 10.0.100.0/24"
            USER_SWITCH[User Switch]
            WORKSTATIONS[Workstations]
            PRINTERS[Printers]
        end
    end
    
    subgraph "Data Center - 10.0.200.0/24"
        DC_SWITCH[Data Center Switch]
        STORAGE[Storage Systems]
        BACKUP[Backup Systems]
    end
    
    INTERNET --> EDGE_ROUTER
    EDGE_ROUTER --> DDoS
    DDoS --> FIREWALL
    FIREWALL --> DMZ_SWITCH
    FIREWALL --> CORE_SWITCH
    
    DMZ_SWITCH --> WEB_SERVERS
    DMZ_SWITCH --> EMAIL_SERVER
    DMZ_SWITCH --> DNS_SERVER
    
    CORE_SWITCH --> MGMT_SERVERS
    CORE_SWITCH --> APP_SERVERS
    CORE_SWITCH --> USER_SWITCH
    CORE_SWITCH --> DC_SWITCH
    
    USER_SWITCH --> WORKSTATIONS
    USER_SWITCH --> PRINTERS
    
    DC_SWITCH --> STORAGE
    DC_SWITCH --> BACKUP
    
    classDef internet fill:#FFB6C1
    classDef edge fill:#87CEEB
    classDef dmz fill:#98FB98
    classDef internal fill:#FFE4B5
    classDef datacenter fill:#DDA0DD
    
    class INTERNET internet
    class EDGE_ROUTER,FIREWALL,DDoS edge
    class DMZ_SWITCH,WEB_SERVERS,EMAIL_SERVER,DNS_SERVER dmz
    class CORE_SWITCH,MGMT_SERVERS,APP_SERVERS,USER_SWITCH,WORKSTATIONS,PRINTERS internal
    class DC_SWITCH,STORAGE,BACKUP datacenter
```

## Data Architecture Diagrams

### Data Flow Diagram
```mermaid
flowchart TB
    subgraph "Data Sources"
        ERP_SRC[ERP System]
        CRM_SRC[CRM System]
        WEB_SRC[Web Analytics]
        EXTERNAL[External APIs]
    end
    
    subgraph "Data Ingestion"
        ETL[ETL Pipeline]
        STREAM[Real-time Streaming]
        API_CONN[API Connectors]
    end
    
    subgraph "Data Processing"
        CLEAN[Data Cleansing]
        TRANSFORM[Data Transformation]
        ENRICH[Data Enrichment]
        VALIDATE[Data Validation]
    end
    
    subgraph "Data Storage"
        RAW_LAKE[(Data Lake - Raw)]
        CURATED_LAKE[(Data Lake - Curated)]
        DWH[(Data Warehouse)]
        MART[(Data Marts)]
    end
    
    subgraph "Data Consumption"
        BI[Business Intelligence]
        ANALYTICS[Advanced Analytics]
        REPORTS[Reports]
        DASHBOARD[Dashboards]
    end
    
    ERP_SRC --> ETL
    CRM_SRC --> ETL
    WEB_SRC --> STREAM
    EXTERNAL --> API_CONN
    
    ETL --> RAW_LAKE
    STREAM --> RAW_LAKE
    API_CONN --> RAW_LAKE
    
    RAW_LAKE --> CLEAN
    CLEAN --> TRANSFORM
    TRANSFORM --> ENRICH
    ENRICH --> VALIDATE
    
    VALIDATE --> CURATED_LAKE
    CURATED_LAKE --> DWH
    DWH --> MART
    
    MART --> BI
    MART --> ANALYTICS
    MART --> REPORTS
    MART --> DASHBOARD
    
    classDef source fill:#FFB6C1
    classDef ingestion fill:#87CEEB
    classDef processing fill:#98FB98
    classDef storage fill:#FFE4B5
    classDef consumption fill:#DDA0DD
    
    class ERP_SRC,CRM_SRC,WEB_SRC,EXTERNAL source
    class ETL,STREAM,API_CONN ingestion
    class CLEAN,TRANSFORM,ENRICH,VALIDATE processing
    class RAW_LAKE,CURATED_LAKE,DWH,MART storage
    class BI,ANALYTICS,REPORTS,DASHBOARD consumption
```

### Data Model Relationships
```mermaid
erDiagram
    CUSTOMER ||--o{ ORDER : "places"
    CUSTOMER ||--o{ INVOICE : "receives"
    ORDER ||--o{ ORDER_ITEM : "contains"
    ORDER_ITEM }o--|| PRODUCT : "includes"
    PRODUCT }o--|| CATEGORY : "belongs to"
    ORDER ||--|| INVOICE : "generates"
    CUSTOMER ||--o{ ADDRESS : "has"
    PRODUCT ||--o{ INVENTORY : "tracked in"
    
    CUSTOMER {
        int customer_id PK
        string first_name
        string last_name
        string email
        date created_date
        boolean active
    }
    
    ORDER {
        int order_id PK
        int customer_id FK
        date order_date
        decimal total_amount
        string status
    }
    
    PRODUCT {
        int product_id PK
        string product_name
        string description
        decimal price
        int category_id FK
    }
    
    CATEGORY {
        int category_id PK
        string category_name
        string description
    }
```

## Security Architecture Diagrams

### Security Layers
```mermaid
graph TB
    subgraph "Perimeter Security"
        FIREWALL[Next-Gen Firewall]
        WAF[Web Application Firewall]
        IPS[Intrusion Prevention]
        DLP[Data Loss Prevention]
    end
    
    subgraph "Network Security"
        SEGMENTATION[Network Segmentation]
        VPN[VPN Gateway]
        NAC[Network Access Control]
        MONITORING[Network Monitoring]
    end
    
    subgraph "Identity & Access"
        IAM[Identity Management]
        MFA[Multi-Factor Auth]
        PAM[Privileged Access]
        SSO[Single Sign-On]
    end
    
    subgraph "Application Security"
        SAST[Static Analysis]
        DAST[Dynamic Analysis]
        RASP[Runtime Protection]
        API_SEC[API Security]
    end
    
    subgraph "Data Security"
        ENCRYPTION[Data Encryption]
        MASKING[Data Masking]
        TOKENIZATION[Tokenization]
        KEY_MGMT[Key Management]
    end
    
    subgraph "Endpoint Security"
        EDR[Endpoint Detection]
        ANTIVIRUS[Antivirus]
        PATCH_MGMT[Patch Management]
        DEVICE_CONTROL[Device Control]
    end
    
    FIREWALL --> SEGMENTATION
    WAF --> API_SEC
    IPS --> MONITORING
    
    IAM --> SSO
    MFA --> PAM
    
    SAST --> RASP
    DAST --> API_SEC
    
    ENCRYPTION --> KEY_MGMT
    MASKING --> TOKENIZATION
    
    EDR --> DEVICE_CONTROL
    ANTIVIRUS --> PATCH_MGMT
    
    classDef perimeter fill:#FFB6C1
    classDef network fill:#87CEEB
    classDef identity fill:#98FB98
    classDef application fill:#FFE4B5
    classDef data fill:#DDA0DD
    classDef endpoint fill:#F0E68C
    
    class FIREWALL,WAF,IPS,DLP perimeter
    class SEGMENTATION,VPN,NAC,MONITORING network
    class IAM,MFA,PAM,SSO identity
    class SAST,DAST,RASP,API_SEC application
    class ENCRYPTION,MASKING,TOKENIZATION,KEY_MGMT data
    class EDR,ANTIVIRUS,PATCH_MGMT,DEVICE_CONTROL endpoint
```

## Implementation and Migration Diagrams

### Migration Timeline
```mermaid
gantt
    title Digital Transformation Migration Timeline
    dateFormat  YYYY-MM-DD
    section Foundation
    Infrastructure Setup     :foundation1, 2024-01-01, 90d
    Security Implementation  :foundation2, 2024-01-15, 75d
    Governance Framework     :foundation3, 2024-02-01, 60d
    
    section Wave 1
    Development Migration    :wave1-1, after foundation1, 60d
    Testing Environment      :wave1-2, after foundation2, 45d
    Basic Applications       :wave1-3, after foundation3, 90d
    
    section Wave 2
    Core Business Systems    :wave2-1, after wave1-1, 120d
    Integration Platform     :wave2-2, after wave1-2, 90d
    Data Migration          :wave2-3, after wave1-3, 105d
    
    section Wave 3
    Mission Critical        :wave3-1, after wave2-1, 150d
    Legacy Decommission     :wave3-2, after wave2-2, 120d
    Optimization           :wave3-3, after wave2-3, 90d
    
    section Completion
    Final Testing          :completion1, after wave3-1, 30d
    Go-Live Support        :completion2, after wave3-2, 45d
    Post-Implementation    :completion3, after wave3-3, 60d
```

### Deployment Architecture
```mermaid
graph TB
    subgraph "Development Environment"
        DEV_CODE[Source Code]
        DEV_BUILD[Build Server]
        DEV_TEST[Unit Tests]
        DEV_DEPLOY[Dev Deployment]
    end
    
    subgraph "Staging Environment"
        STAGE_DEPLOY[Staging Deployment]
        STAGE_TEST[Integration Tests]
        STAGE_UAT[User Acceptance Testing]
        STAGE_APPROVE[Approval Gateway]
    end
    
    subgraph "Production Environment"
        PROD_BLUE[Blue Environment]
        PROD_GREEN[Green Environment]
        LOAD_BALANCER[Load Balancer]
        PROD_MONITOR[Production Monitoring]
    end
    
    subgraph "CI/CD Pipeline"
        GIT_REPO[Git Repository]
        CI_SERVER[CI Server]
        ARTIFACT_REPO[Artifact Repository]
        CD_SERVER[CD Server]
    end
    
    DEV_CODE --> GIT_REPO
    GIT_REPO --> CI_SERVER
    CI_SERVER --> DEV_BUILD
    DEV_BUILD --> DEV_TEST
    DEV_TEST --> DEV_DEPLOY
    
    CI_SERVER --> ARTIFACT_REPO
    ARTIFACT_REPO --> CD_SERVER
    CD_SERVER --> STAGE_DEPLOY
    STAGE_DEPLOY --> STAGE_TEST
    STAGE_TEST --> STAGE_UAT
    STAGE_UAT --> STAGE_APPROVE
    
    STAGE_APPROVE --> PROD_BLUE
    STAGE_APPROVE --> PROD_GREEN
    LOAD_BALANCER --> PROD_BLUE
    LOAD_BALANCER --> PROD_GREEN
    
    PROD_MONITOR --> PROD_BLUE
    PROD_MONITOR --> PROD_GREEN
    
    classDef development fill:#98FB98
    classDef staging fill:#FFE4B5
    classDef production fill:#FFB6C1
    classDef cicd fill:#87CEEB
    
    class DEV_CODE,DEV_BUILD,DEV_TEST,DEV_DEPLOY development
    class STAGE_DEPLOY,STAGE_TEST,STAGE_UAT,STAGE_APPROVE staging
    class PROD_BLUE,PROD_GREEN,LOAD_BALANCER,PROD_MONITOR production
    class GIT_REPO,CI_SERVER,ARTIFACT_REPO,CD_SERVER cicd
```

## Customization Guidelines

### Color Scheme Standards
- **Core Business Functions:** `#FFB6C1` (Light Pink)
- **Supporting Services:** `#87CEEB` (Sky Blue)
- **Enabling Technologies:** `#98FB98` (Pale Green)
- **Data and Storage:** `#FFE4B5` (Moccasin)
- **Security and Compliance:** `#DDA0DD` (Plum)
- **External Systems:** `#F0E68C` (Khaki)

### Diagram Conventions
1. **Start/End nodes:** Use rounded rectangles
2. **Process steps:** Use rectangles
3. **Decision points:** Use diamonds
4. **Data stores:** Use cylinders
5. **External systems:** Use hexagons
6. **Services:** Use circles

### Best Practices
1. Keep diagrams focused and uncluttered
2. Use consistent naming conventions
3. Include legends for complex diagrams
4. Ensure proper flow direction (top-to-bottom, left-to-right)
5. Group related elements using subgraphs
6. Use appropriate arrow types for relationships
7. Include version control information

---
**Template Version:** 1.0  
**Last Updated:** September 19, 2025  
**Owner:** Enterprise Architecture Team  
**Usage:** Standard template for all EA diagrams