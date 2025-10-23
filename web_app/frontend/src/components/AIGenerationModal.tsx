import { useState } from 'react';
import { X, Wand2, Loader2, AlertCircle } from 'lucide-react';
import { apiClient } from '../lib/api-client';
import { useAuthStore } from '../stores/authStore';
import { toast } from 'react-hot-toast';

interface AIGenerationModalProps {
  isOpen: boolean;
  onClose: () => void;
  projectId: string;
  onSuccess: (modelId: string) => void;
}

const MODEL_TYPES = [
  { value: 'archimate_business', label: 'ArchiMate - Business Layer' },
  { value: 'archimate_application', label: 'ArchiMate - Application Layer' },
  { value: 'archimate_technology', label: 'ArchiMate - Technology Layer' },
  { value: 'archimate_strategy', label: 'ArchiMate - Strategy Layer' },
  { value: 'archimate_physical', label: 'ArchiMate - Physical Layer' },
  { value: 'archimate_implementation', label: 'ArchiMate - Implementation Layer' },
  { value: 'bpmn_process', label: 'BPMN - Process Diagram' },
  { value: 'bpmn_collaboration', label: 'BPMN - Collaboration Diagram' },
  { value: 'uml_class', label: 'UML - Class Diagram' },
  { value: 'uml_sequence', label: 'UML - Sequence Diagram' },
  { value: 'uml_activity', label: 'UML - Activity Diagram' },
  { value: 'uml_state', label: 'UML - State Machine Diagram' },
  { value: 'uml_component', label: 'UML - Component Diagram' },
  { value: 'uml_deployment', label: 'UML - Deployment Diagram' },
  { value: 'uml_usecase', label: 'UML - Use Case Diagram' },
];

const GENERATION_MODES = [
  { value: 'create_new', label: 'Create New Model', description: 'Generate a completely new architecture model' },
  { value: 'extend_existing', label: 'Extend Existing', description: 'Add to an existing model (coming soon)', disabled: true },
  { value: 'improve', label: 'Improve Model', description: 'Enhance an existing model with AI suggestions (coming soon)', disabled: true },
];

export default function AIGenerationModal({ isOpen, onClose, projectId, onSuccess }: AIGenerationModalProps) {
  const { user } = useAuthStore();
  const [isLoading, setIsLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);

  const [formData, setFormData] = useState({
    name: '',
    modelType: 'archimate_business',
    context: '',
    requirements: '',
    mode: 'create_new',
    includeDescription: true,
    validateStandards: true,
  });

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    setError(null);
    setIsLoading(true);

    try {
      const response = await apiClient.post(
        '/ai/generate',
        {
          project_id: projectId,
          model_type: formData.modelType,
          context: formData.context,
          requirements: formData.requirements.split('\n').filter(r => r.trim()),
          name: formData.name,
          mode: formData.mode,
          options: {
            include_description: formData.includeDescription,
            validate_standards: formData.validateStandards,
          }
        }
      );

      toast.success('Model generated successfully!');
      onSuccess(response.data.model_id);
      onClose();
      
      // Reset form
      setFormData({
        name: '',
        modelType: 'archimate_business',
        context: '',
        requirements: '',
        mode: 'create_new',
        includeDescription: true,
        validateStandards: true,
      });
    } catch (err: any) {
      const errorMessage = err.response?.data?.detail || 'Failed to generate model';
      setError(errorMessage);
      toast.error(errorMessage);
    } finally {
      setIsLoading(false);
    }
  };

  if (!isOpen) return null;

  return (
    <div className="fixed inset-0 bg-black bg-opacity-50 flex items-center justify-center z-50 p-4">
      <div className="bg-white rounded-lg shadow-xl max-w-3xl w-full max-h-[90vh] overflow-y-auto">
        {/* Header */}
        <div className="flex items-center justify-between p-6 border-b border-gray-200 bg-gradient-to-r from-purple-600 to-indigo-600 text-white rounded-t-lg">
          <div className="flex items-center space-x-3">
            <Wand2 className="w-6 h-6" />
            <h2 className="text-2xl font-bold">AI-Powered Model Generation</h2>
          </div>
          <button
            onClick={onClose}
            className="text-white hover:bg-white/20 rounded-lg p-2 transition-colors"
          >
            <X className="w-5 h-5" />
          </button>
        </div>

        {/* Form */}
        <form onSubmit={handleSubmit} className="p-6 space-y-6">
          {/* Error Alert */}
          {error && (
            <div className="bg-red-50 border border-red-200 rounded-lg p-4 flex items-start space-x-3">
              <AlertCircle className="w-5 h-5 text-red-600 flex-shrink-0 mt-0.5" />
              <div className="flex-1">
                <h3 className="text-sm font-medium text-red-800">Generation Failed</h3>
                <p className="text-sm text-red-700 mt-1">{error}</p>
              </div>
            </div>
          )}

          {/* Model Name */}
          <div>
            <label className="block text-sm font-medium text-gray-700 mb-2">
              Model Name *
            </label>
            <input
              type="text"
              value={formData.name}
              onChange={(e) => setFormData({ ...formData, name: e.target.value })}
              className="w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-purple-500 focus:border-transparent"
              placeholder="e.g., E-Commerce Business Architecture"
              required
            />
          </div>

          {/* Model Type */}
          <div>
            <label className="block text-sm font-medium text-gray-700 mb-2">
              Model Type *
            </label>
            <select
              value={formData.modelType}
              onChange={(e) => setFormData({ ...formData, modelType: e.target.value })}
              className="w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-purple-500 focus:border-transparent"
              required
            >
              {MODEL_TYPES.map((type) => (
                <option key={type.value} value={type.value}>
                  {type.label}
                </option>
              ))}
            </select>
          </div>

          {/* Generation Mode */}
          <div>
            <label className="block text-sm font-medium text-gray-700 mb-3">
              Generation Mode
            </label>
            <div className="space-y-3">
              {GENERATION_MODES.map((mode) => (
                <label
                  key={mode.value}
                  className={`flex items-start space-x-3 p-4 border rounded-lg cursor-pointer transition-colors ${
                    mode.disabled
                      ? 'bg-gray-50 border-gray-200 cursor-not-allowed opacity-60'
                      : formData.mode === mode.value
                      ? 'bg-purple-50 border-purple-500'
                      : 'bg-white border-gray-300 hover:border-purple-300'
                  }`}
                >
                  <input
                    type="radio"
                    name="mode"
                    value={mode.value}
                    checked={formData.mode === mode.value}
                    onChange={(e) => setFormData({ ...formData, mode: e.target.value })}
                    className="mt-1"
                    disabled={mode.disabled}
                  />
                  <div className="flex-1">
                    <p className="font-medium text-gray-900">{mode.label}</p>
                    <p className="text-sm text-gray-600">{mode.description}</p>
                  </div>
                </label>
              ))}
            </div>
          </div>

          {/* Context */}
          <div>
            <label className="block text-sm font-medium text-gray-700 mb-2">
              Context & Background *
            </label>
            <textarea
              value={formData.context}
              onChange={(e) => setFormData({ ...formData, context: e.target.value })}
              className="w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-purple-500 focus:border-transparent h-32 resize-none"
              placeholder="Describe the business context, domain, or system you want to model...&#10;&#10;Example:&#10;We are building an e-commerce platform for a retail company. The system needs to handle customer orders, inventory management, payment processing, and shipping logistics."
              required
            />
            <p className="text-xs text-gray-500 mt-1">
              Provide context about the domain, business, or technical environment
            </p>
          </div>

          {/* Requirements */}
          <div>
            <label className="block text-sm font-medium text-gray-700 mb-2">
              Specific Requirements (Optional)
            </label>
            <textarea
              value={formData.requirements}
              onChange={(e) => setFormData({ ...formData, requirements: e.target.value })}
              className="w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-purple-500 focus:border-transparent h-32 resize-none"
              placeholder="Enter specific requirements, one per line...&#10;&#10;Example:&#10;Must support multi-currency transactions&#10;Integration with existing ERP system&#10;Real-time inventory updates&#10;Mobile-first customer experience"
            />
            <p className="text-xs text-gray-500 mt-1">
              Enter one requirement per line. AI will consider these when generating the model.
            </p>
          </div>

          {/* Options */}
          <div className="space-y-3">
            <label className="block text-sm font-medium text-gray-700">
              Generation Options
            </label>
            
            <label className="flex items-center space-x-3 cursor-pointer">
              <input
                type="checkbox"
                checked={formData.includeDescription}
                onChange={(e) => setFormData({ ...formData, includeDescription: e.target.checked })}
                className="w-4 h-4 text-purple-600 border-gray-300 rounded focus:ring-purple-500"
              />
              <div>
                <p className="text-sm font-medium text-gray-900">Include Descriptions</p>
                <p className="text-xs text-gray-600">Generate detailed descriptions for elements and relationships</p>
              </div>
            </label>

            <label className="flex items-center space-x-3 cursor-pointer">
              <input
                type="checkbox"
                checked={formData.validateStandards}
                onChange={(e) => setFormData({ ...formData, validateStandards: e.target.checked })}
                className="w-4 h-4 text-purple-600 border-gray-300 rounded focus:ring-purple-500"
              />
              <div>
                <p className="text-sm font-medium text-gray-900">Validate Against Standards</p>
                <p className="text-xs text-gray-600">Check compliance with ArchiMate, BPMN, or UML standards</p>
              </div>
            </label>
          </div>

          {/* Info Box */}
          <div className="bg-blue-50 border border-blue-200 rounded-lg p-4">
            <h4 className="text-sm font-semibold text-blue-900 mb-2">💡 Tips for Better Results</h4>
            <ul className="text-sm text-blue-800 space-y-1">
              <li>• Be specific about the business domain and objectives</li>
              <li>• Include key stakeholders and their roles</li>
              <li>• Mention existing systems or constraints</li>
              <li>• Specify compliance or regulatory requirements</li>
              <li>• Reference any architectural patterns or frameworks</li>
            </ul>
          </div>

          {/* Actions */}
          <div className="flex justify-end space-x-3 pt-4 border-t border-gray-200">
            <button
              type="button"
              onClick={onClose}
              className="px-6 py-2 border border-gray-300 text-gray-700 rounded-lg hover:bg-gray-50 transition-colors"
              disabled={isLoading}
            >
              Cancel
            </button>
            <button
              type="submit"
              disabled={isLoading}
              className="px-6 py-2 bg-gradient-to-r from-purple-600 to-indigo-600 text-white rounded-lg hover:from-purple-700 hover:to-indigo-700 transition-colors disabled:opacity-50 disabled:cursor-not-allowed flex items-center space-x-2"
            >
              {isLoading ? (
                <>
                  <Loader2 className="w-4 h-4 animate-spin" />
                  <span>Generating...</span>
                </>
              ) : (
                <>
                  <Wand2 className="w-4 h-4" />
                  <span>Generate Model</span>
                </>
              )}
            </button>
          </div>
        </form>
      </div>
    </div>
  );
}
