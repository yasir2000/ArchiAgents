# TOGAF™ Version 9 - A Pocket Guide

*Copyright © 2009 The Open Group, All Rights Reserved*  
*Personal PDF Edition*

## Table of Contents

### Chapter 1: Introduction to TOGAF
- 1.1 Introduction to TOGAF 9
- 1.2 Structure of the TOGAF Document
- 1.3 What is Architecture in the Context of TOGAF?
- 1.4 What kinds of Architecture does TOGAF deal with?
- 1.5 What does TOGAF Contain?

### Chapter 2: The Architecture Development Method
- 2.1 What is the ADM?
- 2.2 What are the Phases of the ADM?
- 2.3 The ADM in Detail
- 2.4 Scoping the Architecture Activity

### Chapter 3: Key Techniques and Deliverables of the ADM Cycle

### Chapter 4: Guidelines for Adapting the ADM
- 4.1 Introduction
- 4.2 Applying Iteration to the ADM
- 4.3 Applying the ADM at Different Enterprise Levels
- 4.4 Security Architecture and the ADM
- 4.5 Using TOGAF to Define and Govern SOAs

### Chapter 5: Architecture Content Framework
- 5.1 Architecture Content Framework Overview
- 5.2 Content Metamodel
- 5.3 Architectural Artifacts
- 5.4 Architecture Deliverables
- 5.5 Building Blocks

### Chapter 6: The Enterprise Continuum
- 6.1 Overview of the Enterprise Continuum
- 6.2 Architecture Partitioning
- 6.3 Architecture Repository

### Chapter 7: TOGAF Reference Models
- 7.1 TOGAF Foundation Architecture
- 7.2 Integrated Information Infrastructure Reference Model (III-RM)

### Chapter 8: Architecture Capability Framework
- 8.1 Establishing an Architecture Capability
- 8.2 Architecture Governance
- 8.3 Architecture Board
- 8.4 Architecture Compliance
- 8.5 Architecture Skills Framework

---

## Chapter 1: Introduction to TOGAF

### 1.1 Introduction to TOGAF 9

TOGAF is an architecture framework – The Open Group Architecture Framework. Put simply, TOGAF is a tool for assisting in the acceptance, production, use, and maintenance of architectures. It is based on an iterative process model supported by best practices and a re-usable set of existing architectural assets.

TOGAF is developed and maintained by The Open Group Architecture Forum. The first version of TOGAF, developed in 1995, was based on the US Department of Defense Technical Architecture Framework for Information Management (TAFIM). Starting from this sound foundation, The Open Group Architecture Forum has developed successive versions of TOGAF at regular intervals and published each one on The Open Group public web site.

This document covers TOGAF Version 9, referred to as "TOGAF 9" within the text of this document. TOGAF 9 was first published in January 2009. TOGAF 9 is an evolution from TOGAF 8.1.1 and a description of the changes is provided in Appendix A.

TOGAF 9 can be used for developing a broad range of different enterprise architectures. TOGAF complements, and can be used in conjunction with, other frameworks that are more focused on specific deliverables for particular vertical sectors such as Government, Telecommunications, Manufacturing, Defense, and Finance. The key to TOGAF is the method – the TOGAF Architecture Development Method (ADM) – for developing an enterprise architecture that addresses business needs.

### 1.2 Structure of the TOGAF Document

The TOGAF Version 9 document is divided into seven parts:

| Part | Description |
|------|-------------|
| **Part I: Introduction** | This part provides a high-level introduction to the key concepts of enterprise architecture and, in particular, to the TOGAF approach. It contains the definitions of terms used throughout TOGAF and release notes detailing the changes between this version and the previous version of TOGAF. |
| **Part II: Architecture Development Method** | This part is the core of TOGAF. It describes the TOGAF Architecture Development Method (ADM) – a step-by-step approach to developing an enterprise architecture. |
| **Part III: ADM Guidelines and Techniques** | This part contains a collection of guidelines and techniques available for use in applying the ADM. |
| **Part IV: Architecture Content Framework** | This part describes the TOGAF content framework, including a structured metamodel for architectural artifacts, the use of re-usable Architecture Building Blocks (ABBs), and an overview of typical architecture deliverables. |
| **Part V: Enterprise Continuum and Tools** | This part discusses appropriate taxonomies and tools to categorize and store the outputs of architecture activity within an enterprise. |
| **Part VI: TOGAF Reference Models** | This part provides two architectural reference models, namely the TOGAF Technical Reference Model (TRM), and the Integrated Information Infrastructure Reference Model (III-RM). |
| **Part VII: Architecture Capability Framework** | This part discusses the organization, processes, skills, roles, and responsibilities required to establish and operate an architecture practice within an enterprise. |

### 1.3 What is Architecture in the Context of TOGAF?

ISO/IEC 42010:2007 defines "architecture" as:

> "The fundamental organization of a system, embodied in its components, their relationships to each other and the environment, and the principles governing its design and evolution."

TOGAF embraces and extends this definition. In TOGAF, "architecture" has two meanings depending upon the context:

1. A formal description of a system, or a detailed plan of the system at a component level to guide its implementation
2. The structure of components, their inter-relationships, and the principles and guidelines governing their design and evolution over time

### 1.4 What kinds of Architecture does TOGAF deal with?

TOGAF 9 covers the development of four related types of architecture. These four types of architecture are commonly accepted as subsets of an overall enterprise architecture:

| Architecture Type | Description |
|------------------|-------------|
| **Business Architecture** | The business strategy, governance, organization, and key business processes. |
| **Data Architecture** | The structure of an organization's logical and physical data assets and data management resources. |
| **Application Architecture** | A blueprint for the individual application systems to be deployed, their interactions, and their relationships to the core business processes of the organization. |
| **Technology Architecture** | The logical software and hardware capabilities that are required to support the deployment of business, data, and application services. This includes IT infrastructure, middleware, networks, communications, processing, and standards. |

### 1.5 What does TOGAF Contain?

TOGAF reflects the structure and content of an architecture capability within an enterprise. Central to TOGAF is the Architecture Development Method (documented in TOGAF 9, Part II). The architecture capability operates the method. The method is supported by a number of guidelines and techniques. This produces content to be stored in the repository, which is classified according to the Enterprise Continuum. The repository is initially populated with the TOGAF Reference Models.

#### 1.5.1 The Architecture Development Method (ADM)

The ADM describes how to derive an organization-specific enterprise architecture that addresses business requirements. The ADM is the major component of TOGAF and provides guidance for architects on a number of levels:

- It provides a number of architecture development phases (Business Architecture, Information Systems Architectures, Technology Architecture) in a cycle, as an overall process template for architecture development activity.
- It provides a narrative of each architecture phase, describing the phase in terms of objectives, approach, inputs, steps, and outputs.
- It provides cross-phase summaries that cover requirements management.

#### 1.5.2 ADM Guidelines and Techniques

ADM Guidelines and Techniques provides a number of guidelines and techniques to support the application of the ADM. The guidelines address adapting the ADM to deal with a number of usage scenarios, including different process styles and specific specialty architectures. The techniques support specific tasks within the ADM.

#### 1.5.3 Architecture Content Framework

The Architecture Content Framework provides a detailed model of architectural work products, including deliverables, artifacts within deliverables, and the Architecture Building Blocks (ABBs) that deliverables represent.

#### 1.5.4 The Enterprise Continuum

The Enterprise Continuum provides a model for structuring a virtual repository and provides methods for classifying architecture and solution artifacts, showing how the different types of artifacts evolve, and how they can be leveraged and re-used.

#### 1.5.5 TOGAF Reference Models

TOGAF provides two reference models for possible inclusion in an enterprise's own Enterprise Continuum, namely the TOGAF Technical Reference Model (TRM) and the Integrated Information Infrastructure Model (III-RM).

#### 1.5.6 The Architecture Capability Framework

The Architecture Capability Framework is a set of resources, guidelines, templates, background information, etc. provided to help the architect establish an architecture practice within an organization.

---

## Chapter 2: The Architecture Development Method

### 2.1 What is the ADM?

The ADM, a result of contributions from many architects, forms the core of TOGAF. It is a method for deriving organization-specific enterprise architectures and is specifically designed to address business requirements. The ADM describes:

- A reliable, proven way of developing and using an enterprise architecture
- A method of developing architectures on different levels that enable the architect to ensure that a complex set of requirements are adequately addressed
- Guidelines on tools for architecture development

### 2.2 What are the Phases of the ADM?

The ADM consists of a number of phases that cycle through a range of architecture domains that enable the architect to ensure that a complex set of requirements is adequately addressed.

The ADM phases are:

| ADM Phase | Activity |
|-----------|----------|
| **Preliminary Phase** | Prepare the organization for successful TOGAF architecture projects. Undertake the preparation and initiation activities required to meet the business directive for a new enterprise architecture. |
| **Requirements Management** | Every stage of a TOGAF project is based on and validates business requirements. Requirements are identified, stored, and fed into and out of the relevant ADM phases. |
| **Phase A: Architecture Vision** | Set the scope, constraints, and expectations for a TOGAF project. Create the Architecture Vision. Define stakeholders. Validate the business context and create the Statement of Architecture Work. |
| **Phase B: Business Architecture** | Develop Business Architecture. |
| **Phase C: Information Systems Architectures** | Develop Information Systems Architectures (Application & Data). |
| **Phase D: Technology Architecture** | Develop Technology Architecture. |
| **Phase E: Opportunities & Solutions** | Perform initial implementation planning and identify delivery vehicles for the building blocks identified in previous phases. |
| **Phase F: Migration Planning** | Analyze cost benefits and risk. Develop detailed Implementation and Migration Plan. |
| **Phase G: Implementation Governance** | Provide architectural oversight for the implementation. Prepare and issue Architecture Contracts. |
| **Phase H: Architecture Change Management** | Provide continual monitoring and a change management process to ensure that the architecture responds to the needs of the enterprise. |

The ADM is applied iteratively throughout the entire process, between phases, and within them. The ADM supports the concept of iteration at three levels:

- **Cycling around the ADM**: The completion of one phase directly feeds into subsequent phases
- **Iterating between phases**: Returning to previous phases as needed
- **Cycling around a single phase**: Repeated execution of activities within a single ADM phase

### 2.3 The ADM in Detail

Each ADM phase has specific objectives, steps, inputs, and outputs. The phases work together to develop comprehensive enterprise architectures that address business needs while ensuring proper governance and implementation.

### 2.4 Scoping the Architecture Activity

The ADM defines a recommended sequence for phases but cannot determine scope - this must be determined by the organization itself. Scope can be defined and limited across four dimensions:

| Dimension | Considerations |
|-----------|---------------|
| **Enterprise Scope or Focus** | What is the full extent of the enterprise, and how much should the architecting effort focus on? |
| **Architecture Domains** | A complete enterprise architecture should contain all four domains (Business, Data, Application, Technology). |
| **Vertical Scope or Level of Detail** | To what level of detail should the architecting effort go? |
| **Time Period** | What is the time period that needs to be articulated for the Architecture Vision? |

---

## Chapter 3: Key Techniques and Deliverables of the ADM Cycle

This chapter covers the key techniques and deliverables used throughout the ADM cycle, including:

### Major Deliverables and Techniques:

- **Tailored Architecture Framework**: Adapting TOGAF for the enterprise
- **Architecture Principles**: Fundamental rules and guidelines
- **Architecture Vision**: High-level aspirational view
- **Stakeholder Management**: Identifying and managing key players
- **Business Scenarios**: Method for identifying business requirements
- **Gap Analysis**: Identifying differences between baseline and target
- **Architecture Building Blocks**: Reusable components of capability
- **Implementation Planning**: Detailed plans for architecture implementation

### Key Architecture Artifacts:

- **Architecture Definition Document**: Qualitative view of the solution
- **Architecture Requirements Specification**: Quantitative requirements
- **Architecture Roadmap**: Timeline for implementation
- **Transition Architectures**: Intermediate states between baseline and target

---

## Chapter 4: Guidelines for Adapting the ADM

### 4.1 Introduction

The ADM is a generic method that often needs modification for specific enterprise needs. Reasons for tailoring include:

1. Architecture maturity levels within the enterprise
2. Business and architecture principles
3. Integration with other frameworks
4. Corporate governance requirements
5. Outsourcing situations
6. Enterprise size and complexity

### 4.2 Applying Iteration to the ADM

The ADM supports several iteration concepts:

- **Architecture Context iterations**: Establish approach, principles, and scope
- **Architecture Definition iterations**: Create content by cycling through architecture phases
- **Transition Planning iterations**: Create formal change roadmaps
- **Architecture Governance iterations**: Support governance of change activities

### 4.3 Applying the ADM at Different Enterprise Levels

Architectures are typically partitioned according to:
- **Subject Matter**
- **Time Period**
- **Level of Detail**

The ADM can coordinate activities across different architectural teams and levels through hierarchical application.

### 4.4 Security Architecture and the ADM

Security considerations must be addressed throughout the ADM. Key security areas include:
- Authentication
- Authorization
- Audit
- Assurance
- Availability
- Asset Protection
- Administration
- Risk Management

### 4.5 Using TOGAF to Define and Govern SOAs

TOGAF supports Service Oriented Architecture (SOA) through:
- Structured representations linking IT assets to business
- Principles, constraints, frameworks, and standards
- Consistent abstractions of strategies and deliverables
- Repository for holding design information

---

## Chapter 5: Architecture Content Framework

### 5.1 Architecture Content Framework Overview

The Architecture Content Framework provides structure for architectural work products using three categories:

- **Deliverable**: Formal work product that is contractually specified
- **Artifact**: Granular architectural work product from a specific viewpoint
- **Building Block**: Potentially reusable component of capability

### 5.2 Content Metamodel

The metamodel provides definition for all types of building blocks within an architecture, showing how they relate to one another. It includes:

#### 5.2.1 Core and Extensions
- **Core metamodel**: Minimum set supporting traceability
- **Extensions**: Support specific or in-depth modeling

#### 5.2.2 Catalogs, Matrices, and Diagrams
- **Catalogs**: Lists of building blocks
- **Matrices**: Grids showing relationships
- **Diagrams**: Graphical renderings of content

### 5.3 Architectural Artifacts

Artifacts represent individual models created during architecture development. Key concepts include:
- **System**: Collection of components organized for specific functions
- **Stakeholders**: People with key roles or concerns about the system
- **Concerns**: Key interests crucially important to stakeholders
- **Views**: Representations from related sets of concerns
- **Viewpoints**: Perspectives from which views are taken

### 5.4 Architecture Deliverables

TOGAF provides baseline architecture deliverables to define ADM activities and provide starting points for organizational tailoring.

### 5.5 Building Blocks

Building blocks are packages of functionality defined to meet business needs. They exist at different levels:

- **Architecture Building Blocks (ABBs)**: Functional level definitions
- **Solution Building Blocks (SBBs)**: Implementation-specific components

---

## Chapter 6: The Enterprise Continuum

### 6.1 Overview of the Enterprise Continuum

The Enterprise Continuum provides a model for structuring a virtual repository filled with architecture assets and solutions. It distinguishes between:

- **Architecture Continuum**: Architecture assets
- **Solutions Continuum**: Solution assets

The continuum supports:
- **Re-use**: Avoiding re-invention
- **Communication**: Providing consistent language

#### 6.1.1 The Enterprise Continuum and Architecture Re-Use

Assets include:
- Previous architecture work deliverables
- Industry reference models and patterns
- Generic models (like TOGAF TRM)
- Vertical industry specific models

#### 6.1.2 Using the Enterprise Continuum within the ADM

The ADM describes moving from TOGAF Foundation Architecture to organization-specific architectures by adding relevant assets from the Enterprise Continuum.

### 6.2 Architecture Partitioning

Multiple architectures exist in enterprises, leading to partitioning needs because:
- Single architecture addressing all problems is too complex
- Different architectures may conflict
- Different teams need to work on different elements
- Effective reuse requires modular segments

### 6.3 Architecture Repository

The Architecture Repository supports the Enterprise Continuum with components:

- **Architecture Metamodel**: Organizationally tailored framework application
- **Architecture Capability**: Governance parameters and structures
- **Architecture Landscape**: Current building blocks in use
- **Standards Information Base**: Compliance standards
- **Reference Library**: Guidelines, templates, and patterns
- **Governance Log**: Record of governance activity

---

## Chapter 7: TOGAF Reference Models

### 7.1 TOGAF Foundation Architecture

The Foundation Architecture provides a foundation for building specific architectures and components.

#### 7.1.1 Technical Reference Model (TRM)

The TRM is a model and taxonomy of generic platform services providing:
- Terminology definitions
- Coherent component descriptions
- Conceptual Information System description
- Graphical representation as understanding aid

### 7.2 Integrated Information Infrastructure Reference Model (III-RM)

The III-RM focuses on application software space and addresses the challenge of designing integrated information infrastructure for Boundaryless Information Flow. It's a subset of the TRM but expands certain parts, particularly business applications and infrastructure applications.

---

## Chapter 8: Architecture Capability Framework

The Architecture Capability Framework provides reference materials for establishing an architecture function within an organization.

### 8.1 Establishing an Architecture Capability

Implementing architecture capability requires designing four domain architectures:
- **Business Architecture**: Governance, processes, organizational structure
- **Data Architecture**: Enterprise Continuum and Repository structure
- **Application Architecture**: Required functionality and services
- **Technology Architecture**: Infrastructure requirements

### 8.2 Architecture Governance

Architecture governance manages and controls architectures at enterprise level through:
- Control systems for architecture components and activities
- Compliance systems for standards and obligations
- Effective management processes
- Decision structures and stakeholder input
- Accountability practices

### 8.3 Architecture Board

The Architecture Board provides decision-making framework responsible for:
- Sub-architecture consistency
- Reusable component identification
- Enterprise architecture flexibility
- Architecture compliance enforcement
- Architecture discipline maturity improvement
- Architecture-based development adoption

### 8.4 Architecture Compliance

Architecture compliance ensures IT projects comply with architecture roadmap through:
- Project Impact Assessments
- Architecture Compliance Review processes
- Compliance checklists and guidelines

### 8.5 Architecture Skills Framework

The framework provides role, skill, and experience norms for architecture staff across categories:
- **Generic Skills**: Leadership, teamworking, interpersonal skills
- **Business Skills & Methods**: Business cases, process, strategic planning
- **Enterprise Architecture Skills**: Modeling, building block design, systems integration
- **Program/Project Management Skills**: Business change management, project methods
- **IT General Knowledge Skills**: Applications brokering, asset management
- **Technical IT Skills**: Software engineering, security, data management
- **Legal Environment**: Data protection, contract law, procurement law

---

## Appendix A: Migration Summary

TOGAF 9 represents an evolution from TOGAF 8.1.1 with major enhancements including:

- **Modular Structure**: Organized into defined parts with specific purposes
- **Content Framework**: Detailed model of architectural work products
- **Extended Guidance**: Support for architecture hierarchies and governance
- **Architectural Styles**: Detailed ADM application guidance
- **Additional ADM Detail**: Enhanced phases with robust methods

---

## Glossary

**Application Architecture**: A description of the major logical grouping of capabilities that manage the data objects necessary to process the data and support the business.

**Architecture**: 
1. A formal description of a system, or a detailed plan of the system at component level to guide its implementation
2. The structure of components, their inter-relationships, and the principles and guidelines governing their design and evolution over time

**Architecture Building Block (ABB)**: A constituent of the architecture model that describes a single aspect of the overall model.

**Architecture Development Method (ADM)**: The core of TOGAF. A step-by-step approach to develop and use an enterprise architecture.

**Business Architecture**: The business strategy, governance, organization, and key business processes information, as well as the interaction between these concepts.

**Data Architecture**: The structure of an organization's logical and physical data assets and data management resources.

**Enterprise**: The highest level (typically) of description of an organization and typically covers all missions and functions.

**Technology Architecture**: The logical software and hardware capabilities that are required to support deployment of business, data, and application services.

*[Additional glossary terms continue as defined in the original document]*

---

*This document is based on TOGAF™ Version 9 Enterprise Edition*  
*Copyright © 2009 The Open Group, All Rights Reserved*