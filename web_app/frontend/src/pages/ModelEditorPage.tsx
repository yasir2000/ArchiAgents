import { useParams, useNavigate } from 'react-router-dom';
import { useState, useEffect } from 'react';
import { ArrowLeft } from 'lucide-react';
import { VisualEditor } from '../components/visual-editor';
import { apiClient } from '../lib/api-client';
import toast from 'react-hot-toast';

export default function ModelEditorPage() {
  const { id } = useParams<{ id: string }>();
  const navigate = useNavigate();
  const [model, setModel] = useState<any>(null);
  const [loading, setLoading] = useState(true);
  const [saving, setSaving] = useState(false);

  useEffect(() => {
    const fetchModel = async () => {
      try {
        const response = await apiClient.get(`/api/models/${id}`);
        setModel(response.data);
      } catch (error) {
        console.error('Failed to fetch model:', error);
        toast.error('Failed to load model');
      } finally {
        setLoading(false);
      }
    };

    if (id) {
      fetchModel();
    }
  }, [id]);

  const handleSave = async (modelData: any) => {

    setSaving(true);
    try {
      await apiClient.put(`/api/models/${id}`, {
        ...model,
        content: modelData
      });
      toast.success('Model saved successfully');
    } catch (error) {
      console.error('Failed to save model:', error);
      toast.error('Failed to save model');
    } finally {
      setSaving(false);
    }
  };

  if (loading) {
    return (
      <div className="flex items-center justify-center h-full">
        <div className="text-center">
          <div className="animate-spin rounded-full h-12 w-12 border-b-2 border-indigo-600 mx-auto mb-4"></div>
          <p className="text-gray-600">Loading model...</p>
        </div>
      </div>
    );
  }

    return (
      <div className="flex items-center justify-center h-full">
        <div className="text-center">
          <p className="text-gray-600 mb-4">Model not found</p>
          <button
            onClick={() => navigate('/models')}
            className="px-4 py-2 bg-indigo-600 text-white rounded-lg hover:bg-indigo-700"
          >
            Back to Models
          </button>
        </div>
      </div>
    );
  }

  return (
    <div className="h-full flex flex-col">
      <div className="bg-white border-b border-gray-200 px-6 py-4">
        <div className="flex items-center justify-between">
          <div className="flex items-center space-x-4">
            <button
              onClick={() => navigate('/models')}
              className="p-2 hover:bg-gray-100 rounded-lg transition-colors"
              title="Back to models"
            >
              <ArrowLeft className="w-5 h-5 text-gray-600" />
            </button>
            <div>
              <h1 className="text-xl font-bold text-gray-900">{model.name}</h1>
              <p className="text-sm text-gray-600">{model.model_type} Model</p>
            </div>
          </div>
          
          {saving && (
            <div className="flex items-center space-x-2 text-sm text-gray-600">
              <div className="animate-spin rounded-full h-4 w-4 border-b-2 border-indigo-600"></div>
              <span>Saving...</span>
            </div>
          )}
        </div>
      </div>

      <div className="flex-1 overflow-hidden">
        <VisualEditor
          modelId={id || ''}
          modelType={model.model_type.toLowerCase()}
          initialData={model.content}
          onSave={handleSave}
          readOnly={false}
        />
      </div>
    </div>
  );
}
