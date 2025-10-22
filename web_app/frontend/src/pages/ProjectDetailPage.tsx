import { useParams, useNavigate } from 'react-router-dom';
import { useQuery } from '@tanstack/react-query';
import { ArrowLeft, Edit, Trash2, FileBox, Users, Calendar, Plus } from 'lucide-react';
import toast from 'react-hot-toast';
import { apiClient } from '@/lib/api-client';
import { Project, ArchitectureModel } from '@/types';

export default function ProjectDetailPage() {
  const { id } = useParams<{ id: string }>();
  const navigate = useNavigate();

  // Fetch project details
  const { data: project, isLoading: projectLoading } = useQuery<Project>({
    queryKey: ['project', id],
    queryFn: async () => {
      const response = await apiClient.get(`/projects/${id}`);
      return response.data;
    },
    enabled: !!id,
  });

  // Fetch project models
  const { data: models, isLoading: modelsLoading } = useQuery<ArchitectureModel[]>({
    queryKey: ['models', 'project', id],
    queryFn: async () => {
      const response = await apiClient.get(`/models?project_id=${id}`);
      return response.data;
    },
    enabled: !!id,
  });

  const handleBack = () => {
    navigate('/projects');
  };

  const handleModelClick = (modelId: number) => {
    navigate(`/models/${modelId}/edit`);
  };

  const handleDeleteProject = async () => {
    if (!window.confirm('Are you sure you want to delete this project? This action cannot be undone.')) {
      return;
    }

    try {
      await apiClient.delete(`/projects/${id}`);
      toast.success('Project deleted successfully');
      navigate('/projects');
    } catch (error: any) {
      toast.error(error.response?.data?.detail || 'Failed to delete project');
    }
  };

  if (projectLoading) {
    return (
      <div className="flex items-center justify-center h-full">
        <div className="text-gray-600">Loading project...</div>
      </div>
    );
  }

  if (!project) {
    return (
      <div className="flex items-center justify-center h-full">
        <div className="text-gray-600">Project not found</div>
      </div>
    );
  }

  return (
    <div className="p-6 space-y-6">
      {/* Header */}
      <div className="flex items-center justify-between">
        <div className="flex items-center space-x-4">
          <button
            onClick={handleBack}
            className="p-2 hover:bg-gray-100 rounded-lg transition-colors"
          >
            <ArrowLeft className="w-6 h-6 text-gray-600" />
          </button>
          <div>
            <h1 className="text-3xl font-bold text-gray-900">{project.name}</h1>
            <p className="text-gray-600 mt-1">{project.description}</p>
          </div>
        </div>
        <div className="flex items-center space-x-3">
          <button className="flex items-center space-x-2 px-4 py-2 border border-gray-300 rounded-lg hover:bg-gray-50 transition-colors">
            <Edit className="w-5 h-5 text-gray-600" />
            <span>Edit</span>
          </button>
          <button
            onClick={handleDeleteProject}
            className="flex items-center space-x-2 px-4 py-2 border border-red-300 text-red-600 rounded-lg hover:bg-red-50 transition-colors"
          >
            <Trash2 className="w-5 h-5" />
            <span>Delete</span>
          </button>
        </div>
      </div>

      {/* Project Info Cards */}
      <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
        <div className="bg-white rounded-lg shadow p-6">
          <div className="flex items-center space-x-3">
            <div className="bg-blue-100 rounded-lg p-3">
              <FileBox className="w-6 h-6 text-blue-600" />
            </div>
            <div>
              <p className="text-sm text-gray-600">Models</p>
              <p className="text-2xl font-bold text-gray-900">{project.model_count || 0}</p>
            </div>
          </div>
        </div>

        <div className="bg-white rounded-lg shadow p-6">
          <div className="flex items-center space-x-3">
            <div className="bg-green-100 rounded-lg p-3">
              <Users className="w-6 h-6 text-green-600" />
            </div>
            <div>
              <p className="text-sm text-gray-600">Team Members</p>
              <p className="text-2xl font-bold text-gray-900">{project.team_size || 0}</p>
            </div>
          </div>
        </div>

        <div className="bg-white rounded-lg shadow p-6">
          <div className="flex items-center space-x-3">
            <div className="bg-purple-100 rounded-lg p-3">
              <Calendar className="w-6 h-6 text-purple-600" />
            </div>
            <div>
              <p className="text-sm text-gray-600">Created</p>
              <p className="text-lg font-semibold text-gray-900">
                {new Date(project.created_at).toLocaleDateString()}
              </p>
            </div>
          </div>
        </div>
      </div>

      {/* TOGAF Phase */}
      {project.togaf_phase && (
        <div className="bg-white rounded-lg shadow p-6">
          <h2 className="text-xl font-semibold text-gray-900 mb-4">TOGAF Phase</h2>
          <span className="inline-block bg-indigo-100 text-indigo-700 px-4 py-2 rounded-lg font-medium">
            {project.togaf_phase.replace('_', ' ').toUpperCase()}
          </span>
        </div>
      )}

      {/* Models Section */}
      <div className="bg-white rounded-lg shadow">
        <div className="p-6 border-b">
          <div className="flex items-center justify-between">
            <h2 className="text-xl font-semibold text-gray-900">Models</h2>
            <button className="flex items-center space-x-2 bg-blue-600 text-white px-4 py-2 rounded-lg hover:bg-blue-700 transition-colors">
              <Plus className="w-5 h-5" />
              <span>Add Model</span>
            </button>
          </div>
        </div>

        {modelsLoading ? (
          <div className="p-12 text-center text-gray-500">Loading models...</div>
        ) : models && models.length > 0 ? (
          <div className="divide-y">
            {models.map((model) => (
              <div
                key={model.id}
                onClick={() => handleModelClick(model.id)}
                className="p-6 hover:bg-gray-50 cursor-pointer transition-colors"
              >
                <div className="flex items-center justify-between">
                  <div className="flex items-center space-x-4">
                    <div className="bg-purple-100 rounded-lg p-3">
                      <FileBox className="w-5 h-5 text-purple-600" />
                    </div>
                    <div>
                      <h3 className="text-lg font-semibold text-gray-900">{model.name}</h3>
                      <p className="text-sm text-gray-500">
                        {model.model_type.replace(/-/g, ' ').toUpperCase()}
                      </p>
                    </div>
                  </div>
                  <div className="flex items-center space-x-4">
                    <span className={`px-3 py-1 rounded text-xs ${
                      model.status === 'published' ? 'bg-blue-100 text-blue-700' :
                      model.status === 'approved' ? 'bg-green-100 text-green-700' :
                      model.status === 'in_review' ? 'bg-yellow-100 text-yellow-700' :
                      'bg-gray-100 text-gray-700'
                    }`}>
                      {model.status.replace('_', ' ').toUpperCase()}
                    </span>
                    <span className="text-sm text-gray-400">
                      {new Date(model.updated_at).toLocaleDateString()}
                    </span>
                  </div>
                </div>
              </div>
            ))}
          </div>
        ) : (
          <div className="p-12 text-center">
            <FileBox className="w-12 h-12 text-gray-400 mx-auto mb-4" />
            <p className="text-gray-600 mb-4">No models in this project yet</p>
            <button className="inline-flex items-center space-x-2 bg-blue-600 text-white px-6 py-3 rounded-lg hover:bg-blue-700 transition-colors">
              <Plus className="w-5 h-5" />
              <span>Create First Model</span>
            </button>
          </div>
        )}
      </div>
    </div>
  );
}
