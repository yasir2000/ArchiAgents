import { useState } from 'react';
import { Upload, X, File, AlertCircle, CheckCircle, Loader2 } from 'lucide-react';
import { apiClient } from '../lib/api-client';
import { toast } from 'react-hot-toast';

interface ModelImportDialogProps {
  isOpen: boolean;
  onClose: () => void;
  projectId: string;
  onSuccess: (modelId: string) => void;
}

const IMPORT_FORMATS = [
  {
    value: 'archi',
    label: 'Archi Exchange Format',
    description: 'Import from Archi tool (.archimate or .xml)',
    extensions: ['.archimate', '.xml'],
  },
  {
    value: 'ea',
    label: 'Enterprise Architect',
    description: 'Import from Sparx EA (.xml or .xmi)',
    extensions: ['.xml', '.xmi'],
  },
  {
    value: 'mermaid',
    label: 'Mermaid Diagram',
    description: 'Import from Mermaid markdown syntax (.mmd or .md)',
    extensions: ['.mmd', '.md', '.markdown'],
  },
  {
    value: 'gojs',
    label: 'GoJS JSON',
    description: 'Import from GoJS native format (.json)',
    extensions: ['.json'],
  },
  {
    value: 'text',
    label: 'Text Description',
    description: 'Import from plain text description (.txt)',
    extensions: ['.txt'],
  },
];

export default function ModelImportDialog({
  isOpen,
  onClose,
  projectId,
  onSuccess,
}: ModelImportDialogProps) {
  const [selectedFormat, setSelectedFormat] = useState('archi');
  const [selectedFile, setSelectedFile] = useState<File | null>(null);
  const [modelName, setModelName] = useState('');
  const [isLoading, setIsLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);
  const [uploadProgress, setUploadProgress] = useState(0);

  const selectedFormatInfo = IMPORT_FORMATS.find((f) => f.value === selectedFormat);

  const handleFileSelect = (e: React.ChangeEvent<HTMLInputElement>) => {
    const file = e.target.files?.[0];
    if (file) {
      setSelectedFile(file);
      // Auto-fill model name from filename
      if (!modelName) {
        const name = file.name.replace(/\.[^/.]+$/, ''); // Remove extension
        setModelName(name);
      }
      setError(null);
    }
  };

  const handleDragOver = (e: React.DragEvent) => {
    e.preventDefault();
    e.stopPropagation();
  };

  const handleDrop = (e: React.DragEvent) => {
    e.preventDefault();
    e.stopPropagation();

    const file = e.dataTransfer.files?.[0];
    if (file) {
      setSelectedFile(file);
      if (!modelName) {
        const name = file.name.replace(/\.[^/.]+$/, '');
        setModelName(name);
      }
      setError(null);
    }
  };

  const handleImport = async () => {
    if (!selectedFile) {
      setError('Please select a file to import');
      return;
    }

    if (!modelName.trim()) {
      setError('Please provide a model name');
      return;
    }

    setError(null);
    setIsLoading(true);
    setUploadProgress(0);

    try {
      const formData = new FormData();
      formData.append('file', selectedFile);
      formData.append('project_id', projectId);
      formData.append('name', modelName);
      formData.append('format', selectedFormat);

      const response = await apiClient.post('/models/import', formData, {
        headers: {
          'Content-Type': 'multipart/form-data',
        },
        onUploadProgress: (progressEvent) => {
          const progress = progressEvent.total
            ? Math.round((progressEvent.loaded * 100) / progressEvent.total)
            : 0;
          setUploadProgress(progress);
        },
      });

      toast.success('Model imported successfully!');
      onSuccess(response.data.model_id);
      onClose();

      // Reset form
      setSelectedFile(null);
      setModelName('');
      setUploadProgress(0);
    } catch (err: any) {
      const errorMessage = err.response?.data?.detail || 'Failed to import model';
      setError(errorMessage);
      toast.error(errorMessage);
    } finally {
      setIsLoading(false);
    }
  };

  if (!isOpen) return null;

  return (
    <div className="fixed inset-0 bg-black bg-opacity-50 flex items-center justify-center z-50 p-4">
      <div className="bg-white rounded-lg shadow-xl max-w-2xl w-full max-h-[90vh] overflow-y-auto">
        {/* Header */}
        <div className="flex items-center justify-between p-6 border-b border-gray-200 bg-gradient-to-r from-indigo-600 to-purple-600 text-white rounded-t-lg">
          <div className="flex items-center space-x-3">
            <Upload className="w-6 h-6" />
            <h2 className="text-2xl font-bold">Import Model</h2>
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
                <h3 className="text-sm font-medium text-red-800">Import Failed</h3>
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
              value={modelName}
              onChange={(e) => setModelName(e.target.value)}
              className="w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-indigo-500 focus:border-transparent"
              placeholder="e.g., Business Architecture Model"
              required
            />
          </div>

          {/* Format Selection */}
          <div>
            <label className="block text-sm font-medium text-gray-700 mb-3">
              Import Format *
            </label>
            <div className="grid grid-cols-1 md:grid-cols-2 gap-3">
              {IMPORT_FORMATS.map((format) => {
                const isSelected = selectedFormat === format.value;

                return (
                  <button
                    key={format.value}
                    onClick={() => setSelectedFormat(format.value)}
                    className={`text-left p-4 border-2 rounded-lg transition-all ${
                      isSelected
                        ? 'border-indigo-500 bg-indigo-50'
                        : 'border-gray-200 hover:border-indigo-300 bg-white'
                    }`}
                  >
                    <div className="flex items-start space-x-3">
                      <File
                        className={`w-5 h-5 flex-shrink-0 mt-0.5 ${
                          isSelected ? 'text-indigo-600' : 'text-gray-400'
                        }`}
                      />
                      <div className="flex-1 min-w-0">
                        <p
                          className={`font-semibold ${
                            isSelected ? 'text-indigo-900' : 'text-gray-900'
                          }`}
                        >
                          {format.label}
                        </p>
                        <p className="text-xs text-gray-600 mt-1">{format.description}</p>
                        <div className="flex flex-wrap gap-1 mt-2">
                          {format.extensions.map((ext) => (
                            <span
                              key={ext}
                              className="text-xs font-mono bg-gray-100 px-2 py-0.5 rounded"
                            >
                              {ext}
                            </span>
                          ))}
                        </div>
                      </div>
                    </div>
                  </button>
                );
              })}
            </div>
          </div>

          {/* File Upload */}
          <div>
            <label className="block text-sm font-medium text-gray-700 mb-2">
              Select File *
            </label>
            <div
              onDragOver={handleDragOver}
              onDrop={handleDrop}
              className={`border-2 border-dashed rounded-lg p-8 text-center transition-colors ${
                selectedFile
                  ? 'border-green-500 bg-green-50'
                  : 'border-gray-300 hover:border-indigo-400 bg-gray-50'
              }`}
            >
              {selectedFile ? (
                <div className="space-y-3">
                  <CheckCircle className="w-12 h-12 text-green-600 mx-auto" />
                  <div>
                    <p className="text-lg font-semibold text-gray-900">{selectedFile.name}</p>
                    <p className="text-sm text-gray-600 mt-1">
                      {(selectedFile.size / 1024).toFixed(2)} KB
                    </p>
                  </div>
                  <button
                    onClick={() => setSelectedFile(null)}
                    className="text-sm text-red-600 hover:text-red-700 font-medium"
                  >
                    Remove file
                  </button>
                </div>
              ) : (
                <div className="space-y-3">
                  <Upload className="w-12 h-12 text-gray-400 mx-auto" />
                  <div>
                    <p className="text-gray-700 font-medium">
                      Drag and drop your file here, or
                    </p>
                    <label className="text-indigo-600 hover:text-indigo-700 font-medium cursor-pointer">
                      browse files
                      <input
                        type="file"
                        onChange={handleFileSelect}
                        accept={selectedFormatInfo?.extensions.join(',')}
                        className="hidden"
                      />
                    </label>
                  </div>
                  <p className="text-xs text-gray-500">
                    Supported formats: {selectedFormatInfo?.extensions.join(', ')}
                  </p>
                </div>
              )}
            </div>
          </div>

          {/* Upload Progress */}
          {isLoading && uploadProgress > 0 && (
            <div>
              <div className="flex items-center justify-between text-sm text-gray-600 mb-2">
                <span>Uploading...</span>
                <span>{uploadProgress}%</span>
              </div>
              <div className="w-full bg-gray-200 rounded-full h-2">
                <div
                  className="bg-indigo-600 h-2 rounded-full transition-all duration-300"
                  style={{ width: `${uploadProgress}%` }}
                />
              </div>
            </div>
          )}

          {/* Info Box */}
          <div className="bg-blue-50 border border-blue-200 rounded-lg p-4">
            <h4 className="text-sm font-semibold text-blue-900 mb-2">📁 Import Guidelines</h4>
            <ul className="text-sm text-blue-800 space-y-1">
              <li>• Maximum file size: 10 MB</li>
              <li>• Ensure the file matches the selected format</li>
              <li>• The model will be added to the selected project</li>
              <li>• You can edit the imported model after import</li>
              <li>• Complex models may take longer to process</li>
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
              type="button"
              onClick={handleImport}
              disabled={isLoading || !selectedFile}
              className="px-6 py-2 bg-gradient-to-r from-indigo-600 to-purple-600 text-white rounded-lg hover:from-indigo-700 hover:to-purple-700 transition-colors disabled:opacity-50 disabled:cursor-not-allowed flex items-center space-x-2"
            >
              {isLoading ? (
                <>
                  <Loader2 className="w-4 h-4 animate-spin" />
                  <span>Importing...</span>
                </>
              ) : (
                <>
                  <Upload className="w-4 h-4" />
                  <span>Import Model</span>
                </>
              )}
            </button>
          </div>
        </div>
      </div>
    </div>
  );
}
