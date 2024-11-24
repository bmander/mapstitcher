# MapStitcher

## 1. Project Overview

### 1.1 Purpose
The MapStitcher is an open-source web application that enables collaborative georeferencing of historical property atlases, such as [Sanborn fire insurance maps](https://www.loc.gov/collections/sanborn-maps/about-this-collection/) and [Baist real estate atlases](https://pauldorpat.com/maps/1912-baists/). The platform aims to convert these valuable historical documents into accessible, digital geographic resources through community participation.

### 1.2 Key Goals
- Enable crowdsourced georeferencing of historical atlases
- Automate the technical aspects of map processing and tile generation
- Create high-quality, georeferenced outputs in multiple formats
- Foster a community of contributors and historians
- Maintain data quality through collaborative review

## 2. System Architecture

### 2.1 High-Level Components
1. Web Application Frontend
   - User interface for browsing and contributing
   - Map viewer and georeferencing interface
   - Project management dashboard
   - User authentication system

2. Backend Services
   - User/authentication management
   - Project state management
   - Image processing pipeline
   - Tile generation service
   - Storage management

3. Data Storage
   - User database
   - Project metadata database
   - Image storage
   - Generated tile storage

### 2.2 Technology Stack (Proposed)
- Frontend:
  - React/TypeScript for application framework
  - Leaflet for map visualization and georeferencing interface

- Backend:
  - Flask for REST API
  - GDAL for geospatial operations
  - PostgreSQL with PostGIS for spatial data
  - Redis for caching and job queues

- Infrastructure:
  - Docker for containerization
  - S3-compatible storage for images and tiles
  - CDN for tile delivery

## 3. Core Workflows

### 3.1 Project Creation
1. Admin creates new project
2. Uploads source material (scanned pages)
3. Defines project metadata:
   - Atlas name and date
   - Geographic region
   - Reference data sources
   - Expected projection information

### 3.2 Map Panel Extraction
1. User selects a page from project
2. User draws bounding box around map panel
3. System extracts panel and creates new work item
4. User adds metadata:
   - Panel number/reference
   - Coverage area description
   - Notes on condition/quality

### 3.3 Georeferencing
1. User selects panel for georeferencing
2. System displays split view:
   - Historical panel
   - Modern reference map
3. User adds control points:
   - Minimum 4 points required
   - Recommended 8-12 points
   - Quality indicators shown
4. System performs real-time transformation preview
5. Other users can review and modify points

### 3.4 Tile Generation
1. Automatic trigger on control point changes
2. Processing pipeline:
   - Image warping using control points
   - GeoTIFF generation
   - Tile pyramid creation
   - Metadata update
3. Progressive quality levels:
   - Draft: 4+ control points
   - Standard: 8+ points
   - High Quality: 12+ points, peer reviewed

## 4. Data Models

### 4.1 Project
```typescript
interface Project {
  id: string;
  name: string;
  description: string;
  dateCreated: DateTime;
  status: ProjectStatus;
  metadata: ProjectMetadata;
  sourcePages: Page[];
  referenceDatasets: ReferenceData[];
}
```

### 4.2 Page
```typescript
interface Page {
  id: string;
  projectId: string;
  pageNumber: number;
  sourceImage: ImageMetadata;
  extractedPanels: Panel[];
}
```

### 4.3 Panel
```typescript
interface Panel {
  id: string;
  pageId: string;
  bounds: Polygon
  controlPoints: ControlPoint[];
  status: GeoreferenceStatus;
  metadata: PanelMetadata;
  generatedTiles: TileMetadata;
}
```

## 5. Quality Control

### 5.1 Validation Rules
- Minimum control points per panel
- Maximum allowed RMS error
- Required metadata fields
- Image quality thresholds

### 5.2 Review Process
- Peer review system for contributions
- Version control for control points
- Quality scoring system
- Dispute resolution workflow

## 6. Technical Considerations

### 6.1 Performance
- Lazy loading of images and tiles
- Progressive tile generation
- Caching strategy for frequently accessed data
- Background processing for intensive operations

### 6.2 Scalability
- Horizontally scalable services
- Distributed tile generation
- CDN integration for tile delivery
- Queue-based processing pipeline

### 6.3 Storage
- Tiered storage strategy
- Version control for source materials
- Backup and redundancy plan
- Archive format specifications

## 7. Future Considerations

### 7.1 Planned Features
- API for data access
- Export to various GIS formats

### 7.2 Research Opportunities
- Machine learning for panel detection
- Automated control point suggestion
- OCR for text extraction
- Historical address geocoding

## 8. Development Roadmap

### Phase 1: Core Platform
- Basic user management
- Project creation and management
- Simple panel extraction
- Manual georeferencing
- Basic tile generation

### Phase 2: Community Features
- User roles and permissions
- Review system
- Discussion/comments
- Quality metrics

### Phase 3: Automation
- Automated panel detection
- Suggested control points
- Batch processing
- Advanced analytics
