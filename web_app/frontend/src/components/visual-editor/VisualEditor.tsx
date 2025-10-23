import { useState, useRef, useCallback } from 'react';
import * as go from 'gojs';
import DiagramCanvas from './DiagramCanvas';
import ElementPalette, { PaletteElement } from './ElementPalette';
import PropertiesPanel from './PropertiesPanel';
import EditorToolbar from './EditorToolbar';
import { ReactDiagram } from 'gojs-react';

interface VisualEditorProps {
  modelId: string;
  modelType: string;
  initialData?: any;
  onSave?: (modelData: any) => void;
  readOnly?: boolean;
}

export default function VisualEditor({
  modelId,
  modelType = 'archimate',
  initialData,
  onSave,
  readOnly = false
}: VisualEditorProps) {
  const diagramRef = useRef<ReactDiagram>(null);
  const [selectedElement, setSelectedElement] = useState<any>(null);
  const [modelData, setModelData] = useState<any>(initialData || null);
  const [canUndo, setCanUndo] = useState(false);
  const [canRedo, setCanRedo] = useState(false);
  const [gridVisible, setGridVisible] = useState(true);
  const [zoom, setZoom] = useState(1);
  const [showPalette, setShowPalette] = useState(true);
  const [showProperties, setShowProperties] = useState(true);

  // Get diagram instance
  const getDiagram = useCallback((): go.Diagram | null => {
    if (diagramRef.current) {
      return diagramRef.current.getDiagram();
    }
    return null;
  }, []);

  // Handle element selection from palette
  const handleElementSelect = useCallback((element: PaletteElement) => {
    const diagram = getDiagram();
    if (!diagram || readOnly) return;

    diagram.startTransaction('add node');
    
    const data = {
      key: diagram.model.nodeDataArray.length + 1,
      name: element.name,
      type: element.type,
      category: element.category,
      figure: element.figure,
      color: element.color,
      borderColor: element.borderColor,
      loc: '0 0' // Will be placed at diagram center
    };

    diagram.model.addNodeData(data);
    diagram.commitTransaction('add node');
  }, [getDiagram, readOnly]);

  // Handle property changes
  const handlePropertyChange = useCallback((property: string, value: any) => {
    const diagram = getDiagram();
    if (!diagram || !selectedElement) return;

    diagram.startTransaction('update property');
    diagram.model.setDataProperty(selectedElement, property, value);
    diagram.commitTransaction('update property');
  }, [getDiagram, selectedElement]);

  // Handle model changes
  const handleModelChange = useCallback((model: go.Model) => {
    setModelData(model.toJson());
    
    // Update undo/redo state
    const diagram = getDiagram();
    if (diagram) {
      setCanUndo(diagram.undoManager.canUndo());
      setCanRedo(diagram.undoManager.canRedo());
    }
  }, [getDiagram]);

  // Toolbar actions
  const handleSave = useCallback(() => {
    if (onSave && modelData) {
      onSave(modelData);
    }
  }, [onSave, modelData]);

  const handleExport = useCallback(() => {
    // Export functionality will be implemented
    console.log('Export model:', modelData);
  }, [modelData]);

  const handleUndo = useCallback(() => {
    const diagram = getDiagram();
    if (diagram && diagram.undoManager.canUndo()) {
      diagram.undoManager.undo();
    }
  }, [getDiagram]);

  const handleRedo = useCallback(() => {
    const diagram = getDiagram();
    if (diagram && diagram.undoManager.canRedo()) {
      diagram.undoManager.redo();
    }
  }, [getDiagram]);

  const handleZoomIn = useCallback(() => {
    const diagram = getDiagram();
    if (diagram) {
      diagram.commandHandler.increaseZoom();
      setZoom(diagram.scale);
    }
  }, [getDiagram]);

  const handleZoomOut = useCallback(() => {
    const diagram = getDiagram();
    if (diagram) {
      diagram.commandHandler.decreaseZoom();
      setZoom(diagram.scale);
    }
  }, [getDiagram]);

  const handleFitToScreen = useCallback(() => {
    const diagram = getDiagram();
    if (diagram) {
      diagram.commandHandler.zoomToFit();
      setZoom(diagram.scale);
    }
  }, [getDiagram]);

  const handleToggleGrid = useCallback(() => {
    const diagram = getDiagram();
    if (diagram) {
      diagram.grid.visible = !diagram.grid.visible;
      setGridVisible(diagram.grid.visible);
    }
  }, [getDiagram]);

  const handleAutoLayout = useCallback(() => {
    const diagram = getDiagram();
    if (diagram) {
      diagram.layoutDiagram(true);
    }
  }, [getDiagram]);

  const handlePreview = useCallback(() => {
    // Preview functionality will be implemented
    console.log('Preview mode');
  }, []);

  const handleDelete = useCallback(() => {
    const diagram = getDiagram();
    if (diagram && !readOnly) {
      diagram.commandHandler.deleteSelection();
    }
  }, [getDiagram, readOnly]);

  return (
    <div className="h-full flex flex-col bg-gray-50">
      {/* Toolbar */}
      <EditorToolbar
        onSave={handleSave}
        onExport={handleExport}
        onUndo={handleUndo}
        onRedo={handleRedo}
        onZoomIn={handleZoomIn}
        onZoomOut={handleZoomOut}
        onFitToScreen={handleFitToScreen}
        onToggleGrid={handleToggleGrid}
        onAutoLayout={handleAutoLayout}
        onPreview={handlePreview}
        onDelete={handleDelete}
        canUndo={canUndo}
        canRedo={canRedo}
        gridVisible={gridVisible}
        zoom={zoom}
      />

      {/* Main Editor Area */}
      <div className="flex-1 flex overflow-hidden">
        {/* Left Panel - Element Palette */}
        {showPalette && !readOnly && (
          <div className="w-64 flex-shrink-0">
            <ElementPalette
              modelType={modelType}
              onElementSelect={handleElementSelect}
            />
          </div>
        )}

        {/* Center - Diagram Canvas */}
        <div className="flex-1 p-4">
          <DiagramCanvas
            modelData={modelData}
            onModelChange={handleModelChange}
            modelType={modelType}
            readOnly={readOnly}
          />
        </div>

        {/* Right Panel - Properties */}
        {showProperties && (
          <div className="w-80 flex-shrink-0">
            <PropertiesPanel
              selectedElement={selectedElement}
              onPropertyChange={handlePropertyChange}
              onClose={() => setShowProperties(false)}
            />
          </div>
        )}
      </div>

      {/* Status Bar */}
      <div className="bg-white border-t border-gray-200 px-4 py-2">
        <div className="flex items-center justify-between text-xs text-gray-600">
          <div className="flex items-center space-x-4">
            <span>Model ID: {modelId}</span>
            <span>Type: {modelType.toUpperCase()}</span>
            {selectedElement && (
              <span className="text-indigo-600 font-medium">
                Selected: {selectedElement.name || 'Unnamed'}
              </span>
            )}
          </div>
          <div className="flex items-center space-x-4">
            <button
              onClick={() => setShowPalette(!showPalette)}
              className="hover:text-indigo-600"
            >
              {showPalette ? 'Hide' : 'Show'} Palette
            </button>
            <button
              onClick={() => setShowProperties(!showProperties)}
              className="hover:text-indigo-600"
            >
              {showProperties ? 'Hide' : 'Show'} Properties
            </button>
          </div>
        </div>
      </div>
    </div>
  );
}
