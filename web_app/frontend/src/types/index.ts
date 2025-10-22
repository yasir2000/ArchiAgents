// User types
export interface User {
  id: number
  email: string
  username: string
  full_name: string
  role: 'admin' | 'architect' | 'business_analyst' | 'developer' | 'viewer'
  is_active: boolean
  created_at: string
}

// Auth types
export interface LoginRequest {
  username: string
  password: string
}

export interface RegisterRequest {
  email: string
  username: string
  password: string
  full_name: string
  role: string
}

export interface AuthResponse {
  access_token: string
  token_type: string
}

// Project types
export interface Project {
  id: number
  name: string
  description: string
  togaf_phase: string
  owner_id: number
  created_at: string
  updated_at: string
  metadata?: Record<string, any>
  models?: ArchitectureModel[]
}

export interface CreateProjectRequest {
  name: string
  description: string
  togaf_phase: string
  metadata?: Record<string, any>
}

// Model types
export type ModelType =
  | 'archimate-strategy'
  | 'archimate-business'
  | 'archimate-application'
  | 'archimate-technology'
  | 'archimate-physical'
  | 'archimate-implementation'
  | 'archimate-multi-layer'
  | 'bpmn-process'
  | 'bpmn-collaboration'
  | 'bpmn-choreography'
  | 'uml-class'
  | 'uml-sequence'
  | 'uml-use-case'
  | 'uml-activity'
  | 'uml-state-machine'
  | 'uml-component'
  | 'uml-deployment'
  | 'uml-object'
  | 'uml-package'
  | 'uml-timing'
  | 'uml-communication'

export type ModelStatus = 'draft' | 'in_review' | 'approved' | 'published' | 'archived'

export interface ModelElement {
  id: string
  type: string
  name: string
  properties: Record<string, any>
  position?: { x: number; y: number }
}

export interface ModelRelationship {
  id: string
  type: string
  source: string
  target: string
  properties?: Record<string, any>
}

export interface ArchitectureModel {
  id: number
  project_id: number
  name: string
  description: string
  model_type: ModelType
  status: ModelStatus
  elements: ModelElement[]
  relationships: ModelRelationship[]
  version: number
  created_by: number
  created_at: string
  updated_at: string
  ai_generated: boolean
  compliance_score?: number
  metadata?: Record<string, any>
}

export interface CreateModelRequest {
  project_id: number
  name: string
  description: string
  model_type: ModelType
  elements?: ModelElement[]
  relationships?: ModelRelationship[]
}

// AI Generation types
export interface AIGenerationRequest {
  project_id: number
  model_type: ModelType
  name: string
  description?: string
  use_project_context?: boolean
  ai_parameters?: Record<string, any>
}

export interface ValidationIssue {
  severity: 'error' | 'warning' | 'info'
  message: string
  element_id?: string
  suggestion?: string
}

export interface ValidationResult {
  is_valid: boolean
  compliance_score: number
  issues: ValidationIssue[]
  standards_checked: string[]
}

// Collaboration types
export interface CollaborationSession {
  id: number
  model_id: number
  owner_id: number
  session_token: string
  is_active: boolean
  participants: number
  created_at: string
}

export interface CollaborationUpdate {
  type: 'user_joined' | 'user_left' | 'update_element' | 'add_element' | 'delete_element' | 'add_relationship' | 'delete_relationship' | 'cursor_move'
  data: any
  user_id?: number
  timestamp?: string
}

// Dashboard types
export interface DashboardStats {
  total_projects: number
  total_models: number
  models_by_type: Record<string, number>
  models_by_status: Record<string, number>
  recent_activity: ActivityLog[]
}

export interface ActivityLog {
  id: number
  user_id: number
  action: string
  resource_type: string
  resource_id: number
  details: string
  created_at: string
}

// Comment types
export interface Comment {
  id: number
  model_id: number
  user_id: number
  content: string
  element_id?: string
  is_resolved: boolean
  created_at: string
  metadata?: Record<string, any>
}

export interface CreateCommentRequest {
  model_id: number
  content: string
  element_id?: string
  metadata?: Record<string, any>
}

// Export types
export type ExportFormat = 'text' | 'mermaid' | 'kroki' | 'archi' | 'gojs' | 'ea'

export interface ExportRequest {
  model_id: number
  format: ExportFormat
}

export interface ExportResponse {
  content: string
  format: ExportFormat
  filename: string
}
