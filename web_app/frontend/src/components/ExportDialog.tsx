import { useState } from 'react';
import { X, Download, FileText, Code, Image, Loader2, AlertCircle, CheckCircle } from 'lucide-react';
import { apiClient } from '../lib/api-client';
import { toast } from 'react-hot-toast';

interface ExportDialogProps {
  isOpen: boolean;
  onClose: () => void;
  modelId: string;
  modelName: string;
}

const EXPORT_FORMATS = [
  {
    value: 'text',
    label: 'Text Description',
    description: 'Human-readable text format with all elements and relationships',
    icon: FileText,
    extension: 'txt',
    preview: true,
  },
  {
    value: 'mermaid',
    label: 'Mermaid Diagram',
    description: 'Markdown-based diagramming syntax for documentation',
    icon: Code,
    extension: 'mmd',
    preview: true,
  },
  {
    value: 'kroki',
    label: 'Kroki Format',
    description: 'Universal diagram format for rendering with Kroki',
    icon: Image,
    extension: 'kroki',
    preview: false,
  },
  {
    value: 'archi',
    label: 'Archi Exchange',
    description: 'Open Exchange XML format for Archi tool',
    icon: Code,
    extension: 'xml',
    preview: false,
  },
  {
    value: 'ea',
    label: 'Enterprise Architect',
    description: 'XML format compatible with Sparx Enterprise Architect',
    icon: Code,
    extension: 'xml',
    preview: false,
  },
  {
    value: 'gojs',
    label: 'GoJS JSON',
    description: 'Native format for GoJS diagram library',
    icon: Code,
    extension: 'json',
    preview: true,
  },
];

export default function ExportDialog({ isOpen, onClose, modelId, modelName }: ExportDialogProps) {
  const [selectedFormat, setSelectedFormat] = useState('text');
  const [isLoading, setIsLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);
  const [preview, setPreview] = useState<string | null>(null);
  const [showPreview, setShowPreview] = useState(false);

  const selectedFormatInfo = EXPORT_FORMATS.find(f => f.value === selectedFormat);

  const handleExport = async () => {
    setError(null);
    setIsLoading(true);

    try {
      const response = await apiClient.get(`/export/${modelId}/${selectedFormat}`, {
        responseType: 'blob',
      });

      // Create download link
      const url = window.URL.createObjectURL(new Blob([response.data]));
      const link = document.createElement('a');
      link.href = url;
      link.setAttribute('download', `${modelName}.${selectedFormatInfo?.extension || 'txt'}`);
      document.body.appendChild(link);
      link.click();
      link.remove();
      window.URL.revokeObjectURL(url);

      toast.success('Model exported successfully!');
      onClose();
    } catch (err: any) {
      const errorMessage = err.response?.data?.detail || 'Failed to export model';
      setError(errorMessage);
      toast.error(errorMessage);
    } finally {
      setIsLoading(false);
    }
  };

  const handlePreview = async () => {
    if (!selectedFormatInfo?.preview) return;

    setError(null);
    setIsLoading(true);

    try {
      const response = await apiClient.get(`/export/${modelId}/${selectedFormat}`);
      
      // Convert response to text preview
      let previewText = '';
      if (typeof response.data === 'string') {
        previewText = response.data;
      } else if (typeof response.data === 'object') {
        previewText = JSON.stringify(response.data, null, 2);
      }

      setPreview(previewText);
      setShowPreview(true);
    } catch (err: any) {
      const errorMessage = err.response?.data?.detail || 'Failed to generate preview';
      setError(errorMessage);
      toast.error(errorMessage);
    } finally {
      setIsLoading(false);
    }
  };

  if (!isOpen) return null;

  return (
    <div className="fixed inset-0 bg-black bg-opacity-50 flex items-center justify-center z-50 p-4">
      <div className="bg-white rounded-lg shadow-xl max-w-4xl w-full max-h-[90vh] overflow-y-auto">
        {/* Header */}
        <div className="flex items-center justify-between p-6 border-b border-gray-200 bg-gradient-to-r from-green-600 to-teal-600 text-white rounded-t-lg">
          <div className="flex items-center space-x-3">
            <Download className="w-6 h-6" />
            <div>
              <h2 className="text-2xl font-bold">Export Model</h2>
              <p className="text-sm opacity-90 mt-1">{modelName}</p>
            </div>
          </div>
          <button
            onClick={onClose}
            className="text-white hover:bg-white/20 rounded-lg p-2 transition-colors"
          >
            <X className="w-5 h-5" />
          </button>
        </div>

        {/* Content */}
        <div className="p-6 space-y-6">
          {/* Error Alert */}
          {error && (
            <div className="bg-red-50 border border-red-200 rounded-lg p-4 flex items-start space-x-3">
              <AlertCircle className="w-5 h-5 text-red-600 flex-shrink-0 mt-0.5" />
              <div className="flex-1">
                <h3 className="text-sm font-medium text-red-800">Export Failed</h3>
                <p className="text-sm text-red-700 mt-1">{error}</p>
              </div>
            </div>
          )}

          {/* Format Selection */}
          <div>
            <label className="block text-sm font-medium text-gray-700 mb-3">
              Select Export Format
            </label>
            <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
              {EXPORT_FORMATS.map((format) => {
                const Icon = format.icon;
                const isSelected = selectedFormat === format.value;

                return (
                  <button
                    key={format.value}
                    onClick={() => {
                      setSelectedFormat(format.value);
                      setShowPreview(false);
                      setPreview(null);
                    }}
                    className={`text-left p-4 border-2 rounded-lg transition-all ${
                      isSelected
                        ? 'border-green-500 bg-green-50'
                        : 'border-gray-200 hover:border-green-300 bg-white'
                    }`}
                  >
                    <div className="flex items-start space-x-3">
                      <Icon className={`w-5 h-5 flex-shrink-0 mt-0.5 ${
                        isSelected ? 'text-green-600' : 'text-gray-400'
                      }`} />
                      <div className="flex-1 min-w-0">
                        <div className="flex items-center space-x-2">
                          <p className={`font-semibold ${
                            isSelected ? 'text-green-900' : 'text-gray-900'
                          }`}>
                            {format.label}
                          </p>
                          {isSelected && (
                            <CheckCircle className="w-4 h-4 text-green-600" />
                          )}
                        </div>
                        <p className="text-sm text-gray-600 mt-1">{format.description}</p>
                        <div className="flex items-center space-x-2 mt-2">
                          <span className="text-xs font-mono bg-gray-100 px-2 py-1 rounded">
                            .{format.extension}
                          </span>
                          {format.preview && (
                            <span className="text-xs bg-blue-100 text-blue-700 px-2 py-1 rounded">
                              Preview available
                            </span>
                          )}
                        </div>
                      </div>
                    </div>
                  </button>
                );
              })}
            </div>
          </div>

          {/* Preview Section */}
          {showPreview && preview && (
            <div>
              <h3 className="text-lg font-semibold text-gray-900 mb-3">Preview</h3>
              <div className="bg-gray-50 border border-gray-200 rounded-lg p-4 max-h-96 overflow-auto">
                <pre className="text-sm text-gray-800 whitespace-pre-wrap font-mono">
                  {preview}
                </pre>
              </div>
            </div>
          )}

          {/* Info Box */}
          <div className="bg-blue-50 border border-blue-200 rounded-lg p-4">
            <h4 className="text-sm font-semibold text-blue-900 mb-2">📋 Export Information</h4>
            <ul className="text-sm text-blue-800 space-y-1">
              <li>• <strong>Text:</strong> Best for documentation and human review</li>
              <li>• <strong>Mermaid:</strong> Perfect for embedding in markdown files</li>
              <li>• <strong>Kroki:</strong> Universal format for multiple rendering engines</li>
              <li>• <strong>Archi:</strong> Import into Archi tool for further editing</li>
              <li>• <strong>EA:</strong> Compatible with Enterprise Architect tool</li>
              <li>• <strong>GoJS:</strong> Native format for this application's editor</li>
            </ul>
          </div>

          {/* Actions */}
          <div className="flex justify-between items-center pt-4 border-t border-gray-200">
            <div>
              {selectedFormatInfo?.preview && !showPreview && (
                <button
                  type="button"
                  onClick={handlePreview}
                  disabled={isLoading}
                  className="px-6 py-2 border border-blue-500 text-blue-600 rounded-lg hover:bg-blue-50 transition-colors disabled:opacity-50 disabled:cursor-not-allowed flex items-center space-x-2"
                >
                  {isLoading ? (
                    <>
                      <Loader2 className="w-4 h-4 animate-spin" />
                      <span>Loading...</span>
                    </>
                  ) : (
                    <>
                      <FileText className="w-4 h-4" />
                      <span>Preview</span>
                    </>
                  )}
                </button>
              )}
            </div>
            <div className="flex space-x-3">
              <button
                type="button"
                onClick={onClose}
                className="px-6 py-2 border border-gray-300 text-gray-700 rounded-lg hover:bg-gray-50 transition-colors"
                disabled={isLoading}
              >
                Cancel
              </button>
              <button
                type="button"
                onClick={handleExport}
                disabled={isLoading}
                className="px-6 py-2 bg-gradient-to-r from-green-600 to-teal-600 text-white rounded-lg hover:from-green-700 hover:to-teal-700 transition-colors disabled:opacity-50 disabled:cursor-not-allowed flex items-center space-x-2"
              >
                {isLoading ? (
                  <>
                    <Loader2 className="w-4 h-4 animate-spin" />
                    <span>Exporting...</span>
                  </>
                ) : (
                  <>
                    <Download className="w-4 h-4" />
                    <span>Download</span>
                  </>
                )}
              </button>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}
