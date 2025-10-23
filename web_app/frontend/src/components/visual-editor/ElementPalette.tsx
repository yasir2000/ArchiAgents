import { useState } from 'react';
import { Box, Circle, Diamond, Square, Database, Cloud, Server, Users, FileText, Settings, Workflow } from 'lucide-react';

export interface PaletteElement {
  id: string;
  name: string;
  type: string;
  category: string;
  icon: React.ReactNode;
  figure: string;
  color: string;
  borderColor: string;
}

interface ElementPaletteProps {
  modelType: string;
  onElementSelect: (element: PaletteElement) => void;
}

export default function ElementPalette({ modelType, onElementSelect }: ElementPaletteProps) {
  const [selectedCategory, setSelectedCategory] = useState<string>('all');
  const [searchTerm, setSearchTerm] = useState('');

  // ArchiMate elements
  const archiMateElements: PaletteElement[] = [
    // Strategy Layer
    { id: 'capability', name: 'Capability', type: 'Strategy', category: 'strategy', icon: <Box className="w-4 h-4" />, figure: 'RoundedRectangle', color: '#fef3c7', borderColor: '#f59e0b' },
    { id: 'resource', name: 'Resource', type: 'Strategy', category: 'strategy', icon: <Database className="w-4 h-4" />, figure: 'RoundedRectangle', color: '#fef3c7', borderColor: '#f59e0b' },
    { id: 'value-stream', name: 'Value Stream', type: 'Strategy', category: 'strategy', icon: <Workflow className="w-4 h-4" />, figure: 'RoundedRectangle', color: '#fef3c7', borderColor: '#f59e0b' },
    
    // Business Layer
    { id: 'business-actor', name: 'Business Actor', type: 'Business', category: 'business', icon: <Users className="w-4 h-4" />, figure: 'Rectangle', color: '#fef9c3', borderColor: '#eab308' },
    { id: 'business-role', name: 'Business Role', type: 'Business', category: 'business', icon: <Circle className="w-4 h-4" />, figure: 'Ellipse', color: '#fef9c3', borderColor: '#eab308' },
    { id: 'business-process', name: 'Business Process', type: 'Business', category: 'business', icon: <Workflow className="w-4 h-4" />, figure: 'RoundedRectangle', color: '#fef9c3', borderColor: '#eab308' },
    { id: 'business-function', name: 'Business Function', type: 'Business', category: 'business', icon: <Box className="w-4 h-4" />, figure: 'RoundedRectangle', color: '#fef9c3', borderColor: '#eab308' },
    { id: 'business-service', name: 'Business Service', type: 'Business', category: 'business', icon: <Settings className="w-4 h-4" />, figure: 'RoundedRectangle', color: '#fef9c3', borderColor: '#eab308' },
    { id: 'business-object', name: 'Business Object', type: 'Business', category: 'business', icon: <FileText className="w-4 h-4" />, figure: 'Rectangle', color: '#fef9c3', borderColor: '#eab308' },
    
    // Application Layer
    { id: 'application-component', name: 'Application Component', type: 'Application', category: 'application', icon: <Box className="w-4 h-4" />, figure: 'Rectangle', color: '#dbeafe', borderColor: '#3b82f6' },
    { id: 'application-service', name: 'Application Service', type: 'Application', category: 'application', icon: <Settings className="w-4 h-4" />, figure: 'RoundedRectangle', color: '#dbeafe', borderColor: '#3b82f6' },
    { id: 'application-interface', name: 'Application Interface', type: 'Application', category: 'application', icon: <Circle className="w-4 h-4" />, figure: 'Ellipse', color: '#dbeafe', borderColor: '#3b82f6' },
    { id: 'data-object', name: 'Data Object', type: 'Application', category: 'application', icon: <Database className="w-4 h-4" />, figure: 'Rectangle', color: '#dbeafe', borderColor: '#3b82f6' },
    
    // Technology Layer
    { id: 'node', name: 'Node', type: 'Technology', category: 'technology', icon: <Server className="w-4 h-4" />, figure: 'Rectangle', color: '#e0f2fe', borderColor: '#0ea5e9' },
    { id: 'device', name: 'Device', type: 'Technology', category: 'technology', icon: <Box className="w-4 h-4" />, figure: 'Rectangle', color: '#e0f2fe', borderColor: '#0ea5e9' },
    { id: 'system-software', name: 'System Software', type: 'Technology', category: 'technology', icon: <Cloud className="w-4 h-4" />, figure: 'Rectangle', color: '#e0f2fe', borderColor: '#0ea5e9' },
    { id: 'technology-service', name: 'Technology Service', type: 'Technology', category: 'technology', icon: <Settings className="w-4 h-4" />, figure: 'RoundedRectangle', color: '#e0f2fe', borderColor: '#0ea5e9' },
    { id: 'artifact', name: 'Artifact', type: 'Technology', category: 'technology', icon: <FileText className="w-4 h-4" />, figure: 'Rectangle', color: '#e0f2fe', borderColor: '#0ea5e9' },
  ];

  // BPMN elements
  const bpmnElements: PaletteElement[] = [
    { id: 'bpmn-task', name: 'Task', type: 'BPMN', category: 'activity', icon: <Square className="w-4 h-4" />, figure: 'RoundedRectangle', color: '#fef3c7', borderColor: '#f59e0b' },
    { id: 'bpmn-gateway', name: 'Gateway', type: 'BPMN', category: 'gateway', icon: <Diamond className="w-4 h-4" />, figure: 'Diamond', color: '#fef9c3', borderColor: '#eab308' },
    { id: 'bpmn-event-start', name: 'Start Event', type: 'BPMN', category: 'event', icon: <Circle className="w-4 h-4" />, figure: 'Circle', color: '#d1fae5', borderColor: '#10b981' },
    { id: 'bpmn-event-end', name: 'End Event', type: 'BPMN', category: 'event', icon: <Circle className="w-4 h-4" />, figure: 'Circle', color: '#fee2e2', borderColor: '#ef4444' },
    { id: 'bpmn-subprocess', name: 'Sub-Process', type: 'BPMN', category: 'activity', icon: <Box className="w-4 h-4" />, figure: 'RoundedRectangle', color: '#e0e7ff', borderColor: '#6366f1' },
    { id: 'bpmn-pool', name: 'Pool', type: 'BPMN', category: 'container', icon: <Box className="w-4 h-4" />, figure: 'Rectangle', color: '#f3f4f6', borderColor: '#6b7280' },
    { id: 'bpmn-lane', name: 'Lane', type: 'BPMN', category: 'container', icon: <Box className="w-4 h-4" />, figure: 'Rectangle', color: '#fafafa', borderColor: '#9ca3af' },
  ];

  // UML elements
  const umlElements: PaletteElement[] = [
    { id: 'uml-class', name: 'Class', type: 'UML', category: 'structure', icon: <Square className="w-4 h-4" />, figure: 'Rectangle', color: '#dbeafe', borderColor: '#3b82f6' },
    { id: 'uml-interface', name: 'Interface', type: 'UML', category: 'structure', icon: <Circle className="w-4 h-4" />, figure: 'Ellipse', color: '#e0e7ff', borderColor: '#6366f1' },
    { id: 'uml-component', name: 'Component', type: 'UML', category: 'structure', icon: <Box className="w-4 h-4" />, figure: 'Rectangle', color: '#fef3c7', borderColor: '#f59e0b' },
    { id: 'uml-package', name: 'Package', type: 'UML', category: 'structure', icon: <Box className="w-4 h-4" />, figure: 'Rectangle', color: '#fef9c3', borderColor: '#eab308' },
    { id: 'uml-actor', name: 'Actor', type: 'UML', category: 'behavior', icon: <Users className="w-4 h-4" />, figure: 'Circle', color: '#e0f2fe', borderColor: '#0ea5e9' },
    { id: 'uml-usecase', name: 'Use Case', type: 'UML', category: 'behavior', icon: <Circle className="w-4 h-4" />, figure: 'Ellipse', color: '#dbeafe', borderColor: '#3b82f6' },
    { id: 'uml-state', name: 'State', type: 'UML', category: 'behavior', icon: <Box className="w-4 h-4" />, figure: 'RoundedRectangle', color: '#fce7f3', borderColor: '#ec4899' },
  ];

  // Get elements based on model type
  const getElements = (): PaletteElement[] => {
    if (modelType === 'archimate') return archiMateElements;
    if (modelType === 'bpmn') return bpmnElements;
    if (modelType === 'uml') return umlElements;
    return [...archiMateElements, ...bpmnElements, ...umlElements];
  };

  const elements = getElements();

  // Get unique categories
  const categories = ['all', ...new Set(elements.map(e => e.category))];

  // Filter elements
  const filteredElements = elements.filter(element => {
    const matchesCategory = selectedCategory === 'all' || element.category === selectedCategory;
    const matchesSearch = element.name.toLowerCase().includes(searchTerm.toLowerCase()) ||
                         element.type.toLowerCase().includes(searchTerm.toLowerCase());
    return matchesCategory && matchesSearch;
  });

  return (
    <div className="h-full flex flex-col bg-white border-r border-gray-200">
      {/* Header */}
      <div className="p-4 border-b border-gray-200">
        <h3 className="font-semibold text-gray-900 mb-3">Elements</h3>
        
        {/* Search */}
        <input
          type="text"
          placeholder="Search elements..."
          value={searchTerm}
          onChange={(e) => setSearchTerm(e.target.value)}
          className="w-full px-3 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-indigo-500 focus:border-transparent text-sm"
        />
      </div>

      {/* Category Tabs */}
      <div className="px-2 py-2 border-b border-gray-200 overflow-x-auto">
        <div className="flex space-x-1">
          {categories.map(category => (
            <button
              key={category}
              onClick={() => setSelectedCategory(category)}
              className={`px-3 py-1 text-xs font-medium rounded capitalize whitespace-nowrap ${
                selectedCategory === category
                  ? 'bg-indigo-100 text-indigo-700'
                  : 'bg-gray-100 text-gray-600 hover:bg-gray-200'
              }`}
            >
              {category}
            </button>
          ))}
        </div>
      </div>

      {/* Elements Grid */}
      <div className="flex-1 overflow-y-auto p-4">
        <div className="grid grid-cols-2 gap-2">
          {filteredElements.map(element => (
            <button
              key={element.id}
              onClick={() => onElementSelect(element)}
              className="p-3 border border-gray-200 rounded-lg hover:border-indigo-500 hover:bg-indigo-50 transition-colors text-left"
              title={`${element.name} - ${element.type}`}
            >
              <div className="flex items-center space-x-2 mb-1">
                <div style={{ color: element.borderColor }}>
                  {element.icon}
                </div>
                <span className="text-xs font-medium text-gray-900 truncate">
                  {element.name}
                </span>
              </div>
              <div className="text-xs text-gray-500">
                {element.type}
              </div>
            </button>
          ))}
        </div>
        
        {filteredElements.length === 0 && (
          <div className="text-center py-8 text-gray-500">
            <p>No elements found</p>
          </div>
        )}
      </div>
    </div>
  );
}
