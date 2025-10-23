import { useState, useEffect } from 'react';
import { X } from 'lucide-react';

interface PropertyField {
  name: string;
  label: string;
  type: 'text' | 'textarea' | 'select' | 'color';
  options?: string[];
  value?: string;
}

interface PropertiesPanelProps {
  selectedElement: any | null;
  onPropertyChange: (property: string, value: any) => void;
  onClose: () => void;
}

export default function PropertiesPanel({
  selectedElement,
  onPropertyChange,
  onClose
}: PropertiesPanelProps) {
  const [properties, setProperties] = useState<Record<string, any>>({});

  useEffect(() => {
    if (selectedElement) {
      setProperties({
        name: selectedElement.name || '',
        type: selectedElement.type || '',
        description: selectedElement.description || '',
        color: selectedElement.color || '#f3f4f6',
        borderColor: selectedElement.borderColor || '#6b7280',
        documentation: selectedElement.documentation || '',
        properties: selectedElement.properties || '',
      });
    }
  }, [selectedElement]);

  if (!selectedElement) {
    return (
      <div className="h-full flex items-center justify-center bg-gray-50 border-l border-gray-200">
        <p className="text-gray-500 text-sm">Select an element to view properties</p>
      </div>
    );
  }

  const handleChange = (property: string, value: any) => {
    setProperties(prev => ({ ...prev, [property]: value }));
    onPropertyChange(property, value);
  };

  const getPropertyFields = (): PropertyField[] => {
    const baseFields: PropertyField[] = [
      { name: 'name', label: 'Name', type: 'text', value: properties.name },
      { name: 'type', label: 'Type', type: 'text', value: properties.type },
      { name: 'description', label: 'Description', type: 'textarea', value: properties.description },
    ];

    // Add element-specific fields based on type
    if (selectedElement.category === 'application' || selectedElement.category === 'technology') {
      baseFields.push(
        { name: 'properties', label: 'Properties', type: 'textarea', value: properties.properties }
      );
    }

    baseFields.push(
      { name: 'color', label: 'Fill Color', type: 'color', value: properties.color },
      { name: 'borderColor', label: 'Border Color', type: 'color', value: properties.borderColor },
      { name: 'documentation', label: 'Documentation', type: 'textarea', value: properties.documentation }
    );

    return baseFields;
  };

  const fields = getPropertyFields();

  return (
    <div className="h-full flex flex-col bg-white border-l border-gray-200">
      {/* Header */}
      <div className="p-4 border-b border-gray-200 flex items-center justify-between">
        <h3 className="font-semibold text-gray-900">Properties</h3>
        <button
          onClick={onClose}
          className="p-1 hover:bg-gray-100 rounded"
          title="Close properties panel"
        >
          <X className="w-4 h-4 text-gray-500" />
        </button>
      </div>

      {/* Element Info */}
      <div className="p-4 bg-gray-50 border-b border-gray-200">
        <div className="text-xs text-gray-500 mb-1">Selected Element</div>
        <div className="font-medium text-gray-900">{selectedElement.name || 'Unnamed'}</div>
        <div className="text-sm text-gray-600">{selectedElement.type || 'Unknown Type'}</div>
      </div>

      {/* Properties Form */}
      <div className="flex-1 overflow-y-auto p-4 space-y-4">
        {fields.map(field => (
          <div key={field.name}>
            <label className="block text-sm font-medium text-gray-700 mb-1">
              {field.label}
            </label>
            
            {field.type === 'text' && (
              <input
                type="text"
                value={field.value || ''}
                onChange={(e) => handleChange(field.name, e.target.value)}
                className="w-full px-3 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-indigo-500 focus:border-transparent text-sm"
                placeholder={`Enter ${field.label.toLowerCase()}`}
              />
            )}

            {field.type === 'textarea' && (
              <textarea
                value={field.value || ''}
                onChange={(e) => handleChange(field.name, e.target.value)}
                rows={4}
                className="w-full px-3 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-indigo-500 focus:border-transparent text-sm"
                placeholder={`Enter ${field.label.toLowerCase()}`}
              />
            )}

            {field.type === 'select' && field.options && (
              <select
                value={field.value || ''}
                onChange={(e) => handleChange(field.name, e.target.value)}
                className="w-full px-3 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-indigo-500 focus:border-transparent text-sm"
              >
                <option value="">Select {field.label.toLowerCase()}</option>
                {field.options.map(option => (
                  <option key={option} value={option}>{option}</option>
                ))}
              </select>
            )}

            {field.type === 'color' && (
              <div className="flex items-center space-x-2">
                <input
                  type="color"
                  value={field.value || '#ffffff'}
                  onChange={(e) => handleChange(field.name, e.target.value)}
                  className="h-10 w-16 border border-gray-300 rounded cursor-pointer"
                />
                <input
                  type="text"
                  value={field.value || ''}
                  onChange={(e) => handleChange(field.name, e.target.value)}
                  className="flex-1 px-3 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-indigo-500 focus:border-transparent text-sm font-mono"
                  placeholder="#000000"
                />
              </div>
            )}
          </div>
        ))}
      </div>

      {/* Actions */}
      <div className="p-4 border-t border-gray-200 bg-gray-50">
        <button
          onClick={onClose}
          className="w-full px-4 py-2 bg-indigo-600 text-white rounded-lg hover:bg-indigo-700 transition-colors"
        >
          Apply Changes
        </button>
      </div>
    </div>
  );
}
