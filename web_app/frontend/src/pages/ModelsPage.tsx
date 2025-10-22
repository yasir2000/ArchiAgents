import { useState } from 'react';
import { useQuery } from '@tanstack/react-query';
import { useNavigate } from 'react-router-dom';
import { Plus, Grid3x3, List, Search, Filter, FileBox, Sparkles } from 'lucide-react';
import toast from 'react-hot-toast';
import { apiClient } from '@/lib/api-client';
import { ArchitectureModel, ModelType, ModelStatus } from '@/types';

type ViewMode = 'grid' | 'list';

export default function ModelsPage() {
  const navigate = useNavigate();
  const [viewMode, setViewMode] = useState<ViewMode>('grid');
  const [searchQuery, setSearchQuery] = useState('');
  const [filterProject, setFilterProject] = useState<string>('all');
  const [filterType, setFilterType] = useState<string>('all');
  const [filterStatus, setFilterStatus] = useState<string>('all');

  // Fetch models
  const { data: models, isLoading } = useQuery<ArchitectureModel[]>({
    queryKey: ['models'],
    queryFn: async () => {
      const response = await apiClient.get('/models');
      return response.data;
    },
  });

  // Filter models
  const filteredModels = models?.filter((model) => {
    const matchesSearch = model.name.toLowerCase().includes(searchQuery.toLowerCase()) ||
      model.description?.toLowerCase().includes(searchQuery.toLowerCase());
    const matchesProject = filterProject === 'all' || model.project_id.toString() === filterProject;
    const matchesType = filterType === 'all' || model.model_type === filterType;
    const matchesStatus = filterStatus === 'all' || model.status === filterStatus;
    return matchesSearch && matchesProject && matchesType && matchesStatus;
  }) || [];

  const handleModelClick = (modelId: number) => {
    navigate(`/models/${modelId}/edit`);
  };

  if (isLoading) {
    return (
      <div className="flex items-center justify-center h-full">
        <div className="text-gray-600">Loading models...</div>
      </div>
    );
  }

  return (
    <div className="p-6 space-y-6">
      {/* Header */}
      <div className="flex items-center justify-between">
        <div>
          <h1 className="text-3xl font-bold text-gray-900">Models</h1>
          <p className="text-gray-600 mt-1">Manage your architecture models</p>
        </div>
        <button
          className="flex items-center space-x-2 bg-blue-600 text-white px-4 py-2 rounded-lg hover:bg-blue-700 transition-colors"
        >
          <Plus className="w-5 h-5" />
          <span>New Model</span>
        </button>
      </div>

      {/* Filters and View Toggle */}
      <div className="bg-white rounded-lg shadow p-4">
        <div className="flex flex-col lg:flex-row lg:items-center lg:justify-between space-y-4 lg:space-y-0">
          {/* Search */}
          <div className="flex-1 lg:max-w-md">
            <div className="relative">
              <Search className="absolute left-3 top-1/2 transform -translate-y-1/2 text-gray-400 w-5 h-5" />
              <input
                type="text"
                value={searchQuery}
                onChange={(e) => setSearchQuery(e.target.value)}
                placeholder="Search models..."
                className="w-full pl-10 pr-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent"
              />
            </div>
          </div>

          {/* Filters */}
          <div className="flex items-center space-x-3">
            <div className="flex items-center space-x-2">
              <Filter className="w-5 h-5 text-gray-400" />
              <select
                value={filterType}
                onChange={(e) => setFilterType(e.target.value)}
                className="px-3 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent text-sm"
              >
                <option value="all">All Types</option>
                <option value="archimate-layered">ArchiMate Layered</option>
                <option value="archimate-motivation">ArchiMate Motivation</option>
                <option value="bpmn-process">BPMN Process</option>
                <option value="uml-class">UML Class</option>
                <option value="uml-sequence">UML Sequence</option>
              </select>

              <select
                value={filterStatus}
                onChange={(e) => setFilterStatus(e.target.value)}
                className="px-3 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent text-sm"
              >
                <option value="all">All Status</option>
                <option value="draft">Draft</option>
                <option value="in_review">In Review</option>
                <option value="approved">Approved</option>
                <option value="published">Published</option>
              </select>
            </div>

            {/* View Toggle */}
            <div className="flex items-center bg-gray-100 rounded-lg p-1">
              <button
                onClick={() => setViewMode('grid')}
                className={`p-2 rounded ${viewMode === 'grid' ? 'bg-white shadow-sm' : ''}`}
              >
                <Grid3x3 className="w-5 h-5 text-gray-600" />
              </button>
              <button
                onClick={() => setViewMode('list')}
                className={`p-2 rounded ${viewMode === 'list' ? 'bg-white shadow-sm' : ''}`}
              >
                <List className="w-5 h-5 text-gray-600" />
              </button>
            </div>
          </div>
        </div>
      </div>

      {/* Models Display */}
      {filteredModels.length > 0 ? (
        viewMode === 'grid' ? (
          <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
            {filteredModels.map((model) => (
              <ModelCard key={model.id} model={model} onClick={() => handleModelClick(model.id)} />
            ))}
          </div>
        ) : (
          <div className="bg-white rounded-lg shadow">
            {filteredModels.map((model, index) => (
              <ModelListItem
                key={model.id}
                model={model}
                onClick={() => handleModelClick(model.id)}
                isLast={index === filteredModels.length - 1}
              />
            ))}
          </div>
        )
      ) : (
        <div className="bg-white rounded-lg shadow p-12 text-center">
          <FileBox className="w-16 h-16 text-gray-400 mx-auto mb-4" />
          <h3 className="text-lg font-semibold text-gray-900 mb-2">No models found</h3>
          <p className="text-gray-600 mb-6">Create your first architecture model to get started</p>
          <button className="inline-flex items-center space-x-2 bg-blue-600 text-white px-6 py-3 rounded-lg hover:bg-blue-700 transition-colors">
            <Plus className="w-5 h-5" />
            <span>Create Model</span>
          </button>
        </div>
      )}
    </div>
  );
}

interface ModelCardProps {
  model: ArchitectureModel;
  onClick: () => void;
}

function ModelCard({ model, onClick }: ModelCardProps) {
  const statusColors: Record<ModelStatus, string> = {
    draft: 'bg-gray-100 text-gray-700',
    in_review: 'bg-yellow-100 text-yellow-700',
    approved: 'bg-green-100 text-green-700',
    published: 'bg-blue-100 text-blue-700',
    archived: 'bg-gray-100 text-gray-500',
  };

  return (
    <div
      onClick={onClick}
      className="bg-white rounded-lg shadow hover:shadow-lg transition-shadow cursor-pointer"
    >
      <div className="p-6 space-y-4">
        {/* Header */}
        <div className="flex items-start justify-between">
          <div className="flex items-center space-x-3">
            <div className="bg-purple-100 rounded-lg p-3">
              <FileBox className="w-6 h-6 text-purple-600" />
            </div>
            <div>
              <h3 className="text-lg font-semibold text-gray-900">{model.name}</h3>
              <span className="text-xs text-gray-500">{model.model_type.replace(/-/g, ' ').toUpperCase()}</span>
            </div>
          </div>
        </div>

        {/* Description */}
        {model.description && (
          <p className="text-sm text-gray-600 line-clamp-2">{model.description}</p>
        )}

        {/* Stats */}
        <div className="flex items-center justify-between text-sm">
          <span className={`px-2 py-1 rounded text-xs ${statusColors[model.status]}`}>
            {model.status.replace('_', ' ').toUpperCase()}
          </span>
          {model.compliance_score !== null && (
            <div className="flex items-center space-x-1">
              <Sparkles className="w-4 h-4 text-yellow-500" />
              <span className="text-gray-600">{model.compliance_score}% compliant</span>
            </div>
          )}
        </div>

        {/* Footer */}
        <div className="text-xs text-gray-400">
          Updated {new Date(model.updated_at).toLocaleDateString()}
        </div>
      </div>
    </div>
  );
}

interface ModelListItemProps {
  model: ArchitectureModel;
  onClick: () => void;
  isLast: boolean;
}

function ModelListItem({ model, onClick, isLast }: ModelListItemProps) {
  const statusColors: Record<ModelStatus, string> = {
    draft: 'bg-gray-100 text-gray-700',
    in_review: 'bg-yellow-100 text-yellow-700',
    approved: 'bg-green-100 text-green-700',
    published: 'bg-blue-100 text-blue-700',
    archived: 'bg-gray-100 text-gray-500',
  };

  return (
    <div
      onClick={onClick}
      className={`p-6 hover:bg-gray-50 cursor-pointer ${!isLast ? 'border-b' : ''}`}
    >
      <div className="flex items-center justify-between">
        <div className="flex items-center space-x-4 flex-1">
          <div className="bg-purple-100 rounded-lg p-3">
            <FileBox className="w-5 h-5 text-purple-600" />
          </div>
          <div className="flex-1 min-w-0">
            <h3 className="text-lg font-semibold text-gray-900">{model.name}</h3>
            <p className="text-sm text-gray-500">{model.model_type.replace(/-/g, ' ').toUpperCase()}</p>
          </div>
        </div>
        <div className="flex items-center space-x-4">
          <span className={`px-3 py-1 rounded text-xs ${statusColors[model.status]}`}>
            {model.status.replace('_', ' ').toUpperCase()}
          </span>
          {model.compliance_score !== null && (
            <div className="flex items-center space-x-1">
              <Sparkles className="w-4 h-4 text-yellow-500" />
              <span className="text-sm text-gray-600">{model.compliance_score}%</span>
            </div>
          )}
          <span className="text-sm text-gray-400">
            {new Date(model.updated_at).toLocaleDateString()}
          </span>
        </div>
      </div>
    </div>
  );
}
